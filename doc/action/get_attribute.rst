Get attribute
=============

.. default-domain:: taco
.. highlight:: json
.. action:: get_attribute

Requests the value of an attribute of one of the objects in the
server's object cache.
The object is identified by the ``number`` attribute.

::

    {
        "action": "get_attribute",
        "name": "NAME",
        "number": 1
    }
