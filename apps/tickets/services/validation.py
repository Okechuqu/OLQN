def can_check_in(registration) -> bool:
    return registration.status == registration.Status.PAID
