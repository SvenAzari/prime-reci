#Verison 1
#Requirements: Python3
#Version 1 only calculates how many digits is in period of decimal expansion of prime numbers. User needs to take care inputed nuber is prime.

from itertools import count

x = int(input("prime = ")) #unos

li = [] #lista za usporedbu
d = 1
c = 0

while True:
    o = d % x
    try:
        b = li.index(o)
    except ValueError:
        li.append(o)
        d = o * 10
        c +=1
    else:
        break

print (c)
