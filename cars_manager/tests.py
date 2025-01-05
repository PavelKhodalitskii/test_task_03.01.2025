from django.test import TestCase
from django.contrib.auth import login
from django.urls import reverse_lazy

from accounts.service import UserController
from cars_manager.models import Brand, Car


class TestDataBaseMixin:
    brand_name = 'Toyota'

    car_model = "Camry"
    car_description = "Описание"
    car_year = 2019

    def initialize_database(self):
        self.brand = Brand.objects.create(name=self.brand_name)
        self.car = Car.objects.create(make=self.brand,
                                      owner=self.user, 
                                      model=self.car_model,
                                      year=self.car_year,
                                      description=self.car_description)


class UserAuthTestMixin:
    username = 'test_user'
    password = 'password'

    def login_test(self):
        UserController.create_default_perm_group()
        self.user = UserController.register_user(username=self.username,
                                                password=self.password,
                                                first_name="Павел",
                                                last_name="Ходалицкий")
        self.client.login(username=self.username, password=self.password)
    
class CarsMengerViewsTestCase(TestCase, UserAuthTestMixin, TestDataBaseMixin):

    def setUp(self):
        super().setUp()
        self.login_test()
        self.initialize_database()

    def test_cars_list_avalible(self):
        response = self.client.get(reverse_lazy('main_page'))
        self.assertEqual(response.status_code, 200)

    def test_user_have_button_to_add_car(self):
        response = self.client.get(reverse_lazy('main_page'))
        self.assertContains(response, 'id="car_create_link"')
    
    def test_user_can_add_car(self):
        response = self.client.post(reverse_lazy('car_create'), {'brand': self.brand.id,
                                                                'owner': self.user.id,
                                                                'model': 'Corolla',
                                                                'year': 2024,
                                                                'desription': 'Описание'
                                                                })
        self.assertEqual(response.status_code, 200)

    def test_user_can_delete_car(self):
        response = self.client.post(reverse_lazy('car_create'), kwargs={'car_id': self.car.id})
        self.assertEqual(response.status_code, 200)

    def test_user_can_add_comment(self):
        response = self.client.post(reverse_lazy('post_comment', kwargs={'car_id': self.car.id}), 
                                    {"content": "Комментарий",
                                     "car": self.car.id,
                                     "author": self.user.id
                                    })
        self.assertEqual(response.status_code, 200, msg=response.context)