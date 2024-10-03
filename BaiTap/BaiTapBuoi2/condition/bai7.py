# import math

# def day_of_week(year) :
#     day = ((year + math.floor((year - 1) / 4) - math.floor((year - 1) / 100) + math.floor((year - 1) / 400)) % 7)
#     days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     return days[day]


# def main() :
#     try:
#         year = int(input())
#         day = day_of_week(year)
#         print  (f"ngay 1 thang 1 nam {year} la {day}")
#     except ValueError:
#          print("Vui long nhap lai")

# if __name__ == "__main__" :
#     main()
