dist=int(input("Enter distance in km: "))
speed=int(input("Enter the speed in km\hr: "))
if(dist<0 or speed<=0):
    print("Invalid Data Entered")
else:
    time=dist/speed
    print("The time taken is",time,"hours")
