from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=1.0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    slug = models.CharField(unique=True, max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f"{self.title} - {self.author}")
        super().save(force_insert, force_update, using, update_fields)



