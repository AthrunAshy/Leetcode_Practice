# 销售表 Sales：

# +-------------+-------+
# | Column Name | Type  |
# +-------------+-------+
# | sale_id     | int   |
# | product_id  | int   |
# | year        | int   |
# | quantity    | int   |
# | price       | int   |
# +-------------+-------+
# (sale_id, year) 是销售表 Sales 的主键（具有唯一值的列的组合）。
# product_id 是关联到产品表 Product 的外键（reference 列）。
# 该表的每一行显示 product_id 在某一年的销售情况。
# 注意: price 表示每单位价格。
# 产品表 Product：

# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | product_id   | int     |
# | product_name | varchar |
# +--------------+---------+
# product_id 是表的主键（具有唯一值的列）。
# 该表的每一行表示每种产品的产品名称。
 

# 编写解决方案，以获取 Sales 表中所有 sale_id 对应的 product_name 以及该产品的所有 year 和 price 。

# 返回结果表 无顺序要求 。

# 结果格式示例如下。

 

# 示例 1：

# 输入：
# Sales 表：
# +---------+------------+------+----------+-------+
# | sale_id | product_id | year | quantity | price |
# +---------+------------+------+----------+-------+ 
# | 1       | 100        | 2008 | 10       | 5000  |
# | 2       | 100        | 2009 | 12       | 5000  |
# | 7       | 200        | 2011 | 15       | 9000  |
# +---------+------------+------+----------+-------+
# Product 表：
# +------------+--------------+
# | product_id | product_name |
# +------------+--------------+
# | 100        | Nokia        |
# | 200        | Apple        |
# | 300        | Samsung      |
# +------------+--------------+
# 输出：
# +--------------+-------+-------+
# | product_name | year  | price |
# +--------------+-------+-------+
# | Nokia        | 2008  | 5000  |
# | Nokia        | 2009  | 5000  |
# | Apple        | 2011  | 9000  |
# +--------------+-------+-------+


# Pandas 代码：

import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(sales, product, on='product_id', how='left')
    return df[['product_name', 'year', 'price']]


# MySQL 代码：

SELECT p.product_name, s.year, s.price
FROM Sales s
JOIN Product p ON s.product_id = p.product_id;