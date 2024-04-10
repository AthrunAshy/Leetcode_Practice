# 表： Weather

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | recordDate    | date    |
# | temperature   | int     |
# +---------------+---------+
# id 是该表具有唯一值的列。
# 没有具有相同 recordDate 的不同行。
# 该表包含特定日期的温度信息
 

# 编写解决方案，找出与之前（昨天的）日期相比温度更高的所有日期的 id 。

# 返回结果 无顺序要求 。

# 结果格式如下例子所示。

 

# 示例 1：

# 输入：
# Weather 表：
# +----+------------+-------------+
# | id | recordDate | Temperature |
# +----+------------+-------------+
# | 1  | 2015-01-01 | 10          |
# | 2  | 2015-01-02 | 25          |
# | 3  | 2015-01-03 | 20          |
# | 4  | 2015-01-04 | 30          |
# +----+------------+-------------+
# 输出：
# +----+
# | id |
# +----+
# | 2  |
# | 4  |
# +----+
# 解释：
# 2015-01-02 的温度比前一天高（10 -> 25）
# 2015-01-04 的温度比前一天高（20 -> 30）


# Pandas 代码：

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # to_datetime() 函数将 recordDate 列转换为日期时间类型，方便后续计算
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    # 对 DataFrame 按照 recordDate 进行排序
    weather = weather.sort_values(by='recordDate')

    # 将日期向下移动一行，以便与前一天进行比较
    weather['previousTemperature'] = weather['temperature'].shift(1)
    weather['previousDate'] = weather['recordDate'].shift(1)

    # 找出温度比前一天更高的日期的 id
    result = weather[(weather['temperature'] > weather['previousTemperature']) & 
                     (weather['recordDate'] - weather['previousDate'] == pd.Timedelta(days=1))]['id']

    # 输出构造的 DataFrame
    return pd.DataFrame(result)