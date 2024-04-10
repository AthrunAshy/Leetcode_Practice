# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

# 示例 1：


# 输入：list1 = [1,2,4], list2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 示例 2：

# 输入：list1 = [], list2 = []
# 输出：[]
# 示例 3：

# 输入：list1 = [], list2 = [0]
# 输出：[0]
 

# 提示：

# 两个链表的节点数目范围是 [0, 50]
# -100 <= Node.val <= 100
# list1 和 list2 均按 非递减顺序 排列


# Python 代码：

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个虚拟头节点和指针
        dummy = ListNode()
        curr = dummy

        # 遍历两个链表，将较小的节点添加到新链表中
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            # 把curr指针移动到下一个位置
            curr = curr.next

        # 处理剩余未遍历完的链表
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        # 返回新链表的头节点
        return dummy.next

