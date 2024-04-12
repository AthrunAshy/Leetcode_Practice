# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 请必须使用时间复杂度为 O(log n) 的算法。

 

# 示例 1:

# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
# 示例 2:

# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
# 示例 3:

# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
 

# 提示:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums 为 无重复元素 的 升序 排列数组
# -104 <= target <= 104


# Python 代码：

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 初始化 left 和 right 指针，left 指向数组第一个元素，right 指向数组最后一个元素
        left, right = 0, len(nums) - 1

        # 若 target 大于等于数组最后一个元素，则返回 len(nums)
        if target >= nums[right]:
            return right + 1
        # 若 target 小于数组第一个元素，则返回 0
        elif target < nums[left]:
            return left
        
        # 若 target 值在数组的中间，则进行二分查找
        while left <= right:
            mid = (left + right) // 2  # 计算中间索引，// 为整数除法，向下取整

            if nums[mid] == target:  # 若找到目标值，则返回索引
                return mid
            elif nums[mid] < target:  # 若目标值在右半部分，则更新左边界
                left = mid + 1
            else:  # 若目标值在左半部分，则更新右边界
                right = mid - 1
        # 若循环结束，根据while条件，此时right指针在left指针左边，
        # 目标值应该插入的位置在right指针位置的右边，left指针的左边
        # 因此返回 right + 1 或者 left
        return left