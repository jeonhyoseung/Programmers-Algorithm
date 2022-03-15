
n = num = int(input()) # 68을 n,num에 동시에 넣을수 있음
count = 0
while True:
    ten = n // 10   # 몫 구하기 6
    one = n % 10 # 나머지 구하기 8
    total = ten + one # 14
    count += 1 # 횟수 카운트하기
    n = int(str(n % 10) + str(total % 10)) # n에 새로운 값 넣기
    if(num == n): 
        break
print(count)
# TIL :1) n과 num을 동시에 선언이 가능하다는 것
#  10보다 작은수는 따로 구현할 필요 없음

    


    


