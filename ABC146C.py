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
    return A*N+B*len(str(N))

left = 1
right = 10**20
middle = 1
if X<price(middle):
    print (0)
    quit()

while 1<right-left:
    middle = (left+right)//2
    if X<price(middle):
        right = middle
    else:
        left = middle
if 10**9<left:
    print (10**9) 
    quit()

print (left)