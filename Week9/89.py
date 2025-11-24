grade_points = {
    'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C': 5, 'P': 4, 'F': 0
}

grades = {
    101: ['A', 'B+', 'O', 'A+'],
    102: ['B', 'A', 'A+', 'B+'],
    103: ['A+', 'A', 'O', 'O']
}
calc_cgpa = lambda grade_list: round(
    sum(grade_points[g] for g in grade_list) / len(grade_list), 2
)
cgpa_dict = {roll: calc_cgpa(glist) for roll, glist in grades.items()}

print("Original Grades Dictionary:")
print(grades)

print("\nCGPA Dictionary:")
print(cgpa_dict)

