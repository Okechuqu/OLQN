from django.urls import path

from .webhooks import paystack_webhook

app_name = "payments"
urlpatterns = [path("paystack/webhook/", paystack_webhook, name="paystack_webhook")]
