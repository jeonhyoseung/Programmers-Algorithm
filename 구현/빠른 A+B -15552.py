import sys

t= int(sys.stdin.readline())
for _ in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
# TIL : input 대신 sys를 사용하면 시간을 줄일수 있다고 한다