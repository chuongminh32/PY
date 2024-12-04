class Student:
    def __init__(self, cmnd, name, year_of_birth):
        self.cmnd = cmnd
        self.name = name
        self.year_of_birth = year_of_birth
        self.courses = []  # Danh sách các môn học học viên đăng ký

    def add_course(self, course_code, course_name, number_of_hours):
        self.courses.append({
            'course_code': course_code,
            'course_name': course_name,
            'number_of_hours': number_of_hours
        })

    # Định nghĩa hàm __str__ để chuyển đối tượng thành chuỗi dễ đọc
    def __str__(self):
        courses_info = "\n".join([f"   Mã môn: {course['course_code']}, Tên môn: {course['course_name']}, Số tiết: {course['number_of_hours']}" for course in self.courses])
        return f"CMND: {self.cmnd}, Tên: {self.name}, Năm sinh: {self.year_of_birth}\n{courses_info}"

class Center:
    def __init__(self):
        self.students = []  # Danh sách học viên

    def add_student(self, student):
        self.students.append(student)

    def save_to_file(self):
        with open("dssv.txt", "w") as file:
            for student in self.students:
                file.write(str(student) + "\n")

    def show_students(self):
        for student in self.students:
            print(str(student))

    def show_students_with_multiple_courses(self):
        for student in self.students:
            if len(student.courses) >= 2:
                print(str(student))

    def most_popular_course(self):
        course_count = {}
        for student in self.students:
            for course in student.courses:
                course_name = course['course_name']
                if course_name not in course_count:
                    course_count[course_name] = 0
                course_count[course_name] += 1
        most_popular = max(course_count, key=course_count.get)
        print(f"Môn học được nhiều sinh viên đăng ký nhất là: {most_popular}")

    def course_statistics(self):
        course_count = {}
        for student in self.students:
            for course in student.courses:
                course_name = course['course_name']
                if course_name not in course_count:
                    course_count[course_name] = 0
                course_count[course_name] += 1
        for course_name, count in course_count.items():
            print(f"Môn {course_name}: {count} học viên đăng ký")

# Hàm hiển thị menu và xử lý lựa chọn của người dùng
def show_menu():
    print("\n----- MENU -----")
    print("1. Thêm học viên mới")
    print("2. Hiển thị thông tin các học viên")
    print("3. Hiển thị học viên đăng ký ít nhất hai môn học")
    print("4. Hiển thị môn học được nhiều sinh viên đăng ký nhất")
    print("5. Thống kê số lượng học viên trên mỗi môn học")
    print("6. Lưu thông tin học viên vào tập tin")
    print("0. Thoát")
    choice = input("Chọn chức năng (0-6): ")
    return choice

def main():
    center = Center()

    while True:
        choice = show_menu()

        if choice == "1":
            cmnd = input("Nhập CMND học viên: ")
            name = input("Nhập tên học viên: ")
            year_of_birth = int(input("Nhập năm sinh học viên: "))
            student = Student(cmnd, name, year_of_birth)
            
            while True:
                course_code = input("Nhập mã môn học (hoặc nhập 'stop' để dừng): ")
                if course_code.lower() == "stop":
                    break
                course_name = input("Nhập tên môn học: ")
                number_of_hours = int(input("Nhập số tiết môn học: "))
                student.add_course(course_code, course_name, number_of_hours)

            center.add_student(student)
            print(f"Học viên {name} đã được thêm vào trung tâm.")

        elif choice == "2":
            print("\nThông tin các học viên đã đăng ký:")
            center.show_students()

        elif choice == "3":
            print("\nHọc viên đăng ký ít nhất hai môn học:")
            center.show_students_with_multiple_courses()

        elif choice == "4":
            print("\nMôn học được nhiều sinh viên đăng ký nhất:")
            center.most_popular_course()

        elif choice == "5":
            print("\nThống kê số lượng học viên trên mỗi môn học:")
            center.course_statistics()

        elif choice == "6":
            center.save_to_file()
            print("Thông tin học viên đã được lưu vào dssv.txt.")

        elif choice == "0":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
