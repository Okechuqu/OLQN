from decimal import Decimal


def registration_total(event, quantity: int) -> Decimal:
    return event.ticket_price * quantity
