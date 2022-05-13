from factory import fuzzy
from django.urls import reverse_lazy

class TestUploader:
    def test_add_image_file(self, client, image):
        url = reverse_lazy("uploader:file-upload")
        data = {
            "file": image
        }
        response = client.post(url, data)
        assert response.status_code == 400
        response_data = response.json()
        assert "Allowed extensions are: csv." in response_data.get("file")[0]

    def test_add_wrong_file(self, client, wrong_csv_file):
        url = reverse_lazy("uploader:file-upload")
        cfile = open(wrong_csv_file, "rb")
        data = {
            "file": cfile.read()
        }
        response = client.post(url, data)
        assert response.status_code == 400
        response_data = response.json()
        assert "The submitted data was not a file. Check the encoding type on the form." in response_data.get("file")[0]


    def test_add_file_success(self, client, csv_file):
        url = reverse_lazy("uploader:file-upload")
        data = {
            "file": csv_file
        }
        response = client.post(url, data)
        assert response.status_code == 201


    def test_add_file_with_wrong_method(self, client, csv_file):
        url = reverse_lazy("uploader:file-upload")
        data = {
            "file": csv_file
        }
        response = client.put(url, data)
        assert response.status_code == 405