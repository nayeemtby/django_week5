from django.db import models

# Create your models here.

instruments = [
    ('Guiter', 'Guiter'),
    ('Violin', 'Violin'),
    ('Piano', 'Piano')
]


class Musician(models.Model):
    firstName = models.CharField(max_length=30, verbose_name='First Name')
    lastName = models.CharField(max_length=30, verbose_name='Last Name')
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=15, verbose_name='Phone Number')
    instrument = models.CharField(
        max_length=30,
        verbose_name='Instrument Type',
        choices=instruments
    )

    def __str__(self) -> str:
        return self.firstName+' '+self.lastName + '@'+self.phone
        
