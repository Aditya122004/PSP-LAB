def checkStrength(pwd):
    score=0
    has_uppercase=0
    has_lower=0
    has_digit=0
    has_special=0
    if(len(pwd)>=8):
        score=score+1
    for ch in pwd:
        if(ch>='A' and ch<='Z'):
            has_uppercase=1
        elif(ch>='a' and ch<='z'):
            has_lower=1
        elif(ch>='0' and ch<='9'):
            has_digit=1
        else:
            has_special=1
    score+=has_uppercase
    score+=has_digit
    score+=has_lower
    score+=has_special
    if(score>=5):return "Very Strong"
    if(score>=4 and len(pwd)>=8):return "Strong"
    if(score>=3 and len(pwd)>=8):return "Medium"
    return "Weak"
p=input("Enter your Password:")
print(checkStrength(p))