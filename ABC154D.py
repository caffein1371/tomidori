##########################################
import io
import sys

_INPUT = """\
5 3
1 2 2 4 5

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K=map(int,input().split())
plist = list(map(int,input().split()))
