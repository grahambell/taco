Taco
====

Introduction
------------

.. starttacointro

Taco is a system for bridging between scripting languages.
Its goal is to allow you to call routines written for one language from
another.
It does this by running the second language interpreter in a sub-process,
and passing messages about actions to be performed inside that interpreter.

In principle, to interface scripting languages it might be preferable
to embed the interpreter for one as an extension of the other.
However this might not be convenient or possible,
and would need to be repeated for each combination of languages.
Instead Taco only requires a "client" module and "server" script
for each language, which should be straightforward to install,
and its messages are designed to be generic so that they
can be used between any combination of languages.

This documentation describes the Taco system.  For a list of
language implementations, please see the
`Taco Homepage`_.

.. _`Taco Homepage`: http://grahambell.github.io/taco/

.. endtacointro
