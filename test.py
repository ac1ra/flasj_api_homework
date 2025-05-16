def checkword(first, second):

    return f"The sum of {first} and {second} is {int(first)+int(second)}"


if "__main__" == __name__:

    try:
        a = int(input('Введите первое число для суммы:'))
        b = int(input('Введите второе число для суммы:'))
        print(checkword(a, b))
    except ValueError:
        print("Error. You entered the wrong value")
