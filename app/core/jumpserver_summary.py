from __future__ import annotations

# Security-log-analysis mainline JumpServer summarizers.

from typing import Any


def _string(value: Any) -> str:
    return str(value or "").strip()


def _lower(value: Any) -> str:
    return _string(value).lower()


def summarize_login_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    success = 0
    failure = 0
    failed_accounts: dict[str, int] = {}
    proxy_ips: set[str] = set()
    for row in rows:
        status = _string(row.get("状态") or row.get("status"))
        user = _string(row.get("用户名") or row.get("user"))
        ip = _string(row.get("登录 IP") or row.get("login_ip") or row.get("ip"))
        reason = _lower(row.get("原因描述") or row.get("reason"))
        if ip:
            proxy_ips.add(ip)
        if "成功" in status or "success" in _lower(status):
            success += 1
        else:
            failure += 1
            if user:
                failed_accounts[user] = failed_accounts.get(user, 0) + 1
            elif reason:
                failed_accounts[reason] = failed_accounts.get(reason, 0) + 1
    return {
        "total_rows": len(rows),
        "success_count": success,
        "failure_count": failure,
        "top_failed_accounts": [
            {"user": user, "count": count}
            for user, count in sorted(failed_accounts.items(), key=lambda item: item[1], reverse=True)[:8]
        ],
        "proxy_ips": sorted(proxy_ips),
    }


def summarize_command_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    patterns = {
        "提权": ("sudo", "sudo su", "sudo su -"),
        "服务控制": ("systemctl start", "systemctl stop", "systemctl restart", "systemctl status"),
        "删除/替换": ("rm -rf", " mv ", "ln -sf"),
        "权限变更": ("chmod", "chown"),
        "远程/横向操作": ("ssh ", "scp ", "rsync", "telnet", "nc "),
        "下载执行": ("curl ", "wget ", "installer"),
        "本地执行": ("./",),
        "明文敏感参数": ("--private-key",),
    }
    labels = {key: 0 for key in patterns}
    account_counts: dict[str, int] = {}
    effective = 0
    for row in rows:
        command = _string(row.get("命令") or row.get("command"))
        if not command:
            continue
        lowered = command.lower()
        if any(token in lowered for token in ("\u001b", "tmux", "codex", "claude")):
            # very light denoise fallback for single-source mode
            continue
        effective += 1
        user = _string(row.get("用户") or row.get("user"))
        if user:
            account_counts[user] = account_counts.get(user, 0) + 1
        for label, tokens in patterns.items():
            if any(token in lowered for token in tokens):
                labels[label] += 1
    return {
        "total_rows": len(rows),
        "effective_command_count": effective,
        "high_risk_action_labels": {key: value for key, value in labels.items() if value},
        "top_risk_accounts": [
            {"user": user, "count": count}
            for user, count in sorted(account_counts.items(), key=lambda item: item[1], reverse=True)[:8]
        ],
    }


def summarize_transfer_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    uploads = 0
    downloads = 0
    high_risk = 0
    top_uploads: list[dict[str, Any]] = []
    for row in rows:
        operation = _lower(row.get("操作") or row.get("operation"))
        filename = _string(row.get("文件名") or row.get("filename"))
        account = _lower(row.get("账号") or row.get("account"))
        if "上传" in operation or "upload" in operation:
            uploads += 1
            record = {
                "user": _string(row.get("用户") or row.get("user")),
                "asset": _string(row.get("资产") or row.get("asset")),
                "filename": filename,
                "account": _string(row.get("账号") or row.get("account")),
            }
            if len(top_uploads) < 8:
                top_uploads.append(record)
            if "/tmp/" in filename.lower() or account == "root":
                high_risk += 1
        elif "下载" in operation or "download" in operation:
            downloads += 1
    return {
        "total_rows": len(rows),
        "upload_count": uploads,
        "download_count": downloads,
        "high_risk_upload_count": high_risk,
        "top_uploads": top_uploads,
    }


def summarize_operation_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    export_actions = 0
    authorization_updates = 0
    host_or_account_creation = 0
    session_creation = 0
    operator_counts: dict[str, int] = {}
    resource_type_counts: dict[str, int] = {}
    top_operations: list[dict[str, Any]] = []
    create_count = 0
    update_count = 0
    for row in rows:
        user = _string(row.get("用户") or row.get("user"))
        action = _string(row.get("动作") or row.get("action"))
        resource_type = _string(row.get("资源类型") or row.get("resource_type"))
        lowered = action.lower()
        if user:
            operator_counts[user] = operator_counts.get(user, 0) + 1
        if resource_type:
            resource_type_counts[resource_type] = resource_type_counts.get(resource_type, 0) + 1
        if "导出" in lowered or "export" in lowered:
            export_actions += 1
        if "更新" in lowered or "update" in lowered or "授权" in lowered or "grant" in lowered or "bind" in lowered:
            authorization_updates += 1
            update_count += 1
        if "创建" in lowered or "create" in lowered:
            create_count += 1
            if any(token in resource_type.lower() for token in ("主机", "资产", "账号", "用户")):
                host_or_account_creation += 1
            if "会话" in resource_type or "session" in resource_type.lower() or "创建用户会话" in action:
                session_creation += 1
        if len(top_operations) < 8:
            top_operations.append(
                {
                    "user": user,
                    "action": action,
                    "resource_type": resource_type,
                    "resource": _string(row.get("资源") or row.get("resource")),
                    "event_time": _string(row.get("日期") or row.get("event_time")),
                }
            )
    return {
        "total_rows": len(rows),
        "create_count": create_count,
        "update_count": update_count,
        "export_actions": export_actions,
        "authorization_updates": authorization_updates,
        "host_or_account_creation": host_or_account_creation,
        "session_creation": session_creation,
        "operator_counts": operator_counts,
        "resource_type_counts": resource_type_counts,
        "top_operations": top_operations,
    }
