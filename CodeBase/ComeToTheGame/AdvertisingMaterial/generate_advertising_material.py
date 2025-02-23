import PIL
import requests
from io import BytesIO
from PIL import ImageFont, ImageDraw, Image

from CodeBase.ComeToTheGame.AdvertisingMaterial.wrap_text import wrap_text


def generate_advertising_material(image_url, text):
    # Download the image
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # Get image dimensions
    width, height = image.size

    # Define font and size
    try:
        font = ImageFont.truetype("arialbd.ttf", int(height * 0.07))  # Bold font, 7% of image height
    except IOError:
        try:
            font = ImageFont.truetype("arial.ttf", int(height * 0.07))  # Fallback to regular Arial
        except IOError:
            font = ImageFont.load_default()  # Fallback if no TTF is found

    # Create a draw object
    draw = ImageDraw.Draw(image)

    # Wrap text so it fits inside the image width
    margin = int(width * 0.1)  # 10% margin on sides
    max_text_width = width - 2 * margin
    wrapped_lines = wrap_text(text, font, max_text_width, draw)

    # Calculate text block height
    line_spacing = int(height * 0.02)  # Spacing between lines
    text_heights = [draw.textbbox((0, 0), line, font=font)[3] - draw.textbbox((0, 0), line, font=font)[1] for line in wrapped_lines]
    text_height = sum(text_heights) + (len(wrapped_lines) - 1) * line_spacing

    # Determine text starting position (centered in bottom 1/3)
    start_y = height - int(height / 3) + ((int(height / 3) - text_height) // 2)

    # Add text to image with bold effect
    for i, line in enumerate(wrapped_lines):
        text_bbox = draw.textbbox((0, 0), line, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        x_position = (width - text_width) // 2  # Proper centering
        y_position = start_y + sum(text_heights[:i]) + i * line_spacing

        # Simulate bold text by drawing it multiple times slightly offset
        shadow_offset = 2
        for dx in [-shadow_offset, 0, shadow_offset]:
            for dy in [-shadow_offset, 0, shadow_offset]:
                draw.text((x_position + dx, y_position + dy), line, font=font, fill="black")

        draw.text((x_position, y_position), line, font=font, fill="white")  # Final white text on top

    image.show()
    image.save("advertising_material.png")

if __name__ == '__main__':
    image_url = "https://images.sidearmdev.com/resize?url=https%3a%2f%2fdxbhsrqyrr690.cloudfront.net%2fsidearm.nextgen.sites%2fksuowls.com%2fimages%2f2024%2f11%2f22%2fKSU_BASEBALL_HS-20.jpg&width=300&type=webp"
    text = "Come See the KSU Baseball Team this weekend! Grab your tickets now!"
    generate_advertising_material(image_url, text)
