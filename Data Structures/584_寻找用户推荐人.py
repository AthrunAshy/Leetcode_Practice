# 表: Customer

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | referee_id  | int     |
# +-------------+---------+
# 在 SQL 中，id 是该表的主键列。
# 该表的每一行表示一个客户的 id、姓名以及推荐他们的客户的 id。
# 找出那些 没有被 id = 2 的客户 推荐 的客户的姓名。

# 以 任意顺序 返回结果表。

# 结果格式如下所示。

 

# 示例 1：

# 输入： 
# Customer 表:
# +----+------+------------+
# | id | name | referee_id |
# +----+------+------------+
# | 1  | Will | null       |
# | 2  | Jane | null       |
# | 3  | Alex | 2          |
# | 4  | Bill | null       |
# | 5  | Zack | 1          |
# | 6  | Mark | 2          |
# +----+------+------------+
# 输出：
# +------+
# | name |
# +------+
# | Will |
# | Jane |
# | Bill |
# | Zack |
# +------+


# Pandas 代码：

import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # 筛选出 referee_id 不等于 2 或 referee_id 为空的客户，只保留 name 列，注意使用 ~ 取反，| 逻辑或
    # 注意使用 isna() 判断是否为空
    df = customer[~(customer['referee_id'] == 2) | customer['referee_id'].isna()]['name']
    return pd.DataFrame(df)