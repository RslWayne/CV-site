from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
# Create your tests here.

class ResumeTest(APITestCase):

    def setUp(self):
        self.register_url = reverse('create')
        self.user = User.objects.create(username='Rasul Wayne')

    def test_user_create(self):
        data = {

                "full_name": "Rasul Wayne",
                "email": "rmambetaliev@gmail.com",
                "phone": 777456666,
                "address": "China/Shanghai",
                "age": 21,
                "gender": "M",
                "bio": "Millionaire/philanthropist/playboy",
                "user": self.user.pk
            }
        self.response = self.client.post(self.register_url,data)
        print(self.response.data)
        self.assertEqual(self.response.status_code,status.HTTP_201_CREATED)

    def test_with_bad_email(self):
        data = {
                "full_name": "Rasul Wayne",
                "email": "rmambetagmail.com",
                "phone": 777456666,
                "address": "China/Shanghai",
                "age": 21,
                "gender": "M",
                "bio": "Millionaire/philanthropist/playboy",
                "user": self.user.pk
             }
        self.response = self.client.post(self.register_url,data)
        print(self.response.data)
        self.assertEqual(self.response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_with_bad_e(self):
        data = {
            "full_name": "Rasul Wayne",
            "email": "rmambeta@gmail.com",
            "phone": 777456666,
            "address": "China/Shanghai",
            "age": "hjkhkjhkj",
            "gender": "M",
            "bio": "Millionaire/philanthropist/playboy",
            "user": self.user.pk
        }
        self.response = self.client.post(self.register_url, data)
        print(self.response.data)
        self.assertContains(self.response,'valid integer',status_code=400)

    def test_with_bad_e1(self):

        data = {
            "full_name": "Rasul Wayne",
            "email": "rmambeta@gmail.com",
            "phone": 777456666,
            "address": "China/Shanghai",
            "age": 23,
            "gender": "ihhuhuhi",
            "bio": "Millionaire/philanthropist/playboy",
            "user": self.user.pk
        }
        self.response = self.client.post(self.register_url, data)
        print(self.response.data)
        # self.assertEqual(self.response,'valid integer',status_code=400)