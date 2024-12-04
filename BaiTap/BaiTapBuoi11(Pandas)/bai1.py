import pandas as pd
import matplotlib.pyplot as plt

# a. Đọc dữ liệu
df = pd.read_csv("D:/NamII_HK1/PY/SCHOOL/Code/BaiTap/BaiTapBuoi11(Pandas)/Churn_Modelling.csv", header=0, index_col="RowNumber")

# b. Thống kê mô tả
print(df.describe())

# c. Tính trung bình điểm CreditScore theo Geography
avg_credit_score = df.groupby('Geography')['CreditScore'].mean()
print(avg_credit_score)

# d. Phân đều Age thành 5 nhóm độ tuổi
df['AgeGroup'] = pd.qcut(df['Age'], q=5, labels=["Group1", "Group2", "Group3", "Group4", "Group5"])

# e. Vẽ biểu đồ bar chart thống kê số lượng khách hàng theo nhóm độ tuổi
age_group_counts = df['AgeGroup'].value_counts()
age_group_counts.plot(kind='bar', color='skyblue', title='Customer Count by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Customer Count')
plt.show()
