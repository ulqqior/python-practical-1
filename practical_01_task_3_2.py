def calculator():
    print("Калькулятор")
    print("Введіть вираз у форматі: число оператор число")
    print("Введіть 'quit' для виходу, 'history' для історії")
    
    history = []
    
    while True:
        user_input = input("\n> ").strip()
        
        if user_input.lower() == 'quit':
            break
        if user_input.lower() == 'history':
            for item in history:
                print(item)
            continue
            
        parts = user_input.split()
        if len(parts) != 3:
            print("Помилка формату. Спробуйте: 2 + 2")
            continue
            
        try:
            num1 = float(parts[0])
            op = parts[1]
            num2 = float(parts[2])
        except ValueError:
            print("Помилка: операнди мають бути числами")
            continue
            
        if op == '+': res = num1 + num2
        elif op == '-': res = num1 - num2
        elif op == '*': res = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Помилка: ділення на нуль")
                continue
            res = num1 / num2
        elif op == '//':
            if num2 == 0:
                print("Помилка: ділення на нуль")
                continue
            res = num1 // num2
        elif op == '%':
            if num2 == 0:
                print("Помилка: ділення на нуль")
                continue
            res = num1 % num2
        elif op == '**': res = num1 ** num2
        else:
            print("Невідомий оператор")
            continue
            
        expr = f"{num1} {op} {num2} = {res}"
        print(expr)
        history.append(expr)

if __name__ == "__main__":
    calculator()