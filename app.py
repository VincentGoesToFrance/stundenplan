from flask import Flask, jsonify, render_template, request
import sqlite3, json
import mysql.connector 

app = Flask(__name__)

# Sqlite - Datenbank initialisieren
def init_sqlite_db():
    conn = sqlite3.connect("./static/db/database.db")
    cursor = conn.cursor()
    # Löscht die Tabelle, falls sie existiert
    cursor.execute("DROP TABLE IF EXISTS schedule")
    # Erstellt die Tabelle neu
    cursor.execute('''
        CREATE TABLE schedule (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class TEXT,
            year INTEGER,
            week INTEGER,
            time TEXT,
            subject TEXT
        )
    ''')
    conn.commit()
    conn.close()


def seed_sqlite_data():
    with open('./data/beispieldaten.json', 'r') as f:
        beispieldaten = json.load(f)

    conn = sqlite3.connect("./static/db/database.db")
    cursor = conn.cursor()
    
    cursor.executemany('''
        INSERT INTO schedule (class, year, week, time, subject)
        VALUES (?, ?, ?, ?, ?)
    ''', beispieldaten)
    conn.commit()
    conn.close()

# MariaDB initialisieren
def get_mariadb_db():
    mariadb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="stundenplan"
    )
    return mariadb

@app.route('/api/schedule', methods=['GET'])
def get_schedule():
    
    class_name = request.args.get("class")
    year = request.args.get("year")
    week = request.args.get("week")

    # conn = sqlite3.connect("./static/db/database.db")
    conn = get_mariadb_db()
    cursor = conn.cursor()
    query = '''
        SELECT time, subject FROM schedule
        WHERE class = %s AND year = %s AND week = %s
    '''
    # query = '''
    #     SELECT time, subject FROM schedule
    #     WHERE class = ? AND year = ? AND week = ?
    # '''
    cursor.execute(query, (class_name, year, week))
    rows = cursor.fetchall()
    conn.close()

    result = [{"time": row[0], "subject": row[1]} for row in rows]
    return jsonify(result)

# routen
@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    init_sqlite_db()
    seed_sqlite_data()
    app.run(debug=True, host='127.0.0.1', port=5000)