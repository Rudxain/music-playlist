#!/usr/bin/env python3

from typing import Final
from sys import argv, stderr

HELP_TXT: Final = ''


def eprint(*values: object, **kwargs: object):
    '''prints to `stderr`'''
    return print(*values, file=stderr, **kwargs)


def print_help():
	print(HELP_TXT)
	return HELP_TXT


def cmp_fn(a: str, b: str):
	# for a stable sort.
	# this is intentionally case-sensitive, to break ties
	if a == b:
		return 0

	a = a.lower()
	b = b.lower()

	return -1 if a < b else 1

def filter_main_files():
	from os import listdir, path as os_path
	from pathlib import Path

	return filter(lambda s: Path(s).stem == 'main' and os_path.isfile(s), listdir())

def main(*args: str):
	from sys import exit as sys_exit  # avoid collision with global `exit`

	if len(args) < 1:
		return print_help()

	match args[0]:
		case 'help': return print_help()
		case 'check': pass
		case 'add': pass
		case 'sort': pass
		case _:
			eprint('unrecognized subcmd\nuse "help"')
			sys_exit(1)


if '__main__' == __name__:
	main(*argv[1:])
