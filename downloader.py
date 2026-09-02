import requests
import random
import os

PEXELS_API_KEY = "PUT_YOUR_API_KEY_HERE"

headers = {
    "Authorization": PEXELS_API_KEY
}

categories = [
    "nature",
    "ocean",
    "waterfall",
    "forest",
    "mountain"
]

category = random.choice(categories)

url = f"https://api.pexels.com/videos/search?query={category}&per_page=20"

response = requests.get(url, headers=headers)

data = response.json()

video = random.choice(data["videos"])

video_url = video["video_files"][0]["link"]

os.makedirs("downloads", exist_ok=True)

video_data = requests.get(video_url)

with open("downloads/video.mp4", "wb") as f:
    f.write(video_data.content)

print("Downloaded:", category)
