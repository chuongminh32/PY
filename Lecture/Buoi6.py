# | Hàm/Phương thức               | Mô tả                                                                            | Ví dụ                                 | Kết quả                   |
# |-------------------------------|---------------------------------------------------------------------------------|---------------------------------------|---------------------------|
# | str.lower()                   | Chuyển đổi chuỗi thành chữ thường.                                            | 'HELLO'.lower()                       | 'hello'                   |
# | str.upper()                   | Chuyển đổi chuỗi thành chữ in hoa.                                            | 'hello'.upper()                       | 'HELLO'                   |
# | str.title()                   | Chuyển đổi chuỗi thành dạng tiêu đề (chữ cái đầu mỗi từ viết hoa).            | 'hello world'.title()                 | 'Hello World'             |
# | str.strip()                   | Loại bỏ khoảng trắng ở đầu và cuối chuỗi.                                     | '  hello  '.strip()                   | 'hello'                   |
# | str.split()                   | Chia chuỗi thành danh sách các từ.                                             | 'hello world'.split()                 | ['hello', 'world']        |
# | str.join()                    | Nối các phần tử trong danh sách thành chuỗi.                                   | ' '.join(['hello', 'world'])         | 'hello world'             |
# | str.replace(old, new)         | Thay thế tất cả các lần xuất hiện của chuỗi con old bằng new.                 | 'hello'.replace('l', 'L')             | 'heLLo'                   |
# | str.find(sub)                 | Tìm vị trí đầu tiên của chuỗi con sub. Nếu không tìm thấy, trả về -1.         | 'hello'.find('l')                     | 2                         |
# | str.count(sub)                | Đếm số lần xuất hiện của chuỗi con sub trong chuỗi.                           | 'hello'.count('l')                    | 2                         |
# | str.startswith(prefix)        | Kiểm tra xem chuỗi có bắt đầu bằng chuỗi con prefix hay không.                | 'hello'.startswith('he')              | True                      |
# | str.endswith(suffix)          | Kiểm tra xem chuỗi có kết thúc bằng chuỗi con suffix hay không.               | 'hello'.endswith('lo')                | True                      |
# | str.isalpha()                 | Kiểm tra xem ký tự có phải là chữ cái hay không.                              | 'A'.isalpha()                         | True                      |
# | str.isdigit()                 | Kiểm tra xem ký tự có phải là chữ số hay không.                              | '5'.isdigit()                         | True                      |
# | str.isalnum()                 | Kiểm tra xem ký tự có phải là chữ cái hoặc chữ số hay không.                 | 'abc123'.isalnum()                    | True                      |
# | str.isspace()                 | Kiểm tra xem ký tự có phải là khoảng trắng hay không.                         | ' '.isspace()                         | True                      |
# | str.isupper()                 | Kiểm tra xem ký tự có phải là chữ in hoa hay không.                          | 'A'.isupper()                         | True                      |
# | str.islower()                 | Kiểm tra xem ký tự có phải là chữ in thường hay không.                       | 'a'.islower()                         | True                      |
# | str.isprintable()             | Kiểm tra xem ký tự có phải là ký tự có thể in được hay không.                 | 'A'.isprintable()                     | True                      |
# | str.capitalize()              | Chuyển đổi ký tự đầu tiên của chuỗi thành chữ in hoa và tất cả ký tự còn lại thành chữ thường. | 'hello world'.capitalize()            | 'Hello world'             |
# | str.swapcase()                | Đổi chữ in hoa thành chữ in thường và ngược lại.                             | 'Hello World'.swapcase()              | 'hELLO wORLD'             |
# | str.splitlines()              | Chia chuỗi thành danh sách các dòng.                                          | 'Hello\nWorld'.splitlines()           | ['Hello', 'World']        |


# - nam tren nhiu dong : ''', """ .
# * function xu li chuoi
# + str.strip(): loai bo khoang trang 2 dau
# + upper() -> all upper,lower() -> all lower | capitalize(): viet hoa ki tu dau
# + split(","): tach chuoi theo ,
# + sd key word in/not in: check chuoi co ton tai trong chuoi khac khong

# a = "Hello world"
# // ko error. Neu co "hi" -> replace
# print(a.replace("hi", "Global"))

# Sửdụnghàm startswith() / endswith() đểkiểmtra chuỗicó bắtđầuhoặckếtthúc bằngmộtchuỗicon nào không
# s.startswitch('str')

# Sửdụnghàm find() / rfind() đểtrảvềvịtrí đầutiên / cuốicùng tìm thấytrong chuỗihoặc-1 nếukhông tìm thấy
# + find("str"): return -1 neu ko tim thay str
# + rfind("str"): tim kiem tu phai qua trai
# + count("str"): dem so lan xuat hien/ return 0 (not found)
# + join("str"): noi chuoi theo str
# s2 = s1.join(arr): noi arr theo s1 va gan lai cho s2 

# + isalnum(): chu & so
# print("chuongsdid098765434-567".isalnum()) // false 
# print("chuongsdid098765434567".isalnum()) // true
# + isalpha(): chu
# + isdigit(): num
# * Ham can le
# + center/rjust/ljust(len,char)

# Ex:
# str = 'FIT-UTE'
# print(str.center(20))     #       FIT-UTE
# print(str.center(20,"*")) # ******FIT-UTE*******
# print(str.rjust(20, '*')) # *************FIT-UTE
# print(str.ljust(20, '*')) # FIT-UTE*************
#

# print("Hello {0}, my name is {1}".format("Minh","Chuong"))

# module
# import moduleName as otherNameModule
# - import mot phan cua module do
# from math import sqrt, pi
# - nap tat ca module
# from module_name import *  or import module_name

# * khi khai bao sd module -> trinh thong dich se tim cac module tuong ung theo thu tu sau :
# - thu vien hien hah ma script dang goi
# - cac thu muc trong PYTHON path , 1bien moi truong voi ds cac thu muc
# - cac duong dan mac dinh tren Linux/Unix

# * liet ke thuoc tinh phong thuc trong module -> dir()


# lst = []
# n = int(input("Nhap n: "))

# for i in range(n):
#     lst.append(input(f"Nhap phan tu thu {i+1}: "))

# * package : chua nhieu module, package khac nhau
# (doc file __init__.py -> nap thu vien )


# s = input("Nhập xâu kí tự bất kì:")

# kq = False

# for i in range(len(s)-1):

#     if s[i] == "2" and s[i+1] == "1":

#         break

# print(kq)


# s = "12 34 56 ab cd de "

# print(s.find(" "))

# print(s.find("12"))

# print(s.find("34"))

# name = "Codelearn"
# print(name[0])
# Thuộc tính nào của module chứa tên của module đó?

# Câu hỏi 8Trả lời

# a.
# name


# b.
# _name_


# c.
# __init__


# d.
# __name__


# e.
# Đáp án khác

# a, b = "Hello", "world"
# c = a + " " + b
# print(c)

# s = input("Nhập xâu kí tự bất kì:")

# kq = False

# for i in range(len(s)-1):

#     if s[i] == "2" and s[i+1] == "1":

#         break

# print(kq)

s = "abcdefg"
print(s[2])
