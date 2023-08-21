import unittest
from module_4_FLASK.four_three import app, registration, RegistrationForm
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()
csrf.init_app(app)

class TestRegistrationForm(unittest.TestCase):

    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SECRET_KEY'] = 'any secret string'
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = '/registration'
        self.data = dict()

    def test_successful_reg(self):
        self.data['email'] = 'test@ya.ru'
        self.data['phone'] = '9313388022'
        self.data['name'] = 'andrey'
        self.data['address'] = 'SPb'
        self.data['index'] = '111111'
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_reg_email(self):
        self.data['email'] = 'sal;dk123'
        response = self.app.post(self.base_url, data=self.data)
        self.assertNotEqual(response.status_code, 200)

    def test_set_phone(self):
        self.data['phone'] = 7987164654646464646
        response = self.app.post(self.base_url, data=self.data)
        self.assertNotEqual(response.status_code, 200)

    def test_set_name(self):
        self.data['name'] = ['213', 123123]
        response = self.app.post(self.base_url, data=self.data)
        self.assertNotEqual(response.status_code, 200)


    def test_set_address(self):
        self.data[None] = None
        response = self.app.post(self.base_url, data=self.data)
        self.assertNotEqual(response.status_code, 200)


    def test_set_index(self):
        self.data['index'] = 7987164654646464646
        response = self.app.post(self.base_url, data=self.data)
        self.assertNotEqual(response.status_code, 200)