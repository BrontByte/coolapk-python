import io
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import requests
import json


def generate_image(text: str) -> bytes:
    img = Image.new('RGB', (640, 640), color=(255, 255, 255))
    path = str(__file__).replace('utils/image.py', 'assets/GoogleSans-Regular.ttf')
    font = ImageFont.truetype(path, 180)
    draw = ImageDraw.Draw(img)
    draw.text((114, 206), text, font=font, fill=(106, 99, 99))

    byte_data = io.BytesIO()
    img.save(byte_data, 'PNG')

    return byte_data.getvalue()


def generate_time_image() -> tuple:
    now = datetime.strftime(datetime.now(), "%H:%M")
    return generate_image(now)


def generate_btc_image() -> tuple:
    requests_get = requests.get(url='https://api.coindesk.com/v1/bpi/currentprice.json')
    request_json = json.loads(requests_get.text)
    price = request_json['bpi']['USD']['rate_float']
    now = '矿难了吗?\n     ' + datetime.strftime(datetime.now(), "%H:%M") + '\n' + str(price) + '\nUSD=1 BTC'
    return generate_btc(now)


def generate_btc(text: str) -> bytes:
    img = Image.new('RGB', (640, 640), color=(255, 255, 255))
    # path = str(__file__).replace('utils/image.py', '')
    font = ImageFont.truetype('C:/Users/BrontByte/IdeaProjects/coolapk-python/assets/SourceHanSans-VF.ttf.ttc',
                              layout_engine=ImageFont.LAYOUT_BASIC,
                              size=130)
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), text, font=font, fill=(106, 99, 99))

    byte_data = io.BytesIO()
    img.save(byte_data, 'PNG')

    return byte_data.getvalue()
