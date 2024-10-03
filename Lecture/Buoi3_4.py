"""
• List : tập các giá trị có tính thứ tự và có thể thay đổi, phần tử có thể trùng lặp về giá trị []
• Tuple : tập các giá trị có tính thứ tự và không thể thay đổi, phần tử có thể trùng lặp về giá trị ()
• Set : tập các giá trị không có tính thứ tự và không thay đổi *, không chỉ mục, phần tử không trùng lặp {}
• Dictionary : tập các giá trị có tính thứ tự ** và không thể thay đổi, phần tử không trùng lặp về giá trị {key:value}

# 1. LIST 
✓ Khai báo list rỗng lst = []
✓ Khai báo list có các giá trị lst = [2, 5, -1, 5, 8]
✓ Khai báo list có 10 phần tử với giá trị mặc định là 0.5 lst = [0.5] * 10
✓ Lấy số lượng phần tử của list len(list)
✓ Kiểm tra phần tử tồn tại trong list sử dụng từ khóa “in” if value in list:
# * co thu tu: tru cap bang chi muc 
# * khong thay doi: ko them,xoa,thaydoi(modify)
"""
# [[start]:[end][:step]] lấy từ start → end - 1 với bước nhảy step
# lst = [1, 2, 3, 4, 5, 9]
# print(lst[2:5])
# print(lst[ :5])
# print(lst[-4: ])
# print(lst[ :-1])
# print(lst[ : ])
# [3, 4, 5]
# [1, 2, 3, 4, 5]
# [3, 4, 5, 9]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5, 9]


# 7 8 9(len -> break) : in tu 0 -> 8 : end tru di 1 (loop toi vi tri end -> dung vong lap)
# 2,1,0,-1(break): duyet nguoc (in tu len -1 -> 0): toi i = -1 -> break loop
# Ex: in nguoc all value in list
# for i in range(len(lst) - 1, -1, -1):
#     x = lst[i]
#     print(x, end = '\t')
# * \t -> chen dau tab

"""
- GÁN GIÁ TRỊ CHO CÁC PHẦN TỬ TRONG LIST
lst = [5, 7, 2, 9, 6, 3, 10, 17, 16] # len(lst) = 9
➔ lst[1:2] = [6, 8] # [5, 6, 8, 2, 9, 6, 3, 10, 17, 16] # len(lst) = 10 
➔ lst[1:3] = [7] # [5, 7, 9, 6, 3, 10, 17, 16] # len(lst) = 8
- Sử dụng List Comprehension: 
[expression iterable condition]
Ex:
# lst = [1, 2, 3, 4, 5, 9]
# even_lst = [int(x) for x in lst if x % 2 == 0]
# print(even_lst) # [2,4]

- lst.insert(index, value)
lst.insert(2, 9)

- lst.append(value)
Ex:
lst1 = [0, 1, 2, 3]
lst2 = [4, 5]
print(lst1) # [0, 1, 2, 3]
lst1.extend(list2)
print(lst1) # [0, 1, 2, 3, [4, 5]]

- lst1.extend(lst2) : them iterable object vao lst 
Ex:
lst1 = [0, 1, 2, 3]
lst2 = [4, 5]
print(lst1) # [0, 1, 2, 3]
lst1.extend(list2)
print(lst1) # [0, 1, 2, 3, 4, 5]

- lst.remove(value)

- lst.pop(idx) == del lst[index]  # default idx = len-1

- lst.clear(): del all value,obj of lst => []

- / del lst -> delete lst
"""

# SORT in list
"""
# 1. Sử dụng phương thức sort(): sx tren chinh list do 
my_list = [3, 1, 4, 1, 5, 9]
my_list.sort()
print(my_list)  # Output: [1, 1, 3, 4, 5, 9]

my_list.sort(reverse=True)
print(my_list)  # Output: [9, 5, 4, 3, 1, 1]


# 2. Sử dụng hàm sorted(): tao 1 list moi de sx 
my_list = [3, 1, 4, 1, 5, 9]
new_list = sorted(my_list)
print(new_list)  # Output: [1, 1, 3, 4, 5, 9]

new_list = sorted(my_list, reverse=True)
print(new_list)  # Output: [9, 5, 4, 3, 1, 1]


# 3. Sắp xếp danh sách các 
# Sắp xếp theo thứ tự từ điển
str_list = ["apple", "banana", "cherry"]
str_list.sort()
print(str_list)  # Output: ['apple', 'banana', 'cherry']

str_list.sort(reverse=True) # sx nguoc thu tu tu dien
print(str_list)  # Output: ['cherry', 'banana', 'apple']

str_list.sort(key = str.lower) # sắp xếp không phân biệt hoa thường
print(str_list) # Output: ['apple', 'banana', 'cherry']"""


