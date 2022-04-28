from flask import Flask, render_template
from json import load
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
    with open('templates/data_members.json',encoding='UTF8') as inf:
        d = load(inf)
        random_member = sample([d[i] for i in d], 1)[0]
        proflist = ' '.join(sorted([i for i in random_member[3].split(',')], key=lambda x: x))
    param = {}
    param['member'] = random_member[2]
    param['proflist'] = proflist
    return render_template('lichnaya.html', **param)


if __name__ == '__main__':
    main()
