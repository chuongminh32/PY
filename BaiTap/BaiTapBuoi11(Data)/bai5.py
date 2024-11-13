import pandas as pd

# a. Đọc dữ liệu từ tập tin đã cho
df = pd.read_csv('D:/NamII_HK1/PY/SCHOOL/Code/BaiTap/BaiTapBuoi11(chart)/wind.data', delim_whitespace=True)

# b. Hợp nhất ba cột đầu tiên (Yr, Mo, Dy) thành "Yr_Mo_Dy" với định dạng “yyyy-MM-dd”
df['Yr_Mo_Dy'] = pd.to_datetime(df[['Yr', 'Mo', 'Dy']].astype(str).agg('-'.join, axis=1), format='%y-%m-%d')

# c. Đặt cột mới “Yr_Mo_Dy” làm chỉ mục và bỏ các cột cũ
df.set_index('Yr_Mo_Dy', inplace=True)
df.drop(['Yr', 'Mo', 'Dy'], axis=1, inplace=True)

# d. Đếm số lượng giá trị hiện có và còn thiếu từ các cột RPT → MAL
missing_values = df.isnull().sum()
existing_values = df.notnull().sum()

# e. Tính tốc độ gió trung bình của toàn bộ dữ liệu
overall_mean_speed = df.mean().mean()

# f. Tạo DataFrame loc_stats để tính các thống kê cho từng cột từ RPT đến MAL
loc_stats = pd.DataFrame({
    'Min': df.min(),
    'Max': df.max(),
    'Mean': df.mean(),
    'StdDev': df.std()
})

# g. Tính tốc độ gió trung bình trong tháng 1 ở mỗi nơi
january_mean = df[df.index.month == 1].mean()

# h. Giảm dữ liệu, thống kê theo từng năm, theo tháng-năm, và theo tuần-tháng-năm
yearly_stats = df.resample('Y').mean()
monthly_stats = df.resample('M').mean()
weekly_stats = df.resample('W').mean()

# Hiển thị kết quả
print("Số lượng giá trị hiện có và còn thiếu ở các cột từ RPT đến MAL:\n", pd.DataFrame({'Existing': existing_values, 'Missing': missing_values}))
print("\nTốc độ gió trung bình của toàn bộ dữ liệu:", overall_mean_speed)
print("\nThống kê tốc độ gió tại mỗi vị trí:\n", loc_stats)
print("\nTốc độ gió trung bình trong tháng 1 ở mỗi nơi:\n", january_mean)
print("\nThống kê tốc độ gió theo năm:\n", yearly_stats)
print("\nThống kê tốc độ gió theo tháng - năm:\n", monthly_stats)
print("\nThống kê tốc độ gió theo tuần - tháng - năm:\n", weekly_stats)
