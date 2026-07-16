"""Health service."""


def get_health_status() -> dict[str, str]:
    return {"status": "ok", "service": "movepal"}
