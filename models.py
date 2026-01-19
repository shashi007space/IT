from django.db import models
from django.utils.text import slugify

class Platform(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    logo = models.ImageField(upload_to='platform_logos/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Folder(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='folders')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Link(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='links')
    folder = models.ForeignKey(Folder, on_delete=models.SET_NULL, null=True, blank=True, related_name='links')
    title = models.CharField(max_length=150)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
