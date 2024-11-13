import pandas as pd
import matplotlib.pyplot as plt

# a. Đọc dữ liệu từ tập tin đã cho, thiết lập header và index
df = pd.read_csv('D:/NamII_HK1/PY/SCHOOL/Code/BaiTap/BaiTapBuoi11(chart)/Churn_Modelling.csv', header=0, index_col='RowNumber')


print("Dữ liệu đã được tải thành công!")

# b. Thống kê mô tả đối với các trường trong bảng dữ liệu này
description = df.describe()
print("Thống kê mô tả các trường số học:\n", description)

# c. Tính trung bình điểm CreditScore theo Geography
credit_score_mean = df.groupby('Geography')['CreditScore'].mean()
print("Trung bình CreditScore theo Geography:\n", credit_score_mean)

# d. Phân đều Age thành 05 nhóm độ tuổi sao cho mỗi nhóm chiếm 20% số quan sát
df['AgeGroup'] = pd.qcut(df['Age'], q=5, labels=['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'])
print("Đã phân nhóm độ tuổi thành công!")

# e. Vẽ biểu đồ barchart thống kê số lượng khách hàng theo nhóm độ tuổi
age_group_counts = df['AgeGroup'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.bar(age_group_counts.index, age_group_counts.values, color='skyblue')
plt.title('Số lượng khách hàng theo nhóm độ tuổi')
plt.xlabel('Nhóm độ tuổi')
plt.ylabel('Số lượng khách hàng')
plt.show()
