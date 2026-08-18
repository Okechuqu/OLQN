def can_view_finance(user) -> bool:
    return user.is_superuser or user.groups.filter(name="Finance").exists()
