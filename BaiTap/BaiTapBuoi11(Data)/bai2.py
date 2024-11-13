import pandas as pd
import matplotlib.pyplot as plt

# a. Đọc dữ liệu từ tập tin đã cho
df = pd.read_csv('D:/NamII_HK1/PY/SCHOOL/Code/BaiTap/BaiTapBuoi11(chart)/chipotle.tsv', sep='\t')

df['item_price'] = df['item_price'].replace('[\$,]', '', regex=True).astype(float)  # Chuyển item_price thành dạng float
print("Dữ liệu đã được tải thành công!")

# b. Liệt kê những sản phẩm có giá hơn 10$ (lược bỏ những dòng trùng tên sản phẩm)
products_above_10 = df[df['item_price'] > 10]['item_name'].drop_duplicates()
print("Các sản phẩm có giá trên 10$:\n", products_above_10)

# c. Sắp xếp các sản phẩm theo tên
sorted_products = df['item_name'].drop_duplicates().sort_values()
print("Danh sách các sản phẩm đã được sắp xếp theo tên:\n", sorted_products)

# d. Tìm sản phẩm có giá cao nhất trong danh sách
most_expensive_item = df.loc[df['item_price'].idxmax()]
print("Sản phẩm có giá cao nhất là:\n", most_expensive_item)

# e. Cho biết sản phẩm “Veggie Salad Bowl” xuất hiện trong bao nhiêu đơn hàng với tổng số lượng được đặt
veggie_salad_orders = df[df['item_name'] == 'Veggie Salad Bowl']
veggie_salad_count = veggie_salad_orders['order_id'].nunique()
veggie_salad_quantity = veggie_salad_orders['quantity'].sum()
print(f"Sản phẩm 'Veggie Salad Bowl' xuất hiện trong {veggie_salad_count} đơn hàng với tổng số lượng được đặt là {veggie_salad_quantity}")

# f. Vẽ biểu đồ histogram cho 5 sản phẩm được mua nhiều nhất với tần suất mua
top_5_items = df.groupby('item_name')['quantity'].sum().nlargest(5)
plt.figure(figsize=(10, 6))
top_5_items.plot(kind='bar', color='skyblue')
plt.title('Top 5 sản phẩm được mua nhiều nhất')
plt.xlabel('Tên sản phẩm')
plt.ylabel('Tần suất mua')
plt.show()

# g. Vẽ biểu đồ scatter với số lượng mặt hàng được đặt hàng trên mỗi đơn hàng
order_items = df.groupby('order_id')['quantity'].sum()
plt.figure(figsize=(10, 6))
plt.scatter(order_items.index, order_items.values, color='blue', alpha=0.5)
plt.title('Số lượng mặt hàng được đặt trên mỗi đơn hàng')
plt.xlabel('Order ID')
plt.ylabel('Số lượng mặt hàng')
plt.show()
