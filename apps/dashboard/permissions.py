def can_access_dashboard(user) -> bool:
    return user.is_active and user.is_staff
