from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class MyFilterForm(FlaskForm):
    my_filter = SelectField("my_filter", choices=["Comércio", "Administrativo", "Recursos Humanos", "Informática", "Logística"])


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")


class AddForm(FlaskForm):
    task = StringField("task", validators=[DataRequired(), Length(max = 30)])
    area = SelectField("area", choices=["Comércio", "Administrativo", "Recursos Humanos", "Informática", "Logística", "Outros"])
    city = StringField("city", validators=[DataRequired(), Length(max = 30)])
    state = StringField("state", validators=[DataRequired(), Length(max = 2)])
    wage = StringField("subject", validators=[DataRequired(), Length(max = 30)])
    company = StringField("subject", validators=[DataRequired(), Length(max = 100)])
    description = TextAreaField("subject", validators=[DataRequired()])
    assignmen = TextAreaField("subject", validators=[DataRequired()])


class ResetDb(FlaskForm):
    resetDb = SubmitField("Resetar")
