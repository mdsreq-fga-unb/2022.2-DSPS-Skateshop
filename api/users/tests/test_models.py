import pytest

from ..models import User

pytestmark = pytest.mark.django_db


def test_create_user():
    user = User.objects.create_user(
        username='user', email='user@gmail.com', password='passw0rd'
    )

    assert user.username == 'user'
    assert user.email == 'user@gmail.com'
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


def test_create_superuser():
    user = User.objects.create_superuser(
        username='admin', email='admin@gmail.com', password='passw0rd'
    )

    assert user.username == 'admin'
    assert user.email == 'admin@gmail.com'
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser
