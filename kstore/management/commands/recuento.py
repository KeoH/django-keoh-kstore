#encoding:utf-8
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Hola, este es el primer comando!")
