#trapesium rule
from math import *

while True:

    formula = input("Formula: ")
    iterations = int(input("Iterations: "))
    upper = float(input("Upper: "))
    lower = float(input("Lower: "))

    h = (upper - lower)/iterations
    print('h =',h)
    values = []
    x = lower
    y = 0
    print("")
    for i in range(iterations+1):
        exec(formula)
        values.append(y)
        print(x,': ',y)
        if x == upper:
            break
        x += h
    print("")
    answer = 0.5*h*(values.pop(0) + values.pop(len(values)-1) + 2 * (sum(values)))
    print(answer)
    z = input()
