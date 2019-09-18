from django.test import TestCase
from django.test.client import Client

from substituter.models import Product
from accounts.models import User

class TestViewBookmarked(TestCase):

    @classmethod 
    def setUpTestData(cls):
        p = Product.objects.create(name="testproduct")
        u = User.objects.create(email="testmail")
        u.set_password('testpass')
        u.save()
        u.bookmarks.add(p)
    
    def test_bookmarked_no_user_redirect(self):
        response = self.client.get("/bookmarks/bookmarked", follow=True)

        self.assertRedirects(response, 
                            "/accounts/login/?next=/bookmarks/bookmarked/", 
                            status_code=301, 
                            target_status_code=200
        )

    def test_bookmarked_user_200(self):
        c = Client()     
        c.login(email='testmail', password='testpass')

        response = c.get("/bookmarks/bookmarked", follow=True)

        self.assertEqual(response.status_code, 200)

    def test_bookmarked_gets_bookmarks(self):
        c = Client()     
        c.login(email='testmail', password='testpass')

        response = c.get("/bookmarks/bookmarked", follow=True)

        self.assertEqual(response.context['bookmark_list'][0].name,
                         "testproduct"
        )


class TestViewSave(TestCase):


    @classmethod
    def setUpTestData(cls):
        p = Product.objects.create(id=1, name="testname")
        cls.u = User.objects.create(email="testmail")
        cls.u.set_password('testpass')
        cls.u.save()
    
    def test_save_no_user_redirect(self):
        response = self.client.get("/bookmarks/save/1", follow=True)

        self.assertRedirects(response, 
                            "/accounts/login/?next=/bookmarks/save/1", 
                            status_code=302, 
                            target_status_code=200
        )

    def test_save_valid_id(self):
        c = Client()     
        c.login(email='testmail', password='testpass')

        response = c.get("/bookmarks/save/1", follow=True)

        self.assertEqual(User.objects.get(id=self.u.id).bookmarks.all()[0].name, 
                         "testname"
        )

    def test_save_invalid_id(self):
        c = Client()     
        c.login(email='testmail', password='testpass')

        response = c.get("/bookmarks/save/2", follow=True)

        self.assertEqual(response.status_code, 404)