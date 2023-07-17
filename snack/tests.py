from django.test import TestCase
from django.urls import  reverse
# Create your tests here.
from .models import Snack
class TestSnack(TestCase):
    
    def test_status_code(self):
        url = reverse('snack')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_template(self):
        url = reverse('snack')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

class TestSnack(TestCase):
    
    def test_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')



