ans_key=['A','D','B','C','A','D']
st_key=[]
print("Enter Answer:(A/B/C/D):")
for i in range(len(ans_key)):
    ans=input(f"Q{i+1}:").upper()
    st_key.append(ans)
score=0
for i in range(len(ans_key)):
    if ans_key[i]==st_key[i]:
       score+=1
    else:
        score-=0.25
print(f"The score of student is {score}")
percent=(score/len(ans_key))*100
print(f"The student scored {percent:.2f}%")
