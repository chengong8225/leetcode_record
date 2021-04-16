# 整体思路：
# 两两对比，调整逆序对的位置。如果没有逆序对，说明排序已经完成，可以跳出排序过程。
nums = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
nums_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]

def bubble_sort(nums):
    while 1:
        state = 0  # 如果没有逆序对，那就跳出排序过程

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                state = 1
        
        if not state:
            break 

    return nums

print(bubble_sort(nums))
print(nums_out)