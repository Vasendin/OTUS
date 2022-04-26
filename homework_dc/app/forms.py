from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError
from app.models import User


class Faddduser(FlaskForm):
    name = StringField('Username')
    email = StringField('Email')
    submit = SubmitField('Записать')

    def validate_name(self, name):
        name = User.query.filter_by(username=name.data).first()
        if name is not None:
            raise ValidationError('Please use a different name.')
