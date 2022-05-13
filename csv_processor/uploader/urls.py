from django.urls import path
from .views import FileUploadViewSet, UploaderView


urlpatterns = [
    path('', UploaderView.as_view(), name="upload-form"),
    path('add/', FileUploadViewSet.as_view({"post": "create"}), name='file-upload'),
]