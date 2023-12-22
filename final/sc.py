import cmath

def solve_cubic(a, b, c, d):
    # Конвертация коэффициентов в комплексные числа
    a, b, c, d = map(complex, (a, b, c, d))

    # Проверка на нулевой старший коэффициент
    if a == 0:
        raise ValueError("The coefficient 'a' must not be 0 for a cubic equation.")

    # Приведение уравнения к виду x^3 + px + q = 0
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)

    # Вычисление корней через формулу Кардано
    roots = []
    for k in range(3):
        omega_k = cmath.exp(2j * cmath.pi * k / 3)
        term = ((-q/2) + cmath.sqrt((q/2)**2 + (p/3)**3))**(1/3)
        root = omega_k * term - p/(3*omega_k*term) - b/(3*a)
        roots.append(root)

    return roots

# Пример использования
a, b, c, d = 1, -6, 11, -6
print("Roots of the cubic equation are:", solve_cubic(a, b, c, d))
