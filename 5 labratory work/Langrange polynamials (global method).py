def lagrange_basis(x, k, x_values):
    result = 1
    for i in range(len(x_values)):
        if i != k:
            result *= (x - x_values[i]) / (x_values[k] - x_values[i])
    return result

def lagrange_interpolation(x, x_values, y_values):
    result = 0
    for k in range(len(x_values)):
        result += y_values[k] * lagrange_basis(x, k, x_values)
    return result

# Example
x_values = [2.0, 3.0, 4.0, 5.0]
y_values = [7, 5, 8, 7]

x_star = 2.5
result = lagrange_interpolation(x_star, x_values, y_values)

print(f"P({x_star}) = {result}")

