bp=float(input("Enter observed Boiling Point:"))
if(bp>=(0.95*100) and bp<=(1.05*100)):
    print("Water")
elif(bp>=(0.95*357) and bp<=(1.05*357)):
    print("Mercury")
elif(bp>=(0.95*1187) and bp<=(1.05*1187)):
    print("Copper")
elif(bp>=(0.95*2193) and bp<=(1.05*2193)):
    print("Silver")
elif(bp>=(0.95*660) and bp<=(1.05*660)):
    print("Gold")
else:
    print("Substance Unknown")
