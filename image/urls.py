from django.urls import include, path

from image.views import ImageCreateAPIView, UserCreateAPIView

extra_patterns = [
    path("auth/user/", UserCreateAPIView.as_view(), name="user"),
    path("image/", ImageCreateAPIView.as_view(), name="image"),
]

urlpatterns = [
    path("v1/", include(extra_patterns)),
]
