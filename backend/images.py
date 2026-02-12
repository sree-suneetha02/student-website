import psycopg2

# Connect to database
conn = psycopg2.connect(
    host="localhost",
    database="students_db",
    user="suneetha",
    password="suneetha123"
)

cur = conn.cursor()

# Get all students
cur.execute("SELECT roll_no FROM students")
rows = cur.fetchall()

updated = 0

for r in rows:
    roll_no = r[0].strip()

    # new image filename
    image_name = f"{roll_no}.jpg"

    cur.execute(
        """
        UPDATE students
        SET image = %s
        WHERE roll_no = %s
        """,
        (image_name, roll_no)
    )
    updated += 1

conn.commit()
cur.close()
conn.close()

print(f"{updated} image paths updated successfully!")

