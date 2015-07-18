# -*- coding: utf-8 -*-

__author__ = 'Vitalii Maslov'
__version__ = '1.0.0'
__email__ = 'me@pyvim.com'
__license__ = 'MIT'

import requests


class API(object):
    """
    Wrapper for vk.com API.
    """

    def __init__(self, token, version):
        """
        Initialize `API` class.

        :param token: OAuth access token.
        :param version: API version.
        """
        self._token = token
        self._version = version

    def request(self, method, params):
        """
        Send request to API.

        :param method: name of API method.
        :param params: method parameters.
        :returns: answer in dictionary.
        """
        url = 'https://api.vk.com/method/%s' % method
        data = {
            'access_token': self._token,
            'v': self._version
        }
        data.update(params)
        return requests.post(url, data=data).json()

    def __getattr__(self, path):
        try:
            return self.__dict__[path]
        except KeyError:
            return Chain(self, [path])

class Chain(object):
    """
    Create or continue chain to build method name.
    """

    def __init__(self, api, path):
        """
        Initialize `Chain` class.

        :param api: `API` object.
        :param path: part of method name.
        """
        self._api = api
        self._path = path

    def __getattr__(self, path):
        try:
            return self.__dict__[path]
        except KeyError:
            self._path.append(path)
            return Chain(self._api, self._path)

    def __call__(self, **params):
        return self._api.request('.'.join(self._path), params)
