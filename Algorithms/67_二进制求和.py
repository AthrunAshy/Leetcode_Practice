# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。

 

# 示例 1：

# 输入:a = "11", b = "1"
# 输出："100"
# 示例 2：

# 输入：a = "1010", b = "1011"
# 输出："10101"
 

# 提示：

# 1 <= a.length, b.length <= 104
# a 和 b 仅由字符 '0' 或 '1' 组成
# 字符串如果不是 "0" ，就不含前导零


# Python 代码：

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # carry 变量用于记录进位，result 变量用于存储结果
        carry = 0
        result = ""

        # 两个字符串的长度
        m, n = len(a), len(b)

        # i, j 初始化为两个字符串的最后一个字符的索引
        i, j = m - 1, n - 1

        # i, j 逆序遍历两个字符串
        while i >= 0 or j >= 0:

            # s 先初始化为进位
            s = carry
            # 判断 i, j 位置是否到达字符串的最前面
            if i >= 0:
                # 如果 i 位置有字符，则加上 i 位置字符的整数值，因为 i 位置本来是字符，而不是整数
                s += int(a[i])
                # 索引向前移动
                i -= 1
            if j >= 0:
                s += int(b[j])
                j -= 1

            # 计算当前位的和的最后一位 digit 和进位 carry，更新进位 carry 为 s // 2（整除2得到进位）
            digit = s % 2
            carry = s // 2

            # 结果字符串的最高位为当前位的和，先把digit转换为字符串，再加到结果字符串的最左边
            result = str(digit) + result

        # 处理最后一位的进位，如果循环到最后仍有进位，则把进位加到结果字符串最左边
        if carry:
            result = str(carry) + result

        return result