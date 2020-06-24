cat <<-'TEST_CASES' > test.py
#!/usr/bin/env python
import unittest
import webapp
import redis

class TestHello(unittest.TestCase):

    def setUp(self):
        webapp.app.testing = True
        self.app = webapp.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
    
    def test_hits(self):
        rv = self.app.get('/')
        print (rv.data)
        cache = redis.Redis(host='redis', port=6379, decode_responses=True)
        x='Hello World! I have been visited {} times.\n'.format(cache.get('hits'))
        self.assertEqual(rv.data.decode("utf-8"), x)


if __name__ == '__main__':
    unittest.main()
    
TEST_CASES