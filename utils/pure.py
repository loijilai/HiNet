from PIL import Image
import os

# Specify the output directory
output_path = "/home/lai/Research/coco/small_images_png/pure"
os.makedirs(output_path, exist_ok=True)

# Define colors and their filenames
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
}

# Generate and save images
for color_name, rgb in colors.items():
    img = Image.new("RGB", (1024, 1024), rgb)
    img.save(os.path.join(output_path, f"{color_name}.png"))

print(f"Images saved in {output_path}")