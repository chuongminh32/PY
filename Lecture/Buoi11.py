# import numpy as np 
# import matplotlib.pyplot as plt 

# x = np.arange(-4, 3, 0.1)
# y = 3*x**2 + 2*x + 1
# plt.plot(x, y)
# plt.show()

# theta = np.arange(0, 4*np.pi ,0.1)
# r = 0.5*theta
# plt.polar(theta, r)
# plt.show()

# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.axis('equal')
# langs = ['C', 'C++', 'Java', 'Python', 'PHP']
# students = [23,17,35,29,12]
# ax.pie(students, labels = langs,autopct='%1.2f%%')
# plt.show()




# # * Bar chart 
# # Khởi tạo figure và axes
# fig, ax = plt.subplots()

# # Dữ liệu
# langs = ['C', 'C++', 'Java', 'Python', 'PHP']
# students = [23, 17, 35, 29, 48]

# # Vẽ biểu đồ
# ax.bar(langs, students)

# # Hiển thị giá trị từng cột trên đỉnh cột
# for i, value in enumerate(students):
#     ax.text(i, value + 1, str(value), ha='center')  # `value + 1` để hiển thị giá trị phía trên cột

# # Hiển thị biểu đồ
# plt.show()


# # * Bar chart với nhiều nhóm
# # Dữ liệu
# data = [[30, 25, 50, 20],
#         [40, 23, 51, 17],
#         [35, 22, 45, 19]]
# X = np.arange(4)

# # Tạo figure và axes
# fig, ax = plt.subplots()

# # Vẽ các thanh với độ lệch trên trục Ox
# ax.bar(X + 0.00, data[0], color='b', width=0.25, label='Nhóm 1')
# ax.bar(X + 0.25, data[1], color='g', width=0.25, label='Nhóm 2')
# ax.bar(X + 0.50, data[2], color='r', width=0.25, label='Nhóm 3')

# # Thêm nhãn trục Ox và Oy
# ax.set_xlabel("Các danh mục")
# ax.set_ylabel("Giá trị")

# # Hiển thị giá trị trên đỉnh mỗi thanh
# for i in range(len(data)):
#     for j in range(len(data[i])):
#         ax.text(X[j] + i * 0.25, data[i][j] + 1, str(data[i][j]), ha='center')

# # Thêm chú thích (legend)
# ax.legend()

# # Hiển thị biểu đồ
# plt.show()


# xlist = np.linspace(-3.0, 3.0, 100)
# ylist = np.linspace(-3.0, 3.0, 100)
# X, Y = np.meshgrid(xlist, ylist)
# Z = np.sqrt(X**2 + Y**2)
# fig,ax=plt.subplots(1,1)
# cp = ax.contourf(X, Y, Z)
# fig.colorbar(cp) # Add a colorbar to a plot
# ax.set_title('Filled Contours Plot')
# #ax.set_xlabel('x (cm)')
# ax.set_ylabel('y (cm)')
# plt.show()

# from mpl_toolkits import mplot3d
# import numpy as np
# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = plt.axes(projection=
# '3d')
# z = np.linspace(0, 1, 100)
# x = z * np.sin(b20 * z)
# y = z * np.cos(20 * z)
# ax.plot3D(x, y, z, 'gray')
# ax.set_title('3D line plot')
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('company_sales_data.csv')
# profitList = df['total_profit'].tolist()
# monthList = df['month_number'].tolist()
# import pandas as pd
# import matplotlib.pyplot as plt

# # Bước 1: Đọc tập tin
# data = pd.read_csv(r'D:\NamII_HK1\PY\SCHOOL\Code\Lecture\data.csv')

# # Bước 2: Tổng hợp dữ liệu lợi nhuận cho mỗi tháng
# months = data['month_number']
# profit = data['total_profit']

# # Vẽ biểu đồ với các thuộc tính được yêu cầu
# plt.figure(figsize=(10, 6))

# # Biểu đồ đường cho lợi nhuận
# plt.plot(
#     months, profit,
#     linestyle='--',           # Kiểu đường chấm
#     color='r',             # Màu đường kẻ đỏ
#     marker='o',              # Đánh dấu bằng vòng tròn
#     markerfacecolor='b', # Màu đánh dấu vòng tròn
#     linewidth=3              # Chiều rộng đường là 3
# )

# # Thêm chú giải và nhãn
# plt.legend(['Lợi nhuận'], loc='lower right')  # Chú giải ở phía dưới bên phải
# plt.xlabel('Số tháng')                        # Tên nhãn X
# plt.ylabel('Tổng lợi nhuận')                  # Tên nhãn Y
# plt.title('Biểu đồ lợi nhuận theo từng tháng')# Tiêu đề biểu đồ

# # Cài đặt trục X từ 1 đến 12
# plt.xticks(ticks=range(1, 13), labels=range(1, 13))

# # Hiển thị biểu đồ
# plt.show()

# 3/ 
# import pandas as pd
# import matplotlib.pyplot as plt

# # Bước 1: Đọc tập tin CSV
# data = pd.read_csv(r'D:\NamII_HK1\PY\SCHOOL\Code\Lecture\data.csv')

