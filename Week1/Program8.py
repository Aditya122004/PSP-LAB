import math
l=float(input("Enter the length of room: "))
b=float(input("Enter the breadth of room: "))
if(l<0 or b<0):
    print("Invalid Data Entered")
else:
    area=l*b
    print("The area of the room is ",area)
    n=float(input("Enter the side of the tile: "))
    c=float(input("Enter the cost of one tile: "))
    if(n<0 or c<0):
        print("Invalid Data Entered")
    else:
        area_tiles=n*n
        no_tiles=math.ceil(area/area_tiles)
        cost=c*no_tiles
        print("The no of tiles is ",no_tiles)
        print("The cost of the tiles is ",cost)
