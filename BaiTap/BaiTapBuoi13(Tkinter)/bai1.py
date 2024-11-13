import tkinter as tk
from tkinter import messagebox

# Hàm giải phương trình bậc nhất ax + b = 0
def solve_equation():
    try:
        a = float(entry_a.get())  # Lấy giá trị của a
        b = float(entry_b.get())  # Lấy giá trị của b

        if a == 0:
            if b == 0:
                result_entry.delete(0, tk.END)  # Xóa kết quả cũ
                result_entry.insert(0, "Phương trình có vô số nghiệm.")
            else:
                result_entry.delete(0, tk.END)  # Xóa kết quả cũ
                result_entry.insert(0, "Phương trình vô nghiệm.")
        else:
            x = -b / a
            result_entry.delete(0, tk.END)  # Xóa kết quả cũ
            result_entry.insert(0, f"x = {x:.2f}")
    
    except ValueError:
        messagebox.showerror("Lỗi nhập liệu", "Vui lòng nhập đúng giá trị số.")

# Hàm cho nút Tiếp
def clear_fields():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    result_entry.delete(0, tk.END)

# Hàm cho nút Thoát
def exit_program():
    window.quit()

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Giải phương trình bậc nhất")
window.geometry("400x250")

# Dòng 1: Hệ số a và ô nhập liệu
label_a = tk.Label(window, text="Hệ số a:")
label_a.grid(row=0, column=0, padx=10, pady=10, sticky='e')
entry_a = tk.Entry(window)
entry_a.grid(row=0, column=1, padx=10, pady=10)

# Dòng 2: Hệ số b và ô nhập liệu
label_b = tk.Label(window, text="Hệ số b:")
label_b.grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_b = tk.Entry(window)
entry_b.grid(row=1, column=1, padx=10, pady=10)

# Dòng 3: Các nút Giải, Tiếp, Thoát
solve_button = tk.Button(window, text="Giải", command=solve_equation)
solve_button.grid(row=2, column=0, padx=5, pady=10)

continue_button = tk.Button(window, text="Tiếp", command=clear_fields)
continue_button.grid(row=2, column=1, padx=5, pady=10)

exit_button = tk.Button(window, text="Thoát", command=exit_program)
exit_button.grid(row=2, column=2, padx=5, pady=10)

# Dòng 4: Kết quả và ô nhập liệu
label_result = tk.Label(window, text="Kết quả:")
label_result.grid(row=3, column=0, padx=10, pady=10, sticky='e')
result_entry = tk.Entry(window)
result_entry.grid(row=3, column=1, padx=10, pady=10)

# Chạy ứng dụng
window.mainloop()
