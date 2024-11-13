# # Câu hỏi 1:
# # Dựa vào thiết kế của sơ đồ lớp (Class Diagram), mối quan hệ giữa hai lớp Device và Manufacturer trong hình vẽ là "Aggregation".
# # Aggregation (tập hợp) là một mối quan hệ khi một đối tượng có thể tồn tại độc lập với đối tượng khác, tức là Manufacturer có thể tồn tại mà không cần Device. Mối quan hệ này thường biểu diễn bằng mũi tên với hình thoi rỗng.
# # => Đáp án là: a) Aggregation

# # Câu hỏi 2:
# # Chương trình Python trong câu hỏi sẽ in ra thông tin của đối tượng Manufacturer sau khi gọi phương thức describe().
# # Trong đoạn mã, một đối tượng manu1 thuộc lớp Manufacturer được tạo với các giá trị identity=100 và location='Vietnam'.
# # Phương thức describe() in ra chuỗi chứa giá trị của các thuộc tính identity và location.
# # Kết quả của chương trình sẽ là:
# # Identity: 100 - Location: Vietnam

# # Định nghĩa các lớp Person, Student, Teacher, Doctor
# class Person:
#     def __init__(self, name, yob):
#         self.name = name
#         self.yob = yob

#     def describe(self):
#         pass

# class Student(Person):
#     def __init__(self, name, yob, grade):
#         super().__init__(name, yob)
#         self.grade = grade

#     def describe(self):
#         print(f"Student: Name={self.name}, Year of Birth={self.yob}, Grade={self.grade}")

# class Teacher(Person):
#     def __init__(self, name, yob, subject):
#         super().__init__(name, yob)
#         self.subject = subject

#     def describe(self):
#         print(f"Teacher: Name={self.name}, Year of Birth={self.yob}, Subject={self.subject}")

# class Doctor(Person):
#     def __init__(self, name, yob, specialist):
#         super().__init__(name, yob)
#         self.specialist = specialist

#     def describe(self):
#         print(f"Doctor: Name={self.name}, Year of Birth={self.yob}, Specialist={self.specialist}")

# # Định nghĩa lớp Ward với các phương thức addPerson, describe, countDoctor, sortAge, aveTeacherYearOfBirth
# class Ward:
#     def __init__(self, name):
#         self.name = name
#         self.people = []

#     def addPerson(self, person):
#         self.people.append(person)

#     def describe(self):
#         print(f"Ward Name: {self.name}")
#         for person in self.people:
#             person.describe()

#     def countDoctor(self):
#         count = 0
#         for person in self.people:
#             if isinstance(person, Doctor):
#                 count += 1
#         return count

#     def sortAge(self):
#         self.people.sort(key=lambda person: person.yob)

#     def aveTeacherYearOfBirth(self):
#         total_yob = 0
#         count = 0
#         for person in self.people:
#             if isinstance(person, Teacher):
#                 total_yob += person.yob
#                 count += 1
#         if count > 0:
#             return total_yob / count
#         else:
#             return 0

# # Tạo ward và thêm các đối tượng student, teacher, doctor
# ward = Ward("General Ward")
# ward.addPerson(Student("Alice", 2005, "10th Grade"))
# ward.addPerson(Teacher("Mr. Smith", 1980, "Mathematics"))
# ward.addPerson(Teacher("Ms. Davis", 1982, "Biology"))
# ward.addPerson(Doctor("Dr. Lee", 1975, "Cardiology"))
# ward.addPerson(Doctor("Dr. Patel", 1978, "Neurology"))

# # Gọi phương thức describe để in thông tin mọi người trong ward
# ward.describe()

# # Gọi phương thức countDoctor để đếm số lượng bác sĩ
# print("\nNumber of Doctors in Ward:", ward.countDoctor())

# # Sắp xếp mọi người theo tuổi
# ward.sortAge()
# print("\nAfter sorting by age:")
# ward.describe()

# # Tính trung bình năm sinh của các giáo viên
# print("\nAverage Year of Birth of Teachers:", ward.aveTeacherYearOfBirth())


from datetime import datetime

# Định nghĩa các lớp Person, Student, Teacher, Doctor
class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        pass

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(f"Student: Name={self.name}, Year of Birth={self.yob}, Grade={self.grade}")

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(f"Teacher: Name={self.name}, Year of Birth={self.yob}, Subject={self.subject}")

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(f"Doctor: Name={self.name}, Year of Birth={self.yob}, Specialist={self.specialist}")

# Định nghĩa lớp Ward với các phương thức addPerson, describe, countDoctor, sortAge, aveTeacherYearOfBirth
class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def addPerson(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.people:
            person.describe()

    def countDoctor(self):
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sortAge(self):
        self.people.sort(key=lambda person: person.yob)
        # syntax: (key = lamda arguments:expression)

    def aveTeacherYearOfBirth(self):
        total_yob = 0
        count = 0
        for person in self.people:
            # isintance(object, class)
            if isinstance(person, Teacher):
                total_yob += person.yob
                count += 1
        if count > 0:
            return total_yob / count
        else:
            return 0

# Hàm nhập thông tin từ bàn phím
def nhapThongTinPerson():
    loai_person = input("Nhập loại người (Student/Teacher/Doctor): ").strip().lower()
    name = input("Nhập tên: ")
    yob = int(input("Nhập năm sinh: "))

    if loai_person == "student":
        grade = input("Nhập lớp: ")
        return Student(name, yob, grade)

    elif loai_person == "teacher":
        subject = input("Nhập môn giảng dạy: ")
        return Teacher(name, yob, subject)

    elif loai_person == "doctor":
        specialist = input("Nhập chuyên môn: ")
        return Doctor(name, yob, specialist)

    else:
        print("Loại không hợp lệ, hãy thử lại.")
        return None

# Hàm chính
def main():
    ward_name = input("Nhập tên ward: ")
    ward = Ward(ward_name)

    so_luong_nguoi = int(input("Nhập số lượng người muốn thêm vào ward: "))
    for i in range(so_luong_nguoi):
        print(f"\nNhập thông tin người thứ {i+1}:")
        person = nhapThongTinPerson()
        if person:
            ward.addPerson(person)

    print("\nThông tin mọi người trong ward:")
    ward.describe()

    # Đếm số lượng bác sĩ
    print("\nSố lượng bác sĩ trong ward:", ward.countDoctor())

    # Sắp xếp mọi người theo tuổi
    ward.sortAge()
    print("\nSau khi sắp xếp theo tuổi:")
    ward.describe()

    # Tính trung bình năm sinh của giáo viên
    print("\nTrung bình năm sinh của giáo viên:", ward.aveTeacherYearOfBirth())

if __name__ == "__main__":
    main()

