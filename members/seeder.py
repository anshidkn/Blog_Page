from faker import Faker
from members.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

fake = Faker()
def generate_users(num):
    for _ in range(num):
        user = User.objects.create_user(
            username = fake.user_name(),
            password=fake.password(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email()

        )
        user.save()
    
