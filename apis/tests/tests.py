import json
from django.test import TestCase
from django.urls import reverse
from apis.models import NormalModel
from apis.factory.factories import NormalModelFactory

# Create your tests here.
class ModelTestCase(TestCase):
    def setUp(self):
        NormalModel.objects.create(
            user_id = 1, name = "ravi", age = 27)
    
    def test_data(self):
        user = NormalModel.objects.get(user_id=1)
        self.assertEqual(user.name,"ravi")
    
    def test_data_with_error(self):
        user = NormalModel.objects.filter(user_id = 10).first()
        self.assertIsNone(user)    
        

class ViewTestCase(TestCase):
    def setUp(self):
        NormalModel.objects.create(
            user_id=1,name="ravi",age=23
        )
        
        
    def test_get_data(self):
        url = reverse('apis-get', args=[1])
        response =self.client.get(url)
        content = json.loads(response.content)
        print(f'content:{content}')
        
        self.assertEqual(response.status_code,200)
        self.assertIsNotNone(response.content)
        
    
    def test_post_data(self):
        url = reverse('apis-post')
        data = {
            "user_id":"2",
            "name":"raju",
            "age":"34"
        }
        response = self.client.post(url, data=json.dumps(data),       
        content_type="application/json")
        self.assertEqual(response.status_code,200)
        print(response.content)
              