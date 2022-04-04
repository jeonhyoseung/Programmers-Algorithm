A, B, V = map(int, input().split())
 
high = V - A
if high % (A-B) == 0:
    first = int(high/(A-B))
else:
    first = int(high/(A-B) + 1)
print(first + 1)