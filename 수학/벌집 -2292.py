num = int(input())
count_house=1 # 벌집 개수
count =1
while num> count_house:
    count_house+=6*count # 벓집이 6의 배수로 증가 (하단 참고)
    count +=1
print(count)

# 주어진 수의 벌집의 번호로 이동하는 최소 경로를 구하는 문제
# 1
# 2,3,4,5,6,7
# 8,9,10,11,11,12,13,14,15,16,17,18,19
# 1,7,19,37,61 ->6k 씩 증가
