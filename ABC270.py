##########################################
import io
import sys

_INPUT = """\
10 -10 1

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
X,Y,Z = map(int,input().split())

if abs(Y)>=abs(X):
    print (abs(X))
elif X>Y>Z>0 or 0>Z>Y>X:
    print (abs(X))
elif Y*Z<0 and (X>Y>0 or 0>Y>X):
    print (abs(X)+abs(Z)*2)
elif X*Y<0 :
    print (abs(X))
else:
    print (-1)