##########################################
import io
import sys

_INPUT = """\
1000000000000000 1000000000000000 1000000000000000

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
X,K,D = map(int,input().split())

X = abs(X)
if X-K*D>0:
    print (X-K*D)
    quit()

#残りの動ける回数が偶数か奇数か
if (K-(X//D))%2==0:
    print (X-D*(X//D))
else:
    print (abs(X-D*K))
