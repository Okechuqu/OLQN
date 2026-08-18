import hashlib
import hmac
import json

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def paystack_webhook(request):
    """Validate Paystack at the edge; payment verification is completed asynchronously."""
    if request.method != "POST" or not settings.PAYSTACK_WEBHOOK_SECRET:
        return HttpResponseBadRequest()
    signature = request.headers.get("x-paystack-signature", "")
    expected = hmac.new(
        settings.PAYSTACK_WEBHOOK_SECRET.encode(), request.body, hashlib.sha512
    ).hexdigest()
    if not hmac.compare_digest(signature, expected):
        return HttpResponseBadRequest()
    try:
        json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest()
    return HttpResponse(status=202)
