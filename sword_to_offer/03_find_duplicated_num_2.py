# 找出数组中重复的数字2
# 说明： 长度为n+1的数组，所有数字在1到n之间，找出重复的数字且不能修改数组
# 如：{2, 3, 5, 4, 3, 2, 6, 7}, 输出2或3

# tips： 类似于二分法
# 时间复杂度： O(NlogN)
# 空间复杂度： O(1)

def solution(nums):
    if not nums:
        return -1
    
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        count = helper(nums, left, right)

        if left == right:
            if count > 1:
                print(left)
                return left 
            else:
                break 

        if count > mid - left + 1:
            right = mid 
        else:
            left = mid + 1
    return -1 

def helper(nums, left, right):
    if not nums:
        return 0

    count = 0
    for i in nums:
        if i >= left and i <= right:
            count += 1
    return count

if __name__ == '__main__':
    nums = [2, 3, 5, 4, 3, 2, 6, 7]
    print(solution(nums))