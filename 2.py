from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route('/list_prof/<args>')
def list_prof(args):
    param = {}
    param['ol_ul'] = args
    return render_template('ol_ul.html', **param)


if __name__ == '__main__':
    main()
