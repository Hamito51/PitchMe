from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


def create_user(username: str, password: str, email: str, is_active: bool) -> User:
    password = make_password(password)
    user = User(username=username, password=password, email=email, is_active=is_active)
    user.full_clean()
    user.save()
    return user


def sign_up(username: str, email: str, password: str, *args, **kwargs) -> User:
    user = create_user(username=username, email=email, password=password, is_active=True)
    return user
