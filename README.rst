VKLancer
========

Simple usage `API vk.com <https://vk.com/dev>`__.

Usage
-----

.. code:: python

    import vklancer
    from vklancer.utils import authentication, oauth

    token = oauth(authentication(login='YOUR-LOGIN', password='YOUR-PASSWORD'))
    api = vklancer.API(token='token', version='5.34')
    answer = api.users.get(user_ids=1)

Installation
------------

``pip install vklancer``

Requirements
------------
`requests <https://github.com/kennethreitz/requests>`__

Source
------

`GitHub <https://github.com/pyvim/vklancer>`__
