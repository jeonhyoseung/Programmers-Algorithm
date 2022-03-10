A, B, C = map(int, input().split())
print(A*1000+10000) if (A == B == C) else print(A*100+1000) if (A == B or A == C) else print(B*100+1000) if(B==C) else print(max(A,B,C)*100)

# TIL : 수 계산할때 금액 0 갯수 조심 하기!, 
# 삼항 연산자에서 elif 사용이 아닌 else 사용하기,
# 두 수중에 큰수 비교할때는 max 함수 사용!