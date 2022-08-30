##########################################
import io
import sys

_INPUT = """\
2 15
200 5
350 3
"""
sys.stdin = io.StringIO(_INPUT)
##########################################

n,x = map(int,input().split())
vp = []
for i in range(n):
    v,p = map(int,input().split())
    vp.append([v,p])
ans = 0
for i in range(len(vp)):
    #print (vp[i])
    ans+= vp[i][0]*vp[i][1]
    if ans>x*100:
        print (i+1)
        quit()
print (-1)