from django.core.management.base import BaseCommand, CommandError
from mainapp.helpers import test


class Command(BaseCommand):
    help = 'Parse Wiki Data into DB'

    def handle(self, *args, **options):
        print('Starting...')
        try:
            test()
        except:
            raise CommandError("Something went wrong please see mainapp/helpers.py")
        print('Added successfully')
        return
