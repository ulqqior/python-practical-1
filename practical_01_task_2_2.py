import math

def triangle_type(a: float, b: float, c: float) -> str:
    if a + b <= c or a + c <= b or b + c <= a:
        return 'не є трикутником'
    
    if a == b == c:
        return 'рівносторонній'
    elif a == b or b == c or a == c:
        return 'рівнобедрений'
    
    sides = sorted([a, b, c])
    if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9:
        return 'прямокутний'
        
    return 'різносторонній'

def triangle_area(a: float, b: float, c: float) -> float:
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def main():
    try:
        a = float(input("Введіть a: "))
        b = float(input("Введіть b: "))
        c = float(input("Введіть c: "))
        
        t_type = triangle_type(a, b, c)
        print(f"Тип: {t_type}")
        
        if t_type != 'не є трикутником':
            print(f"Площа: {triangle_area(a, b, c):.2f}")
    except ValueError:
        print("Введіть коректні числа.")

if __name__ == "__main__":
    main()