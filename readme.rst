Taskwarrior EXAMPLE Capsule
===========================

This capsule is not actually useful on its own; it's only here to help you
write your own capsules.

Using this example
------------------

First, think of a name for your capsule; then follow the below instructions
before doing anything (in the following examples we're pretending that you're
adding a capsule named "Hello"):

1. Rename the class ``EXAMPLE`` in ``taskwarrior_EXAMPLE_capsule/capsule.py``
   to your capule's name.  In this example, you'd name the class ``Hello``.
2. Rename the folder ``taskwarrior_EXAMPLE_capsule`` to match your capsule's
   function.  For example, if your capsule adds a command called ``hello``,
   you would rename the folder to ``taskwarrior_hello_capsule``.
3. Update ``setup.py`` by following the instructions after comments starting
   with ``CHANGEME``.
4. Update ``LICENSE`` and change "YOUR NAME" to your name.
