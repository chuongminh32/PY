import json  # Thư viện json dùng để xử lý dữ liệu theo định dạng JSON

# Lớp Student chứa thông tin học viên
class Student:
    # Phương thức khởi tạo lớp Student với các thuộc tính: mã số, họ tên, năm sinh, và danh sách môn học
    def __init__(self, id_number, name, birth_year, subjects):
        self.id_number = id_number  # CMND, căn cước, mã số giấy khai sinh
        self.name = name  # Họ tên
        self.birth_year = birth_year  # Năm sinh
        self.subjects = subjects  # Danh sách môn học (mã môn, tên môn, số tiết)

    # Hàm hiển thị thông tin học viên
    def display_info(self):
        # Hiển thị các thông tin cơ bản của học viên
        print(f"CMND/CCCD/MSGS: {self.id_number}")
        print(f"Họ tên: {self.name}")
        print(f"Năm sinh: {self.birth_year}")
        print("Danh sách các môn học:")
        
        # Duyệt qua danh sách các môn học và hiển thị thông tin từng môn
        for subject in self.subjects:
            print(f"  Mã môn: {subject['subject_code']}, Tên môn: {subject['subject_name']}, Số tiết: {subject['hours']}")
        print()

# Hàm nhập thông tin học viên từ người dùng và lưu vào tập tin dssv.txt
def add_student():
    # Nhập thông tin cá nhân của học viên
    id_number = input("Nhập CMND/CCCD/MSGS: ")
    name = input("Nhập họ tên học viên: ")
    birth_year = input("Nhập năm sinh học viên: ")
    subjects = []  # Khởi tạo danh sách các môn học của học viên

    # Vòng lặp để nhập nhiều môn học cho học viên
    while True:
        # Nhập thông tin từng môn học
        subject_code = input("Nhập mã môn học: ")
        subject_name = input("Nhập tên môn học: ")
        hours = int(input("Nhập số tiết: "))
        
        # Thêm thông tin môn học vào danh sách
        subjects.append({
            'subject_code': subject_code,
            'subject_name': subject_name,
            'hours': hours
        })
        
        # Hỏi người dùng có muốn thêm môn học khác không
        another = input("Bạn có muốn thêm môn khác? (y/n): ")
        if another.lower() != 'y':  # Thoát khỏi vòng lặp nếu không thêm môn nữa
            break

    # Tạo đối tượng học viên với thông tin đã nhập
    student = Student(id_number, name, birth_year, subjects)
    # Lưu thông tin học viên vào tập tin
    save_student(student)

# Hàm lưu thông tin học viên vào tập tin dssv.txt
def save_student(student):
    try:
        # Mở tập tin dssv.txt để đọc danh sách học viên hiện có
        with open("dssv.txt", "r") as file:
            students = json.load(file)  # Đọc dữ liệu JSON từ file và chuyển thành danh sách
    except FileNotFoundError:
        students = []  # Nếu file không tồn tại, khởi tạo danh sách trống

    # Thêm thông tin học viên mới vào danh sách
    student_data = {
        'id_number': student.id_number,
        'name': student.name,
        'birth_year': student.birth_year,
        'subjects': student.subjects
    }
    students.append(student_data)

    # Ghi lại danh sách học viên vào file dưới dạng JSON
    with open("dssv.txt", "w") as file:
        json.dump(students, file)

# Hàm hiển thị tất cả học viên từ tập tin dssv.txt
def display_all_students():
    try:
        # Mở tập tin và đọc danh sách học viên
        with open("dssv.txt", "r") as file:
            students = json.load(file)  # Chuyển dữ liệu JSON thành danh sách
            # Hiển thị thông tin từng học viên
            for student in students:
                std = Student(student['id_number'], student['name'], student['birth_year'], student['subjects'])
                std.display_info()
    except FileNotFoundError:
        print("Chưa có học viên nào được đăng ký.")  # Thông báo khi không có học viên nào

