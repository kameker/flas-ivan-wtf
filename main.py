import json

from flask import Flask, render_template
from werkzeug.utils import redirect

from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route('/')
@app.route('/index/<title>')
def index(title):
    param = {}
    param['username'] = "И на Марсе будут яблони цвести!"
    param['title'] = title
    return render_template('index.html', **param)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=3)


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/training/<prof>')
def training(prof):
    param = {}
    param['title'] = prof
    param['typet'] = prof
    return render_template('typeT.html', **param)


if __name__ == '__main__':
    main()
