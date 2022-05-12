def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be 0.")

    return dividend / divisor


grades = []

print("Check average of the grades.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print("Still grades are not available in your list.")
except Exception as e:
    print(e)
else:
    print(f'Average of the all grades is {average}')
finally:
    print("Thanks for using our program!")
