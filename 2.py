from flask import Flask, render_template, redirect
from json import loads
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class Login(FlaskForm):
    username_1 = StringField('Id космонавта', validators=[DataRequired()])
    password_1 = PasswordField('Пароль', validators=[DataRequired()])
    username_2 = StringField('Id капитана', validators=[DataRequired()])
    password_2 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')


def main():
    app.run()


@app.route('/list_prof/<args>')
def list_prof(args):
    param = {}
    param['ol_ul'] = args
    return render_template('ol_ul.html', **param)


@app.route('/member')
def member():
    param = {}
    with open("templates/data_members.json", "rt", encoding="utf8") as f:
        data = loads(f.read())
        param['data'] = data
    return render_template('lichnaya.html', **param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        return redirect('/norm')
    return render_template('login.html', title='Аварийный доступ', form=form)



@app.route('/norm')
def success():
    return render_template('success.html', title='Успешная авторизация')


if __name__ == '__main__':
    main()
