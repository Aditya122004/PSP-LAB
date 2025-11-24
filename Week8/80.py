def roll_No(r_o):
    r_no=str(r_o)
    if(len(r_no)!=9):
        return "Invalid"
    program="PG" if r_no[0] =="2" else "UG"
    dept_code=r_no[1:3]
    departments={
        "01":"CSE",
        "02":"ECE",
        "03":"EEE",
        "04":"IT",
        "05":"MCA",
        "06":"ME"
    }
    department=departments.get(dept_code,"Unknown")
    course_code=r_no[3]
    course_type="Full-time" if course_code=="1" else "Part-time"
    year="20"+r_no[4:6]
    s_roll=r_no[6:]
    return f""" Decoded Roll Number:
        Program:{program}
        Department:{department}
        Course Type:{course_type}
        Year of Admission:{year}
        Student Roll No:{s_roll}
    """
r=input("Enter your roll Number:")
print(roll_No(r))