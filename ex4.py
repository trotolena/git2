def add():
    return x + y


def subtract():
    return x - y


def multiply():
    return x * y


def divide():
    return x / y


def exponentiation():
    return x ** y


def square_root():
    return x ** 0.5, y ** 0.5


def triple_root():
    return x ** 1/3, y ** 1/3


x = eval(input('\nВведіть перше число: ->'))
y = eval(input('\nВведіть друге число: ->'))

print('Виберіть дію у кулькуляторі')
print('\n1 - Додавання '
      '\n2 - Віднімання '
      '\n3 - Множення '
      '\n4 - Ділення '
      '\n5 - Степінь числа(друге число - степінь) '
      '\n6 - Квадратний корінь числа '
      '\n7 - Кубічний корінь числа'
      '\n8 - Завершити')

while True:
    choice = int(input('Виберіть дію з 1/2/3/4/5/6/7/8-->'))
    if choice in (1, 2, 3, 4, 5, 6, 7, 8):
        if choice == 1:
            print("Сума  чисел", x, y, '=', add())
        elif choice == 2:
            print("Результат віднімання чисел", x, y, '=', subtract())
        elif choice == 3:
            print("Добуток двох чисел", x, y, '=', multiply())
        elif choice == 4:
            if y > 0:
                print("Остача ділення чисел", x, y, '=', divide())
            else:
                print("Ділити на 0 не можна")
        elif choice == 5:
            print("Піднесення першого числа ", x, "у ступінь другого числа", y, '=', exponentiation())
        elif choice == 6:
            print("Квадратний корінь першого числа ", x, "і другого числа ", y, '=', square_root())
        elif choice == 7:
            print("Кубічний корінь першого числа ", x, "і другого числа ", y, '=', triple_root())
        elif choice == 8:
            print("Операції закінчено")
            exit()
        else:
            print('Невірний вибір, спробуй ще раз')

