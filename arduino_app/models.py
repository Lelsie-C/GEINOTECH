from django.db import models

# Create your models here.
class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='icons/')  # Requires `Pillow` library for image handling
    link = models.URLField()

class Update(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='icons/', blank=True)  # Requires `Pillow` library for image handling
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

