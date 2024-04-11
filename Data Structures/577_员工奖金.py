# 表：Employee 

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | empId       | int     |
# | name        | varchar |
# | supervisor  | int     |
# | salary      | int     |
# +-------------+---------+
# empId 是该表中具有唯一值的列。
# 该表的每一行都表示员工的姓名和 id，以及他们的工资和经理的 id。
 

# 表：Bonus

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | empId       | int  |
# | bonus       | int  |
# +-------------+------+
# empId 是该表具有唯一值的列。
# empId 是 Employee 表中 empId 的外键(reference 列)。
# 该表的每一行都包含一个员工的 id 和他们各自的奖金。
 

# 编写解决方案，报告每个奖金 少于 1000 的员工的姓名和奖金数额。

# 以 任意顺序 返回结果表。

# 结果格式如下所示。

 

# 示例 1：

# 输入：
# Employee table:
# +-------+--------+------------+--------+
# | empId | name   | supervisor | salary |
# +-------+--------+------------+--------+
# | 3     | Brad   | null       | 4000   |
# | 1     | John   | 3          | 1000   |
# | 2     | Dan    | 3          | 2000   |
# | 4     | Thomas | 3          | 4000   |
# +-------+--------+------------+--------+
# Bonus table:
# +-------+-------+
# | empId | bonus |
# +-------+-------+
# | 2     | 500   |
# | 4     | 2000  |
# +-------+-------+
# 输出：
# +------+-------+
# | name | bonus |
# +------+-------+
# | Brad | null  |
# | John | null  |
# | Dan  | 500   |
# +------+-------+


# Pandas 代码：

import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # 两表合并，合并时使用左连接，保留 Employee 表中所有列
    # 并只保留 empId、name、bonus 列
    df = employee.merge(bonus, how='left', on='empId')[['name', 'bonus']]
    # 用.isna() 方法筛选奖金为空，| 运算符表示或，筛选出符合条件的员工
    return df[(df['bonus'].isna()) | (df['bonus'] < 1000)]