##########################################
import io
import sys

_INPUT = """\
300 333 1

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B,W = map(int,input().split())

W=W*1000
mintemp = 10**15
maxtemp = -10**15

for i in range(1,10**6+10):
    if A*i<=W<=B*i:
        mintemp = min(mintemp,i)
        maxtemp = max(maxtemp,i)

if mintemp == 10**15:
    print ("UNSATISFIABLE")
else:
    print (mintemp,maxtemp)