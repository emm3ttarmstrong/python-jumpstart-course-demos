

def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, current + next
        nums.append(current)

    print(nums)


fibonacci(100)
