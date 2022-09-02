##########################################
import io
import sys

_INPUT = """\
100000
"""
sys.stdin = io.StringIO(_INPUT)
##########################################

N=int(input())
temp = set()
for a in range(2,(10**5+10)):
    for b in range(2,100):
        if a**b<=N:
            temp.add(a**b)
        else:
            break

print (N-len(temp))
