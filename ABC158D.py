##########################################
import io
import sys

_INPUT = """\
a
6
2 2 a
2 1 b
1
2 2 c
1
1


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
from collections import deque

S = input()
Q = int(input())
queue = deque(S)
flag = True
inp = []
for i in range(Q):
   inp.append(list(map(str,input().split())))

#print (inp)
for i in range(Q):
    if inp[i][0]=="1":
        if flag ==True:
            flag=False
        else:
            flag=True
    elif inp[i][0]=="2":
        if flag==True and inp[i][1]=="1":
            queue.appendleft(inp[i][2])
        elif flag==True and inp[i][1]=="2":
            queue.append(inp[i][2])
        elif flag==False and inp[i][1]=="1":
            queue.append(inp[i][2])
        elif flag==False and inp[i][1]=="2":
            queue.appendleft(inp[i][2])

ans = "".join(queue)
if flag ==False:
  ans = ans[::-1]
print (ans)