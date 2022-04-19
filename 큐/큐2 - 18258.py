import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque([])

for _ in range(N):
    b = sys.stdin.readline().split()
    if b[0] == "push":
        q.append(b[1])
    elif b[0] == "pop":
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif b[0] == "size":
        print(len(q))
    elif b[0] == "empty":
        if len(q):
            print(0)
        else:
            print(1)
    elif b[0] == "front":
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif b[0] == "back":
        if len(q):
            print(q[-1])
        else:
            print(-1)

# 스택 문제 이해하면 풀 수 있음