import pandas as pd
import numpy as np

# a. Tạo ba Series khác nhau có kích thước 100
series1 = pd.Series(np.random.randint(1, 5, size=100))       # Giá trị ngẫu nhiên trong đoạn [1 .. 4]
series2 = pd.Series(np.random.randint(1, 4, size=100))       # Giá trị ngẫu nhiên trong đoạn [1 .. 3]
series3 = pd.Series(np.random.randint(10000, 30001, size=100))  # Giá trị ngẫu nhiên trong đoạn [10000 .. 30000]

# b. Tạo một DataFrame bằng cách nối các Series theo cột
# df = pd.concat([series1, series2, series3], axis=1)

# c. Đổi tên các cột thành bedrs, bathrs, price_sqr_meter
# df.columns = ['bedrs', 'bathrs', 'price_sqr_meter']
#     bedrs  bathrs  price_sqr_meter
# 0       4       1            27799
# 1       1       1            23736
# 2       1       3            29446
# 3       4       1            16715
# 4       4       1            10994
# ..    ...     ...              ...
# 95      2       1            26846
# 96      2       2            24379
# 97      2       1            18405
# 98      3       1            28680
# 99      1       1            24969

# d. Tạo một cột DataFrame với giá trị của các Series, gán tên là ‘bigcolumn’
bigcolumn = pd.concat([series1, series2, series3], axis=0).reset_index(drop=True)
df_big = pd.DataFrame(bigcolumn, columns=['bigcolumn'])
print(df_big)

# # e. Lập chỉ mục lại cho DataFrame ở trên, từ 0 → 299
# df_big.index = range(300)

# print("DataFrame ban đầu:\n", df.head())
# print("\nDataFrame với cột 'bigcolumn' và chỉ mục 0 → 299:\n", df_big.head(10))
