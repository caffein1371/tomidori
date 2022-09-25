##########################################
import io
import sys

_INPUT = """\
10 -10 1

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
X,Y,Z = map(int,input().split())

if Y>X>0:
    print (X)
elif 0>X>Y:
    print (abs(X))
elif X>Y>Z>0:
    print (X)
elif 0>Z>Y>X:
    print (abs(X))
elif X>Y>0 and 0>Z:
    print (X+abs(Z)*2)
elif 0>Y>X and 0<Z:
    print (abs(X)+Z*2)
elif Z>X>Y>0:
    print (-1)
elif X>Z>Y>0:
    print (-1)
elif 0>Y>X>Z:
    print (-1)
elif 0>Y>Z>X:
    print (-1)
elif X>Z>0 and 0>Y:
    print (X)
elif 0>Z>X and 0<Y:
    print (abs(X))
elif X>0 and 0>Y>Z:
    print (X)
elif 0>X and 0<Y<Z:
    print (abs(X))
elif X>0 and 0>Z>Y:
    print (X)
elif 0>X and 0<Z<Y:
    print (abs(X)) 