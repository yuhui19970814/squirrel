from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class squirrels(models.Model):
    Unique_Squirrel_ID=models.CharField(
        max_length=20,)
    Longitude= models.DecimalField(
        max_digits=15,
        decimal_places=10)
    Latitude=models.DecimalField(
        max_digits=15,
        decimal_places=10)
    
    AM = 'AM'
    PM = 'PM'
    OTHERS=''
    SHIFT_CHOICES = (
        (AM,'AM'),
        (PM,'PM'),
        (OTHERS,''),
    )
    
    Shift=models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        default=OTHERS,
    )
    
    Date=models.DateField(,
        blank=True,
        null=True,
        max_length=30,
        default=timezone.now)
    
    
    
  
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    OTHERS = ''
    
    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'JUVENILE'),
        (OTHERS, ''),
    )
    
    Age  = models.CharField(
        max_length=5,
        choices=AGE_CHOICES,
        default=OTHERS,
    )
    
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    OTHERS = ''
    COLOR_CHOICES = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
        (OTHERS, ''),
    )
    
    Primary_fur_color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        default=OTHERS,
    )
    

    Location = models.CharField(
        max_length=30,
        choices=LOCATION_CHOICES,
        default=OTHERS,
    )
    
    Specific_location = models.CharField(
            max_length=20,
    )
    
    GROUND_PLANE = 'on the ground'
    ABOVE_GROUND = 'above the ground'
    OTHERS = ''
    LOCATION_CHOICES = (
        (GROUND_PLANE, 'on the ground'),
        (ABOVE_GROUND, 'above the ground'),
        (OTHERS, ''),
    )
    
    Eat = models.BooleanField(
        default=None,
    )
    Forage = models.BooleanField(
        default=None,
    )
    Runs_from = models.BooleanField(
        default=None,
    )
    Run= models.BooleanField(
        default=None,
    )
    Chase = models.BooleanField(
        default=None,
    )
    Tail_flags = models.BooleanField(
        default=None,
    )
    Tail_twitches = models.BooleanField(
        default=None,
    )
    Approaches = models.BooleanField(
        default=None,
    )
    Indifferent = models.BooleanField(
        default=None,
    )
    Other_Activities = models.CharField(
        max_length=50,
    )
    Kuks = models.BooleanField(
        default=None,
    )
    Quaas = models.BooleanField(
        default=None,
    )
    Moans = models.BooleanField(
        default=None,
    )

    Climbing = models.BooleanField(
        default=None,
    )
    
    def __str__(self):
        return self.Unique_Squirrel_ID

