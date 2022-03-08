score = int(input())
print('A') if 90<=score<=100 else print("B") if 80<=score<90 else print ("C") if 70<=score<80 else print("D") if 60<=score<70 else print("F")

# TIL : 아래처럼 간결하기 90보다 큰 경우 80보다 큰 경우로 간결하게 쓸 수 있다
# print('A') if score>=90 else print("B") if score >=80 else print ("C") if score>=70 else print("D") if score>=60 else print("F")
