import unittest
from main import app

class TestWebApp(unittest.TestCase):

    def setUp(self):
        # Create a test client to send requests to the app
        self.app = app.test_client()
        # This line is optional and can be used to show detailed errors in the test results.
        self.app.testing = True

    def test_home_page(self):
        # Send a GET request to the home page
        response = self.app.get('/')
        # Assert that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that the response data contains the expected text
        self.assertIn(b'Hello, World!', response.data)
        self.assertIn(b'This is my Python web application.', response.data)

if __name__ == '__main__':
    unittest.main()
