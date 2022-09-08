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

a = [0]
#期待値は1を初項，1/2を差とする等差数列
for i in range(1,1001):
    temp = 1+(i-1)*(1/2)
    a.append(temp)
#print (a[1])

tempsum = 0
#print (plist[0:K])
for i in range(0,K):
    tempsum+= a[plist[i]]
ans = -10**15
for i in range(K-1,N-1):
    tempsum = tempsum+a[plist[i+1]]-a[plist[i+1-K]]
    ans = max(tempsum,ans)
print (ans)
