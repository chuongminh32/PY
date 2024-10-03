"""* data type : int, float, complex
Số phức (complex) biểu diễn dưới dạng x + yj (trong đó x là phần thực, y là phần ảo và BAT BUOC DE GIA TRI PHAN AO)"""
# Ví dụ: 45j, 3 + 2j, 1 + 3.2e25j, 6 + 1j, 8 – 0j

# z = complex(1,2)
# real => z.real
# image => z.imag

# 1.5e2 (~ 1.5 x 102)

# import sys
# print("Thông tin chi tiết của int:")
# print(sys.int_info)
# print("Thông tin chi tiết của float:")
# print(sys.float_info)

# Trong python, ngoại trừ True,
# False, None viết hoa thì các từ khóa đều là dạng chữ thường. Để xem danh sách từ khóa
# import keyword
# print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

"""• None là một hằng số đặc biệt trong python, đại diện cho biến đó không có giá trị hoặc giá trị Null
and, or, not là các toán tử logic
• as được sử dụng để tạo bí danh khi đang nhập trong một module. import numpy as np
• assert(ném ra lỗi AssertionError) được sử dụng cho mục đích gỡ lỗi
# Ex:
assert condition, "Message"
x = 10
y = 5
assert x > y, "x phải lớn hơn y"
print("Mọi thứ đều ổn!")

Sử dụng 3 cặp nháy đơn ‘‘‘ ’’’, 3 cặp nháy đôi “““ ””” để ghi chú nhiều dòng""
"""

# a 12 (00001100)
# b 15 (00001111)

"""Toán tử Mô tả Ví dụ
& AND (a & b) = 12 (00001100)
| OR (a | b) = 14 (00001111)
^ XOR (2 bit giống nhau trả về 0, 2 bit khác nhau trả về 1) (a ^ b) = 3 (00000011) ( 1 xor 1 = 0, 0 xor 0 = 0, 1 xor 0 = 1)
~ NOT (-a) = -13 (00001101) (bit 0 dao ve 1, 1 dao ve 0)
<< Phép toán dịch bit trái a << 2 = 48 (00110000)
>> Phép toán dịch bit phải a >> 2 = 3 (00000011)
in Nếu 1 đối số thuộc một tập đối số ➔ True và ngược lại a in b // False
not in Nếu 1 đối số không thuộc một tập đối số ➔ True và ngược lại a not in b // True
is Toán tử này sẽ trả về True nếu a == b và ngược lại a is b //False
not is Toán tử này sẽ trả về True nếu a != b và ngược lại a is not b //True"""

# def double(num):
#     """Function to double the value"""
#     return 2 * num

# bin -> dec
# binary_string = '101'
# print(int(binary_string, 2))  # Kết quả: 5

# dec -> bin
# y = -3
# print(bin(y))  # Kết quả: '-0b11'

"""
Thứ tự ưu tiên Toán tử Miêu tả
1 ** Toán tử mũ
2 * / % // Phép nhân, chia, lấy phần dư và lấy phần nguyên
3 + – Toán tử cộng, trừ
4 <= < > >= Các toán tử so sánh
5 <> == != Các toán tử so sánh
6 = %= /= //= -= += *= **= Các toán tử gán
7 is, is not Các toán tử so sánh
8 not, or, and Các toán tử logic"""

"""Các giá trị mặc định trả về False:
None: Giá trị rỗng, không có gì.
False: Giá trị Boolean False.
Số không dưới các dạng:
0: Số nguyên không.
0.0: Số thực không.
0j: Số phức với phần thực và phần ảo đều bằng 0.
Chuỗi rỗng: "" hoặc ''.
Danh sách rỗng: [].
Tuple rỗng: ().
Set rỗng: set().
Từ điển rỗng: {}.
Các đối tượng có phương thức __bool__() hoặc __len__() trả về False hoặc 0.
"""
# # Ex:
# class MyClass:
#     def __bool__(self):
#         return False

# obj = MyClass()
# if obj:
#     print("True")
# else:
#     print("False")  # Kết quả: False


