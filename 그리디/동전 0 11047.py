N, K = map(int, input().split()) 
c = list()
for i in range(N):
    c.append(int(input()))

count = 0
for i in reversed(range(N)):
    count += K//c[i] 
    K = K%c[i]

print(count)