# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

 

# 示例 1：


# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 示例 2：

# 输入：root = []
# 输出：[]
# 示例 3：

# 输入：root = [1]
# 输出：[1]
 

# 提示：

# 树中节点数目在范围 [0, 100] 内
# -100 <= Node.val <= 100


# Python 代码：

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        stack = []
        result = []
        current = root
        # 栈中存放的是节点，所以先把根节点入栈
        while current or stack:
            while current:
                # 左子树入栈
                stack.append(current)
                current = current.left
                
            # 栈顶节点出栈，访问节点值，并将右子树入栈
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result