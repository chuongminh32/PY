
# Menu:
# * Import theory :
# 0.
if  __name__ == "__main__":

# Câu lệnh if __name__ == "__main__": trong Python là một cách thông dụng để 
# xác định xem một tệp Python có đang được chạy như một chương trình chính 
# hay không. Nếu tệp đó đang được chạy trực tiếp (không phải là một module 
# được import), thì khối lệnh bên trong if __name__ == "__main__": sẽ được 
# thực thi.

# Mục đích của if __name__ == "__main__":
# Chạy code khi file được thực thi trực tiếp: Khi bạn muốn chạy một số đoạn
#  mã (ví dụ, một chương trình chính) khi tệp được thực thi trực tiếp.
# Tránh chạy code khi file được import: Khi bạn không muốn đoạn mã đó chạy 
# nếu tệp được import vào một tệp khác như một module.

# * Summary:
- trong file main: 
+ Neu khong inport file khac vao -> lenh trong
 if  __name__ == "__main__":(cua file main) se duoc 
+ Neu import file khac vao -> if  __name__ == "__main__": <=> if  __name__ == "filekhac":
code trong phan else cua file khac se chay:
Ex:
* trong file main:
import filekhac
def main() :
    filekhac.mes("Chuong")
# khi file main co import filekhac vao -> uu tien chay code trong phan else cua file khac 
# sau do chay code trong block code main cua file main 
# => block code main se luon chay khi thuc thi mot file 
if __name__ == "__main__":
    main()

# output: 
# __name__ == filekhac 
# file khac da duoc import ! 
# Hello Chuong 


* trong filekhac
def mes(name):
    print(f"Hello {name}")

if __name__ == "__main__":
    print("file khac chua duoc import")
else :
    # file khac duoc file main import 
    # -> code trong phan else cua file khac (vi __name__ == filekhac) se duoc chay khi chay code trong file main
    # -> Neu trong filekhac khong co code trong phan else ma filekhac da duoc file main
    # import -> auto toan bo code khong duoc ham lop nao bao boc trong file khac se duoc chay khi chay code trong file main
    print(f"__name__ == {__name__}") # filekhac
    print("file khac da duoc import !")  


# * Neu file main import file khac va file khac import file khac 2 
# => file main cung import file khac 2( toan bo code trong phan else file khac 2 se duoc thuc thi neu file main duoc chay )
# code trong phan else duoc chay: vi bien __name__ trong file duoc import khong con ten la __main__ ma la module cua chinh no (tenfile)

# Ex2: bai10, bai11 loop 

# Khi __name__ là "__main__": Tệp đang được chạy trực tiếp, và 
# khối lệnh trong if __name__ == "__main__": sẽ chạy.
# Khi __name__ là tên module: Tệp được import vào một tệp khác,
# và khối lệnh trong if __name__ == "__main__": sẽ không chạy.

  
# 1. Basic Import:
# Suppose you have module.py with a function like this:
# def greet():
#     print("Hello from module!")

# In another file:
# import module

# Now you can use the functions or classes from module.py
# module.greet()  # This will print: Hello from module!

# 2. Import Specific Functions or Classes:
# In another file:
# from module import greet

# Now you can use greet() directly(truc tiep) without the module prefix(tien to)
# greet()  # This will print: Hello from module!

# 3. Import with Alias:
# Importing the whole module with an alias
# import module as mod

# mod.greet()  # This will print: Hello from module!

# Importing a specific function with an alias
# from module import greet as say_hello

# say_hello()  # This will print: Hello from module!

# 4. Import All:
# This imports everything from module.py
# from module import *

# greet()  # This will print: Hello from module!

# 5. Relative Imports:
# project/
# │
# ├── package/
# │   ├── __init__.py
# │   ├── module1.py
# │   └── module2.py
# │
# └── main.py

# If module2.py wants to import something from module1.py, you can use:
# from .module1 import greet

# If main.py wants to import something from module1.py:
# from package.module1 import greet





#  PART I: DATA TYPES, LOOPS, OPERATOR FUNCTIONS

#  PART I: DATA TYPES, LOOPS, OPERATOR FUNCTIONS
# =======================VARIABLE DECLARATION SYNTAX ===================================
# Note: auto define data type (string,num,complex,..)

# # Khai báo biến số nguyên
# x = 10
# print("Giá trị của x:", x)

# # Khai báo biến số thực
# y = 3.14
# print("Giá trị của y:", y)

