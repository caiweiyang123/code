import time

import requests


class Image(object):
    def __init__(self):
        self.url = 'https://image.baidu.com/search/acjson?'
        self.headers = {
            'Cookie': 'BDqhfp=%E7%8B%97%26%260-10-1undefined%26%262668%26%263; __yjs_duid=1_4f0913ce9b51479cf6176498026c1b3e1624421808194; BIDUPSID=34D6429B6590F8A0EE856FBFC987DF67; PSTM=1624439149; BAIDUID=17B7B14C4A13A04C5660AC38D2AFA711:FG=1; BDSFRCVID_BFESS=470OJeC626eUvj3ePJ4U2MnMSBeXSJ7TH6aogmTplB-e8T41-grUEG0PVf8g0Ku-da8AogKK0eOTHk-F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=fRkq_CLaJCv5j5rF-JjHqR08bh_X5-CsJnkj2hcH0KLKMR5a54C5bq8pjb_HW46uL2r-hUOFJMb1MRjvbPcxK-AYqf_OLT0DHCvH-l5TtUJ4eCnTDMRhqt0_e-QyKMnitIT9-pnoHlQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKu-n5jHjJ3eHKt3f; MCITY=-289%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=34299_33802_31660_34277_34004_34072_34092_34094_26350_22160; BAIDUID_BFESS=CB5EA61BC7A5F09546A320494B6DABB9:FG=1; delPer=0; PSINO=3; BA_HECTOR=8k24812g8hak05811c1gfqt540q; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=www.baidu.com; firstShowTip=1; indexPageSugList=%5B%22%E7%8B%97%22%2C%22%E5%A4%96%E6%98%9F%E4%BA%BA%22%2C%22%E6%89%93%E5%A4%96%E6%98%9F%E4%BA%BA%E9%87%8C%E7%9A%84%E9%A3%9E%E8%88%B9%22%2C%22%E9%A3%9E%E8%88%B9%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_ZDc4MzI4NjM0MDQ4OTgzZjIxYjVlMzI2MWU3ODFkNTYxMTYyZDg0NWU3ZjU3YTQ3OTQwNzgxNGE5YzBmZDM1NGIzNzAxYjM5ODU2YjIzMWI3NzNiMDY0Mjk0NmQ5ZjBkMzcxZDBlZTQzZjhjMmI5YjY1MTY5Y2U2YzhmMDA3YTQ1OWJjYjNiNzdkZTNjMDlkM2UxMzgwYTQ3ZjE1ZjYyMg==',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
        self.params = {
            'tn': 'resultjson_com',
            'logid': '7043023419833912364',
            'ipn': 'rj',
            'ct': '201326592',
            'is': '',
            'fp': 'result',
            'queryWord': '狗',
            'cl': '2',
            'lm': '-1',
            'ie': 'utf - 8',
            'oe': 'utf - 8',
            'adpicid': '',
            'st': '-1',
            'z': '',
            'ic': '0',
            'hd': '',
            'latest': '',
            'copyright': '',
            'word': '狗',
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': '0',
            'istype': '2',
            'qc': '',
            'nc': '1',
            'fr': '',
            'expermode': '',
            'nojc': '',
            'pn': '',
            'rn': '30',
            'gsm': '',
            'time': ''
        }
        self.image_list = []

    def get_image(self, num):
        for i in range(0, num):
            self.params['time'] = int(time.time() * 1000)
            self.params['pn'] = i * 30
            response = requests.get(url=self.url, headers=self.headers, params=self.params)
            for j in range(0, len(response.json()['data']) - 1):
                self.image_list.append(response.json()['data'][j]['thumbURL'])

    def save_image(self):
        n = 1
        for i in self.image_list:
            image = requests.get(url=i)
            with open('./狗狗图片/{}.jpg'.format(n), 'wb')as f:
                f.write(image.content)
            n += 1


if __name__ == '__main__':
    image = Image()
    image.get_image(2)
    image.save_image()
