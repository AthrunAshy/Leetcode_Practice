# 表: Courses

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | student     | varchar |
# | class       | varchar |
# +-------------+---------+
# 在 SQL 中，(student, class)是该表的主键列。
# 该表的每一行表示学生的名字和他们注册的班级。
 

# 查询 至少有5个学生 的所有班级。

# 以 任意顺序 返回结果表。

# 查询结果格式如下所示。

 

# 示例 1:

# 输入: 
# Courses table:
# +---------+----------+
# | student | class    |
# +---------+----------+
# | A       | Math     |
# | B       | English  |
# | C       | Math     |
# | D       | Biology  |
# | E       | Math     |
# | F       | Computer |
# | G       | Math     |
# | H       | Math     |
# | I       | Math     |
# +---------+----------+
# 输出: 
# +---------+ 
# | class   | 
# +---------+ 
# | Math    | 
# +---------+
# 解释: 
# -数学课有6个学生，所以我们包括它。
# -英语课有1名学生，所以我们不包括它。
# -生物课有1名学生，所以我们不包括它。
# -计算机课有1个学生，所以我们不包括它。


# Pandas 代码:

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # size() 方法返回每组的大小，相比于coun()方法，size()方法可以返回NaN值，而count()方法不行。
    # reset_index() 方法重置索引，将原来的索引作为列的一部分，并重命名为 'count'。
    df = courses.groupby('class').size().reset_index(name='count')
    return df[df['count'] >= 5]


# MySQL 代码:

SELECT 
    class
FROM 
    courses
GROUPBY 
    class
HAVING COUNT(student) >= 5
;