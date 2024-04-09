# 表: Person

# +-------------+---------+
# | 列名         | 类型     |
# +-------------+---------+
# | PersonId    | int     |
# | FirstName   | varchar |
# | LastName    | varchar |
# +-------------+---------+
# personId 是该表的主键（具有唯一值的列）。
# 该表包含一些人的 ID 和他们的姓和名的信息。
 

# 表: Address

# +-------------+---------+
# | 列名         | 类型    |
# +-------------+---------+
# | AddressId   | int     |
# | PersonId    | int     |
# | City        | varchar |
# | State       | varchar |
# +-------------+---------+
# addressId 是该表的主键（具有唯一值的列）。
# 该表的每一行都包含一个 ID = PersonId 的人的城市和州的信息。
 

# 编写解决方案，报告 Person 表中每个人的姓、名、城市和州。如果 personId 的地址不在 Address 表中，则报告为 null 。

# 以 任意顺序 返回结果表。

# 结果格式如下所示。

 

# 示例 1:

# 输入: 
# Person表:
# +----------+----------+-----------+
# | personId | lastName | firstName |
# +----------+----------+-----------+
# | 1        | Wang     | Allen     |
# | 2        | Alice    | Bob       |
# +----------+----------+-----------+
# Address表:
# +-----------+----------+---------------+------------+
# | addressId | personId | city          | state      |
# +-----------+----------+---------------+------------+
# | 1         | 2        | New York City | New York   |
# | 2         | 3        | Leetcode      | California |
# +-----------+----------+---------------+------------+
# 输出: 
# +-----------+----------+---------------+----------+
# | firstName | lastName | city          | state    |
# +-----------+----------+---------------+----------+
# | Allen     | Wang     | Null          | Null     |
# | Bob       | Alice    | New York City | New York |
# +-----------+----------+---------------+----------+
# 解释: 
# 地址表中没有 personId = 1 的地址，所以它们的城市和州返回 null。
# addressId = 1 包含了 personId = 2 的地址信息。


# Pandas 代码:

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # 合并两个表，使用 personId 作为连接键
    # left join 若 personId 在 address 表中不存在，则 city 和 state 列返回 null
    combined = person.merge(address, on='personId', how='left')
    columns = ['firstName', 'lastName', 'city', 'state']
    # 方括号内指定列顺序，构造结果表
    combined = combined[columns]
    return combined