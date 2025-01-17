from PIL import Image, ImageDraw, ImageFont
import os


input_folder = "input_images"
output_folder = "output_images"
watermark_text = "My Watermark"

os.makedirs(output_folder, exist_ok=True)


for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".png", ".jpeg")):

        image_path = os.path.join(input_folder, filename)
        img = Image.open(image_path)

        img = img.resize((800, 800))

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 30)
        text_width, text_height = draw.textsize(watermark_text, font=font)
        position = (
            img.width - text_width - 10,
            img.height - text_height - 10,
        )
        draw.text(position, watermark_text, (255, 255, 255), font=font)

        output_path = os.path.join(output_folder, filename)
        img.save(output_path)

print("Automatic image editing completed!")
