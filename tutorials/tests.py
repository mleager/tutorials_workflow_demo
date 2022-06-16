from django.test import TestCase
from django.urls import reverse
import pytest
from tutorials.models import Tutorial

# Create your tests here.

# Unit test for URL of "home" index
def test_homepage_access():
    url = reverse('home')
    assert url == "/"

# Integration test - interat with DB via Django models/ORMs
# 1st Example
"""
@pytest.mark.django_db
def test_create_tutorial():
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html' ,
        description='Tutorial on how to apply pytest to a Django application.',
        published=True
    )
    assert tutorial.title == "Pytest"
"""
# ---------------------------------------------------

# Reconfigure 1st Example to a fixture that will
# create a Tutorial object
@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial 

# ---------------------------------------------


# Create a new fixture funtion
@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

# add a test function that uses both fixtures
def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk

# -----------------------------------------


# Test functions to be used with the new_tutorial fixture
def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()