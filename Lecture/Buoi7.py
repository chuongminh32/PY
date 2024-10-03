# __dict__: dictionary chua namespace cua lop
# __init__: constructor  : def __init__ (atributes,..)
# self : cho phep truy cap cac thuoc tinh doi tuong 
import math 

# class Circle:
#     """Lop doi tuong duong tron """
#     def __init__(self, radius):
#         self.radius = radius
#     def calculate_area(self):
#         return round(math.pi * self.radius ** 2, 2)
    

# - khoi tao doi tuong cu the: instance 
# c = Circle(5)
# print(c.__doc__) # lop doi tuong duong tron - ghi chu
# c.radius = 5
# print(c.calculate_area())

# * dau gach duoi -> bo qua
# Ex: 
# a, *_, b = (1,2,3,4) -> a=1, b=4
# for _ in range(5) -> i = _ 

# million = 1_000 -> == 1000
# bin = ob_0010 -> print(bin) == 2

# - - truoc variable -> variable sd noi bo class 
# - - sau var -> tranh xung dot khi sd key python 

# Ex: 
# Biến có dấu gạch dưới kép (__): Biến __c được Python xử lý đặc biệt (mangling). Khi một thuộc tính bắt đầu bằng hai dấu gạch dưới (__), Python sẽ "mangling" nó,
#  nghĩa là sẽ thay đổi tên thuộc tính trong thực tế để tránh việc ghi đè trong các lớp kế thừa. Do đó, trong lớp kế thừa, biến __c không thể bị ghi đè trực tiếp mà
#   Python sẽ đổi tên thành _Sample__c.

# class Sample():
#     # Phương thức khởi tạo
#     def __init__(self):
#         self.a = 1
#         self._b = 2 # Biến nội bộ
#         self.__c = 3 # Biến mangling (private)

# class SecondClass(Sample): # Kế thừa
#     def __init__(self):
#         super().__init__()
#         self.a = "overridden"
#         self._b = "overridden"
#         self.__c = "overridden"  # Không ghi đè trực tiếp biến __c từ lớp cha

# obj2 = SecondClass()
# print(obj2.a)     # Kết quả: overridden
# print(obj2._b)    # Kết quả: overridden
# # print(obj2.__c) # Sẽ gây lỗi AttributeError vì __c đã bị mangling
# print(obj2._SecondClass__c)  # Kết quả: overridden (cách để truy cập biến __c từ lớp cha)
# print(obj2._Sample__c)  # Kết quả: 3 (cách để truy cập biến __c từ lớp cha)

# print(dir(Sample)) 



# *class atributes  : bien lop

# * instance atributes : bien obj

# class SampleClass:
#     class_attr = 100
#     def __init__(self, instance_attr):
#         self.instance_attr = instance_attr 
#     def method(self):
#         print(f"Class atributes: {self.class_attr}")
#         print(f"Instance atributes: {self.instance_attr}")
    


# print(SampleClass.class_attr)
# print(SampleClass.instance_attr) # error -> phai co doi tuong cu the 
# print(SampleClass.__dict__)
# print(SampleClass.__dict__["class_attr"])

# class Label:
#     def __init__(self, text, font):
#         self.__text = text
#         #hoac self.set_text(text)
#         self._font = font
    
#     def get_text(self):
#         return self._text 
    
#     def set_text(self, value):
#         self._text = value.upper() 
    
#     def get_font(self):
#         return self._font
    
#     def set_font(self, value):
#         self._font = value
    

# # Khởi tạo đối tượng Label mà không cần import
# label = Label("Fruits", "Drinks")
# print(label.get_text())  # Kết quả: Fruits

# label.set_text("Vegetable")
# print(label._text)  # Kết quả: VEGETABLE , get_text() == label._text -> _text:noi bo
# # from label import Label
# # label = Label("Fruits", "Drinks")
# # label.get_text()

# # label.set_text("Vegetable")
# # label.get_text()

# - truy cap manling 
# class Label:
#     def __init__(self, text, font):
#         self.__text = text  # Thuộc tính private (mangling)
#         self._font = font
    
