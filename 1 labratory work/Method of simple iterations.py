def simple_iteration(x0, e, max_iter, a):
    for i in range(max_iter):
        x_prev = x0
        x0 = 1/2*(x0 +a/x0)
        if(abs(x_prev-x0)<=e):
            return x0, i
    return x0, i

def f(x):
    return x**0.5

#First example (it was given)
#root, iterations = simple_iteration(2,10**(-5),20,5)
#Second example
#root, iterations = simple_iteration(3,10**(-5),20,10)
#Third example
root, iterations = simple_iteration(4,10**(-5),20,100)
print("Root, iterations:")
print(root, iterations)