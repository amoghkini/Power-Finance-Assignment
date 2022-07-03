from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, SelectField
from wtforms.validators import DataRequired

class searchForm(FlaskForm):
    searchName = StringField('Search something', validators=[DataRequired()])
    caseSensitive = SelectField('Match Case', default="Yes", choices=['Yes','No'], validators=[DataRequired()])
    matchWholeWord = SelectField('Match Whole World', default="Yes", choices=['Yes', 'No'], validators=[DataRequired()])
    submit = SubmitField('Search')
