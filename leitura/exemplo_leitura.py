# opening file the python way
myfile = open('hora_altair.txt','r')
myfile
# reading its lines
lines = myfile.readlines()
lines
# just displaying the lines
for line in lines:
    print line
# processing the lines to get hour minutes and seconds
for line in lines:
    print line
    sline = line.split()
    hour = sline[0]
    min = sline[1]
    sec = sline[2]
    print hour, min, sec
    ang = hour + min/60. + sec/3600.
    print ang

from numpy import *
# now reading it the numpy way
# just reading as an Array
A = loadtxt('hora_altair.txt')
# displaying array and shape
A
A.shape
# showing that arrays have an "inverted" orientation
A[0]
# need to transpose to get what we are used to
TA = transpose(A)
TA
TA[0]
# comparing to original file
cat hora_altair.txt
# making the calculation
ANG = TA[0]+TA[1]/60.+TA[2]/3600.
ANG
# or we can elaborate on loadtxt and get the columns as we like it
hour, min, sec = loadtxt('hora_altair.txt', unpack=True)
hour
min
sec
ANG = hour+min/60.+sec/3600.
ANG
# voila!!!

# now let us save the results the python way
fileout = open('hora_altair.out','w')
# a test, it did not work as it is not a string
for ang in ANG:
    fileout.write(ang)
# one way to write as string (we will see that not very nice, since there is no 
# newline on the format
for ang in ANG:
    fileout.write(str(ang))
# you need to close the file
fileout.close()
# displaying the ouput, everything is on a single line
cat hora_altair.out
# let us fix it
fileout = open('hora_altair.out','w')
# using format to print as we want it. note the \n for newline
for ang in ANG:
    fileout.write("%f\n"%ang)
fileout.close()
cat hora_altair.out

# now let us save it the numpy way
savetxt('hora_altair.outnp',ANG)
# voila, just a line and very fast
cat hora_altair.outnp
# we can elaborate on the savetxt and work the format, for instance
savetxt('hora_altair.outnp',ANG, fmt='%.5f')
cat hora_altair.outnp

# playing with OS commands
import os
# executing a command
os.system('ls')
# executing a command and capturing its stdout
lsin = os.popen('ls').readlines()
lsin
# listing files in a directory
import glob
files = glob.glob('hora_altair.*')
files
for file in files:
    print file
# checking that a file exists
os.path.isfile('hora_altair.txt')
os.path.isfile('hora_altair.tx')

# python has lists and arrays, similar but not the same.
# playing with a list and comparing to arrays
l = range(10)
l
# reversing the order of the list
l.reverse()
l
# sorting the list
l.sort()
l
# introducing conditions and booleans
if os.path.isfile('hora_altair.txt'):
    print files
if os.path.isfile('hora_altair.txt'):
    print files
else:
    print 'File does not exist'
if os.path.isfile('hora_altair.tx'):
    print files
else:
    print 'File does not exist'

# using that knowledge to filter a list 
l
for li in l:
    if li > 5:
        print li
for li in l:
    if li > 5 and li < 7:
        print li
# True and False can be seen as 1 and 0, respectively
# and AND and OR can be seen as * and +, respectively
0*1
0+1

# creating an array
x = arange(10)
x
# easy filtering
x[((x>5)*(x<7))]
# let us try it with a large array 
xx = arange(100000)
xx
xx.shape
# actually, let us not be shy and work with a really large one
xx = arange(1000000)
xx
xx.shape
# fast results and coding
xx[(xx>100)*(x<150)]
xx
xx[(xx>100)*(xx<150)]
xx[(xx>100)*(xx<1500)]
xx[(xx>100.)*(xx<1500.)]
xx[(xx>100.)*(xx<1500.)]*xx

# very resourceful
# generate random numbers following a gaussian distribution
x = randn(100000)
y = randn(100000)
# plotting as a heat map
hexbin(x,y)
show()

