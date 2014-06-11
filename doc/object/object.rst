.. _`object reference`:

Object Reference
================

An object reference is used to refer to an object which has been
constructed on the server side.  In other words, it refers to
an instance of a class in the server's language, not to JSON objects
in Taco messages.  When a :ref:`result` action would contain
an object, the object should be stored in a cache by the server,
and the reference to it replaced with an object reference.
This uses an integer to identify the object.  Object references
can also be used by the client, for example to allow them to be passed as
function arguments.

.. highlight:: json

::

    {
        "_Taco_Object_": 1
    }
