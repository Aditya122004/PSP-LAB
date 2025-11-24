def prime_generator(limit):
    for num in range(2, limit + 1):
        flag=True
        for i in range(2, num):
            if num % i == 0:
                flag=False
                break
        if flag:
            yield num   

n = int(input("Enter the limit: "))
print(f"Prime numbers up to {n} are:")

for prime in prime_generator(n):
    print(prime, end=" ")
