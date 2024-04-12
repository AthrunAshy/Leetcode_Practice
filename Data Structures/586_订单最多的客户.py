# 表: Orders

# +-----------------+----------+
# | Column Name     | Type     |
# +-----------------+----------+
# | order_number    | int      |
# | customer_number | int      |
# +-----------------+----------+
# 在 SQL 中，Order_number是该表的主键。
# 此表包含关于订单ID和客户ID的信息。
 

# 查找下了 最多订单 的客户的 customer_number 。

# 测试用例生成后， 恰好有一个客户 比任何其他客户下了更多的订单。

# 查询结果格式如下所示。

 

# 示例 1:

# 输入: 
# Orders 表:
# +--------------+-----------------+
# | order_number | customer_number |
# +--------------+-----------------+
# | 1            | 1               |
# | 2            | 2               |
# | 3            | 3               |
# | 4            | 3               |
# +--------------+-----------------+
# 输出: 
# +-----------------+
# | customer_number |
# +-----------------+
# | 3               |
# +-----------------+
# 解释: 
# customer_number 为 '3' 的顾客有两个订单，比顾客 '1' 或者 '2' 都要多，因为他们只有一个订单。
# 所以结果是该顾客的 customer_number ，也就是 3 。


# Pandas 代码：

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # 统计每个顾客的订单数量
    order_counts = orders['customer_number'].value_counts()
    # 获取最大订单数量
    max_orders = order_counts.max()
    # 筛选出订单数量等于最大值的顾客号
    largest_customers = order_counts[order_counts == max_orders]
    return largest_customers.reset_index().rename(columns={'index': 'customer_number'})[['customer_number']]
