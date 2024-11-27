from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ROCK_PSYCHE = 'RP'
        TRIP_HOP = 'TH'

    
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices = Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

class Listing(models.Model):

    class Type(models.TextChoices):
       RECORDS = 'RC'
       CLOTHING = 'CG'
       POSTERS = 'PT'
       MISCELLANEOUS = 'MC'
    
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length = 2000)
    sold = models.fields.BooleanField(default=True)
    year = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    type = models.fields.CharField(choices = Type.choices, max_length=5)

