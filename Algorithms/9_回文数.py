# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

# 回文数
# 是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 例如，121 是回文，而 123 不是。
 

# 示例 1：

# 输入：x = 121
# 输出：true
# 示例 2：

# 输入：x = -121
# 输出：false
# 解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3：

# 输入：x = 10
# 输出：false
# 解释：从右向左读, 为 01 。因此它不是一个回文数。
 

# 提示：

# -231 <= x <= 231 - 1


# Python 代码：

class Solution_1:
    def isPalindrome(self, x: int) -> bool:
        # 字符串反过来
        def reverse(text):
            return text[::-1]

        def is_palindrome(text):
            return text == reverse(text)
        
        # 把x转化为字符串
        text = str(x)
        if is_palindrome(text):
            return True
        else:
            return False

class Solution_2:
    def isPalindrome(self, x: int) -> bool:
        # 负数肯定不是回文数， 0肯定是回文数
        if x <= 0:
            return x == 0
        # 个位为0肯定不是回文数
        if x % 10 == 0:
            return False
        # 反转x
        reverse_x = 0
        # 反转x的一半位数
        while x > reverse_x:
            # 反转数进一位，并加上x的最低位
            reverse_x *= 10
            reverse_x += x % 10
            # x去掉最低位
            x //= 10
        # 如果x为回文数：
        # x为偶数长度：后半部分反转后和前半部分一致
        # x为奇数长度：后半部分反转后去掉最低位与x一致
        return reverse_x == x or reverse_x // 10 == x