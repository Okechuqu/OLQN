from .models import StreamChannel


def active_stream():
    return StreamChannel.objects.filter(is_active=True).first()
