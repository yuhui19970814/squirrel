from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

class squirrels(models.Model):
    Longitude= models.DecimalField(
        help_text='Longitude',
        max_digits=20,
        decimal_places=10)
    
    Latitude=models.DecimalField(
        help_text='Latitude',
        max_digits=20,
        decimal_places=10)
    
    Unique_Squirrel_ID=models.CharField(
        help_text=_('Unique_squirrel_id'),
        max_length=50,
    )
    AM = 'AM'
    PM = 'PM'
    OTHERS=''
    SHIFT_CHOICES = (
        (AM,'AM'),
        (PM,'PM'),
        (OTHERS,''),
    )
    shift=models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES,
        default=OTHERS,
    )
    Date = models.DateField(
        help_text=_('Date'),
    )
    
    
    
  
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    OTHERS = ''
    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'JUVENILE'),
        (OTHERS, ''),
    )
    Age  = models.CharField(
        help_text=_('Age of the squirrel'),
        max_length=10,
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
        help_text=_('Primary fur color'),
        max_length=10,
        choices=COLOR_CHOICES,
        default=OTHERS,
    )
    GROUND_PLANE = 'ground plane'
    ABOVE_GROUND = 'above ground'
    OTHERS = ''
    LOCATION_CHOICES = (
        (GROUND_PLANE, 'ground plane'),
        (ABOVE_GROUND, 'above ground'),
        (OTHERS, ''),
    )
    Location = models.CharField(
        help_text=_('Location of the squirrel'),
        max_length=20,
        choices=LOCATION_CHOICES,
        default=OTHERS,
    )
    
    Specific_location = models.CharField(
            help_text = _('Specific Location'),
            max_length=30,
    )
    Running = models.BooleanField(
        default=False,
    )
    Chasing = models.BooleanField(
        default=False,
    )
    Climbing = models.BooleanField(
        default=False,
    )
    Eating = models.BooleanField(
        default=False,
    )
    Foraging = models.BooleanField(
        default=False,
    )
    Other_Activities = models.CharField(
        help_text=_('Other activities squirrel is doing except those mentioned'),
        max_length=30,
    )
    Kuks = models.BooleanField(
        default=False,
    )
    Quaas = models.BooleanField(
        default=False,
    )
    Moans = models.BooleanField(
        default=False,
    )
    Tail_flags = models.BooleanField(
        default=False,
    )
    Tail_twitches = models.BooleanField(
        default=False,
    )
    Approaches = models.BooleanField(
        default=False,
    )
    Indifferent = models.BooleanField(
        default=False,
    )
    Runs_from = models.BooleanField(
        default=False,
    )
    def __str__(self):
        return self.Unique_Squirrel_ID

