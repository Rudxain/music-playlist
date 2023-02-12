#!/usr/bin/env python3

from typing import Final
from sys import argv, stderr


def eprint(*values: object, **kwargs: object):
    '''prints to `stderr`'''
    return print(*values, file=stderr, **kwargs)


DEFAULT_STEM: Final = 'main'


def main(*args: str):
	from sys import exit as sys_exit # avoid collision with global `exit`

	match args[0]:
		case 'check': pass
		case 'add': pass
		case 'sort': pass
		case _:
			eprint('unrecognized subcmd')
			sys_exit(1)


if '__main__' == __name__:
	main(*argv[1:])
