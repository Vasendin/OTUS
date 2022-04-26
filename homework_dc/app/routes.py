from app import app
from app import db
from flask import render_template, flash, redirect, url_for, request
from app.forms import Faddduser
from app.models import User


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def usr():
    users = User.query.all()
    return render_template('lists/users.html', title='Пользователи', users=users)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form1 = Faddduser()
    if form1.validate_on_submit():
        user = User(username=form1.name.data,
                    email=form1.email.data
                    )
        db.session.add(user)
        db.session.commit()
        flash('Пользователь добавлен')
        return redirect(url_for('usr'))
    else:
        flash('Пользователь не добавлен')
    return render_template('lists/add_row.html', title='Новый пользователь', form=form1, user=User.query.all())


@app.route('/delete_user', methods=['GET', 'POST'])
def delete_usr():
    row = request.form['del_id']
    drow = User.query.get(row)
    db.session.delete(drow)
    db.session.commit()
    return redirect(url_for('usr'))
