def generate():
    n = 0
    while True:
        yield (2 ** (2 * n)) + 1
        n += 1

gen = generate()

while True:
    print(next(gen))
    input("Press Enter for next number...")
