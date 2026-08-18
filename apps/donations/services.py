from .models import Donation


def create_pending_donation(**data):
    return Donation.objects.create(status=Donation.Status.PENDING, **data)
