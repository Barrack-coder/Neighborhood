from django.test import TestCase
from .models import neighbourhood,healthservices
from django.contrib.auth.models import User
import datetime as dt

# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Madaraka = neighbourhood(neighbourhood='Madaraka')

    def test_instance(self):
        self.assertTrue(isinstance(self.Madaraka,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Madaraka.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Madaraka.delete_neighbourhood('Madaraka')
        hood = neighbourhood.objects.all()
	self.assertTrue(len(hood)==0)