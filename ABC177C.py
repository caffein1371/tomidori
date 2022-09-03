##########################################
import io
import sys

_INPUT = """\
3
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
temp = 10**9+7
ans = 0
sumans = sum(Alist)
for i in range(N):
    sumans-=Alist[i]
    ans+=sumans*Alist[i]

print (ans%temp)
