N, M = map(int, input().split())
visited = [False] * N
out, out_all = [], []

def solve(depth, N, M):
    if depth == M:
        out_str = ' '.join(map(str, sorted(out)))
        if out_str not in out_all:
            out_all.append(out_str)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solve(depth+1, N, M)
            visited[i] = False
            out.pop()
solve(0, N, M)

for i in out_all:
    print(i)