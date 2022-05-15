from flask_wtf import FlaskForm
from wtforms import SelectField


class MyFilterForm(FlaskForm):
    my_filter = SelectField("my_filter", choices=['Comércio', 'Administrativo', 'Recursos Humanos', 'Informática', 'Logística'])