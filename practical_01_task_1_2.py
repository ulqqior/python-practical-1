def main():
    raw_input = input("Введіть число: ")
    try:
        num_int = int(raw_input)
        num_float = float(raw_input)
        num_bool = bool(num_int)
        
        print(f"int: {num_int}, type: {type(num_int)}")
        print(f"float: {num_float}, type: {type(num_float)}")
        print(f"bool: {num_bool}, type: {type(num_bool)}")
        print(f"Is float? {isinstance(num_float, float)}")
    except ValueError:
        print("Помилка: введене значення — не число")

    name = input("Введіть ім'я: ")
    age = input("Введіть вік: ")
    print(f"Користувач: {name:>15} | Вік: {age:0>3} років")

    my_list = list(range(1, 6))
    print(f"Список з range(): {my_list}")
    print(f"Довжина (len): {len(my_list)}")
    print(f"ID об'єкта (id): {id(my_list)}")

if __name__ == "__main__":
    main()