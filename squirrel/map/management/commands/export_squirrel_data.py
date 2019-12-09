import csv
from map.models import squirrels
from django.core.management import BaseCommand
from django.utils.encoding import smart_str
class Command(BaseCommand):
    help = 'Load a questions csv file into the database'
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    def handle(self,*args,**kargs):
        path=kargs['csv_file']
        with open(path, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow([
                smart_str(u"Unique_Squirrel_ID"),
                smart_str(u"Longitude"),
                smart_str(u"Latitude"),
                smart_str(u"Shift"),
                smart_str(u"Date"),
                smart_str(u"Age"),
                smart_str(u"Primary_fur_color"),
                smart_str(u"Location"),
                smart_str(u"Specific_location"),
                smart_str(u"Running"),
                smart_str(u"Chasing"),
                smart_str(u"Climbing"),
                smart_str(u"Eating"),
                smart_str(u"Foraging"),
                smart_str(u"Other_Activities"),
                smart_str(u"Kuks"),
                smart_str(u"Quaas"),
                smart_str(u"Moans"),
                smart_str(u"Tail_flags"),
                smart_str(u"Tail_twitches"),
                smart_str(u"Approaches"),
                smart_str(u"Indifferent"),
                smart_str(u"Runs_from"),    
                ])
            for obj in squirrels.objects.values():
                spamwriter.writerow([
                    smart_str(obj['Unique_Squirrel_ID']),
                    smart_str(obj["Longitude"]),
                    smart_str(obj["Latitude"]),
                    smart_str(obj["Shift"]),
                    smart_str(obj["Date"]),
                    smart_str(obj["Age"]),
                    smart_str(obj["Primary_fur_color"]),
                    smart_str(obj["Location"]),
                    smart_str(obj["Specific_location"]),
                    smart_str(obj["Running"]),
                    smart_str(obj["Chasing"]),
                    smart_str(obj["Climbing"]),
                    smart_str(obj["Eating"]),
                    smart_str(obj["Foraging"]),
                    smart_str(obj["Other_Activities"]),
                    smart_str(obj["Kuks"]),
                    smart_str(obj["Quaas"]),
                    smart_str(obj["Moans"]),
                    smart_str(obj["Tail_flags"]),
                    smart_str(obj["Tail_twitches"]),
                    smart_str(obj["Approaches"]),
                    smart_str(obj["Indifferent"]),
                    smart_str(obj["Runs_from"]),])
