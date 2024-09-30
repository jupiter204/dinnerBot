from bs4 import BeautifulSoup
import requests
import random
import gc


class shopDict:
    name = ''
    tag = ''
    star = ''
    category = ''
    time = ''
    fee = ''

    def __init__(self, name, tag, star, category, time, fee):
        self.name = name
        self.tag = tag
        self.star = star
        self.category = category
        self.time = time
        self.fee = fee

    def __del__(self):
        pass


with open('url.txt', 'r') as f:
    url = f.readline()
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}
# print(url)


def eatWhat():
    page = requests.get(url, headers=header)
    page.encoding = 'utf-8'

    # with open('test.html', 'wb') as f:
    #     f.write(page.text.encode())
    #     return

    soup = BeautifulSoup(page.text, 'html.parser')
    shops = soup.find_all("li", class_="vendor-tile-new-l")
    list = []
    for shop in shops:
        name = shop.find('div', {
            'class': 'vendor-name f-title-small-font-size fw-title-small-font-weight lh-title-small-line-height ff-title-small-font-family'}).get_text()
        tag = 'https://www.foodpanda.com.tw'+shop.find('a').get('href')
        try:
            star = shop.find('span', {'class': 'rating--label-primary cl-rating-tag-text f-label-small-font-size fw-label-small-font-weight lh-label-small-line-height ff-label-small-font-family'}).text+' '+shop.find(
                'span', {'class': 'rating--label-secondary cl-neutral-secondary f-label-small-secondary-font-size fw-label-small-secondary-font-weight lh-label-small-secondary-line-height ff-label-small-secondary-font-family'}).text
        except:
            star = '沒有評價'
        category = shop.find('div', {'class': 'box-flex vendor-tile-new-info fd-column'}).select(
            'div.vendor-info-row')[0].select_one(':nth-child(1)').text
        time = shop.find('div', {'class': 'box-flex vendor-tile-new-info fd-column'}).select(
            'div.vendor-info-row')[1].select_one(':nth-child(2)').text
        fee = shop.find('div', {'class': 'box-flex vendor-tile-new-info fd-column'}
                        ).select('div.vendor-info-row')[1].select_one(':nth-child(5)').text
        # print(name, tag, star, category, time, fee)
        list.append(shopDict(name, tag, star, category, time, fee))

    del (name, tag, star, category, time, fee)
    gc.collect()
    num = random.randint(0, len(list))
    # print(num, len(list))
    img = f'https://images.deliveryhero.io/image/fd-tw/LH/{
        list[num].tag[40:44]}-listing.jpg?width=400&height=225'
    return list[num].name, list[num].tag, list[num].star, list[num].category, list[num].time, list[num].fee, img


if __name__ == '__main__':
    print(eatWhat())
