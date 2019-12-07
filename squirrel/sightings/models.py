from django.db import models
from django.utils.translation import gettext as _
class Squirrel(models.Model):
    longitude = models.FloatField(
        help_text=_('Longitude'),
    )
    latitude = models.FloatField(
        help_text=_('Latitude'),
    )
    unique_squirrel_id=models.CharField(
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
    date = models.DateField(
        help_text=_('Date'),
    )
    # ???not finished
    hectare_squirrel_number = models.CharField(
        help_text=_('The number of squirrels per hectare'),
        max_length=10,
    )
    
    # others use ''??? 
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    OTHERS = ''
    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'JUVENILE'),
        (OTHERS, ''),
    )
    age  = models.CharField(
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
    primary_fur_color  = models.CharField(
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
    location = models.CharField(
        help_text=_('Location of the squirrel'),
        max_length=20,
        choices=LOCATION_CHOICES,
        default=OTHERS,
    )
    
    specific_location = models.CharField(
            help_text = _('Specific Location'),
            max_length=30,
    )
    running = models.BooleanField(
        default=False,
    )
    chasing = models.BooleanField(
        default=False,
    )
    climbing = models.BooleanField(
        default=False,
    )
    eating = models.BooleanField(
        default=False,
    )
    foraging = models.BooleanField(
        default=False,
    )
    other_activities = models.CharField(
        help_text=_('Other activities squirrel is doing except those mentioned'),
        max_length=30,
    )
    kuks = models.BooleanField(
        default=False,
    )
    quaas = models.BooleanField(
        default=False,
    )
    moans = models.BooleanField(
        default=False,
    )
    tail_flags = models.BooleanField(
        default=False,
    )
    tail_twitches = models.BooleanField(
        default=False,
    )
    approaches = models.BooleanField(
        default=False,
    )
    indifferent = models.BooleanField(
        default=False,
    )
    runs_from = models.BooleanField(
        default=False,
    )
    def __str__(self):
        return self.unique_squirrel_id

