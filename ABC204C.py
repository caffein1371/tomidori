##########################################
import io
import sys

_INPUT = """\
4 5
1 2
2 3
3 2
2 4
3 4

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
from collections import deque

N,M = map(int,input().split())

#有効グラフを以下で作る
attend = [[] for i in range(N)]
for i in range(M):
    A,B = map(int,input().split())
    attend[A].append(B)

print (attend)

print (attend[1][0])

ans = 0

# for i in range(N):
#     que = deque(attend[i])
#     count = 0
#     attendlist = [False]*N
#     while len(deque)!=0:
#         temp = que.popleft()

#         if attendlist[i]==False:
#             attendlist[i]=True
#             count+=1
#             que.append(attend[i])