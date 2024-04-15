# 给你一个二叉树的根节点 root ， 检查它是否轴对称。

 

# 示例 1：


# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 示例 2：


# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
 

# 提示：

# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100


# Python 代码：

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return isMirror(root.left, root.right)
    
# 思路：
# 判断是否对称，可按以下步骤：
# 1. 先判断根节点是否为空，为空则返回True
# 2. 递归判断左子树和右子树是否对称，即判断左子树的左子树和右子树的右子树是否相同，左子树的右子树和右子树的左子树是否相同
# 3. 递归的终止条件是左右子树都为空，或者左右子树有一个为空，则返回False
# 其中，第二步类似判断两个树是否相同，只需要把左右子树交换即可。