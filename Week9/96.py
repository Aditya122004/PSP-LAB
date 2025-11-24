def perfect_generator(limit):
    for num in range(2, limit + 1):
        s = 0
        for i in range(1, num):
            if num % i == 0:
                s += i
        if s == num:
            yield num

n = int(input("Enter the limit: "))

print(f"Perfect numbers up to {n}:")
for p in perfect_generator(n):
    print(p, end=" ")
