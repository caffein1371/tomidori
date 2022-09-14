##########################################
import io
import sys

_INPUT = """\
3 3
1 2
2 3
3 2

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
from collections import deque

N,M = map(int,input().split())

#有効グラフを以下で作る
attend = [[] for i in range(N+1)]
for i in range(M):
    A,B = map(int,input().split())
    attend[A].append(B)

#print (attend)
#print (attend[1][0])

ans = 0

for i in range(1,N+1):
    que = deque()
    que.append(i)
    #print (que)
    count = 1
    attendlist = [False]*(N+1)
    #print (attendlist)
    attendlist[i] = True
    while len(que)!=0:
        temp = que.popleft()
        #print (temp)
        for j in attend[temp]:
            #print (attendlist)
            if attendlist[j]==False:
                #print (j)
                attendlist[j]=True
                count+=1
                que.append(j)
    ans+=count
print (ans)