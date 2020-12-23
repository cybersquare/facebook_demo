from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework.test import APIClient
from rest_framework import status


class TestSample(TestCase):

    def setup(self):
        self.client = APIClient

    def test_index(self): #Method name should start with 'test'
        url = reverse('index')
        res = self.client.get(url)
        # print(res.data)
        self.assertEquals(res.status_code, 200 )
        self.assertEquals(res.data, 'Congratulations, you  have created an API' )

    def test_login(self): #Method name shoudl start with 'test'
        data = {
            "username": "user",
            "password": "pass",
        }
        url = reverse('user_login')
        res = self.client.post(url, data)
        # print(res.data)
        self.assertEquals(res.status_code, 200 )
        self.assertEquals(res.data, 'Login success' )

    
    def test_register(self): #Method name shoudl start with 'test'
        data = {
            "first_name": "George",
            "last_name": "Joseph",
            "gender":"Male",
            "dob":"2000-10-01",
            "email":"george123@baabte.com",
            "password":"password",
            "phone":"123456780",
        }
        url = reverse('user_register')
        res = self.client.post(url, data)
        # print(res.data)
        self.assertEquals(res.status_code, 200 )
        self.assertEquals(res.data, 'Successfully registered' )


    # def test_register(self): #Method name shoudl start with 'test'
    #     url = reverse('user_register')
    #     res = self.client.post(url, data)
    #     # print(res.data)
    #     self.assertEquals(res.status_code, 200 )
    #     self.assertEquals(res.data, 'Successfully registered' )






# command: python manage.py test app1