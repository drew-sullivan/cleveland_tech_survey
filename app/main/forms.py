from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, SelectMultipleField, widgets
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from ..models import Role, User


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
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


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class EditSurveyForm(FlaskForm):
    job_options = ['Consultant (who also writes code)',
                   'Consultant (who does NOT write code)',
                   'Data Scientist',
                   'Database Administrator',
                   'Desktop App Developer',
                   'Developer with Statistics or Mathematics Background',
                   'DevOps Specialist',
                   'Embedded Applications/Devices Developer',
                   'Graphic Designer',
                   'Graphics Programming',
                   'Manager (who also writes code)',
                   'Manger (who does NOT write code)',
                   'Machine Learning Specialist',
                   'Mobile Developer',
                   'Quality Assurance Engineer',
                   'Sales Engineer',
                   'Systems Administrator',
                   'Web Developer',
                   'Other']
    value_description_tuples = [(job, job) for job in job_options]
    jobs = SelectMultipleField('1. Tech Role (Hold the CTRL or CMD key to select more than one)',
                               choices=value_description_tuples)
    submit = SubmitField('Submit')







