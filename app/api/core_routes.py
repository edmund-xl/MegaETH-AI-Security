from __future__ import annotations

from fastapi import APIRouter, File, UploadFile

from app.api.shared import pipeline
from app.models.event import EventEnvelope, NormalizedEvent, RawEvent
from app.models.memory import ClassificationLearningRequest
from app.utils.file_ingest import build_jumpserver_composite_raw_event, parse_file_to_raw_event


router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/skills")
def skills():
    return pipeline.list_skills()


@router.get("/skills/matrix")
def skills_matrix():
    return pipeline.skill_matrix()


@router.get("/pipeline/overview")
def pipeline_overview():
    return pipeline.overview()


@router.get("/reports/recent")
def recent_reports():
    return pipeline.recent()


@router.get("/events/recent")
def recent_events():
    return pipeline.history.list_events()


@router.get("/events/raw")
def raw_events():
    return pipeline.history.list_raw_events()


@router.get("/investigations/recent")
def investigations():
    return pipeline.history.list_investigations()


@router.get("/history")
def history():
    return {
        "events": pipeline.history.list_events(),
        "raw_events": pipeline.history.list_raw_events(),
        "reports": pipeline.history.list_reports(),
        "investigations": pipeline.history.list_investigations(),
    }


@router.get("/memory/rules")
def memory_rules():
    return pipeline.memory.list_rules()


@router.get("/memory/feedback")
def memory_feedback():
    return pipeline.memory.list_feedback()


@router.post("/memory/learn/classification")
def learn_classification(payload: ClassificationLearningRequest):
    raw_event = RawEvent(**payload.raw_event.model_dump())
    return pipeline.memory.learn_classification(
        raw_event=raw_event,
        expected_source_type=payload.expected_source_type,
        expected_event_type=payload.expected_event_type,
        preferred_skills=payload.preferred_skills,
        notes=payload.notes,
        name=payload.name,
    )


@router.post("/normalize/preview")
def normalize_preview(raw_event: RawEvent):
    raw_event, memory = pipeline.memory.apply_raw_event_memory(raw_event)
    normalized = pipeline.normalizer.normalize(raw_event)
    normalized = pipeline.memory.enrich_normalized_event(normalized, memory)
    return normalized


@router.post("/planner/preview")
def planner_preview(event: NormalizedEvent):
    skills, reason = pipeline.planner.plan(event)
    return {
        "skills_to_execute": skills,
        "analysis_reason": reason,
        "classification": pipeline.planner.classify(event),
    }


@router.post("/event")
def process_event(event: NormalizedEvent):
    return pipeline.run(event)


@router.post("/ingest/raw")
def ingest_raw(raw_event: RawEvent):
    return pipeline.ingest_raw(raw_event)


@router.post("/ingest/files")
async def ingest_files(files: list[UploadFile] = File(...)):
    uploaded_count = len(files)
    results = []
    errors = []
    raw_events_for_batch: list[RawEvent] = []
    for upload in files:
        data = await upload.read()
        try:
            raw_event = parse_file_to_raw_event(upload.filename or "uploaded-file", data)
            raw_events_for_batch.append(raw_event)
            raw_event, memory = pipeline.memory.apply_raw_event_memory(raw_event)
            normalized = pipeline.normalizer.normalize(raw_event)
            normalized = pipeline.memory.enrich_normalized_event(normalized, memory)
            classification = pipeline.planner.classify(normalized)
            skills, reason = pipeline.planner.plan(normalized)
            envelope = EventEnvelope(
                raw_event=raw_event,
                normalized_event=normalized,
                classification=classification,
            )
            pipeline.history.save_raw_event(raw_event)
            pipeline.memory.learn_from_analysis(raw_event, normalized, skills)
            report = pipeline.run(normalized, envelope)
            results.append(
                {
                    "filename": upload.filename,
                    "raw_event": raw_event.model_dump(mode="json"),
                    "normalized_event": normalized.model_dump(mode="json"),
                    "planner_preview": {
                        "skills_to_execute": skills,
                        "analysis_reason": reason,
                        "classification": classification,
                    },
                    "report": report.model_dump(mode="json"),
                }
            )
        except ValueError as exc:
            errors.append({"filename": upload.filename, "error": str(exc)})
    composite_raw_event = build_jumpserver_composite_raw_event(raw_events_for_batch)
    composite_generated = False
    if composite_raw_event is not None:
        composite_generated = True
        composite_raw_event, memory = pipeline.memory.apply_raw_event_memory(composite_raw_event)
        composite_normalized = pipeline.normalizer.normalize(composite_raw_event)
        composite_normalized = pipeline.memory.enrich_normalized_event(composite_normalized, memory)
        composite_classification = pipeline.planner.classify(composite_normalized)
        composite_skills, composite_reason = pipeline.planner.plan(composite_normalized)
        composite_envelope = EventEnvelope(
            raw_event=composite_raw_event,
            normalized_event=composite_normalized,
            classification=composite_classification,
        )
        pipeline.history.save_raw_event(composite_raw_event)
        pipeline.memory.learn_from_analysis(composite_raw_event, composite_normalized, composite_skills)
        composite_report = pipeline.run(composite_normalized, composite_envelope)
        results.insert(
            0,
            {
                "filename": "JumpServer Multi-Source Audit Batch",
                "raw_event": composite_raw_event.model_dump(mode="json"),
                "normalized_event": composite_normalized.model_dump(mode="json"),
                "planner_preview": {
                    "skills_to_execute": composite_skills,
                    "analysis_reason": composite_reason,
                    "classification": composite_classification,
                },
                "report": composite_report.model_dump(mode="json"),
            },
        )
    investigation = (
        pipeline.save_investigation_session("Uploaded file batch", results)
        if results
        else None
    )
    return {
        "uploaded_count": uploaded_count,
        "count": len(results),
        "composite_generated": composite_generated,
        "error_count": len(errors),
        "errors": errors,
        "investigation": investigation,
        "results": results,
    }
