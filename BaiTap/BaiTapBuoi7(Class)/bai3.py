class Math:
    # *nso : tuple()
    def __init__(self, *nso):
        self.numbers = nso  # Lưu các số vào thuộc tính numbers

    # Hàm tính tổng n số
    def TinhTong(self):
        return sum(self.numbers)

    # Hàm tính trung bình cộng của n số
    def TinhTrungBinh(self):
        if len(self.numbers) == 0:
            return 0
        return self.TinhTong() / len(self.numbers)

    # Hàm tìm số lớn nhất của n số
    def TimMax(self):
        if len(self.numbers) == 0:
            return None
        return max(self.numbers)

    # Hàm tìm số nhỏ nhất của n số
    def TimMin(self):
        if len(self.numbers) == 0:
            return None
        return min(self.numbers)

    #show 
    def showInfo(self):
        print("Danh sach cac so: ", self.numbers)
        print(f"Tong: {self.TinhTong()}")
        print(f"Trung Binh: {self.TinhTrungBinh()}")
        print(f"Max: {self.TimMax()}")
        print(f"Min: {self.TimMin()}")

math = Math(1,2,3,4,5)
(math.showInfo())
