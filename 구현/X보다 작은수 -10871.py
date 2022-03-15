a,b = map(int, input().split())
c = list(map(int, input().split()))
for i in range(a):
    if c[i] < b:
        print(c[i], end = " ")
# TIL: 1) end 통해서 한 줄 띄어넘기가 아닌 한 칸 공백으로 출력
# 2) list함수 통해서 입력 받은 숫자의 값까지의 리스트를 만듬