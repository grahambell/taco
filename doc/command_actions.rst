.. _`command actions`:

Command Actions
===============

Command actions are sent by the client to instruct the server to
perform various tasks.
After sending a command, the client should wait to recieve one
of the :ref:`response actions` from the server.

.. toctree::
   :maxdepth: 2

   action/call_class_method
   action/call_function
   action/call_method
   action/construct_object
   action/destroy_object
   action/get_attribute
   action/get_value
   action/import_module
   action/set_attribute
   action/set_value
