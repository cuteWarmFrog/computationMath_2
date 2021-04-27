from GraphicDrawer import drawGraphic
import numpy as np
from InputHandler import *
from src.Methods import Bisection, SimpleIterrations, SimpleIterationsSystem

greet()
while 1:
    command = choice()

    if command == '1':
        drawGraphic(lambda x: np.exp(x) - 5 * x)
        left, right = getAAndB()
        accuracy = getAccuracy()
        answer1, iterations1 = Bisection.solve(left, right, accuracy, lambda x: np.exp(x) - 5 * x)
        answer2, iterations2 = SimpleIterrations.solve(left, right, accuracy, lambda x: np.exp(x) - 5 * x,
                                                       lambda x: np.exp(x) - 5)
        print(f'Ответ (половинное деление): {answer1}')
        print(f'итераций: {iterations1}')
        print(f'Ответ (простых итераций): {answer2}')
        print(f'итераций: {iterations2}')

    elif command == '2':
        drawGraphic(lambda x: -6 * x ** 2 - x + 4)
        left, right = getAAndB()
        accuracy = getAccuracy()
        answer = Bisection.solve(left, right, accuracy, lambda x: -6 * x ** 2 - x + 4)
        print(f'Ответ: {answer}')

    elif command == '3':
        drawGraphic(lambda x: np.sqrt(3 - 3*np.cos(x)), lambda x: np.sqrt(2 * (4 - x)))
        left, right = getAAndB()
        accuracy = getAccuracy()
        answerX, answerY, iterations = SimpleIterationsSystem.solve(left, right, accuracy,
                                                                    lambda x: np.sqrt(3 - 3*np.cos(x)),
                                                                    lambda x: np.sqrt(2 * (4 - x)))
        print(answerX, answerY, iterations)

    elif command == '4':
        print('*Программа завершена*')
        break
    else:
        print('введён какой-то кринж')