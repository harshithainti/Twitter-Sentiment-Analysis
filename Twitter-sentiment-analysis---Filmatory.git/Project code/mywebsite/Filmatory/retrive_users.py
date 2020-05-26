from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.last_login)
