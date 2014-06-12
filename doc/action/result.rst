Result
======

.. default-domain:: taco
.. highlight:: json
.. action:: result

This message is used when a command has completed successfully.
The ``result`` attribute holds the return value, if there is one,
or null otherwise.

::

    {
        "action": "result",
        "result": null
    }
