a = int(input())
b = list(map(int, input().split()))
max_ = max(b)

for i in range(a):
    b[i]=b[i]/max_*100
print("%.2f" %(sum(b)/a))