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
C = []
A = []
for i in range(N):
    temp = list(map(int,input().split()))
    C.append(temp[0])
    A.append(temp[1:])
#rint (C)
#print (A)
ansmin = 10**15

#左にシフトさせる（１を立てる）
#2^N試すことになる
for i in range(1<<N):
    cost = 0
    skill = [0]*M
    #パターンを試す
    for shift in range(N):
        #１つ右にシフトビットして，1とのandをとり１をとれば買ったとみなす
        if i>>shift &1==1:
            cost+=C[shift]
            for j in range(M):
                skill[j]+= A[shift][j]
    if X<=min(skill):
        ansmin = min(cost,ansmin)

if ansmin ==10**15:
    print (-1)
else:
    print (ansmin)



