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
        print ("first test")
        print ("==========")
        print ("testing site is up and returning code 200")
        self.assertEqual(rv.status, '200 OK')
        print ("=========")

    def test_hits(self):
        rv = self.app.get('/')
        print ("second test")
        print ("===========")
        print ("data from site is:")
        print (rv.data)
        cache = redis.Redis(host='redis', port=6379, decode_responses=True)
        x='Hello World! I have been visited {} times.\n'.format(cache.get('hits'))
        self.assertEqual(rv.data.decode("utf-8"), x)
        print ("============")


if __name__ == '__main__':
    unittest.main()
