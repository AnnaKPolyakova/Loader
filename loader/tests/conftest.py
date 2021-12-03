import shutil
import tempfile

import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient

User = get_user_model()
NAME = "Test_name"
EMAIL = "test_email@test.com"
PASSWORD = "pass"
SMALL_GIF = (
    b"\x47\x49\x46\x38\x39\x61\x01\x00"
    b"\x01\x00\x00\x00\x00\x21\xf9\x04"
    b"\x01\x0a\x00\x01\x00\x2c\x00\x00"
    b"\x00\x00\x01\x00\x01\x00\x00\x02"
    b"\x02\x4c\x01\x00\x3b"
)


@pytest.fixture
def user():
    return User.objects.create_user(NAME, EMAIL, PASSWORD)


@pytest.fixture
def image():
    return SimpleUploadedFile(
        name="small.gif", content=SMALL_GIF, content_type="image/gif"
    )


@pytest.fixture
def guest_client(user):
    client = APIClient()
    return client


@pytest.fixture
def authorized_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture(scope="session", autouse=True)
def override_setting_media_root():
    """Override settings media root."""
    settings.MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    """Cleanup a testing directory once we are finished."""

    def remove_test_dir():
        shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=False)

    request.addfinalizer(remove_test_dir)
