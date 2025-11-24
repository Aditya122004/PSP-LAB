import math
ram_size=int(input("Enter the size of ram in GB: "))
if(ram_size<=0):
    print("Invalid Data Entered")
else:
    n_bytes=1024**3*ram_size
    bus_size=math.log2(n_bytes)
    print("The size of address bus is ",bus_size)

