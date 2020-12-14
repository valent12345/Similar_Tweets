import unittest
import os
import requests

class FlaskTests(unittest.TestCase):
	
	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		pass

	def tearDown(self):
		pass

	def test_a_index(self):
		response = requests.get('http://localhost:5000')
		self.assertEqual(response.status_code, 200)
		
	def test_b_sentiment_classify_negative(self):	
		params = {
			'sentence': 'I hate you !',
			'form_type': "answer"
		}
		response = requests.post('http://localhost:5000', data=params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, b'This sentence has a negative sentiment')

	def test_c_sentiment_classify_positive(self):	
		params = {
			'sentence': 'I love you',
			'form_type': "answer"
		}
		response = requests.post('http://localhost:5000', data=params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, b'This sentence has a positive sentiment')
		
	def test_d_sentiment_classify_neutral(self):	
		params = {
			'sentence': 'He seems ok !',
			'form_type': "answer"
		}
		response = requests.post('http://localhost:5000', data=params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, b'This sentence has a neutral sentiment')

if __name__ == '__main__':
	unittest.main()
