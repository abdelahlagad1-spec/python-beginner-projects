import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Math", "English"])
    writer.writerow(["Alice", 85, 90])
    writer.writerow(["Bob", 78, 82])
    writer.writerow(["Charlie", 92, 88])

print("students.csv created")
