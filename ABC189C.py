##########################################
import io
import sys

_INPUT = """\
6
2 4 4 9 4 9

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))

l,r,x = 0,0,0
#Alist.append(1)
num = sorted(list(set(Alist)))

maxsum = -10*15
for i in range(len(num)):
  temp=0
  for j in range(len(Alist)):
    if num[i]<=Alist[j]:
      temp+=num[i]
      maxsum=max(temp,maxsum)
    else:
      temp=0
print (maxsum)
