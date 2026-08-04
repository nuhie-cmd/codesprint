import qrcode
import os
from database import get_nodes   # <-- change "db" to whatever you named your file above

# folder to save the QR images into
output_dir = "qr_codes"
os.makedirs(output_dir, exist_ok=True)

nodes = get_nodes()

for node in nodes:
    node_id = node["id"]
    name = node["name"]

    payload = f"SDNS:{node_id}"
    img = qrcode.make(payload)

    safe_name = name.replace(" ", "_").replace("/", "-")
    filename = f"{output_dir}/qr_{node_id}_{safe_name}.png"
    img.save(filename)

    print(f"Saved: {filename}  ->  payload: {payload}")

print(f"\nDone. Generated {len(nodes)} QR codes in '{output_dir}/'")