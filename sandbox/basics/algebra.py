def extract_coefficient_and_contant(first_order_equation):
    '''
    Extracts the coefficient and constant from an equation of the type ax + b = 0

    @param equation: The equation in string format to extract the coefficient and constant from
    @return: The coefficient (a) and the constant (b) of the equation
    '''

    first_order_equation = first_order_equation.replace(" ", "")
    # print("Part 1: ", first_order_equation)

    first_order_equation = first_order_equation.replace("+", "")
    # print("Part 2: ", first_order_equation)

    first_order_equation = first_order_equation.replace("=0", "")
    # print("Part 3: ", first_order_equation)

    first_order_equation = first_order_equation.split("x")
    # print("Part 4: ", first_order_equation)

    a = first_order_equation[0]
    b = first_order_equation[1]

    return a, b


def solve_equation(a, b):
    '''
    Solves the first order algebraic equation ax + b = 0

    @param a: The equation coefficient - a
    @param b: The equation constant - b
    @return: The values for x and y given a and b in the equation ax + b = 0
    '''

    x_solution = -int(b) / int(a)
    y_solution = x_solution + int(b)

    return x_solution, y_solution


is_equation_valid = False

print(extract_coefficient_and_contant.__doc__)

while not is_equation_valid:
    equation = input("Enter an equation of the type ax + b = 0: ")

    if equation is None or equation == "":
        print("Please enter a valid equation")
    else:
        is_equation_valid = True

coefficient, constant = extract_coefficient_and_contant(equation)
# print("The coefficient is: " + coefficient)
# print("The constant is: " + constant)
x, y = solve_equation(coefficient, constant)
print(f"The ({x},{y}) point")
