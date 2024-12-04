
import pandas as pd
import numpy as np

# index series no cung la index cua dataframe 

# Tao df tu dict
# s = {'một': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),
# 'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(s)
# # df = pd.DataFrame(s, index=['a','c','d'])
# print(df)

#    một  hai
# a  1.0  1.0
# b  2.0  2.0
# c  3.0  3.0
# d  NaN  4.0
# e  5.0  NaN

# Tao df tu list
# lst = ['Hello','Flinters','How','Are','You']
# df = pd.DataFrame(lst)
# print(df)

#           0
# 0     Hello
# 1  Flinters
# 2       How
# 3       Are
# 4       You

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
df = pd.DataFrame(arr, columns = ['a','b','c'])
# print(df.iloc[:2, :2])

print(df[['a'
, 'b'
]].head()) 
#    a  b
# 0  1  2
# 1  4  5
# 2  7  8
#    a  b  c
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9

# Truy cập theo slice index: truyền vào index của dòng và cột, sử dụng hàm:
# df.iloc[rows_slice, columns_slice] / df.loc[]
# df.iloc[:5, :5]


# ✓Lọc ra các thị trấn mà có số phòng ở trung bình trên căn hộ là trên 4 và thuế suất trên 250
df[(df['rm']>4) & (df['tax']>250)].head()

# ✓Lọc ra các trường có kiểu dữ liệu float: df.select_dtypes('float').head()


# ✓Sắp xếp dữ liệu giá trị của căn nhà theo chiều giảm dần:
df.sort_values('medv', ascending = False).head()

#✓Sắp xếp đồng thời giá trị của căn nhà và giá trị thuế suất :
df.sort_values(['medv', 'tax'], ascending = False).head()