"""Các giá trị mặc định trả về True:
Bất kỳ giá trị nào không thuộc danh sách "False".
True: Giá trị Boolean True.
Bất kỳ số nào khác 0: Ví dụ 1, -1, 0.5, 3j.
Chuỗi không rỗng: Ví dụ "hello", " " (chuỗi chứa khoảng trắng).
Danh sách không rỗng: Ví dụ [1, 2].
Tuple không rỗng: Ví dụ (1, 2).
Set không rỗng: Ví dụ {1, 2}.
Từ điển không rỗng: Ví dụ {'a': 1}"""

# print(double.__doc__)
# docstring (documentation string): explain function

# name = "Alice"
# age = 30
# formatted_string = "Tên tôi là {1} và tôi {0} tuổi.".format(name, age)
# print(formatted_string)  # Kết quả: Tên tôi là 30 và tôi Alice tuổi.

# Ex2 :Định dạng số
# pi = 3.14159265
# formatted_string = "Giá trị của pi là {:.2f}".format(pi)
# print(formatted_string)  # Kết quả: Giá trị của pi là 3.14

# formatted_string = "{:<2} {:^4} {:>4} {:<4}".format(
#     'trái', 'giữa', 'phải', 'tren')
# print(formatted_string)
# # trái giữa phải tren

# formatted_string = "{:<4} {:^5} {:>4} {:<4}".format(
#     'trái', 'giữa', 'phải', 'tren')
# print(formatted_string)
# # trái giữa  phải tren

# formatted_string = "{:<5} {:^4} {:>4} {:<4}".format(
#     'trái', 'giữa', 'phải', 'tren')
# print(formatted_string)
# # trái  giữa phải tren


"""* "{0:.<4} {1:.>5}".format("val1", "val2") 
=> can le ben trai 4(val1 se luon day sat le ben trai) ki tu cho val1 (idx = 0) 
=> can le ben phai 5(val2 se luon day sat le ben phai) ki tu cho val2 (idx = 1) """

# print('-'*15)
# print('{0:>2} {1:>11}'.format('STT', 'Giá trị'))
# print('-'*15)
# print('{0:>2} {1:>11}'.format(1, 10**10))
# print('{0:>2} {1:>11}'.format(2, 10**9))
# print('{0:>2} {1:>11}'.format(3, 10**8))
# print('{0:>2} {1:>11}'.format(4, 10**7))
# print('{0:>2} {1:>11}'.format(5, 10**6))
# print('{0:>2} {1:>11}'.format(6, 10**5))
# print('{0:>2} {1:>11}'.format(7, 10**4))
# print('{0:>2} {1:>11}'.format(8, 10**3))
# print('{0:>2} {1:>11}'.format(9, 10**2))
# print('{0:>2} {1:>11}'.format(10, 10**1))
# print('-'*15)

# Ex:
# price = int(input("Nhập đơn giá: "))
# count = int(input("Nhập số lượng: "))

# # Tính tổng tiền trước thuế
# totalCostBeforeTax = "{0:>30} {1:>15}".format(
#     "Tổng tiền trước thuế:", "{} * {} = {}".format(price, count, price * count))

# # Tính tiền thuế
# tax_value = 0.1 * price * count
# Tax = "{0:>30} {1:>15.2f}".format("Tiền thuế:", tax_value)

# # Tính tổng tiền sau thuế
# totalCostAfterTax = "{0:>30} {1:>15.2f}".format(
#     "Tổng tiền sau thuế:", price * count + tax_value)

# # In kết quả
# print(totalCostBeforeTax)
# print(Tax)
# print(totalCostAfterTax)


"""
Lỗi cú pháp (Syntax Errors)
• Lỗi thực thi (Run-time Exceptions)
• Lỗi nghiệp vụ (Logic Errors)
• Python cho phép bắt lỗi bằng khối lệnh try … catch …"""


"""- Sử dụng module decimal được cài đặt sẵn trong python để xác định độ chính xác là bao nhiêu số thập phân
Ex:
import decimal
print(decimal.Decimal(0.05)) # 0.05000000000000000277555756156289135105907917022705078125
print(decimal.Decimal('0.05')) # 0.05

a = f"{3/10:.1f}"
b = f"{2/10:.1f}"
c = f"{5/10:.10f}"
print(c == a + b)  # False

A = decimal.Decimal('0.2')
B = decimal.Decimal('0.3')
C = decimal.Decimal('0.5')
print(C = A + B) # True

d = f'{1/13:.10f}'
D = decimal.Decimal(f'{d}')
print(D)
# 0.0769230769"""

