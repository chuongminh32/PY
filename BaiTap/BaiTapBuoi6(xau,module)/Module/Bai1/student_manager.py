# student_manager.py

STUDENTS_LIST = []

def add_student():
    print("Nhập thông tin cho sinh viên mới!\n")
    name = input("Nhập tên sinh viên: ")
    id = input("Nhập mã số sinh viên: ")
    gpa = float(input("Nhập GPA: "))
    stu = {
        'Name': name,
        'ID': id,
        'GPA': gpa
    }
    STUDENTS_LIST.append(stu)
    print(f"Đã thêm sinh viên: {stu}")

def remove_student():
    id = input("Nhập ID sinh viên muốn xóa: ")
    is_found = False
    for stu in STUDENTS_LIST:
        if stu['ID'] == id:
            STUDENTS_LIST.remove(stu)
            is_found = True
            print(f"Đã xóa thành công sinh viên có ID: {id}")
            break
            
    if not is_found:
        print(f"Không tìm thấy sinh viên có ID: {id}")

def modify_student():
    id = input("Nhập ID sinh viên muốn sửa: ")
    is_found = False
    modify_stu = {}

    for stu in STUDENTS_LIST:
        if stu['ID'] == id:
            modify_stu = stu 
            is_found = True 
            break

    if is_found:
        while True:
            print("Nhập thuộc tính cần sửa [1-3]:")
            print("1. Tên")
            print("2. GPA")
            print("3. Thoát")
            choose = input()

            if choose == '1':
                new_name = input("Nhập tên mới: ")
                modify_stu['Name'] = new_name
                print("Đã sửa tên!\n")
            elif choose == '2':
                new_gpa = float(input("Nhập GPA mới: "))
                modify_stu['GPA'] = new_gpa
                print("Đã sửa GPA!\n")
            elif choose == '3':
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập 1, 2 hoặc 3!")

        print("Đã sửa thành công!")
    else: 
        print(f"Không tìm thấy sinh viên có ID: {id}")

def show_list_student():
    if not STUDENTS_LIST:
        print("Danh sách sinh viên trống.")
        return
    print("DANH SÁCH SINH VIÊN\n")
    for stu in STUDENTS_LIST:
        print(f"Mã sinh viên: {stu['ID']}, Tên sinh viên: {stu['Name']}, GPA: {stu['GPA']}\n")
