##########################################
import io
import sys

_INPUT = """\
1234 56789 314159265

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B,X = map(int,input().split())

def price(N):
    return X<A*N+B*len(str(N))

ok = 1
ng = 10**20
middle = 1
if price(middle):
    print (0)
    quit()

while 1<ng-ok:
    middle = (ok+ng)//2
    if price(middle):
        ng = middle
    else:
        ok = middle
if 10**9<ok:
    print (10**9) 
    quit()

print (ok)