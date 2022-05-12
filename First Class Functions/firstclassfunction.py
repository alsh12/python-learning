def divide(dividend, divisior):
    if divisior == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisior


def calculate(*values, operator):
    return operator(*values)


result = calculate(12, 48, operator=divide)

print(result)
