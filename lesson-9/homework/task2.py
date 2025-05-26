import csv
from collections import defaultdict

grades = defaultdict(list)
with open('grades.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        subject = row['Subject']
        grade = int(row['Grade'])
        grades[subject].append(grade)

average_grades = []
for subject, grade_list in grades.items():
    avg = sum(grade_list) / len(grade_list)
    average_grades.append({'Subject': subject, 'Average Grade': round(avg, 1)})

with open('average_grades.csv', mode='w', newline='') as file:
    fieldnames = ['Subject', 'Average Grade']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(average_grades)

print("average_grades.csv file was created successfully.")
