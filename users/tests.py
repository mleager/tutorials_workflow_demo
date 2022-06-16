from django.test import TestCase
from django.urls import reverse
import pytest

# Create your tests here.

# Create a fixture function that will create a test user
@pytest.fixture
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return "test_username", "test_password"     # this returns a tuple

# Create a test function that tests logging into the app
def test_login_user(client, test_user):
    test_username, test_password = test_user    # unpack the tuple
    login_result = client.login(username=test_username, password=test_password)
    assert login_result == True
