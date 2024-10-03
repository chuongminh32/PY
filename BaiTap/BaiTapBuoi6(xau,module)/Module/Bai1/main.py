# main.py

from student_manager import add_student, remove_student, modify_student, show_list_student

def main():
    while True:
        print("\nChọn chức năng:")
        print("1: Thêm sinh viên")
        print("2: Xóa sinh viên")
        print("3: Sửa sinh viên")
        print("4: Xem danh sách sinh viên")
        print("0: Thoát")
        choice = input("Nhập lựa chọn của bạn: ")
        print()

        if choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            modify_student()
        elif choice == '4':
            show_list_student()
        elif choice == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
