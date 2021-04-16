# 找到二维数组中的某个数
# 说明： 数组的行和列都在递增，找出特定的数。返回一个布尔值
# 如：[[1,2,8,9], [2,4,9,12], [4,7,10,13], [6，8，11，15]]

# tips： 类似于二分法
# 时间复杂度： O(m+n)
# 空间复杂度： O(1)

def solution(nums, target):
    if not nums or not nums[0]:
        return False

    m, n = len(nums), len(nums[0])
    row, col = 0, n - 1

    while row < m and col >= 0:
        if nums[row][col] == target:
            return True 
        elif nums[row][col] > target:
            col -= 1
        elif nums[row][col] < target:
            row += 1
    return False

if __name__ == '__main__':
    nums = [[1,2,8,9], [2,4,9,12], [4,7,10,13], [6,8,11,15]]
    target = 5
    print(solution(nums, target))