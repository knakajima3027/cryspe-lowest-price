import requests
from bs4 import BeautifulSoup
import re

import sys
sys.path.append('../')
from app.config import session

sys.path.append('../')
from app.models import Magi

html = requests.get("https://magi.camp/categories/100009/items?page=3")
soup = BeautifulSoup(html.text,'html.parser')
boxs = soup.find_all(class_='item-list__box')

for box in boxs:
    card = Magi()
    if not box.find(class_="item-list__sold-icon"):                    # 「売り切れか」判定
        card.img_url    = box.find('img').get('data-src')
        card.card_name  = box.find(class_="item-list__item-name").string          # カード名
        card.card_price = int(re.sub("\\D", "", box.find(class_="item-list__price-box--price").string.split(" ")[-1]))   # 値段
        card.url        = "https://magi.camp" + box.find("a").get('href')         # リンク  
        card.sale_id    = ("https://magi.camp" + box.find("a").get('href')).split('/')[-1]

        session.add(card)  
        session.commit()