# # Khai báo biến chuỗi
# name = "Alice"
# print("Tên:", name)

# # Khai báo biến boolean
# is_student = True
# print("Có phải là học sinh:", is_student)

# # khai bao nhieu bien tren mot dong 
# a, b, c = 1, 2, 3
# print("Giá trị của a, b, c:", a, b, c)

# # khai bao bien voi gia tri mac dinh 
# d = 0
# print("Giá trị của d:", d)

# # Khai báo một danh sách
# my_list = [1, 2, 3, 4, 5]
# print("Danh sách:", my_list)

# # Khai bao bien mang (array)
# import array as arr

# # Khai báo một mảng số nguyên
# my_array = arr.array('i', [1, 2, 3, 4, 5])
# print("Mảng:", my_array)

# # Khai báo biến từ đầu vào của người dùng
# age = int(input("Nhập tuổi của bạn: "))
# print("Tuổi của bạn là:", age)

# # Khai báo biến từ kết quả của một biểu thức
# result = x + y
# print("Kết quả của x + y:", result)


# =======================SYNTAX INPUT / PRINT ===================================
# input (prompt) -> nhap tu ban phim -> kieu string 
# print(type((int(input (" Nhap so : ")))))
#  -> int

# -------------------------------------------------------------------------------

# Nhan nhieu gia tri 

# map(function,iterable,...)
# function: Là một hàm mà bạn muốn áp dụng lên từng phần tử của các iterable.
# iterable: Là một hoặc nhiều đối tượng có thể lặp lại (ví dụ: list, tuple, set)
# mà bạn muốn áp dụng hàm function lên từng phần tử của chúng.

# Ex: chuyen ds num(string) -> ds num(number)-list 
# Danh sách chuỗi số
# numbers_str = ["1", "2", "3", "4", "5"]
# # Sử dụng map để chuyển đổi thành danh sách các số nguyên
# numbers_int = list(map(int, numbers_str))
# print(numbers_int)  # Output: [1, 2, 3, 4, 5]

# Ex: Nhap nhieu value tu ban phim 
# a,b,c = map(int,input().split())
# print(a,b,c)

# data = input("Nhập các số, cách nhau bởi dấu cách: ")
# numbers = data.split()
# numbers = [int(num) for num in numbers]
# print("Các số bạn đã nhập là:", numbers)
# for num in numbers:
#  print(type(num)) # int

# # Nhận tên và tuổi từ người dùng và in ra kết quả
# name = input("Nhập tên của bạn: ")
# age = int(input("Nhập tuổi của bạn: "))
# print(f"Xin chào, {name}. Bạn {age} tuổi.")

# #print(obj1,obj2,..,seperate,end) || print("Promp",value)
# print( 'java' , 'python' ,sep=' & ',end='!'); 
# # java & python!

# -------------------------------------------------------------------------------

# * In so thap phan sau dau phay 
# Sử dụng format()
# num = 123.456789
# formatted_num1 = "{:.2f}".format(num)
# print("Số thập phân với 2 chữ số sau dấu phẩy (format):", formatted_num1)

# # Sử dụng f-string
# formatted_num3 = f"{num:.2f}"
# print("Số thập phân với 2 chữ số sau dấu phẩy (f-string):", formatted_num3)

# # Sử dụng round()
# rounded_num1 = round(num, 2)
# print("Số thập phân với 2 chữ số sau dấu phẩy (round):", rounded_num1)

# Su dung % 
# formatted_num1 = "%.2f" % num
# print("Số thập phân với 2 chữ số sau dấu phẩy: %.2f" % num)

# -------------------------------------------------------------------------------


# * Chuyen he 2 8 16 -> 10 
# def binary_to_decimal(binary_str):
#     return int(binary_str, 2)

# def octal_to_decimal(octal_str):
#     return int(octal_str, 8)

# def hexadecimal_to_decimal(hexadecimal_str):
#     return int(hexadecimal_str, 16)

# # Ví dụ
# binary_number = "1011"
# octal_number = "17"
# hexadecimal_number = "1A"

# print("Nhị phân", binary_number, "sang thập phân:", binary_to_decimal(binary_number))
# print("Bát phân", octal_number, "sang thập phân:", octal_to_decimal(octal_number))
# print("Thập lục phân", hexadecimal_number, "sang thập phân:", hexadecimal_to_decimal(hexadecimal_number))

