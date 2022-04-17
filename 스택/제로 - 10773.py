a = int(input())
stack = []
for _ in range(a):
    b = int(input())
    if b ==0:
        stack.pop()
    else:
        stack.append(b)
print(sum(stack))

# 입력 : 첫 째 줄에 몇 개의 수를 입력 받을지
# 둘 쨰 줄 부터는 게쏙 추가
# 중간에 0 들어가면 앞에 들어간 수 제거
# stack 으로 문풀
# pop 통해서 제거하면 됨 