from pyzbar.pyzbar import decode
from PIL import Image

a = decode(Image.open('qrcode.png'))
print(a[0].data.decode("utf-8"))

