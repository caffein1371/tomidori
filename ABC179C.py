##########################################
import io
import sys

_INPUT = """\
2 3 2
..#
###
"""
sys.stdin = io.StringIO(_INPUT)
##########################################
H,W,K = map(int,input().split())
gyoretsu = []
for i in range(H):
    temp = list(input())
    gyoretsu.append(temp)
#print (gyoretsu)
ans = 0
for gyored in range(1<<H):
    for retsured in range(1<<W):
        black = 0
        for gyo in range(H):
            for retsu in range(W):
                if gyored>>gyo &1 ==0 and retsured>>retsu &1 ==0:
                    if gyoretsu[gyo][retsu]=="#":
                        black+=1
        if black==K:
            ans+=1
print (ans)

