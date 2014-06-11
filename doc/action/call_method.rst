.. _call_method:

call_method
===========

Calls a method of an object.
The object must already be in the server's object cache,
and is referred to by the ``number`` attribute.
This number will have been provided in a :ref:`object reference`
sent by the server.

The ``context`` attribute is described on the :ref:`call_function`
page.

.. highlight:: json

::

    {
        "action": "call_method",
        "name": "NAME",
        "number": 1,
        "args": [],
        "kwargs": {},
        "context": null
    }
