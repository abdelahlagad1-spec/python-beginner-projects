def sum_all(*args):
    return sum(args)

numbers = [1, 2, 3, 4, 5]
print(f"Sum of {numbers} = {sum_all(*numbers)}")
