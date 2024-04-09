# 表: Person

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | email       | varchar |
# +-------------+---------+
# id 是该表的主键（具有唯一值的列）。
# 此表的每一行都包含一封电子邮件。电子邮件不包含大写字母。
 

# 编写解决方案来报告所有重复的电子邮件。 请注意，可以保证电子邮件字段不为 NULL。

# 以 任意顺序 返回结果表。

# 结果格式如下例。

 

# 示例 1:

# 输入: 
# Person 表:
# +----+---------+
# | id | email   |
# +----+---------+
# | 1  | a@b.com |
# | 2  | c@d.com |
# | 3  | a@b.com |
# +----+---------+
# 输出: 
# +---------+
# | Email   |
# +---------+
# | a@b.com |
# +---------+
# 解释: a@b.com 出现了两次。


# Pandas 代码:

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # duplicates 方法返回重复的行，subset=['email'] 表示只考虑 email 列，keep=False 表示保留所有重复的行
    # person[] 将 duplicates 的结果转换为 DataFrame, 即满足条件的行
    duplicates = person[person.duplicated(subset=['email'], keep=False)]
    # 保留 email 列，并去重
    return duplicates[['email']].drop_duplicates()