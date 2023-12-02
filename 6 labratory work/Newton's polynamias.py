import numpy as np

def divided_diff(x, y):
    n = len(x)
    table = np.zeros((n, n))
    table[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            if x[i + j] != x[i]:
                table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (x[i + j] - x[i])
            else:
                table[i, j] = y[i]
    return table

def newton_interpolation(x, y, x_interp, table):

    n = len(x)
    result = y[0]
    temp = 1
    for i in range(1, n):
        temp *= (x_interp - x[i - 1])
        result += table[i - 1, i] * temp
    return result

# Example
x_values = np.array([1, 2, 4, 5, 7])
y_values = np.array([4, 3, 0, 2, 1])

# 1. Compute the divided differences table for n = 4
table_uneven = divided_diff(x_values[:4], y_values[:4])

# 2. Interpolate the polynomial for x = 3 using n = 4
interpolated_value_uneven = newton_interpolation(x_values[:4], y_values[:4], 3, table_uneven)

print("1. Interpolated value for Newton's divided differences method (uneven nodes):", interpolated_value_uneven)

# 3. Interpolate the polynomial for x = 3 using n = 5
table_even = divided_diff(x_values, y_values)
interpolated_value_even = newton_interpolation(x_values, y_values, 3, table_even)

print("2. Interpolated value for Newton's divided differences method (evenly spaced nodes):", interpolated_value_even)

# 4. Interpolate the polynomial for x = 3 using custom nodes (first three nodes)
table_custom = divided_diff(x_values[:3], y_values[:3])
interpolated_value_custom = newton_interpolation(x_values[:3], y_values[:3], 3, table_custom)

print("3. Interpolated value for Newton's divided differences method (custom nodes):", interpolated_value_custom)

# 5. Interpolate the polynomial for x = 1.5 using n = 6 (adding the known node (4, 0))
x_values_4th = np.array([1, 2, 4, 5, 7, 4])
y_values_4th = np.array([4, 3, 0, 2, 1, 0])
table_4th = divided_diff(x_values_4th, y_values_4th)
interpolated_value_4th = newton_interpolation(x_values_4th, y_values_4th, 1.5, table_4th)

print("4. Interpolated value for Newton's divided differences method at x* = 1.5:", interpolated_value_4th)
