from django.urls import include, path

from image.views import ImageCreateAPIView, UserCreateAPIView

extra_patterns = [
    path("auth/users/", UserCreateAPIView.as_view()),
    path("image/", ImageCreateAPIView.as_view()),
]

urlpatterns = [
    path("v1/", include(extra_patterns)),
]
