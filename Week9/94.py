def hanoi(n, A, B, C):
    if n == 1:
        print(f"Move disk 1 from {A} to {C}")
        return
    hanoi(n-1, A, C, B)
    print(f"Move disk {n} from {A} to {C}")
    hanoi(n-1, B, A, C)

hanoi(3, 'A', 'B', 'C')
