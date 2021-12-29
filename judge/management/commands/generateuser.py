from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from judge.models import Language, Profile


class Command(BaseCommand):
    help = 'generate a user'

    def add_arguments(self, parser):
        parser.add_argument('directory', help='directory')
        parser.add_argument('password', help='password for the user')
        parser.add_argument('language', nargs='?', default=settings.DEFAULT_USER_LANGUAGE,
                            help='default language ID for user')

    def handle(self, *args, **options):
        files = open(options['directory'], 'r')
        line = files.readline()
        while True:
            if not line:
                break
            name = line.split("@")[0]
            name = name.split(".").join("")
            try:
                usr = User(username=name, email=line, is_active=True)
                usr.set_password(options['password'])
                usr.save()

                profile = Profile(user=usr)
                profile.language = Language.objects.get(key=options['language'])
                profile.save()
                line = files.readline()
            except:
                line = files.readline()
        files.close()
