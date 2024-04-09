# 表：Employee 

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | salary      | int     |
# | managerId   | int     |
# +-------------+---------+
# id 是该表的主键（具有唯一值的列）。
# 该表的每一行都表示雇员的ID、姓名、工资和经理的ID。
 

# 编写解决方案，找出收入比经理高的员工。

# 以 任意顺序 返回结果表。

# 结果格式如下所示。

 

# 示例 1:

# 输入: 
# Employee 表:
# +----+-------+--------+-----------+
# | id | name  | salary | managerId |
# +----+-------+--------+-----------+
# | 1  | Joe   | 70000  | 3         |
# | 2  | Henry | 80000  | 4         |
# | 3  | Sam   | 60000  | Null      |
# | 4  | Max   | 90000  | Null      |
# +----+-------+--------+-----------+
# 输出: 
# +----------+
# | Employee |
# +----------+
# | Joe      |
# +----------+
# 解释: Joe 是唯一挣得比经理多的雇员。


# Pandas 代码：

import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # 合并 employee 表与 employee 表，以获取所有经理的工资信息，用 inner 连接，排除没有经理的员工
    data1 = pd.merge(employee, employee, left_on='id', right_on='managerId', how='inner')
    # salary_x 列是经理的工资，salary_y 列是被经理管理的员工的工资，分别对应于 left_on 和 right_on 参数
    data2 = data1[data1['salary_x'] < data1['salary_y']]
    # 选取 name_y 列（被经理管理的员工的姓名）作为结果，并重命名为 Employee
    data3 = data2[['name_y']].rename(columns={'name_y': 'Employee'})
    # 外层方括号是为了将结果转化为 DataFrame 格式，内层方括号是为了选取 Employee 列
    return data3[['Employee']]