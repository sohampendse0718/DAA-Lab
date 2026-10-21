name = input("Enter Student Name: ")

sem1 = []
sem2 = []

# Semester 1
for i in range(5):
    print("\nSemester 1 - Subject", i + 1)

    subject = input("Enter subject name: ")
    theory = float(input("Enter theory marks: "))
    lab = float(input("Enter lab marks: "))

    sem1.append([subject, theory, lab])


# Semester 2
for i in range(5):
    print("\nSemester 2 - Subject", i + 1)

    subject = input("Enter subject name: ")
    theory = float(input("Enter theory marks: "))
    lab = float(input("Enter lab marks: "))

    sem2.append([subject, theory, lab])


# Semester 1 calculations
total1 = sum(subject[1] + subject[2] for subject in sem1)
percentage1 = total1 / 5
sgpa1 = percentage1 / 10


# Semester 2 calculations
total2 = sum(subject[1] + subject[2] for subject in sem2)
percentage2 = total2 / 5
sgpa2 = percentage2 / 10


# CGPA
cgpa = (sgpa1 + sgpa2) / 2


# Display
print("\nStudent Name:", name)
print("\n--- Semester 1 ---")
print(f"{'Subject':<25} {'Theory':>8} {'Lab':>8} {'Total':>8}")

for subject in sem1:
    total = subject[1] + subject[2]
    print(f"{subject[0]:<25} {subject[1]:>8.1f} {subject[2]:>8.1f} {total:>8.1f}")

print(f"Percentage: {percentage1:.1f}")
print(f"SGPA: {sgpa1:.2f}")


print("\n--- Semester 2 ---")
print(f"{'Subject':<25} {'Theory':>8} {'Lab':>8} {'Total':>8}")

for subject in sem2:
    total = subject[1] + subject[2]
    print(f"{subject[0]:<25} {subject[1]:>8.1f} {subject[2]:>8.1f} {total:>8.1f}")

print(f"Percentage: {percentage2:.1f}")
print(f"SGPA: {sgpa2:.2f}")

print(f"\nCGPA: {cgpa:.2f}")