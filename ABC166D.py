##########################################
import io
import sys

_INPUT = """\
1

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
X = int(input())
#an= n**5-(n-1)**5と仮定すると781,211,31,9,31,211,781
for a in range(-120,121):
    for b in range(-120,121):
        if a**5-b**5 ==X:
            print (a,b)
            quit()