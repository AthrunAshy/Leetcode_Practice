# ActorDirector 表：

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | actor_id    | int     |
# | director_id | int     |
# | timestamp   | int     |
# +-------------+---------+
# timestamp 是这张表的主键(具有唯一值的列).
 

# 编写解决方案找出合作过至少三次的演员和导演的 id 对 (actor_id, director_id)

 

# 示例 1：

# 输入：
# ActorDirector 表：
# +-------------+-------------+-------------+
# | actor_id    | director_id | timestamp   |
# +-------------+-------------+-------------+
# | 1           | 1           | 0           |
# | 1           | 1           | 1           |
# | 1           | 1           | 2           |
# | 1           | 2           | 3           |
# | 1           | 2           | 4           |
# | 2           | 1           | 5           |
# | 2           | 1           | 6           |
# +-------------+-------------+-------------+
# 输出：
# +-------------+-------------+
# | actor_id    | director_id |
# +-------------+-------------+
# | 1           | 1           |
# +-------------+-------------+
# 解释：
# 唯一的 id 对是 (1, 1)，他们恰好合作了 3 次。


# Pandas 代码：

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:

    # 找出演员和导演合作次数大于等于 3 的 id 对
    df = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    df = df[df['count'] >= 3]

    # 返回结果
    return df[['actor_id', 'director_id']]


# 关于 Pandas 的 groupby() 函数：
# |  actor_id  |  director_id  |  timestamp  |
# |------------|---------------|-------------|
# |     1      |       1       |      0      |
# |     1      |       1       |      1      |
# |     1      |       2       |      2      |
# |     2      |       1       |      3      |
# |     2      |       2       |      4      |

# groupby(['actor_id', 'director_id']) 按照演员 id 和导演 id 分组
# size() 计算每组的大小
# 输出的结果如下：最后是 size 列，表示每组的大小
# actor_id  director_id
# 1         1              2
#           2              1
# 2         1              1
#           2              1
# dtype: int64

