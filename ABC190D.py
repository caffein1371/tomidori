##########################################
import io
import sys

_INPUT = """\
12

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())

#2N=x*yの問題に変換できる
ans = 0
i = 1
while i*i<=2*N:
    if 2*N%i==0:
        x=i
        y = 2*N//x
        if y%2!=0 and x%2!=1:
            ans+=1
        elif y%2!=1 and x%2!=0:
            ans+=1
    i+=1

print (ans*2)