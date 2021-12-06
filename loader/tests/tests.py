import pytest
from django.urls import reverse

from image.models import Image

CREATE_USER_URL = reverse("user")
ADD_IMAGE_URL = reverse("image")


pytestmark = pytest.mark.django_db


class TestLoaderAPI:
    def test_create_user_url(self, guest_client):
        url = CREATE_USER_URL
        data = {"username": "Testy", "email": "test@test6.ru", "password": "testtest"}
        response = guest_client.post(url, data=data)
        assert response.status_code == 201, (
            f"Проверьте, что при POST запросе {url} " f"возвращается " f"статус 200"
        )

    def test_image_url_for_authorized_client(self, authorized_client, image):
        """An authorized user is allowed access"""
        url = ADD_IMAGE_URL
        data = {"[0]image": image}

        response = authorized_client.post(url, data, format="multipart")
        assert response.status_code == 201, (
            f"Проверьте, что при POST запросе {url} " f"возвращается " f"статус 201"
        )

    def test_image_url_for_guest_client(self, guest_client, image):
        """Unauthorized user is not allowed access"""
        url = ADD_IMAGE_URL
        data = {"[0]image": image}

        response = guest_client.post(url, data, format="multipart")
        assert response.status_code == 403, (
            f"Проверьте, что при POST запросе {url} " f"возвращается " f"статус 201"
        )

    def test_image_create(self, authorized_client, image):
        url = ADD_IMAGE_URL
        data = {"[0]image": image}
        count_objects_in_db = Image.objects.all().count()
        response = authorized_client.post(url, data, format="multipart")
        count_objects_in_db_after_request = Image.objects.all().count()
        assert count_objects_in_db_after_request == count_objects_in_db + 1, (
            f"Проверьте, что при POST запросе {url} " f"создается объект Image"
        )
