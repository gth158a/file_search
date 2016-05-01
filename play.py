

def factorial(n):
    if n == 1:
        return 1

    else:
        return n * factorial(n - 1)

print("5!={:,}, 3!={:,}, 11!= {:,}".format(
    factorial(5),
    factorial(3),
    factorial(11)
))

# Fibonacci using tuple projection

def fibonacci2(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, current + next
        nums.append(current)

    return nums

for n in fibonacci2(100):
    print(n, end=", ")

# Generator method - coroutine



def fibonacci2_co(limit):
    current = 0
    next = 1

    while current < limit:
        current, next = next, current + next
        yield current

print("\nprint with yield")
for n in fibonacci2_co(100):
    print(n, end=", ")