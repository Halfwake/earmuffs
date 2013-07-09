earmuffs
========

Wish that Python had dynamic scope like Common Lisp? Now you can pretend!

````python
from earmuffs import * # the * is bad style, but there's only like 4 things, so whatever

defvar(name = 'teddy') # Creates a new dynamic variable 'name' with the value 'teddy'.
defvar(name = 'bob') # Does nothing because the variable 'name' already has a value.
defparameter('name' = 'zack') # Overwrites the variable 'name' with the value 'zack'.

earmuffs('name') # Looks up a value in the environment. Think of it like saying *name* in Common Lisp. Oh, and the value is 'zack'.
with let(name = 'stacey'): # Let shadows an already existing value.'
    earmuffs('name') # The value is 'stacey'.
earmuffs('name') # Now it's 'zack' again!

def get_name():
    return earmuffs('name')

with let(name = 'xavier'):
    get_name() # Now it's Xavier, since dynamic scope lookup is different than lexical.

with let(name = 'jenny', a = 'a letter'):
    (earmuffs('name'), earmuffs('a'),) # The value is ('jenny', 'a letter',)
    with let(name = 'jenny jenson'):
        (earmuffs('name'), earmuffs('a'),) # The value is ('jenny jenson', 'a letter',)
    with let(a = 'alpha'):
        (earmuffs('name'), earmuffs('a'),) # The value is ('jenny', 'alpha',)
    (earmuffs('name'), earmuffs('a'),) # The value is ('jenny', 'a letter',)

````

Happy Hacking!
