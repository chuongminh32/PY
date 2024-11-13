import pandas as pd

# a. Đọc dữ liệu từ tập tin đã cho, sử dụng ký tự phân tách là dấu '|' 
df = pd.read_csv('D:/NamII_HK1/PY/SCHOOL/Code/BaiTap/BaiTapBuoi11(chart)/u.user', sep='|')

# b. Độ tuổi trung bình của mỗi nghề nghiệp
avg_age_by_occupation = df.groupby('occupation')['age'].mean()
print("Độ tuổi trung bình của mỗi nghề nghiệp:\n", avg_age_by_occupation)

# c. Tỷ lệ số lượng người trên mỗi nghề và sắp xếp từ cao đến thấp
occupation_counts = df['occupation'].value_counts(normalize=True) * 100
sorted_occupation_counts = occupation_counts.sort_values(ascending=False)
print("\nTỷ lệ phần trăm trên mỗi nghề nghiệp (sắp xếp từ cao đến thấp):\n", sorted_occupation_counts)

# d. Độ tuổi nhỏ nhất và lớn nhất cho mỗi nghề nghiệp
age_min_max_by_occupation = df.groupby('occupation')['age'].agg(['min', 'max'])
print("\nĐộ tuổi nhỏ nhất và lớn nhất cho mỗi nghề nghiệp:\n", age_min_max_by_occupation)

# e. Tuổi trung bình cho mỗi tổ hợp của nghề nghiệp và giới tính
avg_age_by_occupation_gender = df.groupby(['occupation', 'gender'])['age'].mean()
print("\nTuổi trung bình cho mỗi tổ hợp của nghề nghiệp và giới tính:\n", avg_age_by_occupation_gender)

# f. Tỷ lệ phần trăm nam và nữ trên mỗi nghề nghiệp
gender_counts_by_occupation = df.groupby(['occupation', 'gender']).size().unstack(fill_value=0)
gender_percentage_by_occupation = gender_counts_by_occupation.div(gender_counts_by_occupation.sum(axis=1), axis=0) * 100
print("\nTỷ lệ phần trăm nam và nữ trên mỗi nghề nghiệp:\n", gender_percentage_by_occupation)
