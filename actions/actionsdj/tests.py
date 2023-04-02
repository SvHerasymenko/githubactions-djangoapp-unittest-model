from django.test import TestCase
from actionsdj.models import Products, User, Hero

class TestProducts(TestCase):

    @classmethod
    def setUpTestData(cls):
        Products.objects.create(
        name = "Macbook",
        description = "very nice machine",
        price = "17500.00",
        url = "https://rozetka.com.ua/ua/apple_macbook_air_13_m1_256gb_2020_gold/p245161897/?gclid=CjwKCAjwrJ-hBhB7EiwAuyBVXS98Ea-s1-ArftoyE9wHpbS9MD-MlE6XZVHrhXJW8L0Kv0zjr8qbDBoCUJ4QAvD_BwE",
        status = "True")

    def test_name_label(self):
        products = Products.objects.get(id = 1)
        result = products._meta.get_field('name').verbose_name
        self.assertEquals(result,'Name')

    def test_name_max_length(self):
        products = Products.objects.get(id = 1)
        result = products._meta.get_field('name').max_length
        self.assertEquals(result,100)

    def test_description_label(self):
        products = Products.objects.get(id = 1)
        result = products._meta.get_field('description').verbose_name
        self.assertEquals(result,'Description')

    def test_description_max_length(self):
        products = Products.objects.get(id = 1)
        result = products._meta.get_field('description').max_length
        self.assertEquals(result,250)

    def test_price_label(self):
        products = Products.objects.get(id = 1)
        result = products._meta.get_field('price').verbose_name
        self.assertEquals(result,'Price')

    def test_url_label(self):
        products = Products.objects.get(id = 1)
        result = products._meta.get_field('url').verbose_name
        self.assertEquals(result,'Url')
    
    def test_url_max_length(self):
        products = Products.objects.get(id = 1)
        result = products._meta.get_field('url').max_length
        self.assertEquals(result,100)

    def test_status_label(self):
        products = Products.objects.get(id = 1)
        result = products._meta.get_field('status').verbose_name
        self.assertEquals(result,'Status')
    
class TestUser(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(
        name = "Sviatoslav",
        email = "sviatoslav@gmail.com",
        phone = +380234432,
        balance = 12345.34,
        status = True)

    def test_name_label(self):
        user = User.objects.get(id = 1)
        result = user._meta.get_field('name').verbose_name
        self.assertEquals(result,'Name')

    def test_name_max_length(self):
        user = User.objects.get(id = 1)
        result = user._meta.get_field('name').max_length
        self.assertEquals(result,100)

    def test_email_label(self):
        user = User.objects.get(id = 1)
        result = user._meta.get_field('email').verbose_name
        self.assertEquals(result,'Email')

    def test_email_max_length(self):
        user = User.objects.get(id = 1)
        result = user._meta.get_field('email').max_length
        self.assertEquals(result,100)

    def test_phone_label(self):
        user = User.objects.get(id = 1)
        result = user._meta.get_field('phone').verbose_name
        self.assertEquals(result,'Phone')

    def test_balance_label(self):
        user = User.objects.get(id = 1)
        result = user._meta.get_field('balance').verbose_name
        self.assertEquals(result,'Balance')

    def test_status_label(self):
        user = User.objects.get(id = 1)
        result = user._meta.get_field('status').verbose_name
        self.assertEquals(result,'Status')

class TestHero(TestCase):

    @classmethod
    def setUpTestData(cls):
        Hero.objects.create(
        name = "Stiv",
        hitpoint = "20",
        power_attack = "12",
        armor = "123.321",
        speed = "100.98")
    
    def test_name_label(self):
        hero = Hero.objects.get(id = 1)
        result = hero._meta.get_field('name').verbose_name
        self.assertEquals(result,'Name')

    def test_name_max_length(self):
        hero = Hero.objects.get(id = 1)
        result = hero._meta.get_field('name').max_length
        self.assertEquals(result,100)

    def test_hitpoint_label(self):
        hero = Hero.objects.get(id = 1)
        result = hero._meta.get_field('hitpoint').verbose_name
        self.assertEquals(result,'Hitpoint')

    def test_power_attack_label(self):
        hero = Hero.objects.get(id = 1)
        result = hero._meta.get_field('power_attack').verbose_name
        self.assertEquals(result,'Power_attack')

    def test_armor_label(self):
        hero = Hero.objects.get(id = 1)
        result = hero._meta.get_field('armor').verbose_name
        self.assertEquals(result,'Armor')

    def test_speed_label(self):
        hero = Hero.objects.get(id = 1)
        result = hero._meta.get_field('speed').verbose_name
        self.assertEquals(result,'Speed')
