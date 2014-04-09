# Range.py
import numpy as np
import sys

#sys.version
# out: '2.7.3rc2 (default, Mar 22 2012, 04:35:15) \n[GCC 4.6.3]'
#np.version.version
# out: '1.6.2'

size = int(1E6)

for x in range(size): x ** 2
# out: 10 loops, best of 3: 136 ms per loop

for x in xrange(size): x ** 2
# out: 10 loops, best of 3: 88.9 ms per loop

# avoid this
#for x in np.arange(size): x ** 2
#out: 1 loops, best of 3: 1.16 s per loop

# use this
np.arange(size) ** 2
#out: 100 loops, best of 3: 19.5 ms per loop