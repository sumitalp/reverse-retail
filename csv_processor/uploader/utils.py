from datetime import datetime
from django.conf import settings


def handle_uploaded_file(f):
    """
    This method is responsible for uploading file at target folder.
    Returns file object.
    """
    now = datetime.now().strftime("%m%d%Y%H%M%S")
    with open(f"{settings.MEDIA_ROOT}/{now}_{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        return destination
    return ""
