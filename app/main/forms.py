from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class MnemonicForm(FlaskForm):
    mnemonic = StringField("Please enter your algorand mnemonic?", validators=[DataRequired()])
    submit = SubmitField('Submit')
