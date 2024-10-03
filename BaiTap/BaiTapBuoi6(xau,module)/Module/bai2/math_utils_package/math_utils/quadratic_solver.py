# math_utils/quadratic_solver.py
import cmath

def solve_quadratic(a, b, c):
    """
    Tìm nghiệm của phương trình bậc 2: ax^2 + bx + c = 0.
    
    :param a: Hệ số a
    :param b: Hệ số b
    :param c: Hệ số c
    :return: Tuple chứa hai nghiệm
    """
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    return root1, root2
