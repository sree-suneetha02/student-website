import csv
import json

input_csv = "student.csv"
output_json = "students.json"

students = []
counter = 1

with open(input_csv, "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")  # tab-separated file
    header = next(reader)  # skip header

    for row in reader:
        if len(row) < 7:
            continue

        name = row[2].strip()
        roll_no = row[3].strip()
        feedback = row[6].strip()

        students.append({
            "roll_no": roll_no,
            "name": name,
            "image": f"images/{roll_no}.jpg",
            "feedback": feedback
        })

        counter += 1

with open(output_json, "w", encoding="utf-8") as f:
    json.dump(students, f, indent=2)

print(f"{len(students)} students written to students.json")

