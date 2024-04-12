# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。

# 单词 是指仅由字母组成、不包含任何空格字符的最大
# 子字符串
# 。

 

# 示例 1：

# 输入：s = "Hello World"
# 输出：5
# 解释：最后一个单词是“World”，长度为5。
# 示例 2：

# 输入：s = "   fly me   to   the moon  "
# 输出：4
# 解释：最后一个单词是“moon”，长度为4。
# 示例 3：

# 输入：s = "luffy is still joyboy"
# 输出：6
# 解释：最后一个单词是长度为6的“joyboy”。
 

# 提示：

# 1 <= s.length <= 104
# s 仅有英文字母和空格 ' ' 组成
# s 中至少存在一个单词


# Python 代码：

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 先将字符串反转，然后统计最后一个单词的长度
        s = s[::-1]
        num = 0
        for i in range(0, len(s)):
            # 原来的字符串末尾的空格字符，现在变成了第一个单词的开头，所以跳过
            # 第一次遇到非空格字符，num 加 1
            if s[i] != ' ': num += 1
            # 非空格字符后遇到的第一个空格字符，说明当前单词结束，跳出循环，返回 num
            if num != 0 and s[i] == ' ': break
        return num

