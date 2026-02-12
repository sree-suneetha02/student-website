import csv
import json

input_csv = "student.csv"
output_json = "students.json"

students = []
counter = 1

with open(input_csv, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print("Row:", row)  # debug

        # skip empty rows
        if len(row) < 4:
            continue

        name = row[2].strip()
        roll_no = row[3].strip()

        # feedback may or may not exist
        feedback = ""
        if len(row) > 6:
            feedback = row[6].strip()

        students.append({
            "roll_no": roll_no,
            "name": name,
            "image": f"images/student{counter}.jpg",
            "feedback": feedback
        })

        counter += 1

with open(output_json, "w", encoding="utf-8") as f:
    json.dump(students, f, indent=2)

print(f"{len(students)} students written to students.json")

