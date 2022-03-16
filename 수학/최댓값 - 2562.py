numbers = [int(input()) for _ in range(9)]
print(max(numbers))
print(numbers.index(max(numbers))+ 1)
# TIL : comprehension 표현식 : [실행문장 for 변수 in iterable 자료형] 형식으로 사용하면 됨 
