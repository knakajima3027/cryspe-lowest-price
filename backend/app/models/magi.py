import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from app import db

class Magi(db.Model):
    __tablename__ = 'magi_db' # テーブル名

    key = Column('id', Integer, primary_key = True)  # 識別キー

    card_name  = Column('card_name', String(100))  # カード名                              
    card_price = Column('card_price', Integer)     # カードの値段                        
    sale_id    = Column('sales_id', String(50))    # カードの販売ID
    url        = Column('url', String(150))        # カード詳細ページURL
    img_url    = Column('img_url', String(150))    # カード画像のURL