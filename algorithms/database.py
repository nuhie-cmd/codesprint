import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="smart_navigation"
)

cursor = conn.cursor(dictionary=True)


def get_nodes():
    cursor.execute("SELECT * FROM nodes")
    return cursor.fetchall()


def get_edges():
    cursor.execute("SELECT * FROM edges")
    return cursor.fetchall()
