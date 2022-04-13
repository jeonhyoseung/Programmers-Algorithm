a,b,c= map(int,input().split())
if b>=c:
    print(-1)
else:
  print(int(a/(c-b))+1)

# 아래 코드처럼 하면 시간초과
# a,b,c= list(map(int,input().split()))
# cnt =0
# s=0
# if b>c:
#     cnt = -1
# else:
#     while s >=0:
#         cnt +=1
#         s =a+(b*cnt)-c*cnt
# print(cnt)

