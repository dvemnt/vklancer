VKLancer
========

Simple usage `API vk.com <https://vk.com/dev>`__.

Usage
-----

.. code:: python

    from vklancer import api

    vk = api.API('your access token')
    response = vk.users.get(user_ids=1)

    print(response)

    {'response': [{'last_name': 'Дуров', 'id': 1, 'first_name': 'Павел'}]}

Installation
------------

``pip install vklancer``

Source
------

`GitHub <https://github.com/pyvim/vklancer>`__
