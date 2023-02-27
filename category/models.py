from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    decription = models.CharField(max_length=128)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
    def __str__(self):
        return f'{self.category_name}'

