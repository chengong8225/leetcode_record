# 找出数组中重复的数字
# 说明： 长度为n的数组，所有数字在0到n-1之间，找出重复的数字
# 如：{2, 3, 1, 0, 2, 5, 3}, 输出2或3

# tips： 利用数组下标
# 时间复杂度： O(N)
# 空间复杂度： O(1)

def solution(nums):
    if not nums:
        return None 
    
    n = len(nums)

    for i in nums:
        if i < 0 or i >= n:
            return False

    for i in range(len(nums)):
        while nums[i] != i:
            tmp1, tmp2 = nums[nums[i]], nums[i]
            if tmp1 == tmp2:
                print(tmp2)
                return True
            nums[nums[i]] = tmp2
            nums[i] = tmp1
    return False 

if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(solution(nums))