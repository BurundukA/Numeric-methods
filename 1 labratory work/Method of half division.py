import random
import sys
import math
e = 0.01
def f(x):
    #First example (it was given for tests)
    #func = (x-2)*(x-3)**2*(x-7)
    #Second example
    #func = 1/x - 2
    #Third example
    func = math.log(x)-1
    return func

#Here can be a problem ecaouse of function's domain
def start_approax():
    min_value = -1000
    max_value = 1000
    x_left_first = random.randint(min_value, max_value)
    x_right_first = random.randint(min_value, max_value)
    while((f(x_left_first)*f(x_right_first)) >0 and x_left_first>x_right_first):
        x_left_first = random.randint(min_value, max_value)
        x_right_first = random.randint(min_value, max_value)
    return x_left_first,  x_right_first
def dih(x_left, x_right, e, max_iter = 1000):
    iter = 0
    x_middle = 0
    while (abs(x_right-x_left)>e and iter < max_iter):
        if(abs(x_right-x_left)<e):
            return x_right-x_left
        iter+=1
        x_middle = (x_left+x_right)/2
        if (f(x_left)*f(x_middle) < 0):
            x_right = x_middle
        elif (f(x_middle)*f(x_right)<0):
            x_left = x_middle
        else:
            return x_middle
    if (iter == max_iter):
        print("Iteration limit is exceeded:")
        return x_middle
    else:
        return x_middle

#x_left, x_right = start_approax()
print("Start interval:")
print(1, 5)
print("Root:")
print((dih(1, 5, e, 1000)))
