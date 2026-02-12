from flask import Flask, jsonify, request, render_template, send_from_directory
import psycopg2
import os
app = Flask(__name__)
app = Flask(__name__, static_folder="images", static_url_path="/images")
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="students_db",
        user="suneetha",
        password="suneetha123"
    )
IMAGE_FOLDER = os.path.join(os.getcwd(), "images")
# Serve images
@app.route('/images/<path:filename>')
def get_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Students API
@app.route("/students")
def students():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))
    random_mode = request.args.get("random", "false")
    reset = request.args.get("reset", "false")

    # if reset is true → go back to page 1
    if reset == "true":
        page = 1

    offset = (page - 1) * limit

    conn = get_connection()
    cur = conn.cursor()

    # total count
    cur.execute("SELECT COUNT(*) FROM students")
    total = cur.fetchone()[0]
    # choose query
    if random_mode == "true":
        order_clause = "ORDER BY RANDOM()"
    else:
        order_clause = "ORDER BY id"

    query = f"""
        SELECT roll_no, name, image, feedback
        FROM students
        {order_clause}
        LIMIT %s OFFSET %s
    """

    cur.execute(query, (limit, offset))
    rows = cur.fetchall()
    students_list = []
    for r in rows:
        students_list.append({
            "roll_no": r[0],
            "name": r[1],
            "image": f"/images/{r[2]}",
            "feedback": r[3]
        })

    cur.close()
    conn.close()

    return jsonify({
        "page": page,
        "limit": limit,
        "total": total,
        "students": students_list
    })

if __name__ == "__main__":
     print("Server will run on http://localhost:5000")
     print("Access from network: http://<your-ip>:5000")
     app.run(debug=True, host='0.0.0.0', port=5000)

