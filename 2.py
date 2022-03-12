from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route('/training/<prof>')
def training(prof):
    param = {}
    param['title'] = prof
    param['typet'] = prof
    return render_template('typeT.html', **param)


if __name__ == '__main__':
    main()