# XỬ LÝ LIST
"""- REVERSE
# lst.reverse() 
- COPY : tao ban sao lst , neu dung phep gan -> tham chieu tren 1 obj (thay doi cung nhau)
# lst1 = lst0.copy() or lst1 = lst(lst0)
- JOIN : +, append, extend

"""
# matrix = [
#     [100, 14, 8, 22, 71],
#     [0, 243, 68, 1, 30],
#     [90, 21, 7, 67, 112],
#     [115, 200, 70, 150, 8]
# ]

# In ma trận
# print("Ma trận:")
# for row in matrix:  # Duyệt từng dòng
#     for x in row:    # Lấy phần tử trên mỗi dòng
#         print('{:>4}'.format(x), end=' ') # f'{x:>4}'
#     print()  # Xuống dòng sau khi in một dòng của ma


# LIST ĐA CHIỀU
# row = 5
# column = 3
# lst = [[0] * column] * row
# print(lst)
# # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


# 2. TUPLE:() (giong voi list nhung tuple ko thay doi)
"""
• obj in tuple have many type data
• Tuple access faster than lst
• Tuple can convert to lst and reverse
• Tuple can unchangeable when created
• not delete,add,search on tuple
• val of tuple unchangeable
• Không thể xóa từng phần tử riêng lẻ của tuple
• Lệnh del sẽ xóa toàn bộ Tuple
• Tạo ra một tuple rỗng, cú pháp: tup1 = ();
• Tạo ra một tuple chỉ chứa một giá trị đơn, thêm dấu phẩy: tup1 = (50, );

THAO TÁC VỚI TUPLE
Chuyển đổi qua lại giữa tuple – list
• Thêm tuples vào tuples
Ví dụ:
tuple1 = (1, 2, 3, 4, 5, 6, 7)
tuple2 = (8, )
tuple1 += tuple2
print(tuple1) # (1, 2, 3, 4, 5, 6, 7, 8)
• Xóa phần tử khỏi tuples: cách 1
• Xóa tuple: del <tuple>

Khi khởi tạo một tuple, các giá trị được gán cho tuple → packing (đóng gói)
• Trong python cho phép trích xuất các giá trị từ tuple → unpacking (mở gói)
• Có thể sử dụng một dấu * duy nhất để lấy các giá trị còn lại trong tuple khi unpacking

friends = ('Tí', 'Tèo', 'Tũn', 'Tĩn')
(Ti, Teo, Tun, Tin) = friends
(Ti, Teo,*AnhEm) = friends
print(Ti) # Tí
print(Tun) # Tũn
print(AnhEm) # ['Tũn', 'Tĩn']

• Đếm phần tử xuất hiện trong tuple : count(<value>)
• Vị trí đầu tiên của giá trị cần tìm : index(<value>)
• Tuple hỗ trợ các toán tử + (Nối tuple) và * (Nhân bản tuple)

('Hi!', ) * 4
('Hi!', 'Hi!', 'Hi!', 'Hi!')

"""

# 3. SET:{} (ko thu tu, ko thay doi(co the them,xoa), ko trung)
# Khai báo set sử dụng dấu ngoặc nhọn { } hoặc hàm set( )
# • myset = {1, 2, 3, 4, 5}
# • myset = set({"1, 2, 3, 4, 5"})

"""- 1 – True hoặc 0 – False được xem là cùng một giá trị
- Sử dụng vòng lặp để lấy đối tượng
- Sử dụng phương thức add() để thêm đối tượng mới vào trong set
- Sử dụng phương thức update() để thêm đối tượng từ một đối tượng khác như: set, list, tuple, dictionary"""

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {6, 7}
# mylist = [6, 7]
# mytyple = (6, 7)
# myset1.add(6)
# print(myset1)  # … ?
# myset1.update(myset2)
# print(myset1)  # … ?
# myset1.update(mylist)
# print(myset1)  # … ?
# myset1.update(mytyple)
# print(myset1)  # … ?

# {1, 2, 3, 4, 5, 6}
# {1, 2, 3, 4, 5, 6, 7}
# {1, 2, 3, 4, 5, 6, 7}
# {1, 2, 3, 4, 5, 6, 7}


