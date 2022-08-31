##########################################
import io
import sys

_INPUT = """\
4 330
0 1 10 100
1 0 20 200
10 20 0 300
100 200 300 0
"""
sys.stdin = io.StringIO(_INPUT)
##########################################
import itertools

N,K = map(int,input().split())
Tlist = []
for i in range(N):
    T = list(map(int,input().split()))
    Tlist.append(T)
