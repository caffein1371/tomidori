##########################################
import io
import sys

_INPUT = """\
5 5
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0
"""
sys.stdin = io.StringIO(_INPUT)
##########################################
import itertools

N,K = map(int,input().split())
Tlist = []
for i in range(N):
    T = list(map(int,input().split()))
    Tlist.append(T)
#print(Tlist)
ans = 0
root = tuple()
for v in itertools.permutations(range(1,N),N-1):
    root=(0,)+v+(0,)
    temp = 0
    for i in range(N):
        #print (Tlist[root[i]][root[i+1]])
        temp+=Tlist[root[i]][root[i+1]]
    if temp==K:
        ans+=1
print (ans)
