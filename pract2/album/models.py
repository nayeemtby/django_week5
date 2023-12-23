from django.db import models
from django.forms import ValidationError

from musician.models import Musician

# Create your models here.

def validate_rating(value):
    if value <1 or value > 5:
        raise ValidationError(
            ("Rating must be between 1 and 5 inclusive"),
        )


class Album(models.Model):
    name = models.CharField(max_length=30, verbose_name='Album Name')
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    released = models.DateField(verbose_name='Album Release Date')
    rating = models.DecimalField(
        decimal_places=2,
        max_digits=3,
        verbose_name='Rating',
        validators=[validate_rating],
    )

    def __str__(self) -> str:
        return self.name + ' by ' + self.musician.firstName
