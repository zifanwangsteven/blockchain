from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User
from algosdk import mnemonic

def validate_mnemonic(form, field):
    try:
        mnemonic.to_private_key(field.data)
    except:
        raise ValidationError("Invalid Mnemonic")

class RegisterAccount(FlaskForm):
    public_account = StringField("Your Algorand Public Account", validators=[DataRequired()])
    submit = SubmitField('Submit')

class MnemonicForm(FlaskForm):
    mnemonic = StringField("Your 16-word Mnemonic", validators=[DataRequired(), validate_mnemonic])
    submit = SubmitField('Submit')

