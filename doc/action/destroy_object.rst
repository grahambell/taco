Destroy object
==============

.. default-domain:: taco
.. highlight:: json
.. action:: destroy_object

This action allows the server to remove the corresponding object
from its object cache.
The object is identified by the ``number`` attribute.
The client should not attempt to refer to the object again
after permitting its destruction.

::

    {
        "action": "destroy_object",
        "number": 1
    }