# # Bước 2: Lấy dữ liệu cho các tháng và số lượng bán của từng sản phẩm
# months = data['month_number']
# facecream_sales = data['facecream']
# facewash_sales = data['facewash']
# toothpaste_sales = data['toothpaste']
# bathingsoap_sales = data['bathingsoap']
# shampoo_sales = data['shampoo']
# moisturizer_sales = data['moisturizer']

# # Bước 3: Vẽ biểu đồ
# plt.figure(figsize=(12, 8))

# # Vẽ đường cho mỗi sản phẩm
# plt.plot(months, facecream_sales, linestyle='-', color='blue', marker='o', label='Face Cream Sales Data')
# plt.plot(months, facewash_sales, linestyle='-', color='orange', marker='o', label='Face Wash Sales Data')
# plt.plot(months, toothpaste_sales, linestyle='-', color='green', marker='o', label='Toothpaste Sales Data')
# plt.plot(months, bathingsoap_sales, linestyle='-', color='red', marker='o', label='Bathing Soap')
# plt.plot(months, shampoo_sales, linestyle='-', color='purple', marker='o', label='Shampoo')
# plt.plot(months, moisturizer_sales, linestyle='-', color='brown', marker='o', label='Moisturizer')

# # Bước 4: Thêm chú giải và nhãn
# plt.legend(loc='upper left')  # Chú giải ở góc trên bên trái
# plt.xlabel('Số tháng')        # Tên nhãn X
# plt.ylabel('Số đơn vị bán')   # Tên nhãn Y
# plt.title('Biểu đồ số lượng bán của các sản phẩm theo từng tháng')  # Tiêu đề biểu đồ

# # Bước 5: Cài đặt trục X từ 1 đến 12
# plt.xticks(ticks=range(1, 13), labels=range(1, 13))

# # Bước 6: Hiển thị lưới cho biểu đồ
# plt.grid()

# # Bước 7: Hiển thị biểu đồ
# plt.show()  



# 4/
# # Hiển thị biểu đồ
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# data = pd.read_csv(r'D:\NamII_HK1\PY\SCHOOL\Code\Lecture\data.csv')
# plt.figure(figsize=(10, 6))

# plt.xticks(ticks=range(1, 13), labels=range(1, 13))
# plt.yticks(range(4500, 10001, 500))  


# plt.scatter(data['month_number'], data['toothpaste'], color='blue', label='Tooth paste Sales data', marker='o')
# plt.xlabel('Month Number')                     
# plt.ylabel('Number of utils Sold')  
# plt.title('Tooth paste Sales data') 

# plt.grid(linestyle='--')
# plt.legend()
# plt.show()


# # 5
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Đọc dữ liệu từ file CSV
# data = pd.read_csv(r'D:\NamII_HK1\PY\SCHOOL\Code\Lecture\data.csv')

# # Lấy dữ liệu cho các sản phẩm và số tháng
# months = data['month_number']
# facecream_sales = data['facecream']
# facewash_sales = data['facewash']

# # Thiết lập vị trí cho các thanh (cột) của từng sản phẩm để không bị chồng lên nhau
# bar_width = 0.35  # Độ rộng của từng thanh
# index = np.arange(len(months))  # Vị trí của các thanh

# # Vẽ biểu đồ cột đứng
# plt.figure(figsize=(12, 6))
# plt.bar(index, facecream_sales, width=bar_width, label='Face Cream Sales', color='blue')
# plt.bar(index + bar_width, facewash_sales, width=bar_width, label='Facewash Sales', color='orange')

# # Thêm nhãn và tiêu đề
# plt.xlabel('Month Number')
# plt.ylabel('Number of Units Sold')
# plt.title('Monthly Sales Data for Face Cream and Facewash')

# # Thiết lập giá trị cho trục X và thêm chú giải
# plt.xticks(index + bar_width / 2, months)
# plt.legend()

# # Hiển thị biểu đồ
# plt.show()


# 9/
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
data = pd.read_csv(r'D:\NamII_HK1\PY\SCHOOL\Code\Lecture\data.csv')

# Lấy dữ liệu cho số tháng và các sản phẩm
months = data['month_number']
facewash_sales = data['facewash']
bathingsoap_sales = data['bathingsoap']

# Tạo một figure và hai biểu đồ con
plt.figure(figsize=(12, 8))

# Biểu đồ con cho dữ liệu sữa rửa mặt
plt.subplot(2, 1, 1)  # 2 hàng, 1 cột, biểu đồ con 1
plt.plot(months, facewash_sales, color='blue', marker='o', linestyle='-', linewidth=2)
plt.title('Sales Data for Facewash')
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.grid(True)

# Biểu đồ con cho dữ liệu xà phòng tắm
plt.subplot(2, 1, 2)  # 2 hàng, 1 cột, biểu đồ con 2
plt.plot(months, bathingsoap_sales, color='green', marker='o', linestyle='-', linewidth=2)
plt.title('Sales Data for Bathing Soap')
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.grid(True)

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()
