import requests
import base64
from PIL import Image
import io
import random



host = 'localhost'


payload = {
    "prompt":"Beautiful Young woman:SuperGirl , ultra detailed, 8k, trending on art station,beautiful lighting",
    "steps":50
}

def DecodeStableDiffusionImage(dic:dict)->Image:
    for i in responsedict['images']:
        return Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))


r = requests.post(url=f"http://{host}:7860/sdapi/v1/txt2img",json=payload)
responsedict = r.json()
image = DecodeStableDiffusionImage(responsedict)
image.save(f"stablediffusionimage{random.randint(1,10000)}.png")