"""• Sử dụng phương thức remove(<value>) để xóa đối tượng cụ thể (phát sinh lỗi nếu đối tượng không tồn tại): myset.remove(val)
• Sử dụng phương thức discard(<value>) để xóa đối tượng (không phát sinh lỗi nếu đối tượng không tồn tại) : myset.discard(val)
• Sử dụng phương thức pop( ) để xóa đối tượng ngẫu nhiên: myset.pop()
• Sử dụng phương thức clear( ) để xóa toàn bộ đối tượng có trong set: myset.clear()
• Sử dụng từ khóa del để xóa đối tượng set: del myset

• Sử dụng phương thức union() hoặc toán tử | để nối hai set hoặc giữa set và tuple
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y) # hoặc x | y

• Sử dụng phương thức intersection() hoặc toán tử & giữ lại đối tượng chung giữa hai set (giao)
# Ví dụ:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)  # hoặc x & y
print(z)  # apple
# • Sử dụng phương thức intersection_update() giống với intersection() và gán (đè) vào set hiện tại
# Ví dụ:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)  # hoặc x &= y
print(x)  # apple

# • Sử dụng phương thức difference(<set>) hoặc toán tử - để giữ lại đối tượng không xuất hiện trong <set>
# Ví dụ:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)  # hoặc z = x - y
print(z)  # {'banana', 'cherry'}
# • Sử dụng phương thức difference_update(<set>) giống với difference() và cập nhật vào set hiện tại
# Ví dụ:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)  # hoặc x -= y
print(x)  # {'banana', 'cherry'}

# • Sử dụng phương thức symmetric_difference(<set>) hoặc toán tử ^ không xuất hiện đồng thời ở các sets
# Ví dụ:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)  # hoặc z = x ^ y
print(z)  # {'banana', 'cherry', 'microsoft', 'google'}
# • Sử dụng phương thức symmetric_difference_update(<set>) giống symmetric_difference(), gán (đè) set hiện tại
# Ví dụ:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)  # hoặc x ^= y
"""
import pandas as pd

# URL của tập dữ liệu Heart Disease
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"

# Đọc dữ liệu từ URL
column_names = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", 
                "exang", "oldpeak", "slope", "ca", "thal", "target"]
heart_disease = pd.read_csv(url, names=column_names, na_values="?")

# Xem thông tin dữ liệu
print(heart_disease.info())

# Tách features và target
X = heart_disease.drop("target", axis=1)
y = heart_disease["target"]

# Hiển thị dữ liệu
print(X.head())
print(y.head())


# 3. DICTIONARY:() ()
"""Dictionary là danh sách có chứa tập hợp các phần tử có tính thứ tự *, có thể thay đổi và không được trùng lặp
• Mỗi phần tử của dictionary được thể hiện dưới dạng một cặp(key: value)
✓ Một cặp(key: value) trong dictionary còn được gọi là một item
✓ Mỗi key được phân tách với value tương ứng bằng một dấu:
✓ Các item được phân tách bởi dấu phẩy,
✓ Toàn bộ dictionary được bọc bởi một cặp dấu {}
✓ Trong dictionary, tất cả các key phải là duy nhất(unique)
✓ Các giá trị ở trong dictionary có thể được truy cập bởi cặp dấu[]
✓ Giá trị của một đối tượng trong dictionary có thể là bất kỳ kiểu dữ liệu nào

- khai bao:
mydict = {key: value, ..}
mydict = dict(key: value, ..)

- Thao tac:
Sử dụng key_name
• Sử dụng phương thức get( < key_name > )
• Lấy danh sách keys sử dụng phương thức keys()
• Lấy danh sách giá trị sử dụng phương thức values()
• Lấy danh sách đối tượng theo dạng tuples sử dụng phương thức items()
dict = {'1': "mot", '2': "hai"}
for key, val in dict.items():
    print(key, val, end=' ') # 1 mot 2 hai
• Kiểm tra key có tồn tại trong dictionary: if key_name in <dictionary > :
# print(mydict['name']) # Tran
# print(mydict.get('age')) # 37
# print(mydict.keys()) # dict_keys(['name', 'age', 'country'])
# print(mydict.values()) # dict_values(['Tran', 37, 'Vietnam’])
# print(mydict.items()) # dict_items([('name','Tran'),age' (',37), ('country','Vietnam')])  

- cap nhat obj
• Sử dụng key_name
• Sử dụng phương thức update({'key_name':new_value})
Ví dụ:
mydict['name'] = 'Quang’
mydict.update({'name':'Quang'})

- xoa obj:
• Sử dụng phương thức pop('key_name')
• Sử dụng phương thức popitem() để xóa đối tượng cuối được thêm vào (*)
• Sử dụng phương thức clear() để làm trống dictionary
• Sử dụng từ khóa del để xóa đối tượng dictionary
Ví dụ:
mydict.pop('name')
mydict.popitem()
mydict.clear()
del mydict

- duyet
Lấy key_name:
• for key in mydict: print(key)
• for key in mydict.keys(): print(key)
• Lấy value:
• for key in mydict: print(mydict[key])
• for x in mydict.values(): print(x)
• Lấy giá trị (key : value):
• for key, value in mydict.items(): print(key, value)
=> dict.items(): return key,value o dang tuple
    
"""