# Hàm hiển thị các học viên đã đăng ký ít nhất hai môn học
def display_students_with_two_subjects():
    try:
        # Đọc dữ liệu từ tập tin
        with open("dssv.txt", "r") as file:
            students = json.load(file)
            # Duyệt qua từng học viên và kiểm tra điều kiện
            for student in students:
                if len(student['subjects']) >= 2:  # Chỉ hiển thị học viên có ít nhất 2 môn
                    std = Student(student['id_number'], student['name'], student['birth_year'], student['subjects'])
                    std.display_info()
    except FileNotFoundError:
        print("Chưa có học viên nào được đăng ký.")  # Thông báo nếu file không tồn tại

# Hàm hiển thị môn học được nhiều học viên đăng ký nhất
def display_most_registered_subject():
    try:
        # Đọc dữ liệu từ tập tin
        with open("dssv.txt", "r") as file:
            students = json.load(file)
            subject_count = {}  # Khởi tạo dictionary để đếm số lượng học viên đăng ký từng môn
            
            # Duyệt qua danh sách học viên và đếm số lượng đăng ký mỗi môn
            for student in students:
                for subject in student['subjects']:
                    if subject['subject_code'] in subject_count:
                        # key = ma mon hoc subject['subject_code'] , tang 
                        subject_count[subject['subject_code']]['count'] += 1
                    else:
                        subject_count[subject['subject_code']] = {
                            'name': subject['subject_name'],
                            'count': 1
                        }

            # Tìm môn học có số lượng đăng ký lớn nhất
            max_registered = max(subject_count.values(), key=lambda x: x['count'])
            print(f"Môn học được nhiều sinh viên đăng ký nhất: {max_registered['name']} với {max_registered['count']} học viên.")
    except FileNotFoundError:
        print("Chưa có học viên nào được đăng ký.")  # Thông báo nếu file không tồn tại

# Hàm thống kê số lượng học viên trên mỗi môn học
def count_students_per_subject():
    try:
        # Đọc dữ liệu từ tập tin
        with open("dssv.txt", "r") as file:
            students = json.load(file)
            subject_count = {}  # Khởi tạo dictionary để đếm số lượng học viên đăng ký từng môn
            
            # Duyệt qua danh sách học viên và đếm số lượng đăng ký mỗi môn
            for student in students:
                for subject in student['subjects']:
                    if subject['subject_code'] in subject_count:
                        subject_count[subject['subject_code']]['count'] += 1
                    else:
                        subject_count[subject['subject_code']] = {
                            'name': subject['subject_name'],
                            'count': 1
                        }

            # Hiển thị số lượng học viên trên mỗi môn học
            print("Số lượng học viên trên mỗi môn học:")
            for subject_code, info in subject_count.items():
                print(f"Mã môn: {subject_code}, Tên môn: {info['name']}, Số học viên: {info['count']}")
    except FileNotFoundError:
        print("Chưa có học viên nào được đăng ký.")  # Thông báo nếu file không tồn tại

# Chương trình chính - giao diện điều khiển chính của chương trình
def main():
    while True:
        # Hiển thị menu lựa chọn cho người dùng
        print("\n=== Quản lý học viên trung tâm AI ===")
        print("1. Nhập thông tin học viên")
        print("2. Hiển thị thông tin tất cả học viên")
        print("3. Hiển thị học viên đăng ký ít nhất hai môn")
        print("4. Hiển thị môn học được nhiều học viên đăng ký nhất")
        print("5. Thống kê số lượng học viên trên mỗi môn học")
        print("6. Thoát")
        
        # Nhận lựa chọn của người dùng
        choice = input("Lựa chọn của bạn: ")

        # Thực hiện chức năng tương ứng với lựa chọn của người dùng
        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            display_students_with_two_subjects()
        elif choice == "4":
            display_most_registered_subject()
        elif choice == "5":
            count_students_per_subject()
        elif choice == "6":
            print("Chương trình kết thúc.")  # Thông báo khi thoát chương trình
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")  # Thông báo khi người dùng nhập sai

# Điểm bắt đầu của chương trình
if __name__ == "__main__":
    main()  # Gọi hàm main để chạy chương trình
