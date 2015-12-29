# coding=utf-8

import unittest

from vklancer import api


class APITests(unittest.TestCase):

    def setUp(self):
        """Initialize `vklancer.API` class for tests."""
        self.token = 'token'
        self.version = 'version'
        self.api = api.API(token=self.token, version=self.version)

    def test_initialize(self):
        self.assertEqual(self.api._API__token, self.token)
        self.assertEqual(self.api._API__version, self.version)

    def test_single_chain(self):
        self.assertEqual(self.api.execute._API__method, 'execute')

    def test_multiple_chain(self):
        self.assertEqual(self.api.users.get._API__method, 'users.get')

    def test_send_request(self):
        self.assertTrue(isinstance(self.api.users.get(user_ids=1), dict))

if __name__ == '__main__':
    unittest.main()
