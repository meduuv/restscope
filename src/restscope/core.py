from collections import Counter


def normalize_endpoint(endpoint: dict) -> dict:
    return {
        "method": str(endpoint.get("method", "GET")).upper(),
        "path": str(endpoint.get("path", "/")).strip() or "/",
    }


def group_by_method(endpoints: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = {}
    for endpoint in endpoints:
        item = normalize_endpoint(endpoint)
        groups.setdefault(item["method"], []).append(item)
    return groups


def duplicates(endpoints: list[dict]) -> list[dict]:
    normalized = [normalize_endpoint(item) for item in endpoints]
    counts = Counter((x["method"], x["path"]) for x in normalized)
    return [x for x in normalized if counts[(x["method"], x["path"])] > 1]