# cach khac 2 8 16 -> 10
# a = 0b1101
# print(a) 
# b = 0o123
# print(b) 
# c = 0x22A
# print(c)


# * 10 -> 2,8,16 
# [2:] loai bo tien to truoc (2:0b ; 8: 0o ; 16: 0x) 

# def decimal_to_binary(decimal_num):
#     return bin(decimal_num)[2:]

# def decimal_to_octal(decimal_num):
#     return oct(decimal_num)[2:]

# def decimal_to_hexadecimal(decimal_num):
#     return hex(decimal_num)[2:].upper()

# # Ví dụ
# decimal_number = 42

# binary_number = decimal_to_binary(decimal_number)
# octal_number = decimal_to_octal(decimal_number)
# hexadecimal_number = decimal_to_hexadecimal(decimal_number)

# print(f"Số thập phân {decimal_number} sang nhị phân: {binary_number}")
# print(f"Số thập phân {decimal_number} sang bát phân: {octal_number}")
# print(f"Số thập phân {decimal_number} sang thập lục phân: {hexadecimal_number}")

# -------------------------------------------------------------------------------


# * "" || value a = 0 => bool = false , a!=0 => bool a = true
# a=100
# print(bool(a))
# => True

# -------------------------------------------------------------------------------

# *Ep kieu: a=int/float/str(s) (s:xau)

# -------------------------------------------------------------------------------

# hoan vi 
# a,b,c = 10,20,30 
# a,b=b,a
# / : thap phan ; // chia nguyen ; ** luy thua ; (a is/is not b)  ;  ( c in || not in s) -> kt xau c co trong s hay ko
# Ex:
# a = 10
# b = 20
# c = b - 10
# if(a is not b) : print('a khac b')
# if(a is c) : print('a = c')

# s = "chuong"
# if ('c' not in s) : print ('Yé')
# else:print('Nô')

# -------------------------------------------------------------------------------

# *Khac biet giua ham voi phuong thuc 
# Sự khác biệt chính giữa hàm và phương thức:

# Liên kết với đối tượng:
# Hàm: Độc lập, không liên kết với bất kỳ đối tượng cụ thể nào.
# Phương thức: Liên kết với đối tượng cụ thể (thông qua self trong Python).

# Cách gọi:
# Hàm: Gọi trực tiếp bằng tên hàm và truyền các đối số cần thiết.
# Phương thức: Gọi thông qua đối tượng và sử dụng dấu chấm (.) để gọi, tức là object.method().

# Vị trí định nghĩa:
# Hàm: Được định nghĩa và sử dụng ở bất kỳ đâu trong chương trình.
# Phương thức: Thường được định nghĩa bên trong định nghĩa của một lớp.
# Hàm định nghĩa bên ngoài lớp
# Ex:
# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Alice"))  # Gọi hàm greet trực tiếp

# # Phương thức trong lớp
# class MyClass:
#     def say_hello(self):
#         print("Hello, world!")

# obj = MyClass()
# obj.say_hello()  # Gọi phương thức say_hello của đối tượng obj



# =======================FUNCTION AND METHOD BUILT-IN ===================================

# Syn:
# def function_name(parameters):
#     """Docstring của hàm"""
#     # Đoạn mã của hàm
#     statement1
#     statement2
#     ...
#     return value


# * Các hàm toán học cơ bản:
# import math
# print(help(math)) -> all method of math 

# import math || from math import * -> ko can dung math.
# 1.Hàm số mũ và căn bậc hai:
# math.sqrt(x): Trả về căn bậc hai của x.(float)
# math.isqrt(x): Trả về căn bậc hai của x.(int)
# math.pow(x, y): Trả về x mũ y.
# math.exp(x): Trả về e mũ x.
# math.log(x, base): Trả về logarithm cơ số base của x (mặc định base là e).

# # 2.Hàm số học học cơ bản:
# math.ceil(x): Trả về số nguyên lớn nhất không nhỏ hơn x.
# math.floor(x): Trả về số nguyên nhỏ nhất không lớn hơn x.
# math.trunc(x): Trả về phần nguyên của x.
# math.factorial(x): Trả về giai thừa của x.
# math.gcd(a,b): Greatest Common devided
# math.lcm(a,b):Longest Common Multiple 
# math.comb(n,k): Trả về số cách chọn k mục từ n mục mà không lặp lại và không có thứ tự.(n!/k!(n-k)!)
# math.perm(n,k):Trả về số cách chọn k mục từ n mục mà không lặp lại và có thứ tự(n!/(n-k)!)
# math.fabs(x): absolute |x|

