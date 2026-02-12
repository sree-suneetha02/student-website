import json
import psycopg2

# Connect to database
conn = psycopg2.connect(
    host="localhost",
    database="students_db",
    user="suneetha",
    password="suneetha123"
)

cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    roll_no TEXT,
    name TEXT,
    image TEXT,
    feedback TEXT
);
""")

conn.commit()

# Load JSON data
with open("students.json", "r") as f:
    students = json.load(f)

# Insert data
for s in students:
    cur.execute(
        """
        INSERT INTO students (roll_no, name, image, feedback)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (roll_no) DO NOTHING
        """,
        (s["roll_no"], s["name"], s["image"], s["feedback"])
    )

conn.commit()
cur.close()
conn.close()

print("JSON data inserted into database!")

