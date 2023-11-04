def parabolic_interpolation(x, y, x_star):
    n = len(x)
    if n < 3:
        raise ValueError("At least 3 data points are required for interpolation.")

    for i in range(n - 2):
        if x[i] <= x_star <= x[i + 2]:
            break
    else:
        raise ValueError("x* is not within the range of provided data points.")

    x1, x2, x3 = x[i], x[i + 1], x[i + 2]
    y1, y2, y3 = y[i], y[i + 1], y[i + 2]

    a1 = ((x_star - x2) * (x_star - x3)) / ((x1 - x2) * (x1 - x3))
    a2 = ((x_star - x1) * (x_star - x3)) / ((x2 - x1) * (x2 - x3))
    a3 = ((x_star - x1) * (x_star - x2)) / ((x3 - x1) * (x3 - x2))

    result = a1 * y1 + a2 * y2 + a3 * y3

    return result

# Example
x = [-1, 0, 1, 3, 4]
y = [-1, 0, 1, 27, 64]
x_star = 2.0
interpolated_value = parabolic_interpolation(x, y, x_star)
print(f"The interpolated value at x* = {x_star} is {interpolated_value}")
