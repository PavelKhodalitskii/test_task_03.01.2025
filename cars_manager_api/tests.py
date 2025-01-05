from django.test import TestCase
from rest_framework.test import APIRequestFactory

from cars_manager.tests import UserAuthTestMixin, TestDataBaseMixin


class RequestTestMixin:
    def __init__(self, *args, **kwargs):
        self.request_factory = APIRequestFactory()

class CarsManagerApiTestCase(TestCase, UserAuthTestMixin, TestDataBaseMixin):
    def setUp(self):
        super().setUp()
        self.login_test()
        self.initialize_database()

    pass