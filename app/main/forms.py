# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from ..models import Role, User
from ..survey_questions_and_answers import survey_questions_and_answers


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class EditSurveyForm(FlaskForm):
    questions = {}
    for k in survey_questions_and_answers.keys():
        questions[k] = [(v, v) for v in survey_questions_and_answers[k]]

    tech_roles = SelectMultipleField('1. Tech Role (Hold the CTRL or CMD key to select more than one)', choices=questions["Tech Roles"])
    years_of_professional_experience = SelectField('2. Years of Professional Experience', choices=questions["Years of Professional Experience"], coerce=int)
    gender = SelectField('3. Gender', choices=questions["Gender"])
    ethnicity = SelectField('4. Ethnicity', choices=questions["Ethnicity"])
    highest_educational_attainment = SelectField('5. Highest Educational Attainment', choices=questions["Highest Educational Attainment"])
    submit = SubmitField('Submit')







