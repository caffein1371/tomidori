##########################################
import io
import sys

_INPUT = """\
300 333 1

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B,W = map(int,input().split())

W=W*1000
#個数の最大値を求める
maxtemp = W//A
mintemp = W//B
if W%A==0 and W%B==0:
    print (str(mintemp)+" "+str(maxtemp))
    quit()

#個数の最小値を求める
minans = float(INF)
maxans = float(-INF)

for i in range(A,B+1,5):
    


print (maxtemp)
print (mintemp)
# for i in range():
#     if W%i=0 and W-(W//i)==0:



