**Chicken chicken chicken: chicken chicken** (*ccc:cc* for short) is an esolang inspired by [Chicken](https://esolangs.org/wiki/Chicken). The only valid tokens are `chicken` and punctuations.

### Syntax and execution
Please refer to [the esolang wiki page](https://esolangs.org/wiki/ccc:cc) for details.

### Examples
There are some examples in the `examples` folder: Hello world, cat program, A+B Problem, XKCD Random Number and infinite loop.

### Interpreter
There is an interpreter in Python which consists of 3 files:
1. `parser_module.py` uses [pyparsing](https://pypi.org/project/pyparsing) to parse the code into nested lists.
2. `vm.py` defines the VM, variables and built-in functions.
3. `main.py` is the main interpreter file which defines the execution logics.

Have fun!
