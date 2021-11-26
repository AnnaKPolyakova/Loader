from django.contrib.auth import get_user_model
from django.db import models

from image.validators import validate_image

User = get_user_model()


class Image(models.Model):
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Изображение",
        help_text="Загрузите фотографию",
        validators=[validate_image],
    )

    user = models.ForeignKey(
        User,
        verbose_name="Автор изображения",
        related_name="user",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
