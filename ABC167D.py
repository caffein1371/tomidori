##########################################
import io
import sys

_INPUT = """\
4 5
3 2 4 1

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K = map(int,input().split())
Alist =list(map(int,input().split()))

