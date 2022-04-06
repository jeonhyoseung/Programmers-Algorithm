# 문제 설명 : 
# N이 주어지고 N의 개수를 갖는 A,B의 배열이 주어진다
# S = A[0] × B[0] + ... + A[N-1] × B[N-1]
# S의 최솟값을 구하면 된다
# -> A의 최소값 * B의 최댓값
# 단, B의 배열은 재배열 하면 안됨



# a = int(input())
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))

# sorted_b = sorted(b,reverse=True)
# sorted_c = sorted(c)

# s=0
# for i in range(a):
#     s+= sorted_b[i] * sorted_c[i]

# print(s)

# 위와 같이 풀면 정답으로 인정되나 B 배열은 순서를 바꾸지 
# 않아야 하기에 pop 함수를 사용해야 함

a = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
s=0
for i in range(a):
    s+= min(b)*max(c) # 배열 b의 최솟값 * 배열 c의 최댓값
    b.pop(b.index(min(b))) # 배열 b 중에서 최솟값을 갖는 값의 인덱스를 구해서 제거
    c.pop(c.index(max(c)))  # 배열 c 중에서 최댓값을 갖는 값의 인덱스를 구해서 제거
 
print(s)
