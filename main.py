"""
chicken chicken chicken: chicken chicken
An esolang with only "chicken"s and punctuations.

main.py [-v] [file]
-v: Verbose mode. When this mode is on, unlike the standard behavior of this
esolang, errors don't print "chicken!" but raise Python exceptions instead.
This mode is useful for debugging.
"""
from parser_module import *
import vm


def runfunct(x):
    if x[0][0] == "chicken":
        return vm.vm.getvar(len(x[0]))
    elif x[0][0] == '"':
        return vm.Char(len(x[0][1]))
    funcid, args = len(x[0][0]), x[0][1][1:-1]
    realargs = list(map(runfunct, args))
    return vm.vm.call_func(funcid, *realargs)


def runline(x):
    if x:
        x = x[0]
    if len(x) < 2 or x[1] != ":":
        return
    vm.vm.setvar(len(x[0]), runfunct(x[2]))


def interpret_program(code):
    parsed = chicken_code.parse_string(code, parse_all=True)
    while 1:
        ln = vm.vm.getvar(1) - 1
        if ln >= len(parsed):
            return
        runline(parsed[ln])
        vm.vm.setvar(1, vm.vm.getvar(1) + 1)


def ccc_cc(code):
    try:
        interpret_program(code)
    except:
        print("chicken!")


import sys

verbose = int("-v" in sys.argv)
f = [ccc_cc, interpret_program]
if "-v" in sys.argv:
    sys.argv.remove("-v")
if len(sys.argv) > 1:
    f[verbose](open(sys.argv[1]).read())
else:
    f[verbose](sys.stdin.read())
