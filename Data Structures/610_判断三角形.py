# 表: Triangle

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | x           | int  |
# | y           | int  |
# | z           | int  |
# +-------------+------+
# 在 SQL 中，(x, y, z)是该表的主键列。
# 该表的每一行包含三个线段的长度。
 

# 对每三个线段报告它们是否可以形成一个三角形。

# 以 任意顺序 返回结果表。

# 查询结果格式如下所示。

 

# 示例 1:

# 输入: 
# Triangle 表:
# +----+----+----+
# | x  | y  | z  |
# +----+----+----+
# | 13 | 15 | 30 |
# | 10 | 20 | 15 |
# +----+----+----+
# 输出: 
# +----+----+----+----------+
# | x  | y  | z  | triangle |
# +----+----+----+----------+
# | 13 | 15 | 30 | No       |
# | 10 | 20 | 15 | Yes      |
# +----+----+----+----------+


# Pandas 代码:

import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:

    # apply 方法用于对 DataFrame 进行列操作，axis=1 表示对每一列进行操作
    # lambda 函数用于定义一个匿名函数，不需要 def ，lambda arguments: expression
    # 该函数判断该三角形是否可以形成，即判断三个长度之和是否大于最长边的两倍
    # 即两边之和大于第三边，z是最长边，x+y>z => x+y+z>2z
    triangle['triangle'] = triangle.apply(lambda row: 'Yes' if sum(row) > 2 * max(row) else 'No', axis=1)

    return triangle