import requests
from bs4 import BeautifulSoup

html = requests.get("https://magi.camp/categories/100009/items?page=3")
soup = BeautifulSoup(html.text,'html.parser')
boxs = soup.find_all(class_='item-list__box')

for box in boxs:
   # print(box)
    if not box.find(class_="item-list__sold-icon"):                    # 「売り切れか」判定
        print(box.find('img').get('data-src'))                         # 画像URL
        print(box.find(class_="item-list__item-name").string)          # カード名
        print(box.find(class_="item-list__price-box--price").string)   # 値段
        print("https://magi.camp" + box.find("a").get('href'))         # リンク  
    print("----------------------")