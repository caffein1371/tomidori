##########################################
import io
import sys

_INPUT = """\
6
2 4 4 9 4 9

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
import numpy as np
N = int(input())
Alist = list(map(int,input().split()))

l,r,x = 0,0,0

num = sorted(list(set(Alist)),reverse=True)

temp = -10**15
nlist = np.array(Alist)
print (nlist)
#for i in range(len(num)):