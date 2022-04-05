N, M = map(int,input().split())
numlist = list(map(int, input().split()))
answer = 0
for i in range(len(numlist)):
    for j in range(i+1, len(numlist)):
        for k in range(j+1, len(numlist)):
            sum = numlist[i] + numlist[j] + numlist[k]
            if sum <=M:
                answer = max(answer,sum)

print(answer)  
# 문제 설명 _ 
# N : 카드 개수
# M : 원하는 합
# 2 line : 카드의 수
# 출력 -> 3장 뽑았을때 M에 가장 가까운 수

# 해설 설명 : 브루트포스 알고리즘 (무식한 방식의 완전탐색 알고리즘) 
# Line 2) 받은 입력 값을 lst화 해서 정리
# Line 4~  3중포문을 사용하여 모든 경우를 따져서 M보다 작거나 같으면 answer에 넣고
# answer에서 최대값을 고르고 맨 마직 for문에서의 answer를 출력
# 가령 카드의 수가 5,6,7,8,9 일 경우
# (5,6,7) , (5,6,8), (5,6,9), (5,7,8),(5,7,9),(6,7,8) 로 for 문이 진행 됨