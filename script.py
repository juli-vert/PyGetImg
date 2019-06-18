import requests as rq
from io import BytesIO
from PIL import Image
from os import path
url = 'https://domain/base_route/'
for i in range(1,401):
    uri = '{0}.jpg'.format(str(i))
    u = path.join(url,uri)
    r = rq.get(u)
    img = Image.open(BytesIO(r.content))
    fpath = '{0}.bmp'.format(str(i))
    img.save(fpath)
