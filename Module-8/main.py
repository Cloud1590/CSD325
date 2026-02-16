import json

# Function to print student list
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , "
              f"Email = {student['Email']}")

# Load JSON file
with open("student.json", "r") as file:
    students = json.load(file)

print("----- Original Student List -----")
print_students(students)

# Add new student
new_student = {
    "F_Name": "Daniel",
    "L_Name": "Vance",
    "Student_ID": 21429236,
    "Email": "dvance@my365.bellevue.edu"
}

students.append(new_student)

print("\n----- Updated Student List -----")
print_students(students)

# Write updated list back to JSON file
with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nstudent.json file has been updated.")