n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')
# 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
# 평균 이상인 학생 수