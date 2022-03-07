A,B,C = map(int,input().split())

print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')
# TIL : 1) map 함수를 쓰면 한번에 선언까지 할 수 있음
# 2) print를 여러번 쓰는 것보다 마지막에 sep='\n'으로 가능 함
