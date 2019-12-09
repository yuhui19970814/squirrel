# Generated by Django 3.0 on 2019-12-09 22:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squirrels',
            name='Shift',
        ),
        migrations.AddField(
            model_name='squirrels',
            name='shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM'), ('', '')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Age',
            field=models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'JUVENILE'), ('', '')], default='', help_text='Age of the squirrel', max_length=10),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Approaches',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Chasing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Climbing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, help_text='Date', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Eating',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Foraging',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Indifferent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Kuks',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Latitude',
            field=models.DecimalField(decimal_places=10, help_text='Latitude', max_digits=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Location',
            field=models.CharField(choices=[('ground plane', 'ground plane'), ('above ground', 'above ground'), ('', '')], default='', help_text='Location of the squirrel', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Longitude',
            field=models.DecimalField(decimal_places=10, help_text='Longitude', max_digits=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Moans',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Other_Activities',
            field=models.CharField(help_text='Other activities squirrel is doing except those mentioned', max_length=30),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Primary_fur_color',
            field=models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black'), ('', '')], default='', help_text='Primary fur color', max_length=10),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Quaas',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Running',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Runs_from',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Specific_location',
            field=models.CharField(help_text='Specific Location', max_length=30),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Tail_flags',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Tail_twitches',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Unique_Squirrel_ID',
            field=models.CharField(help_text='Unique_squirrel_id', max_length=50),
        ),
    ]
