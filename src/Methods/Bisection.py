def solve(left, right, accuracy, func):
    x = (right + left) / 2
    print("Left Right x  func(x) right-left")
    print(f'{left} {right} {x} {func(x)} {right - left}')

    iterations = 0
    while right - left > accuracy and abs(func(x)) > accuracy:
        iterations += 1
        if func(left) * func(x) < 0: right = x
        else: left = x
        x = (right + left) / 2
        print(f'{left} {right} {x} {func(x)} {right - left}')

    return x, iterations

# todo format output
