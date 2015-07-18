# -*- coding:utf-8 -*-

__author__ = 'Vitalii Maslov'
__email__ = 'me@pyvim.com'
__version__ = '1.0.0'
__license__ = 'MIT'

import unittest

import vklancer


class APITests(unittest.TestCase):

    def setUp(self):
        """
        Initialize `vklancer.API` class for tests.

        Note: paste your access token and API version.
        """
        self.api = vklancer.API(token='YOUR-TOKEN', version='YOUR-VERSION')

    def test_chain(self):
        self.assertEqual(self.api.users.get._path, ['users', 'get'])
        self.assertEqual(self.api.execute._path, ['execute'])

    def test_request_to_api(self):
        answer = self.api.users.get(user_ids=1)
        self.assertIsInstance(answer, dict)

if __name__ == '__main__':
    unittest.main()


