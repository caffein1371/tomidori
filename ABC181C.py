##########################################
import io
import sys

_INPUT = """\
9
8 2
2 3
1 3
3 7
1 0
8 8
5 6
9 7
0 1
"""
sys.stdin = io.StringIO(_INPUT)
##########################################

import itertools

N = int(input())
ans = []
for i in range(N):
  x,y = map(int,input().split())
  ans.append([x,y])
#print (ans)
for v in itertools.permutations(ans,3):
  #v[0]が１つ目，v[1]が２つ目,v[2]が3つ目
  #print (v)
  if (v[2][1]-v[0][1])*(v[1][0]-v[0][0])==(v[1][1]-v[0][1])*(v[2][0]-v[0][0]):
      print ("Yes")
      quit()
print ("No")
