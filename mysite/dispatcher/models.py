from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
from django.db import models

class Trailer(models.Model):
    name = models.CharField('Type', max_length=200, help_text='Enter the Type of the trailer (e.g. Refrigerated Trailers)')
    
    def __str__(self):
        return self.name



class Truck(models.Model):
    
    plate = models.CharField('Plate number', max_length=6)
    producer = models.ForeignKey('Producer', on_delete=models.SET_NULL, null=True)
    summary = models.TextField('Summary', max_length=1000, help_text='Trumpas knygos aprašymas')
    vin = models.CharField('Vin code', max_length=17, help_text='17 characters <a href="https://www.autocheck.com/vehiclehistory/vin-basics')
    trailer = models.ManyToManyField(Trailer, help_text='Select the Type of the trailer')

    def __str__(self):
        return self.plate
    
    def get_absolute_url(self):
        """Nurodo konkretaus aprašymo galinį adresą"""
        return reverse('truck-detail', args=[str(self.id)])


class TruckInstance(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Dispatchers ID for the Truck')
    truck = models.ForeignKey('Truck', on_delete=models.SET_NULL, null=True) 
    expected_return = models.DateField('Will be available', null=True, blank=True)

    LOAN_STATUS = (
        ('ser', 'Service'),
        ('tri', 'Trip'),
        ('rea', 'Ready'),
        ('res', 'Reserved'),
    )

    status = models.CharField(
        max_length=3,
        choices=LOAN_STATUS,
        blank=True,
        default='s',
        help_text='Status',
    )

    class Meta:
        ordering = ['expected_return']

    def __str__(self):
        return f'{self.id} ({self.truck.plate})'


class Producer(models.Model):
    
    brand = models.CharField('Brand', max_length=100)
    country = models.CharField('country', max_length=100)

    class Meta:
        ordering = ['country', 'brand']

    def get_absolute_url(self):
        """Returns the url to access a particular producer instance."""
        return reverse('producer-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.country} {self.brand}'