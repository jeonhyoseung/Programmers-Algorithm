a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()
for i in a:
    b = b.replace(i, 'a') 
print(len(b))

# TIL : replace(a,b) -> a를 b로 바꿈
# replace 함수 : 입력받은 문자 중에 list a 안에 있는 알파벳을 찾아서 알파벳a로 바꾼다
