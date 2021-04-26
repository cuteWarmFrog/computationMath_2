def solve(left, right, accuracy, func, derivative):
    x0 = 0
    if derivative(left) > derivative(right):
        x0 = left
    else:
        x0 = right

    lambd = -1 / derivative(x0)

    x = lambd * func(x0)

    iterations = 0
    print('iterations x0 xi func(xi) xi-x0')
    while abs(func(x)) > accuracy and abs(x - x0) > accuracy:
        iterations += 1
        x0 = x
        x = x0 + lambd * func(x0)
        print(f'{iterations} {x0} {x} {func(x)} {x - x0}')

    return x, iterations
