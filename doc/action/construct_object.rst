.. _construct_object:

construct_object
================

Instructs the server to call the constructor for the given class.
If successfull, an :ref:`object reference` should be returned
in the :ref:`result` message.

.. highlight:: json

::

    {
        "action": "construct_object",
        "class": "NAME",
        "args": [],
        "kwargs": {}
    }
