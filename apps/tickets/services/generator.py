from secrets import token_urlsafe


def ticket_token():
    return token_urlsafe(24)
