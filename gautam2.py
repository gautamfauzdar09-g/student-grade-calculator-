students = {
    "Amit": 92,
    "Priya": 78,
    "Rahul": 65,
    "Sneha": 45,
    "Vikram": 33,
}

for name, marks in students.items():
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    elif marks >= 40:
        grade = "E"
    else:
        grade = "F"

    print(name, "-", marks, "marks -> Grade:", grade)