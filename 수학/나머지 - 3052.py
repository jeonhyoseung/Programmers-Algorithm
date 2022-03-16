array = [] # 42로 나눈 나머지를 저장 
for i in range(10):  
    a = int(input()) # 입력값을 받는 변수
    array.append(a%42) # 42로 나눈 나머지를 배열끝에 저장
array = set(array)  # set은 배열의 필터링, 즉 중복제거
print(len(array))  # len은 arr의 길이를 출력 = 갯수 출력