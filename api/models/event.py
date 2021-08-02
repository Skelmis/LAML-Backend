from django.db import models
from django.utils.text import slugify


class Event(models.Model):
    slug = models.SlugField(max_length=25, unique=True)
    title = models.TextField()
    description = models.TextField()
    item_type = models.CharField(max_length=100)
    item_max = models.PositiveSmallIntegerField(
        help_text="Soft max for slugs to crawl towards"
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.slug)

        super(Event, self).save(*args, **kwargs)
