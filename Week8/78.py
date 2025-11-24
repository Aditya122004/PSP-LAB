def corrupt(s):
    c=""
    for ch in s:
        c+=chr(ord(ch)+3)
    return c
def uncorrupt(s):
    o=""
    for ch in s:
        o+=chr(ord(ch)-3)
    return o
s=input("Enter a string")
c=corrupt(s)
o=uncorrupt(c)
print(c)
print(o)