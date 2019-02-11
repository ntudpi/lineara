from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True)
    material_type = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    photo = models.ImageField(upload_to='photo', blank=True, null=True, default='default.png')
    drawing = models.ImageField(upload_to='drawing', blank=True, null=True, default='default.png')
    transcription = models.ImageField(upload_to='transcription', blank=True, null=True, default='default.png')

    def __str__(self):
        return str(self.id) + " - " + self.name
