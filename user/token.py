from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.get(username='Diako888')
token = Token.objects.get(user=user)

print(f"Token for {user.username}: {token.key}")
