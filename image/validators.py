from django.core.exceptions import ValidationError

LIMIT_KB = 20099


def validate_image(image):
    if image.size > LIMIT_KB * 1024:
        raise ValidationError("Image file too large ( > 200kb )")
    return image
