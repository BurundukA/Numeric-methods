import Theorems_about_roots as rt
import math
from sympy import diff, symbols, cos, sin, exp
from scipy.misc import derivative
import numexpr as ne
import random

def f(f, xl):
    x = xl
    g = ne.evaluate(f)
    return g

def derivative(fx):
    x, y = symbols('x y')
    fxp = diff(fx)
    return fxp

def initial_approximation(index, fx):
    if len(index) > 0:
        r, R = rt.theorem_3(index)
        x0 = random.randint(int(r), int(R))
    else:
        x0 = random.randint(-100, 100)
    if (f(fx, x0)*(f(str(der[1]), x0))<=0):
        if len(index) > 0:
            r, R = rt.theorem_3(index)
            x0 = random.randint(int(r), int(R))
        else:
            x0 = random.randint(-100, 100)
    return x0

def Newton(x0, eps, iter, der):
    xk =x0
    xk1 = xk - (f(fx, xk)/f(str(der[0]), xk))
    kol =1
    while (abs(xk1-xk) > eps):
        if(kol > iter):
            print("Too many iterations")
            break
        else:
            xk = xk1
            xk1 = xk - (f(fx, xk) / f(str(der[0]), xk))
            kol+=1
    return xk1

def simpleNewron(x0, eps, iter, der):
    xk = x0
    xk1 = xk - (f(fx, xk) / f(str(der[0]), x0))
    kol = 1
    while (abs(xk1 - xk) > eps):
        if (kol > iter):
            print("Too many iterations")
            break
        else:
            xk = xk1
            xk1 = xk - (f(fx, xk) / f(str(der[0]), x0))
            kol += 1
    return xk1

def Newton_Broyden(x0, eps, iter, der):
    ck = 1
    xk = x0
    xk1 = xk - ck*(f(fx, xk) / f(str(der[0]), x0))
    kol = 1
    while (abs(xk1 - xk) > eps):
        if (kol > iter):
            print("Too many iterations")
            break
        else:
            while (abs(fx, xk1)>=abs(fx, xk)):
                ck = random.randint(-100, 100)
            xk = xk1
            xk1 = xk - ck*(f(fx, xk) / f(str(der[0]), xk))
            kol += 1
    return xk1

def Secant(x0, eps, sigma, iter, der):
    fpxkm0 = (f(fx, x0)-f(fx, (x0-sigma)))/sigma
    xk0 = x0
    xk = x0 - (f(fx, x0))/(f(fx, x0))*x0
    xk1 = xk - (f(fx, xk))/(f(fx, xk)-f(fx, xk0))*(xk-xk0)
    kol = 1
    while (abs(xk1 - xk) > eps):
        if (kol > iter):
            print("Too many iterations")
            break
        else:
            xk0 = xk
            xk = xk1
            xk1 = xk - (f(fx, xk))/(f(fx, xk)-f(fx, xk0))*(xk-xk0)
            kol += 1
    return xk1

print("Newton method:")
index = []
der = []
eps = 0.001
iter =100
fx = "x**2 - exp(-x)"
der.append(derivative(fx))
der.append(derivative(der[0]))
x0 = initial_approximation(index, fx)
#example for Newton
xka = Newton(1, eps, iter, der)
print(xka)
#random x0 for Newton
print(Newton(x0, eps, iter, der))


#example for simpleNewron
print("Simple Newton method:")
index = [1, -1, 0, 1]
der = []
eps = 0.001
iter =100
fx = "x**3 - x+1"
der.append(derivative(fx))
der.append(derivative(der[0]))
x0 = initial_approximation(index, fx)
xka = simpleNewron(-2, eps, iter, der)
print(xka)
#random x0 simpleNewron
print(simpleNewron(x0, eps, iter, der))

#example for Newton-Broyden
print("Newton-Broyden method:")
index = [1, -1, 0, 1]
der = []
eps = 0.001
iter =100
fx = "x**3 - x+1"
der.append(derivative(fx))
der.append(derivative(der[0]))
x0 = initial_approximation(index, fx)
xka = simpleNewron(-2, eps, iter, der)
print(xka)
#random x0 Newton-Broyden
print(simpleNewron(x0, eps, iter, der))

#example for Secant
print("Secant method:")
index = [1, -1, 0, 1]
der = []
eps = 0.001
iter =100
fx = "x**3 - x+1"
der.append(derivative(fx))
der.append(derivative(der[0]))
x0 = initial_approximation(index, fx)
xka = simpleNewron(-2, eps, iter, der)
print(xka)
#random x0 Secant
print(simpleNewron(x0, eps, iter, der))