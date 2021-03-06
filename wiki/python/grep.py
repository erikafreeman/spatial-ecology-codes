#!/usr/bin/env python
#
# Python script that works like a simplified "grep" command
# which doesn't read from stdin
#
import sys, re
from os.path import basename

if len(sys.argv) < 3:
    sys.stderr.write('Usage: %s regex file ...\n' % basename(sys.argv[0]))
    sys.exit(1)

r = re.compile(sys.argv[1])

for fn in sys.argv[2:]:
    try:
        fobj = open(fn, 'rt')
        try:
            for s in fobj:
                if r.search(s):
                    sys.stdout.write(s)
        finally:
            fobj.close()
    except IOError, e:
        sys.stderr.write('error opening file %r\n' % fn)
