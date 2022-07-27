from django.db import models
from django.urls import reverse
import uuid

class Producer(models.Model):
    name = models.CharField('Brand', max_length=200, help_text='Enter the Name of the Producer (e.g. Lamberet)', null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producer"
        verbose_name_plural = "Producers"


class Trailer(models.Model):

    type = models.CharField('Type', max_length=200, null=True, blank=True)
    features = models.ForeignKey('Features', on_delete=models.SET_NULL, null=True, related_name='trailers')
    summary = models.TextField('Summary', max_length=1000, help_text='Other information', null=True, blank=True)
    platenr = models.CharField('Plate number', max_length=5, help_text='Plate number', null=True, blank=True)
    producer = models.ManyToManyField(Producer, help_text='Enter the Name of the producer')

    def __str__(self):
        return self.type
    
    def get_absolute_url(self):
        return reverse('trailer-detail', args=[str(self.id)])

    def display_producer(self):
        return ', '.join(producer.name for producer in self.producer.all()[:3])
    
    display_producer.short_description = "Producer"


class TrailerInstance(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Dispatchers ID for the Trailer')
    trailer = models.ForeignKey('Trailer', on_delete=models.SET_NULL, null=True) 
    dexpected_return = models.DateField('Will be available', null=True, blank=True)

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
        default='res',
        help_text='Statusas',
    )

    class Meta:
        ordering = ['dexpected_return']

    def __str__(self):
        return f'{self.id} ({self.trailer.type})'


class Features(models.Model):
    
    volume = models.CharField('Volume m3', max_length=2)
    axles = models.CharField('Number of axles', max_length=1)

    class Meta:
        ordering = ['axles', 'volume']

    def get_absolute_url(self):
        
        return reverse('trailer-detail', args=[str(self.id)])

    def display_trailers(self):
        return ', '.join(trailer.type for trailer in self.trailers.all()[:3])

    display_trailers.short_description = 'Trailers'    
    

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.axles} {self.volume}'