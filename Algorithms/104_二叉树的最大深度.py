# 给定一个二叉树 root ，返回其最大深度。

# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

 

# 示例 1：



 

# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
# 示例 2：

# 输入：root = [1,null,2]
# 输出：2
 

# 提示：

# 树中节点的数量在 [0, 104] 区间内。
# -100 <= Node.val <= 100


# Python 代码：

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 边界条件：递归到空节点，返回 0
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

# 有点类似爬楼梯递归问题，左边和右边的高度，取最大值加 1 就是当前节点的高度