#     def get_text(self):
#         return self.__text
    
#     def set_text(self, value):
#         self.__text = value.upper()  # Chuyển chữ thành in hoa
    
#     def get_font(self):
#         return self._font
    
#     def set_font(self, value):
#         self._font = value

# # Khởi tạo đối tượng Label
# label = Label("Fruits", "Drinks")
# print(label.get_text())  # Sử dụng phương thức get_text() để truy cập __text, kết quả: Fruits

# label.set_text("Vegetable")
# print(label.get_text())  # Sử dụng phương thức get_text() để truy cập, kết quả: VEGETABLE

# # Truy cập trực tiếp __text bằng cách mangling (không khuyến khích)
# print(label._Label__text)  # Kết quả: VEGETABLE


# from datetime import date

# class Employee:
#     def __init__(self, name, birth_date):
#         self.name = name
#         self.birth_date = birth_date
    
#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, value):
#         self._name = value.upper()  # Chuyển tên thành in hoa
    
#     @property
#     def birth_date(self):
#         return self._birth_date
    
#     @birth_date.setter
#     def birth_date(self, value):
#         self._birth_date = date.fromisoformat(value)  # Chuyển birth_date từ chuỗi thành đối tượng date

# # Khởi tạo đối tượng Employee
# join = Employee("John", "2001-02-07")

# # Truy cập thuộc tính name
# print(join.name)  # Kết quả: JOHN

# # Truy cập thuộc tính birth_date
# print(join.birth_date)  # Kết quả: 2001-02-07 (dạng datetime.date)

# # Đổi giá trị name
# join.name = "John name"
# print(join.name)  # Kết quả: JOHN NAME




# - __getattr__(), __setattr__()


# Polymorphism : tinh da hinh
# class Birth:
#     def intro(self):
#         print("this is bird")
#     def flight(self):
#         print("flying method")
# class Eagle(Birth):
#     def flight(self):
#         print("Eagle Flying")
# class Hawks(Birth):
#     def flight(self):
#         print("Hawks flying")

# obj_birth = Birth()
# obj_eag = Eagle()
# obj_haw = Hawks()
# obj_birth.intro()
# obj_birth.flight()
# obj_eag.intro()
# obj_eag.flight()
# obj_haw.intro()
# obj_haw.flight()

# Abstract : tinh truu tuong 
# Lớp Trừu Tượng và Phương Thức Trừu Tượng trong Python:
# Lớp trừu tượng (abstract class) là lớp không thể khởi tạo trực tiếp mà chỉ được sử dụng như một lớp cha cho các lớp con. Nó chứa các phương thức mà các lớp con phải triển khai.
# Phương thức trừu tượng (abstract method) là phương thức được khai báo trong lớp cha, nhưng không có phần thân thực thi. Các lớp con phải định nghĩa lại các phương thức này.
# ABC (Abstract Base Class) là lớp cơ bản mà bạn cần kế thừa để định nghĩa một lớp trừu tượng trong Python.
# @abstractmethod là decorator được sử dụng để khai báo một phương thức là trừu tượng, bắt buộc lớp con phải triển khai

# Ex:
# from abc import ABC, abstractmethod

# # Lớp trừu tượng Shape
# class Shape(ABC):
    
#     @abstractmethod
#     def calculate_perimeter(self):
#         pass

#     @abstractmethod
#     def calculate_area(self):
#         pass

#     def display_info(self):
#         print(f"Chu vi: {self.calculate_perimeter()}")
#         print(f"Diện tích: {self.calculate_area()}")

# # Hình tròn kế thừa từ lớp trừu tượng Shape
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def calculate_perimeter(self):
#         return 2 * 3.1415 * self.radius

#     def calculate_area(self):
#         return 3.1415 * self.radius ** 2

# # Hình chữ nhật kế thừa từ lớp trừu tượng Shape
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def calculate_perimeter(self):
#         return 2 * (self.width + self.height)

#     def calculate_area(self):
#         return self.width * self.height

# # Sử dụng
# circle = Circle(5)
# rectangle = Rectangle(3, 4)

# circle.display_info()
# rectangle.display_info()
