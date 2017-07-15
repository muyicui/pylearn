#!/usr/bin/env python

'makeTextFile.py -- create text file'

import os

# get filename
while True:
    fname = raw_input('Enter file name: ')
    if os.path.exists(fname):
        print"*** ERROR: '%s' already exists" % fname
    else:
        break

# get file content (text) lines
all = []
print "\nEnter lines ('.' by itself to quit).\n"

# loop until user terminates input
while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with NEWLINE line terminator
fobj = open(fname, 'w')
fobj.write('\n'.join(all))
fobj.close()
print 'DONE!'


#!/usr/bin/env python

'readTextFile.py -- read and display text file'

# get filename
fname = raw_input('Enter file name: ')
print

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError, e:
    print"*** file open error:", e
else:
    # display contents to the screen
    for eachLine in fobj:
        print eachLine,
    fobj.close()
