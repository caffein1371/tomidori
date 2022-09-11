##########################################
import io
import sys

_INPUT = """\
6
30 10 60 10 60 50

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Hlist = [0]+list(map(int,input().split()))

dp = [10**15]*(N+1)

dp[1]=0
dp[2]=abs(Hlist[2]-Hlist[1])

for i in range(3,N+1):
    cost2=dp[i-2]+abs(Hlist[i]-Hlist[i-2])
    cost1=dp[i-1]+abs(Hlist[i]-Hlist[i-1])
    dp[i]= min(cost2,cost1)
print (dp[N])