# 2/
# def main():
#     try:
#         # Nhập số lượng phần tử trong danh sách
#         n = int(input("Nhập số lượng phần tử trong danh sách (n ≥ 0): "))

#         # Kiểm tra xem n có phải là số hợp lệ không
#         if n < 0:
#             print("Số lượng phần tử không thể nhỏ hơn 0.")
#             return

#         # Khởi tạo danh sách để lưu trữ các số thực
#         numbers = []

#         # Nhập các số thực và thêm vào danh sách
#         for i in range(n):
#             number = float(input(f"Nhập số thực thứ {i+1}: "))  # == "Nhap so thuc thu {0}".format(i+1)
#             numbers.append(number)

#         # Tính trung bình cộng nếu danh sách không rỗng
#         if n > 0:
#             average = sum(numbers) / n
#             print(f"Trung bình cộng của các số là: {average:.2f}")
#         else:
#             print("Danh sách không có phần tử nào để tính trung bình cộng.")

#     except ValueError:
#         print("Error")


# if __name__ == "__main__":
#     main()


# 3/
# def main():
#     n = int(input("Nhap so luong phan tu: "))

#     numbers = []

#     for i in range(n):
#         num = float(input(f"Nhap gia tri thu {i+1}: "))
#         numbers.append(num)

#     indexNegative = -1
#     for i in range(n):
#         if numbers[i] < 0:
#             indexNegative = i
#             break

#     print(f"Vi tri am dau tien la: {indexNegative+1}")


# if __name__ == "__main__":
#     main()


# 12/
# cach 1
# n = int(input("Nhap so luong phan tu: "))
# numbers = []
# for i in range(n):
#     num = float(input(f"Nhap phan tu thu {i+1}: "))
#     numbers.append(num)

# evenArray = [x for x in numbers if x % 2 == 0]
# evenArray.sort()
# oddArray = [x for x in numbers if x % 2 != 0]
# oddArray.sort(reverse=True)

# e_index = 0
# o_index = 0

# for i in range(n):
#     if numbers[i] % 2 == 0:
#         numbers[i] = evenArray[e_index]
#         e_index += 1 // or evenArray.pop(0)
#     else:
#         numbers[i] = oddArray[o_index]
#         o_index += 1

# for num in numbers:
#     print(num, end=" ")


# cach 2
# n = int(input("Nhap so luong phan tu: "))
# numbers = []

# for i in range(n):
#     numbers.append(int(input(f"Nhap phan tu thu {i+1}: ")))

# for i in range(n):
#     for j in range(i+1, n):
#         if numbers[i] % 2 == 0 and numbers[j] % 2 == 0 and numbers[j] < numbers[i]:
#             temp = numbers[i]
#             numbers[i] = numbers[j]
#             numbers[j] = temp

#         if numbers[i] % 2 != 0 and numbers[j] % 2 != 0 and numbers[i] < numbers[j]:
#             temp = numbers[i]
#             numbers[i] = numbers[j]
#             numbers[j] = temp


# for num in numbers:
#     print(num, end=" ")

# myList = [1, 6, 3, 4, 5, 5, 1]

# _max = myList[0]

# index_max = 0

# for i in range(1, len(myList)):

#     if myList[i] > _max:

#         _max = myList[i]

#         index_max = i

# print(index_max)
# lst = [5, 7, 2, 9, 6, 3, 10, 17, 16]


# print(lst[5:-1])


# print(lst[5::1])


# print(lst[4:])


# print(lst[-4:2])


# def sieve(n):
#     primes = [True] * (n+1)

#     p = 2

#     while p * p < n:
#         if primes[p]:
#             for i in range(p*p, n+1, p):
#                 primes[i] = False
#         p += 1

#     primesArray = [x for x in range(2, n+1) if primes[x] == True]
#     return primesArray


# if __name__ == "__main__":
#     N = int(input("Nhap N: "))
#     prime = []
#     prime = sieve(N)
#     print(prime)
