from flask import Flask, render_template
from json import loads
from random import sample

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route('/list_prof/<args>')
def list_prof(args):
    param = {}
    param['ol_ul'] = args
    return render_template('ol_ul.html', **param)


@app.route('/member')
def member():
    with open("templates/data_members.json", "rt", encoding="utf8") as f:
        list_ = loads(f.read())
    return render_template('lichnaya.html', list_=list_)


if __name__ == '__main__':
    main()
