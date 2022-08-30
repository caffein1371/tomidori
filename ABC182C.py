##########################################
import io
import sys

_INPUT = """\
6227384
"""
sys.stdin = io.StringIO(_INPUT)
##########################################

N = input()

temp = [int(i)%3 for i in N]
#print (temp)
intN = int(N)

if intN%3==0:
    print (0)
elif intN%3==1:
    #print (temp)
    if 1 in temp:
        if len(N)<=1:
            print (-1)
        elif len(N)>=2:
            print (1)
    else:
        if len(N)<=2:
            print (-1)
        elif len(N)>=3:
            print (2)
elif intN%3==2:
    if 2 in temp:
        if len(N)<=1:
            print (-1)
        else:
            print (1)
    else:
        if len(N)<=2:
            print (-1)
        else:
            print (2)