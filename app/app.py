from flask import Flask, render_template, request
from models.models import OnegaiContent

from models.database import db_session
from datetime import datetime

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
  name = request.args.get("name") # クエリストリングからname属性の値を受け取る
  all_onegai = OnegaiContent.query.all()
  return render_template("index.html", name=name, all_onegai=all_onegai) # index.htmlにnameの情報を送ってWebページを表示させる


@app.route("/index", methods=["post"])
def post():
  name = request.args.get("name") # クエリストリングからname属性の値を受け取る
  all_onegai = OnegaiContent.query.all()
  return render_template("index.html", name=name, all_onegai=all_onegai)

@app.route("/add", methods=["post"])
def add():
  title = request.form["title"]
  body = request.form["body"]
  content = OnegaiContent(title=title, body=body, date=datetime.now())
  db_session.add(content)
  db_session.commit()
  return index()

if __name__ == "__main__":
    app.run(debug=True)

