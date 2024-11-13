import numpy as np 
def solve():
    arr = np.random.randint(1, 101, size = (2,7))
    # ngay ban duoc nhieu hang nhat 
    print(arr)
    max_day_price = 0
    day_a = 0
    for i in range(7):
        sum = 0
        for j in range(2):
            sum += arr[j][i]
        if sum > max_day_price:
            max_day_price = sum 
            day_a = i
    print(f"Ngay {day_a + 1} ban duoc hang nhieu nhat tuan")
    
    # thoi diem ban duoc nhieu hang nhat
    max_b = 0
    time_b = ""
    day_b = 0
    for i in range(2):
        for j in range(7):
            if arr[i][j] > max_b:
                max_b = arr[i][j]
                day_b = j+1
                time_b = "Sang" if i == 0 else "Chieu"
    
    print(f"Ngay {day_b}, buoi {time_b} ban duoc nhieu hang nhat.")

    # buoi nao ban duoc nhieu hang nhat
    max_c = 0
    time_c = ""
    for i in range(2):
        sum_c = 0
        for j in range(7):
            sum_c += arr[i][j] 
        
        if sum_c > max_c :
            max_c = sum_c
            time_c = "Sang" if i == 0 else "Chieu"
        
    print(f"Buoi {time_c} ban duoc nhieu hang hon.")


if __name__ == "__main__":
    solve()
        