# 整体思路：
# 依次选择最小的数插在最前面。
nums = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
nums_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]

def select_sort(nums):
    res = []

    while nums:
        # min_idx 记录最小值及其下标
        min_idx = [0, nums[0]]

        for i in range(len(nums)):
            if nums[i] < min_idx[1]:
                min_idx = [i, nums[i]]
        
        res.append(min_idx[1])
        nums.remove(min_idx[1])
    return res

print(select_sort(nums))
print(nums_out)
