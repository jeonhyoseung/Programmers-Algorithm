a = int(input())
b=0
for i in range(1,a+1):
    b+= i 
print(b)

# TIL : 1) range는 a+1까지해야 a까지 범위 설정이 됨
# 2) sum 함수를 이용하면 쉽게 풀 수 있음
# print(sum(range(1, int(input())+1)))
