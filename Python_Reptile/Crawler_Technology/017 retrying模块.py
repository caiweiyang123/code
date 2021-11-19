import requests
from retrying import retry


@retry(stop_max_attempt_number=3)
def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    print(11111)

    # 发送请求，获取response
    response = requests.get(url, headers=headers, timeout=2)
    return response


def test(url):
    response = get_data(url)
    return response


if __name__ == '__main__':
    url = "http://www.google.com"
    test(url)
