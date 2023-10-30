def generate(student_marks):
    for stuedent, marks in student_marks.items():
        avg_marks = sum(marks.values()) / len(marks)
        yield {"name ": stuedent, "avg": avg_marks}


student_marks = {"Alaa": {'Math': 60,
                          "Expertsystem": 80, "programming": 65}}
for student in generate(student_marks):
    print(student)