# # 3.Hằng số toán học:
# math.pi: Giá trị của π.
# math.e: Giá trị của e.

# # 4.Hàm số lượng giác:
# math.sin(x), math.cos(x), math.tan(x): Sin, cosin, và tangent của x (đơn vị là radian).
# math.asin(x), math.acos(x), math.atan(x): Arcsin, arccosin, và arctangent của x.

# # 5.Các hàm khác:
# math.degrees(x): Chuyển đổi radian thành độ.
# math.radians(x): Chuyển đổi độ thành radian.
# math.isclose(a, b, rel_tol=1e-09, abs_tol=0.0): Kiểm tra xem a và b có gần nhau không

# =======================IF-ELSE | FOR | WHILE ===================================
# 1.IF ELSE 

# if condition:
#     # Code được thực thi nếu điều kiện là True
#     statement1
#     statement2
#     ...
# elif condition2:
#     # Code được thực thi nếu condition2 là True
#     statement3
#     statement4
#     ...
# else:
#     # Code được thực thi nếu không có điều kiện nào ở trên là True
#     statement5
#     statement6
#     ...

# Ex: 
# x = 10

# if x > 0:
#     print("x là số dương")
# elif x < 0:
#     print("x là số âm")
# else:
#     print("x là số không")

# -------------------------------------------------------------------------------

# 2.FOR 
# iterable = range(start,stop,step) || range(stop)
# start: Giá trị bắt đầu của dãy số (bao gồm).
# stop: Giá trị kết thúc của dãy số (không bao gồm).
# step: Bước nhảy giữa các giá trị trong dãy số (mặc định là 1).


# for item in iterable:
#     # Code được lặp lại cho mỗi phần tử trong iterable
#     statement1
#     statement2
#     ...

# Ex:
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# -------------------------------------------------------------------------------

# 3.WHILE 
# while condition:
#     # Code được lặp lại khi điều kiện là True
#     statement1
#     statement2
#     ...

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# -------------------------------------------------------------------------------

# range():
# 1.range(stop)
# 2.range(stop,start,end)
# Ex:
# # Tạo một danh sách các số từ 1 đến 10
# numbers = list(range(1, 11))
# print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Tạo một danh sách các số chẵn từ 0 đến 10
# even_numbers = list(range(0, 11, 2))
# print(even_numbers)  # Output: [0, 2, 4, 6, 8, 10]

# # Tạo một danh sách các số từ 10 đến 1 (ngược lại)
# reverse_numbers = list(range(10, 0, -1))
# print(reverse_numbers)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# ======================LIST ===================================
# 1. Initialize:
# # a.Khởi tạo danh sách rỗng
# # Sử dụng cặp dấu []
# empty_list = []

# # Sử dụng hàm list()
# empty_list = list()
# s = 'Chuong Minh'
# newList = list(s)
# print(newList)
# ['C', 'h', 'u', 'o', 'n', 'g', ' ', 'M', 'i', 'n', 'h']

# b.Khởi tạo danh sách với các giá trị mặc định
# # Danh sách các số nguyên
# numbers = [1, 2, 3, 4, 5]

# # Danh sách các chuỗi
# fruits = ['apple', 'banana', 'cherry']

# c.Sử dụng comprehension để khởi tạo danh sách
# # *[expression for item in iterable if condition] = list Comprehension
# # Tạo một danh sách chứa bình phương của các số từ 1 đến 10
# squares = [x**2 for x in range(1, 11)]

# # Tạo một danh sách chứa các số chẵn từ 1 đến 10
# even_numbers = [x for x in range(1, 11) if x % 2 == 0]

# # Tạo một danh sách 2 chiều (ma trận)
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# # d.Nhap từ ban phím các giá trị 
# # Khởi tạo một danh sách rỗng
# my_list = []

# # Nhập số lượng phần tử từ người dùng
# n = int(input("Nhập số lượng phần tử trong danh sách: "))

# # Nhập các giá trị từ bàn phím và thêm vào danh sách
# for i in range(n):
#     value = input(f"Nhập giá trị thứ {i+1}: ")
#     my_list.append(value)

# # In danh sách sau khi nhập
# print("Danh sách sau khi nhập:", my_list)

