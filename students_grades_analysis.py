names_grades_students = [{"Name": "Ayra", "Grade" : 86},
                         {"Name": "Amelia", "Grade" : 47},
                         {"Name": "Ananya", "Grade" : 73},
                         {"Name": "Angela", "Grade" : 57},
                         {"Name": "Amy", "Grade" : 38}]

total_grade = 0
for student in names_grades_students:
    total_grade = student["Grade"] + total_grade

avg_grade = total_grade / len(names_grades_students)
print(avg_grade)
print(total_grade)

student_grade = 0
for student in names_grades_students:
    if student["Grade"] > avg_grade:
        print(f"{student['Name']} is above avg")
    else:
        print(f"{student['Name']} is below avg")


