def multiply(*args):
    product = 1
    for num in args:
        product *= num
    return product


def addition(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(multiply(3,5,9,7))