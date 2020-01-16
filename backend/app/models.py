import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime

try:
    from app.config import Base
except:
    from config import Base

try:
    from app.config import ENGINE
except:
    from config import ENGINE


class Card(Base):
    __tablename__ = 'CardDB' # テーブル名

    key = Column('id', Integer, primary_key = True)  # 識別キー

    card_name  = Column('card_name', String(100))  # カード名                              
    card_price = Column('card_price', Integer)     # カードの値段                        
    sale_id    = Column('sales_id', String(50))    # カードの販売ID
    url        = Column('url', String(150))        # カード詳細ページURL
    img_url    = Column('img_url', String(150))    # カード画像のURL
    store_id   = Column('store', String(150))      # カード販売サイト名


# 実行するとテーブルを生成
def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)