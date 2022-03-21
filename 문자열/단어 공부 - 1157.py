s = input().upper()
s_set = list(set(s))

cnt = []

for i in s_set :
    cnt.append(s.count(i))

if cnt.count(max(cnt)) >1 :
    print("?")
else : 
    print(s_set[cnt.index(max(cnt))])    