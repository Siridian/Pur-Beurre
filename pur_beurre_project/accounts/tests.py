from django.test import TestCase
from django.test.client import Client

from .models import User, UserManager
from substituter.models import Product

# Models

class TestUserModel(TestCase):
    def test_attributes(self):
        user = User.objects.create(email='test@user.model',
                                   first_name="usermodelname",
                                   password="testpass"
        )
        p = Product.objects.create(name="productname")
        user.bookmarks.add(p)

        self.assertTrue(isinstance(user, User))
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.password), str)
        self.assertTrue(isinstance(user.bookmarks.all()[0], Product))


# Views

class TestViewSignup(TestCase):
    def test_signup_works(self):
        response = self.client.post("/accounts/signup/", {
            'email': 'test@signup.works',
            'first_name': 'testworks',
            'password1': 'testpass',
            'password2': 'testpass'
            }
        )

        self.assertEqual(User.objects.get(email='test@signup.works').first_name,
                                          "testworks"
        )

    def test_signup_redirects(self):

        response = self.client.post("/accounts/signup/", {
            'email': 'test@signup.redirects',
            'first_name': 'testfn',
            'password1': 'testpass',
            'password2': 'testpass'
            }
        )

        self.assertRedirects(response, 
                             "/", 
                             status_code=302, 
                             target_status_code=200
        )
        self.assertIn('_auth_user_id', self.client.session)

    def test_signup_fails(self):
        response = self.client.post("/accounts/signup/", {
            'email': 'testmailsignupredirects',
            'first_name': 'testfn',
            'password1': 'testpass',
            'password2': 'testpass'
            }
        )

        self.assertEqual(response.status_code, 200)       
        

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