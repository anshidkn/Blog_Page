from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
import random


class Command(BaseCommand):
    help = "Creates 20 unique users with fake names and emails."

    def handle(self, *args, **options):
        fake = Faker()
        Faker.seed(1234)  

        for i in range(20):
           
            while True:
                email = fake.email()
                if not User.objects.filter(email=email).exists():
                    break

            
            username = email.split("@")[0]

         
            password = fake.password()
            user = User.objects.create_user(username=username, email=email, password=password)

       
            user.first_name = fake.first_name()
            user.last_name = fake.last_name()
            user.save()

           
            print(f"Created user {i+1}: {user.first_name} {user.last_name} ({user.email}) with password '{password}'")
