sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수일 경우 부터 제외시키기
        bag += (sugar // 5)  
        print(bag)
        break # while 문 나오기
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 반복 설탕은 -3, 가방은 +1
else :
    print(-1) # 예외 처리