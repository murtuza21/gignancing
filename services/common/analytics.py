import json
import os


def track(event: str, data: dict | None = None) -> None:
    if os.getenv("DEMO_MODE") == "true":
        print(f"ANALYTICS {event} {json.dumps(data or {})}")
