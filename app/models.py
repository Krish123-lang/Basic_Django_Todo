import uuid
from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Blog(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    new_slug = AutoSlugField(populate_from='title', null=True, unique=True, default=None)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
