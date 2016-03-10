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

    def test_send_request__with_pass_method(self):
        self.assertTrue(
            isinstance(self.api.request('users.get', user_ids=1), dict)
        )

    def test_get_url(self):
        self.assertEqual(
            self.api.users.get.get_url(user_ids=1, v='0'),
            'https://api.vk.com/method/users.get?access_token=token&user_ids=1&v=0'
        )

    def test_get_url__with_pass_method(self):
        self.assertEqual(
            self.api.get_url('users.get', user_ids=1, v='0'),
            'https://api.vk.com/method/users.get?access_token=token&user_ids=1&v=0'
        )

if __name__ == '__main__':
    unittest.main()
