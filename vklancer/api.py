# coding=utf-8

import requests


class API(object):

    """Wrapper for vk.com API."""

    def __init__(self, token=None, version='5.42', **kwargs):
        """
        Override __init__.

        :param token: `str` OAuth2 access token.
        :param version: `str` API version.
        """
        self.__token = token
        self.__version = version
        self.__method = kwargs.get('method', '')

    def __request(self, **kwargs):
        """
        Send request to API.

        :returns: answer in dictionary.
        """
        url = 'https://api.vk.com/method/{}'.format(self.__method)
        kwargs['v'] = self.__version

        if self.__token is not None:
            kwargs['access_token'] = self.__token

        return requests.post(url, data=kwargs).json()

    def __getattr__(self, attr):
        """Override __getattr__."""
        method = ('{}.{}'.format(self.__method, attr)).lstrip('.')
        return API(self.__token, version=self.__version, method=method)

    def __call__(self, **kwargs):
        """Override __call__."""
        return self.__request(**kwargs)
