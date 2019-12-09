from map.models import squirrels

import csv
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self,*args,**kargs):
        path=kargs['csv_file']
        with open(path) as f:
            reader = csv.DictReader(f)
            data=list(reader)
            for row in data:
                try:
                    p=squirrels(
                        Unique_Squirrel_ID=row['Unique Squirrel ID'],
                        Longitude=row['X'],
                        Latitude=row['Y'],
                        Shift=row['Shift'],
                        Date=row['Date'][4:]+'-'+row['Date'][:2]+'-'+row['Date'][2:4],
                        Age=row['Age'],
                        Primary_fur_color=row['Primary Fur Color'],
                        Location=row['Location'],
                        Specific_location=row['Specific Location'],
                        Running=row['Running'].capitalize(),
                        Chasing=row['Chasing'].capitalize(),
                        Climbing=row['Climbing'].capitalize(),
                        Eating=row['Eating'].capitalize(),
                        Foraging=row['Foraging'].capitalize(),
                        Other_Activities=row['Other Activities'],
                        Kuks=row['Kuks'].capitalize(),
                        Quaas=row['Quaas'].capitalize(),
                        Moans=row['Moans'].capitalize(),
                        Tail_flags=row['Tail flags'].capitalize(),
                        Tail_twitches=row['Tail twitches'].capitalize(),
                        Approaches=row['Approaches'].capitalize(),
                        Indifferent=row['Indifferent'].capitalize(),
                        Runs_from=row['Runs from'].capitalize(),

                    
                        )
                    p.save()
                except:
                    pass
