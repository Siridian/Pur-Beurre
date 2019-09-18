from django.test import TestCase
from django.urls import reverse

from .views import index, detail, legal
from .models import Product, Category


class TestViewIndex(TestCase):
    
    def test_index_200(self):
        response = self.client.get(reverse(index))

        self.assertEqual(response.status_code, 200)


class TestViewDetail(TestCase):

    @classmethod  # <- setUpClass doit être une méthode de classe, attention !
    def setUpTestData(cls):
        Product.objects.create(id = 1,
                               name = "testname",
                               grade = "a",
                               link = "testurl.com",
                               description = "testdescription",
                               image = "testurl.com"
        )

    def test_legal_valid_id(self):
        response = self.client.get("/substituter/detail/1", follow=True)

        self.assertEqual(response.status_code, 200)

    def test_legal_invalid_id(self):
        response = self.client.get("/substituter/detail/2", follow=True)

        self.assertEqual(response.status_code, 404)

    def test_legal_correct_context(self):
        response = self.client.get("/substituter/detail/1", follow=True)

        self.assertEqual(response.context['product'].name, "testname")


class TestViewLegal(TestCase):

    def test_legal_200(self):
        response = self.client.get("/substituter/legal/")

        self.assertEqual(response.status_code, 200)