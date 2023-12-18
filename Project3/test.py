import unittest
import app
import json

class FlaskWebForumTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_user_registration(self):
        response = self.app.post('/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpass'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        response = self.app.post('/login', data=json.dumps({
            'username': 'testuser',
            'password': 'testpass'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', json.loads(response.data))

    def test_create_post(self):
        response = self.app.post('/post', data=json.dumps({
            'msg': 'Hello World'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data))

    def test_read_post(self):
        # Assuming a post with id 1 exists
        response = self.app.get('/post/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('msg', json.loads(response.data))

    def test_update_post(self):
        # Assuming a post with id 1 exists
        response = self.app.put('/post/1', data=json.dumps({
            'msg': 'Hello World Updated'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_post(self):
        # Assuming a post with id 1 exists and you have the correct key
        # Replace 'your_key' with the actual key
        response = self.app.delete('/post/1/delete/your_key')
        self.assertEqual(response.status_code, 200)

   

if __name__ == '__main__':
    unittest.main()
