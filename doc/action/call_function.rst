Call function
=============

.. default-domain:: taco
.. highlight:: json
.. action:: call_function

Instructs the server to call the given function.

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

This action (and the related actions :action:`call_class_method` and
:action:`call_method`) include a ``context`` attribute in order
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
