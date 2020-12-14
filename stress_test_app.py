import unittest
import requests
import grequests
import time
import os


class FlaskTests(unittest.TestCase):

    def setUp(self):
        os.environ['NO_PROXY'] = '0.0.0.0'
        pass

    def tearDown(self):
        pass

    def test_index(self):
        n = 1000
        urls = []

        for i in range(n):
            urls.append('http://localhost:5000')

        responses = (grequests.get(u) for u in urls)

        start = time.time()
        simultaneous_responses = grequests.map(rs)
        end = time.time()
        t = end - start

        for i in range(n):
            self.assertEqual(simultaneous_responses[i].status_code, 200)
        print('The {} requests took: {} seconds'.format(n, t))


if __name__ == '__main__':
    unittest.main()
