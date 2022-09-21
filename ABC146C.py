##########################################
import io
import sys

_INPUT = """\
1234 56789 314159265

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B,X = map(int,input().split())

ans = -10**15

i = 0
while A*i+B*(i//10+1)<=X:
    ans = max(ans,A*i+B*(i//10+1))
    i+=1
if i ==0:
    print (0)
else:
    print (i-1)