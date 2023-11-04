def interpolate_lagrange(x, x_values, y_values):
    # Find the interval [xi, xi+1] where x* lies
    i = 0
    while i < len(x_values) - 1 and x > x_values[i + 1]:
        i += 1
    xi = x_values[i]
    xi_plus_1 = x_values[i + 1]

    #Compute L1(x) coefficients
    L1_x = ((x - xi_plus_1) / (xi - xi_plus_1))
    L1_xi_plus_1 = ((x - xi) / (xi_plus_1 - xi))

    # Check the condition P1i(x*) + P1i+1(x*) = 1
    condition_check = L1_x + L1_xi_plus_1
    if abs(condition_check - 1.0) > 1e-10:
        print("Condition P1i(x*) + P1i+1(x*) = 1 not satisfied.")
        return None

    # Calculate f(x*)
    f_x = L1_x * y_values[i] + L1_xi_plus_1 * y_values[i + 1]
    return f_x

# Example
x_values = [-1.0,  0.0, 1.0, 3.0, 4.0]
y_values = [-1.0, 0.0, 1.0, 27.0, 64.0]
x_star = 2.0
result = interpolate_lagrange(x_star, x_values, y_values)
if result is not None:
    print(f"f({x_star}) = {result}")
