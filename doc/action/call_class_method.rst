Call class method
=================

.. default-domain:: taco
.. highlight:: json
.. action:: call_class_method

Instructs the server to call the given class method.

The ``context`` attribute is described on the :action:`call_function`
page.

::

    {
        "action": "call_class_method",
        "name": "NAME",
        "class": "CLASS",
        "args": [],
        "kwargs": {},
        "context": null
    }
