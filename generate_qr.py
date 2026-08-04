import os
import qrcode
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nuhie043",
    database="smart_navigation"
)

cursor = conn.cursor(dictionary=True)

# Get all nodes from the database
cursor.execute("SELECT id, name FROM nodes")
nodes = cursor.fetchall()

# Folder to save QR codes
output_folder = "frontend/qr_codes"
os.makedirs(output_folder, exist_ok=True)

# Generate one QR per node
for node in nodes:
    node_id = node["id"]
    node_name = node["name"]

    # Payload stored inside the QR
    payload = f"SDNS:{node_id}"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )

    qr.add_data(payload)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    filename = node_name.lower().replace(" ", "_").replace("/", "-") + ".png"
    img.save(os.path.join(output_folder, filename))

    print(f"{filename} -> {payload}")

cursor.close()
conn.close()

print("QR codes generated successfully.")
