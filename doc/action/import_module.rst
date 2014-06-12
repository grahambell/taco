Import module
=============

.. default-domain:: taco
.. highlight:: json
.. action:: import_module

Instructs the server to attempt to load the module specified by the
``name`` attribute.
The interpretation of the ``args`` (arguments) and ``kwargs`` (keyword
arguments) attributes can differ between different Taco server
implementations as is appropriate for different programming languages.

::

    {
        "action": "import_module",
        "name": "NAME",
        "args": [],
        "kwargs": {}
    }
