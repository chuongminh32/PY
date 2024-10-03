
s = input("Nhap chuoi s: ")
result = ""

for i in range(0, len(s)):
    tmp = ""
    for j in range(i, len(s)):
        if s[j] not in tmp:
            tmp += s[j] 
        else :
            break
    if len(tmp) > len(result):
            result = tmp 

print(result)
