import os
import sqlite3
import qrcode

# Path to SQLite database
DB_PATH = "nav.db"

# Connect to database
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Get all nodes
cursor.execute("SELECT id, name FROM nodes ORDER BY id")
nodes = cursor.fetchall()

# Output folder
output_folder = "frontend/qr_codes"
os.makedirs(output_folder, exist_ok=True)

for node in nodes:
    node_id = node["id"]
    node_name = node["name"]

    # QR payload
    payload = f"SDNS:{node_id}"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(payload)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    filename = (
        node_name.lower()
        .replace(" ", "_")
        .replace("&", "and")
    )

    img.save(os.path.join(output_folder, f"{filename}.png"))

print(f"Generated {len(nodes)} QR codes successfully.")

conn.close()
