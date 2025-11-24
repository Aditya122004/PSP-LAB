import math
s1=int(input("Enter side 1: "))
s2=int(input("Enter side 2: "))
s3=int(input("Enter side 3: "))
if(s1<=0 or s2<=0 or s3<=0 or (s1+s2<=s3) or (s2+s3<=s1) or (s1+s3<=s2)):
    print("Invalid Data Entered")
else:
    s=(s1+s2+s3)/2
    area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    print("The Area of triangle is ",area)
