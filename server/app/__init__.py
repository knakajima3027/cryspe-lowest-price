from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# config.pyを参照して設定を行う
app.config.from_object('app.config')

# データベースの定義
db = SQLAlchemy(app)

migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')
