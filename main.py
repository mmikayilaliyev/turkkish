#!/usr/bin/env python3

import sys
import seperater

while True:
	k=str(input())
	try:
		print(seperater.allornot(k))
	except EOFError:
		print('Try again',file=sys.stderr)

