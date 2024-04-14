# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

 

# 示例 1：

# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。
# 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
# 示例 2：

# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
# 解释：需要合并 [1] 和 [] 。
# 合并结果是 [1] 。
# 示例 3：

# 输入：nums1 = [0], m = 0, nums2 = [1], n = 1
# 输出：[1]
# 解释：需要合并的数组是 [] 和 [1] 。
# 合并结果是 [1] 。
# 注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
 

# 提示：

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109


# Python 代码：

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # nums1 指针 p1 指向 nums1 m-1 位置，nums2 指针 p2 指向 nums2 末尾，nums1 指针 p 指向 nums1 末尾
        p1, p2, p = m - 1, n - 1, m + n - 1

        # nums2 还有要合并的元素
        while p2 >= 0:  
            
            # 如果 nums1[p1] 大于 nums2[p2]，则把 nums1[p1] 放到 nums1[p] 位置
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            # 如果 p1 < 0，即 nums1 已经全部合并完，或者 nums1[p1] 小于等于 nums2[p2]，则把 nums2[p2] 放到 nums1[p] 位置
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

# 时间复杂度：O(m+n)，其中 m 和 n 分别表示 nums1 和 nums2 的元素数目，分别遍历 nums1和nums2，最多需要 m+n 次。
# 空间复杂度：O(1)，在原来的数组 nums1 上进行操作，不需要额外的空间。
# nums2 数组的数字移到末尾空位，占用一个空位，总共空位数等于 nums2 的元素个数，足够放下 nums2 的元素。
# nums1 数组的数字移到末尾空位，又产生了一个新的空位，空位个数不变，还是等于 nums2 的元素个数，所以足够放下 nums2 的元素。