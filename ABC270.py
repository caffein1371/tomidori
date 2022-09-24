##########################################
import io
import sys

_INPUT = """\
5 3

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B = map(int,input().split())

print (A|B) 