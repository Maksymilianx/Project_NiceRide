import pytest
from django.contrib.auth.models import User

from NiceRide.models import Car, Opinions


@pytest.fixture
def user():
    u = User()
    u.username = 'uzytkownik'
    u.set_password('haslohaslo')
    u.save()
    return u


@pytest.fixture
def messages(user):
    msg = []
    for x in range(10):
        m = Messages()
        m.content = 'jakis content'
        m.from_user = user
        m.save()
        msg.append(m)
    return msg