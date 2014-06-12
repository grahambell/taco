Construct object
================

.. default-domain:: taco
.. highlight:: json
.. action:: construct_object

Instructs the server to call the constructor for the given class.
If successfull, an :object:`_Taco_Object_` reference should be returned
in the :action:`result` message.

::

    {
        "action": "construct_object",
        "class": "NAME",
        "args": [],
        "kwargs": {}
    }
