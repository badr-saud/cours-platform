import helpers
from django.db import models
from cloudinary.models import CloudinaryField

helpers.cloudinary_init()


# Create your models here.
class AccessRequirements(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email", "Wmail required"


class publishStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"


def handle_upload(instance, filename):
    return f"{filename}"


class Course(models.Model):
    pass
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    image = CloudinaryField("image", null=True)
    access = models.CharField(
        max_length=5,
        choices=AccessRequirements.choices,
        default=AccessRequirements.EMAIL_REQUIRED,
    )
    status = models.CharField(
        max_length=5, choices=publishStatus.choices, default=publishStatus.DRAFT
    )

    @property
    def is_published(self):
        return self.status == publishStatus.PUBLISHED
