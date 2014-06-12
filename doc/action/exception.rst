Exception
=========

.. default-domain:: taco
.. highlight:: json
.. action:: exception

The ``exception`` action signifies that an exception or error of some type
occurred while a command action was being handled.
It can be used by the server to raise errors explicitly,
such as when an unrecognised action message is received,
as well as for exceptions trapped by the server while
attempting to carry out commands.

The ``message`` attribute contains a string representation of the
error.

::

    {
        "action": "exception",
        "message": "MESSAGE"
    }
