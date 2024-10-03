# random_array.py
import random

def generate_random_array(n, min_value, max_value):
    """
    Tạo mảng ngẫu nhiên có n phần tử nằm trong khoảng [min_value, max_value].
    
    :param n: Số lượng phần tử của mảng
    :param min_value: Giá trị tối thiểu
    :param max_value: Giá trị tối đa
    :return: Mảng số ngẫu nhiên
    """
    return [random.randint(min_value, max_value) for _ in range(n)]
