year = int(input())
print ('1') if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0) else print('0')

#TIL : 정수를 출력하더라도 ''붙이고, = 한 개가 아닌 == 2개 채크!