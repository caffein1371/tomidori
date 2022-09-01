##########################################
import io
import sys

_INPUT = """\
100000

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
import math
N=int(input())
print (math.log2(N))
print (2**16)
print (2**17)