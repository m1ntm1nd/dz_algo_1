num = int(input())
if not(abs(num) > 2147483647):
    num = bin(num)
    print(num)
    nums = str(num)
    nums = nums[0] + nums[2:]
    print(nums)
    max = 0
    for y in range(len(nums)):
        count = 0
        flag = 0
        for x in nums[y:]:
            if x == '0' and flag == 0:
                count +=1
                flag = 1
            elif x == '0' and flag == 1:
                break
            else:
                count +=1
        if count > max:   
            max = count
    print(max)
