try:
    x = int(input())
except ValueError:
    print("Invalid input")


def recursive_fact(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 1
    elif n == 1:
        return n

    else:
        return n * recursive_fact(n - 1)


print(recursive_fact(x))
