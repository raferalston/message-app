from django.core.management.base import BaseCommand

from clients.models import ClientModel

class Command(BaseCommand):
    help = 'Populate clients db data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Begin populating db'))
        tag = 'even'
        for i in range(6):
            if not i % 2:
                tag = 'even'
            else:
                tag = 'odd'
            ClientModel.objects.create(
                phone=f'7999999999{i+1}',
                mobile_operator_code=f'{i}',
                tag=tag
                )

        self.stdout.write(self.style.SUCCESS('Done populating db'))