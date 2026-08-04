import qrcode
import os

locations = [
    "main_block",
    "mechanical_block",
    "canteen",
    "cse_department",
    "cse_aiml_department",
    "is_department",
    "aiml_lab_1",
    "aiml_lab_2",
    "aiml_lab_3",
    "second_year_classroom",
    "third_year_classroom",
    "fourth_year_classroom"
]

output_folder = "frontend/qr_codes"
os.makedirs(output_folder, exist_ok=True)

for location in locations:
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(location)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{output_folder}/{location}.png")

print("QR codes generated successfully.")
