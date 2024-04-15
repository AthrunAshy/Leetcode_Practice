# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

 

# 示例 1：


# 输入：p = [1,2,3], q = [1,2,3]
# 输出：true
# 示例 2：


# 输入：p = [1,2], q = [1,null,2]
# 输出：false
# 示例 3：


# 输入：p = [1,2,1], q = [1,1,2]
# 输出：false
 

# 提示：

# 两棵树上的节点数目都在范围 [0, 100] 内
# -104 <= Node.val <= 104


# Python 代码：

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 必须先判断p和q是否都为空
        if not p and not q:
            return True
        # 不都为空情况下，再判断p和q是否只有其中一个为空
        if not p or not q:
            return False
        # 都不为空情况下，再判断p和q的val是否相同
        if p.val!= q.val:
            return False
        # 递归判断左右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

   
# 上面三个 if 语句的作用是递归的边界条件
# 注意前两个 if 语句顺序不能颠倒，防止出现短路效应，在 p 和 q 都为空的情况下，直接返回 False
