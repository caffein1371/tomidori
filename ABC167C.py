##########################################
import io
import sys

_INPUT = """\
3 3 10
60 2 2 4
70 8 7 9
50 2 3 9

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M,X = map(int,input().split())
clist = []
for i in range(N):
    clist.append(list(map(int,input().split())))
print (clist)
