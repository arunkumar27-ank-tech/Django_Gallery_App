from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    images = models.ImageField(null=False, blank=False)
    description = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.description

        