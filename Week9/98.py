import random

def otp_validator(func):
    def wrapper(otp):
        user_otp = input("Enter OTP: ")
        if user_otp == otp:
            print("OTP Verified Successfully!")
            func()
        else:
            print("Invalid OTP!")
    return wrapper

@otp_validator
def access_granted():
    print("Access Granted!")

otp=""
for i in range(6):
    otp+=str(random.randint(0,9))
print("Your OTP is:", otp)

access_granted(otp)
