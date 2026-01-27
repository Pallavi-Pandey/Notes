from PIL import Image
import os

input_path = "/mnt/data/sign.jpeg"
output_path = "/mnt/data/sign_20kb.jpg"

img = Image.open(input_path).convert("RGB")

# Try different qualities to get close to 20KB
target_size = 20 * 1024  # 20 KB
best_path = None

for quality in range(95, 5, -5):
    img.save(output_path, format="JPEG", quality=quality, optimize=True)
    size = os.path.getsize(output_path)
    if size <= target_size:
        break

os.path.getsize(output_path), output_path
