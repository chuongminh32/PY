import tkinter as tk
from tkinter import messagebox

# Hàm đánh giá biểu thức khi nhấn nút "=" hoặc phím Enter
def evaluate(event=None):
    try:
        result = eval(entry.get())  # Đánh giá biểu thức
        entry.delete(0, tk.END)  # Xóa màn hình
        entry.insert(tk.END, str(result))  # Hiển thị kết quả
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")  # Thông báo lỗi nếu có

# Hàm để xóa màn hình
def clear():
    entry.delete(0, tk.END)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Simple Calculator")

# Tạo ô nhập liệu
entry = tk.Entry(root, width=40, borderwidth=5, font=('Arial', 18), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Danh sách các nút của máy tính
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Vị trí ban đầu của các nút
row_val = 1
col_val = 0

# Tạo các nút máy tính và thêm vào giao diện
for button in buttons:
    action = lambda x=button: entry.insert(tk.END, x)  # Hàm thêm giá trị vào ô nhập liệu
    if button == "=":  # Nút "=" thực hiện phép tính
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda: evaluate(None))
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=action)
    
    btn.grid(row=row_val, column=col_val, sticky='nsew', padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Nút "Clear"
clear_button = tk.Button(root, text="Clear", padx=20, pady=20, font=('Arial', 18), command=clear)
clear_button.grid(row=row_val, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)

# Cập nhật kích thước của các cột và hàng để các nút có kích thước đồng đều
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(row_val + 1):
    root.grid_rowconfigure(i, weight=1)

# Liên kết phím Enter với hàm tính toán
root.bind('<Return>', evaluate)

# Chạy ứng dụng
root.mainloop()
