# # * Tupple
# friends = ('Ti', 'Teo', 'Tun', 'Tin')

# (*a, b, c) = friends
# (*c, d) = friends

# print(a, b, " ", c, d, end=" ")

# t = (1, 2, 3)
# print(t.index(5))


# myset1 = {1, 2, 3}
# myset2 = {6, 7}
# mylist = [6, 7]
# mytuplr = (6, 7)
# myset1.add(myset2)
# print((myset1))
# myset1.update(myset2)
# print((myset1))

# myset1.update(mytuplr)
# print((myset1))

# myset1.update(mylist)
# print((myset1))

# x = {"apple", "banana", "chery"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection_update(y)
# z = x.union(y)
# xh trong x/ ko trong y
# z = x.difference(y)
# z = x - y
# x.difference_update(y)
# print(x)
# x = x - y

# z = x ^ y : bo di phan giao x va y
# {'google', 'chery', 'apple', 'microsoft', 'banana'}


# 1. List (Danh sách)
# Cú pháp: []
# Đặc điểm:
# Thứ tự: Có thứ tự (các phần tử được lưu trữ và truy cập theo thứ tự chèn).
# Thay đổi: Có thể thay đổi (mutable), nghĩa là bạn có thể thêm, xóa, hoặc thay đổi phần tử sau khi đã tạo.
# Phần tử trùng lặp: Cho phép phần tử trùng lặp.
# Ví dụ:
# python
# Copy code
# my_list = [1, 2, 3, 4, 4]
# 2. Tuple (Bộ dữ liệu)
# Cú pháp: ()
# Đặc điểm:
# Thứ tự: Có thứ tự (giống như list).
# Không thay đổi: Bất biến (immutable), nghĩa là sau khi tạo tuple, bạn không thể thay đổi các phần tử bên trong.
# Phần tử trùng lặp: Cho phép phần tử trùng lặp.
# Ví dụ:
# python
# Copy code
# my_tuple = (1, 2, 3, 4, 4)
# 3. Set (Tập hợp)
# Cú pháp: {} hoặc dùng hàm set()
# Đặc điểm:
# Thứ tự: Không có thứ tự (các phần tử không có vị trí cố định).
# Thay đổi: Có thể thay đổi, nhưng các phần tử phải là các giá trị bất biến (immutable), như số, chuỗi, tuple.
# Không cho phép trùng lặp: Mọi phần tử trong set đều là duy nhất.
# set.add(elem): Thêm phần tử elem vào set.
# set.remove(elem): Xóa phần tử elem khỏi set. Ném lỗi KeyError nếu  phần tử không tồn tại.
# set.discard(elem): Xóa phần tử elem nếu nó có mặt, không ném lỗi nếu phần tử không tồn tại.
# set.pop(): Xóa và trả về một phần tử ngẫu nhiên từ set.
# set.clear(): Xóa tất cả các phần tử khỏi set.


# * dictionary
# my_dict = {'a': 1, 'b': 2, 'c': 3}

# # Truy cập và cập nhật phần tử
# print(my_dict['a'])  # 1
# my_dict['d'] = 4
# print(my_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# # Sử dụng get() và pop()
# print(my_dict.get('e', 'Not Found'))  # Not Found
# popped_value = my_dict.pop('b')
# print(popped_value)  # 2
# print(my_dict)  # {'a': 1, 'c': 3, 'd': 4}

# # Lấy danh sách khóa, giá trị và cặp (key, value)
# print(my_dict.keys())  # dict_keys(['a', 'c', 'd'])
# print(my_dict.values())  # dict_values([1, 3, 4])
# print(my_dict.items())  # dict_items([('a', 1), ('c', 3), ('d', 4)])

# # Sao chép từ điển
# new_dict = my_dict.copy()
# print(new_dict)  # {'a': 1, 'c': 3, 'd': 4}


# fruits = ("apple", "banana", "cherry")
# print(len(fruits))


# fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(fruits[2:5])


# bai 1
# s = input()

# # Convert the input string to a list of integers
# lst = s.split(",")
# lst = [int(x) for x  in s.split(",")]

# # Convert the input string to a tuple of integers
# tpl = tuple(int(x) for x in s.split(","))

# tpl = tuple(lst)
# print(lst, ", ", tpl)


# bai 2

# Danh sách lưu trữ các tuple
# data = []

# # Nhập các tuple
# for _ in range(n):
#     # Đọc từng dòng dữ liệu từ bàn phím
#     line = input()
#     # Phân tách dữ liệu từ dòng nhập vào
#     name, age, score = line.split(',')
#     # Chuyển đổi age và score thành số nguyên
#     age = int(age)
#     score = int(score)
#     # Thêm tuple vào danh sách
#     data.append((name, age, score))

# # Sắp xếp danh sách theo thứ tự tăng dần: name, age, score
# # sorted_data = sorted(data, key=lambda x: (x[0], x[1], x[2]))

# # In kết quả
# print("Danh sách đã sắp xếp:")
# for item in sorted_data:
#     print(item)

# s = input()
# a = []
# b = []

# while s != "":
#     a = s.split(",")
#     t = tuple(a)
#     b.append(t)
#     s = input()

# b.sort()
# print(b)

# d1 = {"one": 11, "two": 22, "three": 33, "four": 44, "five": 55}
# keys = ['two', 'five']
# d2 = {}


# for k in keys:
# d2[k] = d1[k]


# print(d2)


# T1 = (1, 9, 1, 6, 3, 4)
# ttl = 0
# for x in T1:
#     ttl += x
# print(ttl)


# import random
# t1 = ()
# for i in range(5):
#     x = random.randint(0, 100)
#     t1 += (x,)
# print(t1)


# d1 = {"one": 11, "two": 22, "three": 33, "four": 44, "five": 55}
# L1 = list(d1.items())
# print(L1)

# T1 = (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
# s1 = set(T1)
# print(s1)


# d1 = {"one": "eleven", "2": 2, "three": 3,
#       "11": "eleven", "four": 44, "two": 2}
# vals = list(d1.values())  # all values
# uvals = [v for v in vals if vals.count(v) == 1]  # unique values
# d2 = {}


# for k, v in d1.items():
#     if v in uvals:
#         d = {k: v}
#         d2.update(d)


# print("dict with unique value:", d2)


# l1 = [1, 2, 3, 4, 5]
# l2 = [4, 5, 6, 7, 8]
# s1 = set(l1)
# s2 = set(l2)
# commons = s1 & s2
# commonlist = list(commons)
# print(commonlist)


# tuple1 = (-1, -2, 3, 4)
# *soam, *soduong = tuple1
# print(soduong)


# dic = {"a": 2, "b": 3}
# dic.pop("a")
# dic.pop("b")
# print(dic)

# s = {1, 2, 3}
# print(s)

# s.clear()
# print(s)
# a = "{2,3,4}"

# print(type(a))


set(50, 40, 20, 30, 10)
