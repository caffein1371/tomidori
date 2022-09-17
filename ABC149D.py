##########################################
import io
import sys

_INPUT = """\
30 5
325 234 123
rspsspspsrpspsppprpsprpssprpsr

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()

#print (T)
ans = 0
history = []

for i in range(N):
    if T[i]=='s':
        if i<K:
            ans+=R
            history.append('r')
        elif K<=i and history[i-K]!='r':
            ans+=R
            history.append('r')
        else:
            history.append('x')

    if T[i]=='p':
        if i<K:
            ans+=S
            history.append('s')
        elif K<=i and history[i-K]!='s':
            ans+=S
            history.append('s')
        else:
            history.append('x')

    if T[i]=='r':
        if i<K:
            ans+=P
            history.append('p')
        elif K<=i and history[i-K]!='p':
            ans+=P
            history.append('p')
        else:
            history.append('x')

#print (history)
print (ans)
