import httpx
from django.conf import settings


def verify_transaction(reference: str) -> dict:
    response = httpx.get(
        f"https://api.paystack.co/transaction/verify/{reference}",
        headers={"Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"},
        timeout=15,
    )
    response.raise_for_status()
    return response.json()
