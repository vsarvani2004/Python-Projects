num_subjects = int(input("Enter total number of subjects: "))
total = 0 
if num_subjects <= 0:
    print("Invalid input, number of subjects cannot be zero or negative")
    exit()  
for i in range(1, num_subjects+1): # alternative: for i in range(num_subjects):
        marks = float(input(f"Enter marks for subject {i}: ")) #marks = float(input(f"Enter marks for subject {i+1}: "))
        if marks < 0 or marks > 100:
            print("Invalid input, marks should be between 0 and 100")
            exit() 
        total += marks
average = total / num_subjects
if average >= 90:
    grade = 'A+'
elif average >= 80:
    grade = 'A'
elif average >= 70:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 50:
    grade = 'D'
else:
        grade = 'F'
print(f"Total Marks: {total}")
print(f"Average Marks: {average: .2f}")  #print(f"Average Marks: {round(average, 3)}") 
if(average >= 50):
    print("Status: Pass")
else:
    print("Status: Fail")
print(f"Grade: {grade}")  