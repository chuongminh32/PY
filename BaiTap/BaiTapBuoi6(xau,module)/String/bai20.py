def count_characters(s):
    digit_count = 0   # Đếm ký tự số
    upper_count = 0   # Đếm ký tự in hoa
    lower_count = 0   # Đếm ký tự thường
    special_count = 0 # Đếm ký tự đặc biệt

    for char in s:
        if char.isdigit():  # Kiểm tra ký tự số
            digit_count += 1
        elif char.isupper():  # Kiểm tra ký tự in hoa
            upper_count += 1
        elif char.islower():  # Kiểm tra ký tự thường
            lower_count += 1
        else:  # Nếu không thuộc các loại trên, là ký tự đặc biệt
            special_count += 1

    return digit_count, upper_count, lower_count, special_count

# Test chương trình
input_str = input("Nhập vào một chuỗi: ")
digits, uppers, lowers, specials = count_characters(input_str)

print(f"Số lượng ký tự số: {digits}")
print(f"Số lượng ký tự in hoa: {uppers}")
print(f"Số lượng ký tự thường: {lowers}")
print(f"Số lượng ký tự đặc biệt: {specials}")
