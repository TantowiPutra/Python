def add_numbers(*args):
    print(type(args)) # Tuple

    ans = 0
    for x in args:
        ans += x

    return ans

res = add_numbers(1, 2, 3, 4, 5, 6, 7)
print(res)