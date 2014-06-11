.. _set_attribute:

set_attribute
=============

Sets the value of an attribute of an object in the server's object cache.
The object is identified by the ``number`` message attribute.

.. highlight:: json

::

    {
        "action": "set_attribute",
        "name": "NAME",
        "number": 1,
        "value": "VALUE"
    }
