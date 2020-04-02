from random import randrange

nums = []

def check(num_list, taget):

    result = false

    for x in num_list:
        if x == target:
            result = True
            break

#루프를 nums가 6개가 되는동안
while len(nums) < 6:

    num = randrange(1,46)
    nums.append(num)

    if check(nums, num) == True:
        continue
#1부터 45 사이의 숫자를 뽑는다
#    num.pop(nums)

    print(nums)
#뽑은 값이 있다면 다시 뽑는다


