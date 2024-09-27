from django.db import models

# Create your models here.


class AccessRequirements(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email_required", "Wmail required"


class publishStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"


class Course(models.Model):
    pass
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    # image =
    access = models.CharField(
        max_length=10,
        choices=AccessRequirements.choices,
        default=AccessRequirements.ANYONE,
    )
    status = models.CharField(
        max_length=10, choices=publishStatus.choices, default=publishStatus.DRAFT
    )

    @property
    def is_published(self):
        return self.status == publishStatus.PUBLISHED
