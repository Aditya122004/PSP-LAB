from datetime import datetime

def employee_info(**data):
    dob = datetime.strptime(data["dob"], "%d-%m-%Y")
    doj = datetime.strptime(data["doj"], "%d-%m-%Y")
    today = datetime.today()

    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    exp_years = today.year - doj.year
    exp_months = today.month - doj.month
    exp_days = today.day - doj.day
    if exp_days < 0:
        exp_months -= 1
        exp_days += 30
    if exp_months < 0:
        exp_years -= 1
        exp_months += 12

    return {
        "Age": f"{age} years",
        "Experience": f"{exp_years} years, {exp_months} months, {exp_days} days"
    }

employees = {}
n = int(input("Enter number of employees: "))

for i in range(n):
    name = input("Name: ")
    dob = input("DOB (dd-mm-yyyy): ")
    designation = input("Designation: ")
    doj = input("Date of Joining (dd-mm-yyyy): ")
    employees[name] = employee_info(name=name, dob=dob, designation=designation, doj=doj)

print("Employee Details:")
for name, info in employees.items():
    print(f"{name} -> {info}")
