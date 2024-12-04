from abc import ABC, abstractmethod


class Common(ABC):
    def __init__(self, id="", d=0, r=0):
        self.id = id
        self.d = d
        self.r = r

    def __str__(self):
        return f"Mã số: {self.id}, Chiều dài: {self.d}, Chiều rộng: {self.r}"

    def nhap(self):
        self.id = input("Nhập ID: ")
        self.d = int(input("Nhập chiều dài: "))
        self.r = int(input("Nhập chiều rộng: "))

    @abstractmethod
    def cal(self):
        pass

    def dienTich(self):
        return self.d * self.r


class DatTrong(Common):
    def cal(self):
        return self.d * self.r * 30000000


class BietThu(Common):
    def phiKinhDoanh(self):
        return self.r * 5000

    def cal(self):
        return self.d * self.r * 100000000


class NhaO(Common):
    def __init__(self, id="", d=0, r=0, soLau=0):
        super().__init__(id, d, r)
        self.soLau = soLau

    def cal(self):
        return self.d * self.r * 60000000 + self.soLau * 100000000

class KhachSan(Common):
    def __init__(self, id="", d=0, r=0, soSao=0):
        super().__init__(id, d, r)
        self.soSao = soSao

    def cal(self):
        return self.d * self.r * 70000000 + self.soSao * 50000000

    def phiKinhDoanh(self):
        return self.r * 10000

class MainClass:
    def __init__(self):
        self.dsBds = []

    def add(self, bds):
        self.dsBds.append(bds)

    def i(self):
        for bds in self.dsBds:
            print(bds)

    def soLuongBdsTheoTungLoai(self):
        cnt_nhaO = 0
        cnt_bietThu = 0
        cnt_khachSan = 0
        cnt_datTrong = 0

        for bds in self.dsBds:
            if isinstance(bds, NhaO):
                cnt_nhaO += 1
            elif isinstance(bds, BietThu):
                cnt_bietThu += 1
            elif isinstance(bds, KhachSan):
                cnt_khachSan += 1
            elif isinstance(bds, DatTrong):
                cnt_datTrong += 1

        print(f"Có {cnt_bietThu} biệt thự, {cnt_nhaO} nhà ở, {cnt_khachSan} khách sạn, {cnt_datTrong} đất trống.")

    def dsBdsCoDienTichTren1000(self):
        result = [bds for bds in self.dsBds if bds.dienTich() > 1000]
        for bds in result:
            print(bds)

    def tongPhiKinhDoanh(self):
        phi = 0
        for bds in self.dsBds:
            if isinstance(bds, BietThu) or isinstance(bds, KhachSan):
                phi += bds.phiKinhDoanh()
        return phi

def inputBds():
    typeBds = input("Nhập loại bất động sản (nhao, biethu, khachsan, dattrong): ").lower()
    id = input("Nhap id: ")
    d = int(input("Nhap chieu dai: "))
    r = int(input("Nhap chieu rong: "))
    if typeBds == "dattrong":
        return DatTrong(id, d, r)
    elif typeBds == "bietthu":
        return BietThu(id, d, r)
    elif typeBds == "nhao":
        soLau = int(input("Nhap so lau: "))
        return NhaO(id, d, r, soLau)
    elif typeBds == "khachsan":
        soSao = int(input("Nhap so sao: "))
        return KhachSan(id,d,r,soSao)
    else: 
        return None


def main():
    dsBds = MainClass()
    n = int(input("Nhập số lượng bất động sản: "))

    for i in range(n):
        print(f"Nhập thông tin cho bất động sản thứ {i + 1}: ")
        dsBds.add(inputBds())

    print("\nDanh sách bất động sản:")
    dsBds.i()

    print("\nThống kê số lượng bất động sản:")
    dsBds.soLuongBdsTheoTungLoai()

    print("\nDanh sách bất động sản có diện tích trên 1000m²:")
    dsBds.dsBdsCoDienTichTren1000()

    print("\nTổng phí kinh doanh:")
    print(f"{dsBds.tongPhiKinhDoanh():,.0f} VND")


if __name__ == "__main__":
    main()
