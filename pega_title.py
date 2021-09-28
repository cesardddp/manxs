from typing import Dict, List
from bs4 import BeautifulSoup as bs
import requests as r
import json

urls = [
    "https://youtu.be/wTNMsAUV-ck",
    "https://youtu.be/tx72vkCz5zw",
    "https://youtu.be/ZF1CX-GvWmE",
    "https://youtu.be/RNVth0WraVU",
    "https://youtu.be/hlP-lESKS44",
    "https://youtu.be/rciLqxxUcOU",
    "https://youtu.be/6Xdqu3aC_HE",
    "https://youtu.be/jqOIeAy7TFo",
]
videos = []
for video in urls:
    videos.append(
        {"titulo": bs(r.get(video).content, "html.parser").find("title").text, "src": video.split("/")[-1]}
    )
    # import pdb;pdb.set_trace()
    

print("json dumped",json.dump(videos,open("videos.json",'w')))
from pprint import pprint;pprint(videos)
