import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()


import random
from faker import Faker
from AppTwo.models import User

fake = Faker()


def populate(N=5):
    """
    Fn: fill database with fake data
    Arg: N as an integer to represent how many entries | 5 default
    Ret: null
    """
    for entry in range(N):
        fake_name = fake.name().split(' ')
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fake.email()
        usr = User.objects.get_or_create(first_name=fake_first_name,
                                         last_name=fake_last_name,
                                         email=fake_email)[0]
        usr.save()

if __name__=='__main__':
    print('Starting populate()')
    populate(20)
    print('Finished populate()')
