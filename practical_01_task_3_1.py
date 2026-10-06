def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def harmonic_sum(n: int) -> float:
    h_sum = 0.0
    for i in range(1, n + 1):
        h_sum += 1 / i
    return h_sum

def multiplication_table(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:<4}", end="")
        print()

def main():
    try:
        n = int(input("Введіть число n: "))
        if n <= 0:
            print("Число має бути додатним.")
            return
            
        print(f"{n}! = {factorial(n)}")
        print(f"Гармонічна сума H({n}) = {harmonic_sum(n):.6f}")
        print(f"\nТаблиця множення {n}x{n}:")
        multiplication_table(n)
    except ValueError:
         print("Введіть ціле число.")

if __name__ == "__main__":
    main()