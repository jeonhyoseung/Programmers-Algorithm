import sys
N = int(sys.stdin.readline())
stack=[]
for _ in range(N):
    a = sys.stdin.readline().split() #  입력받을떄 split 이용해서 나눠서 입력받음
    b = a[0] # 첫 번째 입력된 값

    if b =="push":
        c = a[1]
        stack.append(c) 
    
    elif b=="pop":
        if len(stack)==0:
            print(-1)
        else :
            print(stack.pop())

    elif b=="size": 
        print(len(stack))

    elif b == "empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    
    elif b =="top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])




# 명령은 총 다섯 가지이다.
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.