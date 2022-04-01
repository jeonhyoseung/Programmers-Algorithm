import sys
input = sys.stdin.readline

N = int(input()) 
for _ in range(N):
    word = input().rstrip()

    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:] :
                 N -= 1
                 break 

print(N)

# 해석: 단어 길이의 -1 만큼 확인하는데 만약에 현재 위치의 알파벳과 다음 위치의 알파벳이 다르면
# 지금 위치의 알파벳이 뒤로 똑같은 알파벳이 있으면 총 단어의 개수에서 1을 뺀다.
# TIL : 
# 1) rstrip()은 오른쪽의 문자열을 제거하는 것인데 parameter가 없는 경우
# rstrip()은 스페이스바, 텝, 공백줄 제거
