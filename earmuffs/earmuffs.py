'Provides Common Lisp style dynamic scope functionality.'

_environment = {} #Not to ever be accessed directly.

def defparameter(**kargs):
    'Creates a dynamic variable for each keyword argument.'
    for var_name, value in kargs.items():
        _environment[var_name] = value
    return kargs

def defvar(**kargs):
    'Creates a dynamic variable for each keyword argument, unless that name is already bound.'
    for var_name, value in kargs.items():
        if var_name not in _environment.keys():
            _environment[var_name] = value
        else:
            del kargs[var_name]
    return kargs

class let(object):
    'Shadows other dynamic variables when used in a with statement.'
    def __init__(self, **kargs):
        self.new = kargs
    def __enter__(self):
        self.old = _environment.copy()
        _environment.update(self.new)
    def __exit__(self, type, value, traceback):
        global _environment
        _environment = self.old

def earmuffs(var_name):
    'Looks up a dynamic variable.'
    try:
        return _environment[var_name]
    except KeyError:
        raise NameError("Name does not exist in the dynamic scope.")
