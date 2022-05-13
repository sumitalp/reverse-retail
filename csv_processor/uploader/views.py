import logging
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.views.generic import TemplateView

from .serializers import FileSerializer
from .utils import handle_uploaded_file
from .tasks import process_csv


logger = logging.getLogger(__name__)


class FileUploadViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        path = handle_uploaded_file(request.FILES['file'])
        if path:
            # Though it's a long running task, system should call celery here
            process_csv.delay(path.name)
            logger.info("Celery task has called and will return success message.")
            return Response({"detail": f"File has uploaded successfully at {path.name}"}, status=status.HTTP_201_CREATED)
        logger.error("Failed to upload file at target folder.")
        return Response({"detail": "File is not uploaded at destination."}, status=status.HTTP_400_BAD_REQUEST)


class UploaderView(TemplateView):
    template_name = "uploader/uploader_form.html"
