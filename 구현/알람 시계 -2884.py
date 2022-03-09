a, b = map(int, input().split())

if b >= 45:
    print(a, b-45)
elif b <= 44 and a >= 1:
    print(a-1, b+15)
else:
    print(23, b+15)

#  TIL : 삼항 연산자로 풀기에는 기존 문제들과 다르기에 if-elif 사용

# 다른 방법
# a, b = map(int, input().split()) 
# a, b = divmod(a * 60 + b - 45, 60) print(a % 24, b)
# print(a % 24, b)
# 수학적인 풀이로 몫과 나머지를 반환하는 divmod를 사용하는 방법이다.

