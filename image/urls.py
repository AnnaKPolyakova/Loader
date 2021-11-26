from django.urls import include, path

from image.views import UserCreateAPIView

extra_patterns = [
    path("auth/users/", UserCreateAPIView.as_view()),
]

urlpatterns = [
    path("v1/", include(extra_patterns)),
]