# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

 

# 示例 1：

# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：

# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
 

# 提示：

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成


# Python 代码：

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 列表为空情况处理
        if not strs:
            return ""

        # 将字符串数组按照字典序排序，即按照字母表顺序排列，
        # 因为第一个和最后一个字符串的公共前缀部分，也必然是中间字符串的公共前缀部分，
        # 这样只需要比较第一个和最后一个字符串的公共前缀即可
        strs.sort()

        # 获取排序后的第一个和最后一个字符串
        first_str = strs[0]
        last_str = strs[-1]

        # 比较第一个和最后一个字符串的公共前缀
        prefix = ""
        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] == last_str[i]:
                prefix += first_str[i]
            else:
                break

        return prefix