import math
l=int(input("Enter length of room: "))
b=int(input("Enter breadth of room: "))
n=int(input("Enter side of square tile: "))
squareCost=int(input("Enter cost of one square tile: "))
lTile=int(input("Enter length of rectangle tile: "))
bTile=int(input("Enter breadth of rectangle tile: "))
rectangleCost=int(input("Enter cost of one rectangle tile: "))
areaRoom=l*b
areaSquare=n**2
areaRectangle=lTile*bTile
squareTiles=math.ceil(areaRoom/areaSquare)
squareTilesCost=squareCost*squareTiles
rectangleTiles=math.ceil(areaRoom/areaRectangle)
rectangleTilesCost=rectangleCost*squareTiles
print(f"The no of square tiles required is {squareTiles} which would cost {squareTilesCost}")
print(f"The no of rectangle tiles required is {rectangleTiles} which would cost {rectangleTilesCost}")

