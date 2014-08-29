
import time

import numpy as np
import pyfits as pf


# lendo o FITS
t = time.time()

f = 'myfits.fits'
print f

h = pf.open(f)
tb = h[1].data

tfits = time.time()-t
print  tfits, "s to read FITS"

#print tb


# lendo o ASCII
t = time.time()

f = 'myfits.asc'
print f

X = np.loadtxt(f)

tasc = time.time()-t
print  tasc, "s to read ASCII"


print tfits/tasc

