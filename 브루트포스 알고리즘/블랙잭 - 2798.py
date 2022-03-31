n, m = map(int, input().split())
numlist = list(map(int, input().split()))

answer = 0

for i in range(len(numlist)):
    for j in range(i + 1, len(numlist)):
        for k in range(j + 1, len(numlist)):
            sum = numlist[i] + numlist[j] + numlist[k]
            if sum <= m:
                answer = max(answer, sum)
print(answer)
 
# 딜러는 N장의 카드를 숫자가 보이게
# ->
# M을 외치면
# ->
# N장의 카드 중 3장을 골라야 함
# ->
# M을 넘지 않으면서 M과 가깝게 3장을 골라야 함

# 입력
# N M
# A1, A2 --------AN

# 출력
# M에 최대한 가까운 카드 3장의 합