import io
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


def generate_image(text: str) -> bytes:
    img = Image.new('RGB', (640, 640), color=(255, 255, 255))
    path=str(__file__).replace('utils/modles.py','assets/GoogleSans-Regular.ttf')
    font = ImageFont.truetype(path, 180)
    draw = ImageDraw.Draw(img)
    draw.text((114, 206), text, font=font, fill=(106, 99, 99))

    byte_data = io.BytesIO()
    img.save(byte_data, 'PNG')

    return byte_data.getvalue()


def generate_time_image() -> tuple:
    now = datetime.strftime(datetime.now(), "%H:%M")
    return generate_image(now)
