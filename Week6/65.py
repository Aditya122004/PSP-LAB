coordinates=[(1,2),(-2,-9),(0,0),(-2,9),(5,-8),(0,5),(-4,0)]
quadrant=[]
for i in coordinates:
    if i[0]==0 and i[1]==0:
        quadrant.append("Origin")
    elif i[0]==0:
        quadrant.append("Y-axis")
    elif i[1]==0:
        quadrant.append("X-axis")
    elif i[0]>0 and i[1]>0:
        quadrant.append("I")
    elif i[0]<0 and i[1]>0:
        quadrant.append("II")
    elif i[0]<0 and i[1]<0:
        quadrant.append("III")
    else:
        quadrant.append("IV")
print(quadrant)
