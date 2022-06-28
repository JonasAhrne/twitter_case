import unittest
from unittest.mock import patch
import methods
import example

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_emoji(self):
        self.assertEqual(10, 10)

    def test_schema(self):
        self.assertEqual(10, 10)

    def test_api(self):
        with patch('methods.create_url') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            #schedule = methods.create_url('key')

            mocked_get.assert_called_with('http://url.com/1193924/328913999s89723')

if __name__ == '__main__':
    unittest.main() 
