import tkinter as tk
from tkinter import messagebox
import math

# Hàm giải phương trình bậc 2 ax^2 + bx + c = 0


def solve_quadratic():
    try:
        # Lấy giá trị của a, b, c
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Tính delta (discriminant)
        delta = b**2 - 4*a*c

        if a == 0:
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Không phải phương trình bậc 2.")
        elif delta > 0:
            # Hai nghiệm phân biệt
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            result_entry.delete(0, tk.END)
            result_entry.insert(0, f"x1 = {x1:.2f}, x2 = {x2:.2f}")
        elif delta == 0:
            # Nghiệm kép
            x = -b / (2*a)
            result_entry.delete(0, tk.END)
            result_entry.insert(0, f"x = {x:.2f}")
        else:
            # Phương trình vô nghiệm
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Phương trình vô nghiệm.")

    except ValueError:
        messagebox.showerror("Lỗi nhập liệu", "Vui lòng nhập đúng giá trị số.")

# Hàm cho nút Tiếp


def clear_fields(): 
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    result_entry.delete(0, tk.END)

# Hàm cho nút Thoát


def exit_program():
    window.quit()


# Tạo cửa sổ chính
window = tk.Tk()
window.title("Giải phương trình bậc 2")
window.geometry("400x300")

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

# Dòng 3: Hệ số c và ô nhập liệu
label_c = tk.Label(window, text="Hệ số c:")
label_c.grid(row=2, column=0, padx=10, pady=10, sticky='e')
entry_c = tk.Entry(window)
entry_c.grid(row=2, column=1, padx=10, pady=10)

# Dòng 4: Các nút Giải, Tiếp, Thoát
solve_button = tk.Button(window, text="Giải", command=solve_quadratic)
solve_button.grid(row=3, column=0, padx=10, pady=10)

continue_button = tk.Button(window, text="Tiếp", command=clear_fields)
continue_button.grid(row=3, column=1, padx=10, pady=10)

exit_button = tk.Button(window, text="Thoát", command=exit_program)
exit_button.grid(row=3, column=2, padx=10, pady=10)

# Dòng 5: Kết quả và ô nhập liệu
label_result = tk.Label(window, text="Kết quả:")
label_result.grid(row=4, column=0, padx=10, pady=10, sticky='e')
result_entry = tk.Entry(window)
result_entry.grid(row=4, column=1, padx=10, pady=10)

# Chạy ứng dụng
window.mainloop()
