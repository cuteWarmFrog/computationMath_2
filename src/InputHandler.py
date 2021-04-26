def greet():
    print('Привет, чувствуй себя как дома, но не забыай, что ты в гостях!\n')


def choice():
    print('Доступные уравнения и системы:\n' +
          '1. e^x - 5x = 0 (деление пополам)\n' +
          '   e^x - 5x = 0 (метод простой итераций)\n\n' +
          '2. x^3 - x + 4 = 0 (деление пополам)\n' +
          '   x^3 - x + 4 = 0 (метод простой итерации)\n' +
          '     \n' +
          '3. система    0.1*x^2 + x + 0.2*y^2 - 0.3 = 0\n' +
          '   уравнений  0.2*x^2 + y - 0.1xy - 0.7 = 0 (метод простой итерации)\n' +
          '\n' +
          '4. Выход\n')
    command = input('Введите номер команды: ')
    return command


def getAAndB():
    print('Введите [а, b]')
    a = float(input('a = '))
    b = float(input('b = '))
    return a, b


def getAccuracy():
    accuracy = float(input('Введите точность: '))
    return accuracy