# e.Sử dụng hàm list() với iterable khác
# # Chuyển đổi tuple thành danh sách
# my_tuple = (1, 2, 3)
# list_from_tuple = list(my_tuple)

# # Chuyển đổi set thành danh sách
# my_set = {4, 5, 6}
# list_from_set = list(my_set)

# # Chuyển đổi chuỗi thành danh sách các ký tự
# my_string = "hello"
# list_from_string = list(my_string)

# -------------------------------------------------------------------------------

#  2. List Methods
# .Thêm và xóa phần tử:
# append(): Thêm một phần tử vào cuối danh sách.
# insert(): Chèn một phần tử vào vị trí chỉ định.
# extend(): Mở rộng danh sách bằng cách thêm các phần tử từ một iterable.

# .Xóa phần tử:
# remove(): Xóa phần tử đầu tiên có giá trị xác định.
# pop(): Xóa và trả về phần tử tại vị trí chỉ định hoặc cuối cùng nếu không có chỉ số.
# clear(): Xóa tất cả các phần tử trong danh sách.

# .Sắp xếp và đảo ngược:
# sort(): Sắp xếp danh sách.
# reverse(): Đảo ngược thứ tự các phần tử trong danh sách.

# .Tìm kiếm và đếm:
# index(): Trả về chỉ số của phần tử đầu tiên có giá trị xác định.
# count(): Đếm số lần xuất hiện của một phần tử trong danh sách.

# .Sao chép:
# copy(): Sao chép danh sách.

# .Hàm tính toán:
# len(): Trả về độ dài của danh sách.
# sum(): Tính tổng các phần tử trong danh sách.
# max(): Trả về giá trị lớn nhất trong danh sách.
# min(): Trả về giá trị nhỏ nhất trong danh sách.

# .Hàm liên quan đến chỉ số:
# enumerate(): Trả về một đối tượng enumerate, chứa các cặp chỉ số và giá trị.
# zip(): Kết hợp các phần tử từ các danh sách (hoặc các iterable khác) thành các tuple.

# .Hàm khác:
# sorted(): Trả về một danh sách mới, sắp xếp từ một iterable.
# filter(): Lọc các phần tử của một iterable dựa trên một hàm điều kiện.
# map(): Áp dụng một hàm cho từng phần tử của một iterable.

# Ex: 
# # Khai báo một danh sách
# my_list = [1, 3, 5, 7, 9]

# # Thêm một phần tử vào cuối danh sách
# my_list.append(11)

# # Chèn một phần tử vào vị trí chỉ định
# my_list.insert(1, 2)

# Ex extend(): 
# Initial list
# fruits = ['apple', 'banana', 'cherry']
# # List to be added
# more_fruits = ['orange', 'mango', 'grapes']
# # Using extend() method
# fruits.extend(more_fruits)
# print(fruits)
# ['apple', 'banana', 'cherry', 'orange', 'mango', 'grapes']


# # Xóa phần tử đầu tiên có giá trị là 3
# my_list.remove(3)

# # Xóa và trả về phần tử tại vị trí 2
# popped_value = my_list.pop(2)

# # Sắp xếp danh sách
# my_list.sort()

# # Đảo ngược thứ tự các phần tử trong danh sách
# my_list.reverse()

# # Tính tổng các phần tử trong danh sách
# total = sum(my_list)

# # Đếm số lần xuất hiện của giá trị 5 trong danh sách
# count_five = my_list.count(5)

# print(my_list)  # Output: [11, 9, 7, 5, 2, 1]
# print(total)    # Output: 35
# print(count_five)  # Output: 1

# ---------------------------List Tech----------------------------------------------------

# Ex: 
# a = [1,2,3,4,'28 tech',50.4]
# print(a)
# # [1, 2, 3, 4, '28 tech', 50.4]

# # Ex: 
# s = '28 tech'
# a = list(s)
# print(a)
# # ['2', '8', ' ', 't', 'e', 'c', 'h']

# # Ex: 
# a = list(range(20))
# print (a)
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] 

# print(a[2]) 
# # 2
# print(a[-2])
# # 18

# # Ex:
# a = [1,2,3,4]
# for i in range(0,len(a)):
#     print(a[i],end=' ')
# for item in a :
#     print(item,end=' ')
# # 1 2 3 4
# print()

