# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,SubmitField, SelectMultipleField, TextAreaField, widgets
from wtforms.validators import DataRequired
from app.static.survey.survey import cleveland_tech_survey


def _get_answer_tuples():
    answer_tuples = {}
    categories = cleveland_tech_survey.keys()
    for category in categories:
        questions = cleveland_tech_survey[category]
        for question in questions:
            answer_tuples[question] = [(answer, answer) for answer in cleveland_tech_survey[category][question]]
    return answer_tuples


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class EditSurveyForm(FlaskForm):
    answer_tuples_by_question = _get_answer_tuples()

    # community_profile = cleveland_tech_survey["Community Profile"]
    # technology = cleveland_tech_survey["Technology"]
    # work = cleveland_tech_survey["Work"]
    # cleveland = cleveland_tech_survey["Cleveland"]

    gender = SelectField('Gender', choices=answer_tuples_by_question["Gender"])
    # print '\n'
    # print gender
    # print '\n'
    # print answer_tuples_by_question['Gender']
    # print '\n'
    ethnicity = SelectField('Ethnicity', choices=answer_tuples_by_question["Ethnicity"])
    highest_educational_attainment = SelectField('Highest Educational Attainment', choices=answer_tuples_by_question["Highest Educational Attainment"])
    undergraduate_major = SelectField('Undergraduate Major', choices=answer_tuples_by_question["Undergraduate Major"])
    how_you_learned_to_code = MultiCheckboxField('How You Learned to Code', choices=answer_tuples_by_question["How You Learned to Code"])
    primary_programming_languages_used_at_work = MultiCheckboxField('Primary Programming Languages Used at Work', choices=answer_tuples_by_question["Primary Programming Languages Used at Work"])
    primary_database_technologies_used_at_work = MultiCheckboxField('Primary Database Technologies Used at Work', choices=answer_tuples_by_question["Primary Database Technologies Used at Work"])
    primary_platforms_used_at_work = MultiCheckboxField('Primary Platforms Used at Work', choices=answer_tuples_by_question["Primary Platforms Used at Work"])
    primary_development_environments_used_at_work = MultiCheckboxField('Primary Development Environments Used at Work', choices=answer_tuples_by_question["Primary Development Environments Used at Work"])
    primary_version_control_systems_used_at_work = MultiCheckboxField('Primary Version Control Systems Used at Work', choices=answer_tuples_by_question["Primary Version Control Systems Used at Work"])
    tech_roles = MultiCheckboxField('Tech Role', choices=answer_tuples_by_question["Tech Roles"])
    years_of_professional_experience = SelectField('Years of Professional Experience', choices=answer_tuples_by_question["Years of Professional Experience"], coerce=int)
    total_compensation = SelectField('Annual Amount Earned From all Tech Activities Combined', choices=answer_tuples_by_question["Total Compensation"])
    satisfaction_with_compensation = SelectField('Satisfaction with Compensation', choices=answer_tuples_by_question["Satisfaction with Compensation"], coerce=int)
    what_you_value_most_in_compensation = MultiCheckboxField("What You Value Most in Compensation", choices=answer_tuples_by_question["What You Value Most in Compensation"])
    how_many_days_per_week_you_work_from_home = SelectField("How Many Days Per Week You Work From Home", choices=answer_tuples_by_question["How Many Days Per Week You Work From Home"], coerce=int)
    company_size = SelectField('Company Size', choices=answer_tuples_by_question["Company Size"])
    total_hours_worked_per_week = SelectField('Total Hours Worked Per Week', choices=answer_tuples_by_question["Total Hours Worked Per Week"], coerce=int)
    job_satisfaction = SelectField('Job Satisfaction', choices=answer_tuples_by_question["Job Satisfaction"], coerce=int)
    a_customer_calls_late_friday_evening = SelectField('A Customer Calls Late Friday Evening', choices=answer_tuples_by_question["A Customer Calls Late Friday Evening"])
    work_life_balance = SelectField('Work Life Balance', choices=answer_tuples_by_question["Work Life Balance"], coerce=int)
    how_you_found_your_current_job = MultiCheckboxField('How You Found Your Current Job', choices=answer_tuples_by_question["How You Found Your Current Job"])
    most_annoying_work_issue = MultiCheckboxField('Most Annoying Work Issue', choices=answer_tuples_by_question["Most Annoying Work Issue"])
    favorite_office_perk = MultiCheckboxField('Favorite Office Perk', choices=answer_tuples_by_question["Favorite Office Perk"])
    what_keeps_you_in_cleveland = MultiCheckboxField('What Keeps You in Cleveland', choices=answer_tuples_by_question["What Keeps You in Cleveland"])
    favorite_cleveland_pro_sports_team = SelectField('Favorite Cleveland Pro Sports Team', choices=answer_tuples_by_question["Favorite Cleveland Pro Sports Team"])
    favorite_cleveland_hangout_area = SelectField('Favorite Cleveland Hangout Area', choices=answer_tuples_by_question["Favorite Cleveland Hangout Area"])
    favorite_cleveland_activity = SelectField('Favorite Cleveland Activity', choices=answer_tuples_by_question["Favorite Cleveland Activity"])
    feedback = TextAreaField('Please provide feedback for the survey')

    submit = SubmitField('Submit')
