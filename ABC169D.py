##########################################
import io
import sys

_INPUT = """\
1000000007

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())

z = 2
#整数 Nの素因数の最大値は高々\sqrt{N}以下になる

def fac(N):
    fact = []
    i = 2 
    while i*i<=N:
        if N%i==0:
            fact.append(i)
            N=N//i
        else:
            i+=1
    if N!=1:
        fact.append(N)

    return fact

fact = list(set(fac(N)))
#print (fact)

ans = 0
if N==1:
    print (0)
    quit()

for p in fact:
    for e in range(1,10**12):
        if N%p**e==0:
            ans+=1
            N = N//p**e
        else:
            break

print (ans)