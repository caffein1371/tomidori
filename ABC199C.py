##########################################
import io
import sys

_INPUT = """\
2
FLIP
6
1 1 3
2 0 0
1 1 2
1 2 3
2 0 0
1 1 4

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N=int(input())
S=list(input())
Q=int(input())
#print (S)
for i in range(Q):
    T,A,B = map(int,input().split())
    #print (S[N:2*N])
    if T==2:
        #S[0:N+1],S[N:2*N] = S[N:2*N],S[0:N+1]
        temp = S[0:N]
        S[0:N] = S[N:2*N]
        S[N:2*N] = temp

    elif T==1:
        S[A-1], S[B-1] = S[B-1], S[A-1]
print ("".join(S))
