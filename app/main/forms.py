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


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class EditSurveyForm(FlaskForm):
    questions = {}
    for k in survey_questions_and_answers.keys():
        questions[k] = [(v, v) for v in survey_questions_and_answers[k]]

    tech_roles = MultiCheckboxField('1. Tech Role', choices=questions["Tech Roles"])
    years_of_professional_experience = SelectField('2. Years of Professional Experience', choices=questions["Years of Professional Experience"], coerce=int)
    gender = SelectField('3. Gender', choices=questions["Gender"])
    ethnicity = SelectField('4. Ethnicity', choices=questions["Ethnicity"])
    highest_educational_attainment = SelectField('5. Highest Educational Attainment', choices=questions["Highest Educational Attainment"])
    undergraduate_major = SelectField('6. Undergraduate Major', choices=questions["Undergraduate Major"])
    how_you_learned_to_code = MultiCheckboxField('7. How You Learned to Code', choices=questions["How You Learned to Code"])
    primary_programming_languages_used_at_work = MultiCheckboxField('8. Primary Programming Languages Used at Work', choices=questions["Primary Programming Languages Used at Work"])
    primary_database_technologies_used_at_work = MultiCheckboxField('9. Primary Database Technologies Used at Work', choices=questions["Primary Database Technologies Used at Work"])
    primary_platforms_used_at_work = MultiCheckboxField('10. Primary Platforms Used at Work', choices=questions["Primary Platforms Used at Work"])
    primary_development_environments_used_at_work = MultiCheckboxField('11. Primary Development Environments Used at Work', choices=questions["Primary Development Environments Used at Work"])
    primary_version_control_systems_used_at_work = MultiCheckboxField('12. Primary Version Control Systems Used at Work', choices=questions["Primary Version Control Systems Used at Work"])
    annual_amount_earned_from_all_tech_activities_combined = SelectField('13. Annual Amount Earned From all Tech Activities Combined', choices=questions["Annual Amount Earned From all Tech Activities Combined"])
    what_you_value_most_in_compensation = MultiCheckboxField("14. What You Value Most in Compensation", choices=questions["What You Value Most in Compensation"])
    how_many_days_per_week_you_work_from_home = SelectField("15. How Many Days Per Week You Work From Home", choices=questions["How Many Days Per Week You Work From Home"], coerce=int)
    company_size = SelectField('16. Company Size', choices=questions["Company Size"])
    job_satisfaction = SelectField('17. Job Satisfaction', choices=questions["Job Satisfaction"], coerce=int)
    work_life_balance = SelectField('18. Work Life Balance', choices=questions["Work Life Balance"], coerce=int)
    how_you_found_your_current_job = MultiCheckboxField('19. How You Found Your Current Job', choices=questions["How You Found Your Current Job"])
    most_annoying_work_issue = MultiCheckboxField('20. Most Annoying Work Issue', choices=questions["Most Annoying Work Issue"])
    favorite_office_perk = MultiCheckboxField('21. Favorite Office Perk', choices=questions["Favorite Office Perk"])
    what_keeps_you_in_cleveland = MultiCheckboxField('22. What Keeps You in Cleveland', choices=questions["What Keeps You in Cleveland"])
    favorite_cleveland_pro_sports_team = SelectField('23. Favorite Cleveland Pro Sports Team', choices=questions["Favorite Cleveland Pro Sports Team"])
    favorite_cleveland_hangout_area = SelectField('24. Favorite Cleveland Hangout Area', choices=questions["Favorite Cleveland Hangout Area"])
    favorite_cleveland_activity = SelectField('25. Favorite Cleveland Activity', choices=questions["Favorite Cleveland Activity"])
    submit = SubmitField('Submit')







