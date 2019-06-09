
# Create your tests here.
import json

from django.test import TestCase, Client

client = Client()
generated_fields = ['updated', 'created']


class SlotsTestCase(TestCase):
    """
    Running into oauth2_providers application issue hence not able to log in.
    Hence writing test case only for public apis for now.
    """

    fixtures = ['user.json', 'auth.json', 'test_initial_data.json']

    def __init__(self, *args, **kwargs):
        super(SlotsTestCase,self).__init__(*args, **kwargs)
        self.maxDiff = None

    def test_slots_list(self):
        response = client.get('/api/slot/')
        self.assertEqual(200, response.status_code)

    def test_get_slot_by_id(self):
        response = client.get('/api/slot/1/')
        self.assertEqual(200, response.status_code)

    def test_create_user(self):
        data = {
              "password": "mkgandhi",
              "username": "mohandas",
              "last_login": "2019-06-09T20:23:47.152Z",
              "is_superuser": False,
              "first_name": "mohandas",
              "last_name": "karamchand",
              "email": "mohandas@example1.com",
              "is_staff": False,
              "is_active": True,
              "date_joined": "2019-06-09T20:23:47.152Z"
            }
        resp = client.post('/api/user/registration/', data, content_type='application/json')
        self.assertEqual(201, resp.status_code)

    #TODO: Resolve oauth2 issue for login and test protected api's
    # def test_login(self):
    #     data = {
    #         "username": 'mohandas',
    #         "password": 'mkgandhi'
    #     }
    #     response = client.post('/api/login/', data, content_type='application/json')
    #
    #     self.assertEqual(200,200)


