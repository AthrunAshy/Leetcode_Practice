# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。

 

# 示例 1：


# 输入：head = [1,1,2]
# 输出：[1,2]
# 示例 2：


# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]
 

# 提示：

# 链表中节点数目在范围 [0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序 排列


# Python 代码：

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        
        # 新建一个指针，指向头节点，用于遍历链表
        curr = head

        # 遍历链表，如果 curr 当前节点和 curr.next 节点的值相同，则把 curr.next.next 节点的值赋值给 curr.next 节点
        # 相当于删除了 curr.next 节点
        # 再次比较 curr 当前节点和 curr.next 节点的值
        # 如果不同，则指针向后移动
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        # 链表经过上述操作后可能被修改，返回头节点将整个列表重新返回
        return head