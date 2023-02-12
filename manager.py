#!/usr/bin/env python3

from typing import Final
from sys import argv

DEFAULT_STEM: Final = 'main'


def main(*args: str):
	if args[0] == 'sort':
		pass


if '__main__' == __name__:
	main(*argv[1:])
