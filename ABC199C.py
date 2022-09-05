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
S.insert(0,"0")
flag = True
ans = []
for i in range(Q):
    T,A,B = map(int,input().split())
    #print (S[N:2*N])
    if T==2:
        if flag:
            flag =False
        else:
            flag =True
    elif T==1:
        if flag:
            S[A],S[B]=S[B],S[A]
        #A,BがNより大きいか小さいかで，A,Bの移動距離を変える
        else:
            if A<=N:
                A+=N
            else:
                A-=N
            if B<=N:
                B+=N
            else:
                B-=N
            S[A],S[B]=S[B],S[A]

left = S[1:N+1]
right = S[N+1:2*N+1]
    #Nを境に入れ替える
if flag ==True:
    ans = left+right
else:
    ans = right+left
print ("".join(ans))
