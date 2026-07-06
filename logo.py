import os
from PIL import Image

INPUT_DIR = "input"
OUTPUT_DIR = "output"
LOGO_FILE = "logo.png"

os.makedirs(OUTPUT_DIR, exist_ok=True)

logo = Image.open(LOGO_FILE).convert("RGBA")
logo = logo.resize((100, 100), Image.LANCZOS)

for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(INPUT_DIR, filename)

        image = Image.open(image_path).convert("RGBA")

        x = (image.width - logo.width) // 2
        y = image.height - logo.height - 15

        image.paste(logo, (x, y), logo)

        output_path = os.path.join(OUTPUT_DIR, filename)

        if filename.lower().endswith((".jpg", ".jpeg")):
            image.convert("RGB").save(output_path, quality=95)
        else:
            image.save(output_path)

        print(f"Processed: {filename}")

print("Done!")
