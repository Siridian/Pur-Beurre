from django.test import TestCase
from django.test.client import Client

from .models import User


class TestViewSignup(TestCase):
    def test_signup_works(self):
        response = self.client.post("/accounts/signup", {
            'email': 'testmail',
            'first_name': 'testfn',
            'password1': 'testpass',
            'password2': 'testpass'
            }
        )


class TestViewDashboard(TestCase):

    @classmethod 
    def setUpTestData(cls):
        u = User.objects.create(email="testmail")
        u.set_password('testpass')
        u.save()
    
    def test_dashboard_no_user_redirect(self):
        response = self.client.get("/accounts/dashboard", follow=True)

        self.assertRedirects(response, 
                            "/accounts/login/?next=/accounts/dashboard/", 
                            status_code=301, 
                            target_status_code=200
        )

    def test_dashboard_user_200(self):
        c = Client()     
        c.login(email='testmail', password='testpass')

        response = c.get("/accounts/dashboard/", follow=True)

        self.assertEqual(response.status_code, 200)

    def test_dashboard_gets_user(self):
        c = Client()     
        c.login(email='testmail', password='testpass')

        response = c.get("/accounts/dashboard", follow=True)

        self.assertEqual(response.context['user'].email, "testmail")