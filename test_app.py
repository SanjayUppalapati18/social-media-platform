import unittest
from app import app

class SocialMediaAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_post(self):
        response = self.app.post('/api/posts', json={'user_id': 101, 'content': 'Hello ASE Lab!'})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
