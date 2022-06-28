import unittest
from unittest.mock import patch
import methods
import example

class Test(unittest.TestCase):

    def setUp(self):
        self.message = example.message
        self.message_data = example.message_data
        self.text_result = example.text_result
        self.text_emoji = example.text_emoji

    def test_extract_emoji(self):
        self.assertEqual(methods.extract_emoji(self.text_emoji),'\ud83d\ude02')  

    def test_decodeutf16(self):
        self.assertEqual(methods.decode_utf18(self.message_data['text']), self.text_result)

    def test_api(self):
        with patch('methods.call_api_to_pubsub') as mocked_get:
            mocked_get.return_value.ok = '200'
            mocked_get.return_value.text = self.message

            # Need mock call for API

if __name__ == '__main__':
    unittest.main() 
