a= int(input())
number = list(map(int, input().split()))
print(min(number), max(number))
# for 문 이용한 코드
#  max = number[0]
# min = number[0]
# for i in number[1: ]:
#     if i > max:
#         max =i
#     elif i < min:
#         min = i
# print(min, max)
