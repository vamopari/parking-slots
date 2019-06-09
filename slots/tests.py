
# Create your tests here.
import json

from django.test import TestCase, Client

client = Client()
generated_fields = ['updated', 'created']


class SlotsTestCase(TestCase):

    fixtures = ['user.json', 'auth.json', 'test_initial_data.json']

    def __init__(self, *args, **kwargs):
        super(SlotsTestCase,self).__init__(*args, **kwargs)
        self.maxDiff = None

    # def test_login(self):
    #     data = {
    #         "username": 'vishalmopari',
    #         "password": 'mypassword@123'
    #     }
    #     response = client.post('/api/login/', data, content_type='application/json')

    #     self.assertEqual(200,200)

    def test_slots_list(self):
        response = client.get('/api/slot/')
        self.assertEqual(200, response.status_code)

    def test_get_slot_by_id(self):
        response = client.get('/api/slot/1/')
        self.assertEqual(200, response.status_code)
