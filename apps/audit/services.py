from .models import AuditEvent


def record_event(*, actor, action, path, metadata=None):
    return AuditEvent.objects.create(
        actor=actor, action=action, path=path, metadata=metadata or {}
    )
