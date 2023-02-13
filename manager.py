#!/usr/bin/env python3

from typing import Final, TypeVar, Callable, Literal
from sys import argv, stderr

T = TypeVar('T')


is_sorted: Final[
	Callable[[list[T], Callable[[T, T], bool]], bool]
] = lambda l, cmp: all(cmp(l[i], l[i + 1]) for i in range(len(l) - 1))


def eprint(*values: object, **kwargs: object):
    '''prints to `stderr`'''
    return print(*values, file=stderr, **kwargs)


def print_help():
	HELP_TXT: Final = ''
	print(HELP_TXT)
	return HELP_TXT


# stable ordering.
# this is intentionally case-sensitive, to break ties
cmp_caseless: Final[
	Callable[[str, str], Literal[0, -1, 1]]
] = lambda a, b: 0 if a == b else (-1 if a.lower() < b.lower() else 1)
'''compare strings case-insensitive (except if equal)'''


def filter_main_files():
	'''get an iterator of files whose stem is "main"'''
	from os import listdir, path as os_path
	from pathlib import Path

	# order matters: 1st check stem (fast), then syscall (slow)
	return filter(lambda s: Path(s).stem == 'main' and os_path.isfile(s), listdir())


def main(*args: str):
	from sys import exit as sys_exit  # avoid collision with global `exit`

	if len(args) < 1:
		eprint('no args')
		return print_help()

	match args[0]:
		case 'help': return print_help()
		# to-do = pass
		case 'check':
			for m in filter_main_files():
				with open(m) as f:
					'\n'.split(f.read())
		case 'add': pass
		case 'sort': pass
		case subcmd:
			eprint(f'unrecognized subcmd: "{subcmd}"\nuse "help"')
			sys_exit(1)


if '__main__' == __name__:
	main(*argv[1:])
