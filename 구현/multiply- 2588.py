A = int(input())  
B = input()      

AxB2 = A * int(B[2])
AxB1 = A * int(B[1])
AxB0 = A * int(B[0])
AxB = A * int(B)

print(AxB2, AxB1, AxB0, AxB, sep='\n')

# TIL 1)  첫 문자는 숫자로 변환하고 두번째 문자는 문자열 그대로
# 2) 문자열의 인덱스를 이용해서 곱셈 표현하기