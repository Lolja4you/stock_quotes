from core.management.base import BaseCommand

class Command(BaseCommand):
    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)
        ...
    def execute(self, *args, **options):
        # выполнять код тут
        print('Meow ^_^')
        print('run')
        return super().execute(*args, **options)
    
    def handle(self, *args, **options):
        # перехватывать ошибки и состояния тут
        ...
    