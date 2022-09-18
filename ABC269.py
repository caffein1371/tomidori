##########################################
import io
import sys

_INPUT = """\
576461302059761664

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
X = int(input())
ans = []
for i in range(X):
    for j in range(i>>1):
        print(X&j) 

ans=list(set(ans))

for i in range(len(ans)):
    print (ans[i])