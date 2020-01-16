import requests
from bs4 import BeautifulSoup
import re
from time import sleep 

import sys
sys.path.append('../')
from app.config import session

sys.path.append('../')
from app.models import Card


# 既存のデータを削除
session.query(Card).filter(Card.store_id=="magi").delete()
session.commit()


# Magiのスクレイピング
for i in range(1, 10 ** 2):
    html = requests.get(
        "https://magi.camp/items/search?forms_search_items%5Bcategory_id%5D=100009&forms_search_items%5Bfrom_price%5D=&forms_search_items%5Bkeyword%5D=&forms_search_items%5Bpage%5D=1&forms_search_items%5Bquality%5D=&forms_search_items%5Bsort%5D=&forms_search_items%5Bstatus%5D=presented&forms_search_items%5Btag_id%5D=&forms_search_items%5Bto_price%5D=&page={}"
        .format(i)
        )
    soup = BeautifulSoup(html.text,'html.parser')
    boxs = soup.find_all(class_='item-list__box')

    if boxs:
        for box in boxs:
            card = Card()         
            card.img_url     = box.find('img').get('data-src')                                                                # 画像URL
            card.card_name   = box.find(class_="item-list__item-name").string
            card.card_price  = int(re.sub("\\D", "", box.find(class_="item-list__price-box--price").string.split(" ")[-1]))   # 値段
            card.url         = "https://magi.camp" + box.find("a").get('href')                                                # リンク  
            card.sale_id     = ("https://magi.camp" + box.find("a").get('href')).split('/')[-1]
            card.store_id    = "magi"

            # DBにデータを追加
            session.add(card)  
            session.commit()

        sleep(5) #5秒間待機してから次のスクレイピング
    
    else:
        break


# イーサマーケット