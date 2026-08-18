def amount_matches(payload: dict, expected_kobo: int) -> bool:
    data = payload.get("data", {})
    return data.get("status") == "success" and data.get("amount") == expected_kobo
