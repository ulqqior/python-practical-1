import math

def main():
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))

    sum_squares = a**2 + b**2 + c**2
    
    average = (a + b + c) / 3
    
    discriminant = b**2 - 4*a*c
    
    hypotenuse = math.sqrt(a**2 + b**2)
    
    is_triangle = (a + b > c) and (a + c > b) and (b + c > a)

    print(f"Сума квадратів: {sum_squares:.2f}")
    print(f"Середнє арифметичне: {average:.2f}")
    print(f"Дискримінант: {discriminant:.2f}")
    print(f"Гіпотенуза (катети a, b): {hypotenuse:.2f}")
    print(f"Чи утворюють трикутник: {is_triangle}")

if __name__ == "__main__":
    main()