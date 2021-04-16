# 整体思路： 分治，找到某一个数的正确位置后，分成左小右大两个数组，再次快排。
nums = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
nums_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]

def quick_sort(nums, left, right):
    if left >= right:
        return 
    
    i, j = left, right
    base = nums[left]

    while i < j:
        while i < j and nums[j] >= base:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

        while i < j and nums[i] <= base:
            i += 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    # nums[left], nums[i] = nums[i], nums[left]
    quick_sort(nums, left, i - 1)
    quick_sort(nums, i + 1, right)

print(nums)
quick_sort(nums, 0, len(nums) - 1)
print(nums)