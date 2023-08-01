# At that exercise i made a function that multiplicate all the non declarated arguments
# and return the total value, after another function must show if the total value is pair or odd

def multiplication(*args):
    total = 1
    for number in args:
        total = total * number
    return total

final_value = multiplication(2,4,5,6,7,9)
print(final_value)

def pair_odd(total):
    if total % 2 == 0:
        return f'The number {total} is pair'
    return f"The number {total} is odd"
print(pair_odd(final_value))