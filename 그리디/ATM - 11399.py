n = int(input())
s = list(map(int, input().split()))
num = 0
s.sort() # 오름차순 정렬
for i in range(n):
    for j in range(i + 1):
        num += s[j]
print(num)