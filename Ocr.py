import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("UPSTAGE_API_KEY")
# filename = "test.png"
url = "https://api.upstage.ai/v1/document-ai/ocr"
headers = {"Authorization": f"Bearer {api_key}"}


def ocr(doc):
    files = {"document": doc}
    response = requests.post(url, headers=headers, files=files)
    # print(response.json())
    resj = response.json()
    img_text = resj["text"]

    return img_text