# for i in range(len(a)-1,-1,-1):
#     print(a[i],end=' ')
# # 4 3 2 1
    
    
# # *Edit value in list 
# a = [1,2,3,4,"C++","28Tech"]
# a[-1] = "Java"
# print(a)
# [1, 2, 3, 4, 'C++', 'Java']


# # *Day mot phan tu vao sau list 
# a = [1,2,3,4]
# a.append(100) 

# *Xoa value qua index
# a.pop(index) 

# auto erase back value 
# a.pop() 


# * Xoa value
# a.remove(value)

# *Xoa tat ca value
# a.clear()


# *List tu nhan ban duoc 
# Tao 100 chu so 0 
# a = [0] * 100 

# *Tim gia tri trong list (function in :O(n))
# if value in a: code 


# * Noi 2 list : a.extend(b)

# *Mot so phuong thuc list 
# - a.copy() 
# Ex: 
# a = [1,2,3]
# b = a 
# print(a is b) 
# # true 
# c = a.copy()
# print(c is a)
# # false 

# B55 copy list , tham so cho ham 
# a = [1,2,3,4]
# b = a 
# a b cung id 
# c = a.copy()
# a & c != id  

# def change(arr):
    # arr[0] = 10 

# B56 List Slicing 
# cat list a tai index start toi value tai chi so stop-1 voi bc nhay step 
# a[start:stop:step] 
# a = [10,20,30,40,50]
# b = a[2:5:1] 
# print(b) 
# # 30 40 50 

# # Ex: a 2  3  1  5  7   4   3
# # idx  -7 -6 -5 -4 -3  -2   -1

# b = a[1:-2] 
# # 3 1 5 7 
# b = a[-4:-1]
# # 5 7 4 

# * Lat nguoc list 
# a = [2,3,1] 
# b = a[::-1] 
# print(b)
# 1 3 2 

# * Thay doi gia tri trong list 
# a = [1,2,3,4]
# a[1:3] = [10,10] || [] -> xoa 
# 1 10 10 4 
# print (a)

# * Chen va xoa voi list slicing 
# Ex: chen vao dau 
# a = ['x' ,'y','z'] 
# a[ :0] = [10,20,30]
# print(a)

# Ex: chen vao cuoi 
# a[len(a):] = [10,20,30]

# * copy bang list slicing 
# a = ['x','y','z'] 
# b = a[:]
# print(b) 
# a & b != id 

# B57 Ham Lambda 
# sync: lambda para : expresion  || res = func para1,para2,.. : expresion (arguments,..)
# Ex: 
# def func(n):
#     return 2*n

# func = lambda x : x*2 

# *Tinh chat: IIFE (goi ngay lap tuc) Immediately Invoked Function Expression
# Ex: 
# sum = lambda x,y,z : x+y+z 
# print(sum(1,2,3))
# # IIFE 
# print((lambda x,y,z : x + y + z)(1,2,3)) 
# Ex:
# res =  (lambda a,b,c : a + b + c) (1,2,3)
# print(res)

# # Ex: binh phuong tat ca phan tu trong a 
# a = [1,2,3]
# b = list(map(lambda x : x**2,a)) 
# print(b)

# # Ex: loc cac so chan co trong mang 
# c = list(filter(lambda x : x % 2 == 0,a))

# # Ex: if else trong lambda 
# findMax = lambda x, y : x if x > y else y 
# print(findMax(100,200))

# B58 List Comprehension 
# - Syntax: var_list = [expresion for var in iterible] || var_list = [expression for var in iterible if_clause]
# - expression: Bieu thuc thuc hien cho moi vong lap
# - var: bien , item trong iterable 
# - iterable: collection chua cac object (list, tuple, str,..)

# Ex:
# a = [1, 2, 3, 4, 5, 6]
# b = [x**2 for x in a]
# print(b)
# [1, 4, 9, 16, 25, 36]

# Ex2: 
# def sumDigit(n):
#     sum = 0
#     while n!=0:
#         sum += n%10
#         n//=10
#     return sum

# a = [12, 123, 111]
# b = [sumDigit(x) for x in a]
# print(b)
# # [3, 6, 3]

# Ex3:
# import math
# def prime(n):
#     for i in range(2, math.isqrt(n)+1):
#         if n%i ==0:
#             return False
#     return n>1
# a = [1, 2, 3, 4, 5, 6]
# b = [x**2 for x in a if prime(x)]
# print(b)

# * Nested list:
# [ expression for var in iterable] 
# expression = [expression for var in iterable]

