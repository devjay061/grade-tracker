import csv
import os
import pandas as pd

def grade_calculator(avg):
    if avg >= 90:
        return 'A','pass'
    elif avg >= 80:
        return 'B','pass'
    elif avg >= 70:
        return 'C','pass'
    elif avg >= 60:
        return 'D','pass'
    elif avg >= 50:
        return 'E','pass'
    else:
        return 'F','fail'

def add_student():
    name = input("Enter student's name: ").title()
    with open(fname, 'a', newline='') as file:
        writer = csv.writer(file)
        for i in range(1,6):
            subject= input(f"Enter name of subject {i}: ")
            grade = float(input(f"Enter grade for subject {i}: "))
            if not (0 <= grade <= 100):
                print("Invalid grade. Please enter a number between 0 and 100.")
                return
            writer.writerow([name, subject, grade])
            print(f"Added {name} with grade {grade} for {subject} to the file.")

def show_student_report():
    name = input("Enter student's name to view report: ")
    
    with open(fname, 'r') as file:
        reader = csv.reader(file)
        grades = [row for row in reader if row[0] == name]
    
    if not grades:
        print(f"No records found for {name}.")
        return
    s=sum(float(grade[2]) for grade in grades)
    avg=s/len(grades)
    grade_letter, status = grade_calculator(avg)
    print(f"Report for {name}:")
    for grade in grades:
        print(f"Subject: {grade[1]}, Grade: {grade[2]}")
    print(f"Average Grade: {avg:.2f}")
    print(f"Letter Grade: {grade_letter}")
    print(f"Status: {status}")

def class_summary():
    df = pd.read_csv(fname)
    #calculate average grade for each student
    student_average = df.groupby('Name')['Grade'].mean()

    #topper and topper avg
    topper = student_average.idxmax()
    topper_avg = student_average.max()

    #average grade for each subject
    subject_avg = df.groupby('Subject')['Grade'].mean()

    #class average
    class_avg = student_average.mean()
    print("\nClass Summary:")
    print("-----------------------------")
    print(f"🏆 Top Performer: {topper} ({topper_avg:.2f})")
    print("\nSubject Averages:")
    for subject, avg in subject_avg.items():
        print(f"{subject:<15} {avg:.2f}")
    print("-----------------------------")
    print(f"{'Class Average':<15} {class_avg:.2f}")

def main():
    while True:
        print("\nGrade Tracker Menu:")
        print("1. Add Student Grades")
        print("2. Show Student Report")
        print("3. Show Class Summary")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            show_student_report()
        elif choice == '3':
            class_summary()
        elif choice == '4':
            print("Exiting the Grade Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    

#main
# Check if the file exists, if not create it and write the header
fname= "grades.csv"
file_exists = os.path.isfile(fname)
if not file_exists:
    with open(fname, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Subject', 'Grade'])

#show_student_report()
class_summary() 