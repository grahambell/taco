.. _call_function:

call_function
=============

Instructs the server to call the given function.

.. highlight:: json

::

    {
        "action": "call_function",
        "name": "NAME",
        "args": [],
        "kwargs": {},
        "context": null
    }

Context
-------

This action (and the related actions :ref:`call_class_method` and
:ref:`call_method`) include a ``context`` attribute in order
to support context-sensitive languages.  Clients for such
languages may attempt to set this attribute automatically,
and servers for languages which are not sensitive to context
are free to ignore it.

It can take the following values:

* ``"scalar"``
* ``"list"``
* ``"map"``
* ``"void"``
* null
