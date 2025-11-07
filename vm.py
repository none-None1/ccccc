"""
ccc:cc VM: Manages variables and built-in functions
"""
from random import randint


class Variable:
    """
    Variables in ccc:cc
    """

    def __init__(self, obj=None, getter=None, setter=None):
        self.obj = obj
        self.getter = getter
        self.setter = setter

    def get(self):
        if self.obj is not None:
            return self.obj
        return self.getter()

    def set(self, x):
        if self.obj is not None:
            self.obj = x
        else:
            self.setter(x)


class Char(int):
    pass


stdin_variable = Variable(getter=input, setter=lambda x: None)
stdout_variable = Variable(
    getter=lambda: None,
    setter=lambda x: print(chr(int(x)), end="") if isinstance(x, Char) else print(x),
)
adder, multiplier = 0, 1


def adder_get():
    global adder
    t = adder
    adder = 0
    return t


def adder_set(x):
    global adder
    adder += int(x)


def multiplier_get():
    global multiplier
    t = multiplier
    multiplier = 1
    return t


def multiplier_set(x):
    global multiplier
    multiplier *= int(x)


adder_variable = Variable(getter=adder_get, setter=adder_set)
multiplier_variable = Variable(getter=multiplier_get, setter=multiplier_set)


class VM:
    """
    Main VM class
    """

    def __init__(self):
        self.mem = {
            1: Variable(1),
            2: stdin_variable,
            3: stdout_variable,
            4: adder_variable,
            5: multiplier_variable,
            6: Variable(1),
        }
        self.funcs = {
            1: (lambda x: -int(x)),
            2: (lambda a, b, c: b if a else c),
            3: (lambda: randint(0, 1)),
            4: lambda x: Char(x),
        }

    def getvar(self, x):
        return self.mem[x].get()

    def setvar(self, x, y):
        if x in self.mem:
            self.mem[x].set(y)
        else:
            self.mem[x] = Variable(y)

    def call_func(self, f, *args):
        return self.funcs[f](*args)


vm = VM()
