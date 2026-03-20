from __future__ import annotations

import os

import uvicorn

from app.main import app


def main() -> None:
    port = int(os.getenv("PORT", "8010"))
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=port,
        log_level="info",
        loop="asyncio",
        http="h11",
        ws="websockets",
    )


if __name__ == "__main__":
    main()
