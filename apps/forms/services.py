from apps.parish.models import ContactSubmission


def create_contact_submission(**data):
    return ContactSubmission.objects.create(**data)
