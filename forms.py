from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Email, EqualTo, URL


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username')
    password1 = PasswordField('Password')
    password2 = PasswordField('Repeat Password')
    submit = SubmitField('Register')


class CreateForm(FlaskForm):
    name = StringField('Name', render_kw={'placeholder': 'Name', 'class': 'border border-black'},
                       validators=[DataRequired()])
    map_url = URLField('Map URL', render_kw={'placeholder': 'Map URL', 'class': 'border border-black'},
                       validators=[DataRequired(), URL()])
    img_url = URLField('Image URL', render_kw={'placeholder': 'Image URL', 'class': 'border border-black'},
                       validators=[DataRequired(), URL()])
    location = StringField('Location', render_kw={'placeholder': 'Location', 'class': 'border border-black'},
                           validators=[DataRequired()])
    has_sockets = BooleanField('Has Sockets', render_kw={'class': 'border border-black'}, validators=[DataRequired()])
    has_toilet = BooleanField('Has Toilet', render_kw={'class': 'border border-black'}, validators=[DataRequired()])
    has_wifi = BooleanField('Has Wifi', render_kw={'class': 'border border-black'}, validators=[DataRequired()])
    can_take_calls = BooleanField('Can Take Calls', render_kw={'class': 'border border-black'},
                                  validators=[DataRequired()])
    seats = StringField('Seats', render_kw={'placeholder': 'Seats', 'class': 'border border-black'},
                        validators=[DataRequired()])
    coffee_price = StringField('Coffee Price',
                               render_kw={'placeholder': 'Coffee Price', 'class': 'border border-black'},
                               validators=[DataRequired()])
    submit = SubmitField('Create', render_kw={'class': 'btn btn-primary'})
