import tkinter as tk
from tkinter import messagebox

# Hàm đánh giá biểu thức khi nhấn nút "=" hoặc phím Enter
def evaluate(operation):
    try:
        a = float(entry_a.get())  # Lấy số a từ entry_a
        b = float(entry_b.get())  # Lấy số b từ entry_b
        result = None

        if operation == "add":  # Cộng
            result = a + b
        elif operation == "subtract":  # Trừ
            result = a - b
        elif operation == "multiply":  # Nhân
            result = a * b
        elif operation == "divide":  # Chia
            if b == 0:
                raise ValueError("Cannot divide by zero.")
            result = a / b

        entry_c.delete(0, tk.END)  # Xóa màn hình kết quả
        entry_c.insert(tk.END, str(result))  # Hiển thị kết quả
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input: " + str(e))  # Thông báo lỗi nếu có

# Hàm để xóa màn hình
def clear():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("23110187")  # Tiêu đề cửa sổ chính

# Tiêu đề cho phần tính toán
header_label = tk.Label(root, text="Cộng trừ nhân chia", font=('Arial', 14, "bold"))
header_label.grid(row=0, column=0, columnspan=3, pady=10)  # Căn giữa tiêu đề, thêm khoảng cách

# Các widget cho cộng, trừ, nhân, chia
label_a = tk.Label(root, text="Số a:")
label_a.grid(row=1, column=1)
entry_a = tk.Entry(root, width=20)  # Thiết lập width cho Entry a
entry_a.grid(row=1, column=2)

label_b = tk.Label(root, text="Số b:")
label_b.grid(row=2, column=1)
entry_b = tk.Entry(root, width=20)  # Thiết lập width cho Entry b
entry_b.grid(row=2, column=2)

label_c = tk.Label(root, text="Kết quả:")
label_c.grid(row=3, column=1)
entry_c = tk.Entry(root, width=20)  # Thiết lập width cho Entry c
entry_c.grid(row=3, column=2)

# Nút cộng, trừ, nhân, chia với width bằng nhau
button_a = tk.Button(root, text="Cộng", command=lambda: evaluate("add"), width=10)
button_a.grid(row=1, column=0)

button_b = tk.Button(root, text="Trừ", command=lambda: evaluate("subtract"), width=10)
button_b.grid(row=2, column=0)

button_c = tk.Button(root, text="Nhân", command=lambda: evaluate("multiply"), width=10)
button_c.grid(row=3, column=0)

button_d = tk.Button(root, text="Chia", command=lambda: evaluate("divide"), width=10)
button_d.grid(row=4, column=0)

# Nút xóa và thoát
clear_button = tk.Button(root, text="Xóa", command=clear, width=10)
clear_button.grid(row=5, column=0)

exit_button = tk.Button(root, text="Thoát", command=root.quit, width=10)
exit_button.grid(row=5, column=1)

# Chạy ứng dụng
root.mainloop()
