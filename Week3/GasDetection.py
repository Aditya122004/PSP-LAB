colour=input("Enter the colour of cylinder: ")
colour=colour.upper()
if(colour[0]=="O"):
    print("Ammonia")
elif(colour[0]=="B"):
    print("Carbon Monoxide")
elif(colour[0]=="Y"):
    print("Hydrogen")
elif(colour[0]=="G"):
    print("Oxygen")
else:
    print("Contents Unknown")