# - lay 10 chu so thap phan
# print(f"{1/13:.10f}")


# import decimal
# print(decimal.Decimal(1) / decimal.Decimal(13)) # 0.07692307692307692307692307692
# decimal.getcontext().prec = 10
# print(decimal.Decimal(1) / decimal.Decimal(13))


"""* try-except được sử dụng để xử lý ngoại lệ (lỗi) trong quá trình thực thi chương trình mà không làm chương trình bị gián đoạn , finally luôn được thực thi
try:
    # Khối lệnh có thể gây ra lỗi
except ExceptionType:
    # Khối lệnh xử lý khi có lỗi

Ex:
try:
    # Cố gắng chia một số cho 0
    result = 10 / 0
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")

Ex: finally
try:
file = open("laptrinhPython.txt")
try:
file.write("Welcome to laptrinhPython.com!")
except:
print("Something went wrong when writing!")
finally: # always close file
file.close()
except:
print("Something went wrong when opening!")

* tu khóa raise trong python cho phép “ném” ra một exception nếu thỏa một điều kiện nào đó.
a = 1
b = 0
if b == 0:
raise Exception("Sorry, cannot divide by 0!")
else:
print("x = ", a/b)


- py hỗ trợ khối else trong trường hợp while kết thúc một các bình thường (tức không dùng break để kết thúc) 
* else cũng không được thực thi neu trong while kết thúc bằng lệnh break
while expression:
# while-block
else:
# else-block
-py hỗ trợ else block trong trường hợp for kết thúc một cách bình thường (tức là không phải dùng break để kết thúc)
for expression:
# for-block
else:
# else-block
"""

# Exercise
# a, b = 12, 5
# print('True') if b // a else  print('False')

# print('False') if -3 else print('True')

# print('False') if None else print('True')

# try:
#     print("throw")
# except:
#     print("except")
# finally:
#     print("finally")

# number = 5.0
# try:
#     r = 10/number
#     print(r)
# except:
#     print("Oops! Error occurred.")

# Để hiển thị lỗi mà không dùng try/catch ta sử dụng từ khóa nào kết với cấu trúc kiểm tra điều kiện?

# try:
#     print("throw")
# except:
#     print("except")
# finally:
#     print("finally")

# number = 5.0
# try:
#     r = 10/number
#     print(r)
# except:
#     print("Oops! Error occurred.")

#     try:
# # đoạn code có thể gây ra lỗi
#     pass
# except (TypeError, ZeroDivisionError):
#     print("Python Quiz")

# import math

# def giai_phuong_trinh_bac_hai(a, b, c):
#     if a == 0:
#         if b == 0:
#             if c == 0:
#                 return "Phương trình vô số nghiệm."
#             else:
#                 return "Phương trình vô nghiệm."
#         else:
#             return f"Phương trình có nghiệm: x = {-c / b:.2f}"

#     delta = b**2 - 4*a*c

#     if delta > 0:
#         x1 = (-b + math.sqrt(delta)) / (2*a)
#         x2 = (-b - math.sqrt(delta)) / (2*a)
#         return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1:.2f}, x2 = {x2:.2f}"
#     elif delta == 0:
#         x = -b / (2*a)
#         return f"Phương trình có nghiệm kép: x = {x:.2f}"
#     else:
#         return "Phương trình vô nghiệm."

# # Test hàm
# a = float(input("Nhập hệ số a: "))
# b = float(input("Nhập hệ số b: "))
# c = float(input("Nhập hệ số c: "))

# ket_qua = giai_phuong_trinh_bac_hai(a, b, c)
# print(ket_qua)

# if 'toan' in {'cntt': 1, 'toan': 2, 'sinh': 3}:

#     print(1)

# if 'a' in 'cntt':

#     print(2)

# print(3)
# i = 0; x = 0

# while i < 10:

#     if i % 2 == 0:

#         x += 1

#     i += 1
# print(x)
