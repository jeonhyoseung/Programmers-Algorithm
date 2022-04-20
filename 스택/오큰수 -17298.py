import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().splilt()))
stack = []
answer = [-1 for i in range(n)]

for i in range(len(arr)):
    while stack and arr[stack[-1]] <arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)
print(*answer)


# # 1. 입력의 속도를 줄이기 위해 import sys / input = sys.stdin.readline을 사용했다.
# 2. 스택은 값이 아닌 '인덱스'를 저장해야 한다는 것을 오랜 삽질 후에 깨달았다.
# 3. 기본적으로 오큰수가 없으면 -1을 출력해야 하므로 정답 배열 answer을 -1로 초기화해준다.
# 4. 입력받은 수들 배열 arr을 탐색
#   4-1. stack이 비어있지 않고, arr[스택 맨위]가 arr[i]보다 작으면 반복
#     4-1-1. answer의 stack.pop()한 인덱스 자리에 arr[i]를 넣는다.
#   4-2. stack에 i를 넣는다.
# 5. 꿀팁인데, 파이썬에서 배열을 print할 때, 앞에 *을 붙여주면 공백을 기준으로 원소들만 나열된다.