from dotenv import load_dotenv
import os
import requests

load_dotenv()
NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")
HEADERS = {
    "X-Naver-Client-Id": NAVER_CLIENT_ID,
    "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
}


def searchLocal(names: list):
    doc = []
    url = "https://openapi.naver.com/v1/search/local"
    for name in names:
        params = {"query": name, "display": 5}
        res = requests.get(url, params, headers=HEADERS)
        try:
            res.raise_for_status()
            doc.extend(res.json()["items"])
        except Exception as e:
            print(e)

    return doc


def searchWeb(names: list):
    doc = {}
    url = "https://openapi.naver.com/v1/search/webkr"
    for name in names:
        params = {"query": name, "display": 10}
        res = requests.get(url, params, headers=HEADERS)
        try:
            res.raise_for_status()
            doc[name] = res.json()["items"]
        except Exception as e:
            print(e)

    return doc


if __name__ == "__main__":
    print(
        searchLocal(
            [
                "김&안 치과 의원",
                "김형우 안용석 차과의원",
                "백세튼튼정형외과의원",
                "디와이텔레콤",
                "다이소 신림점",
            ]
        )
    )
    print(
        searchWeb(
            [
                "김&안 치과 의원",
                "김형우 안용석 차과의원",
                "백세튼튼정형외과의원",
                "디와이텔레콤",
                "다이소 신림점",
            ]
        )
    )
