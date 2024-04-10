# Customers 表：

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# 在 SQL 中，id 是该表的主键。
# 该表的每一行都表示客户的 ID 和名称。
# Orders 表：

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | customerId  | int  |
# +-------------+------+
# 在 SQL 中，id 是该表的主键。
# customerId 是 Customers 表中 ID 的外键( Pandas 中的连接键)。
# 该表的每一行都表示订单的 ID 和订购该订单的客户的 ID。
 

# 找出所有从不点任何东西的顾客。

# 以 任意顺序 返回结果表。

# 结果格式如下所示。

 

# 示例 1：

# 输入：
# Customers table:
# +----+-------+
# | id | name  |
# +----+-------+
# | 1  | Joe   |
# | 2  | Henry |
# | 3  | Sam   |
# | 4  | Max   |
# +----+-------+
# Orders table:
# +----+------------+
# | id | customerId |
# +----+------------+
# | 1  | 3          |
# | 2  | 1          |
# +----+------------+
# 输出：
# +-----------+
# | Customers |
# +-----------+
# | Henry     |
# | Max       |
# +-----------+


# Pandas 代码：

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # 连接两个表
    df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='outer')
    # 找出没有订购任何东西的顾客
    customers_not_ordered = df[df['customerId'].isnull()]
    # 结果表
    result = pd.DataFrame(customers_not_ordered['name'])
    result.columns = ['Customers']
    return result