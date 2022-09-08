##########################################
import io
import sys

_INPUT = """\
10 4
17 13 13 12 15 20 10 13 17 11

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K=map(int,input().split())
plist = list(map(int,input().split()))

e = [0]*N
#期待値は1を初項，1/2を差とする等差数列
for i in range(N):
    e[i] = (plist[i]+1)/2
#print (e[0])

tempsum = 0
for i in range(0,K):
    tempsum+= e[i]
ans = tempsum
for i in range(K,N):
    tempsum = tempsum+e[i]-e[i-K]
    ans = max(tempsum,ans)
print (ans)
