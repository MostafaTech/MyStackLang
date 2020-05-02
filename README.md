# My Stack Language
A silly simple implemention of a stack based programming language in python

## Simple add program
This example gets two digits and pushes them into stack. Then adds the two last values in the stack and prints them.
```
PUSH S'Sum is: '
PUSH ARG1
PUSH ARG2
ADDS
STRJ
PRNT
```
And run
```sh
$ python ./stack-lang.py ./tests/simple-add.sl 23 17
Sum is: 40
```