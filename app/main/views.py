from flask import render_template, redirect, url_for, abort, flash, request, jsonify
from flask_login import login_required, current_user
from app.main.graphing.graphs import get_graph_dict
from app.main.graphing.data_analysis import get_user_data_df
from app.static.survey.survey import questions_by_category, cleveland_tech_survey
from . import main
from .forms import EditSurveyForm
from .. import db
from ..models import User


@main.route('/')
def index():
    num_respondents = User.query.filter_by().count()
    return render_template('index.html', cleveland_tech_survey=cleveland_tech_survey, num_respondents=num_respondents)


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/data', methods=['GET', 'POST'])
def post_chart_data():
    users = User.query.filter_by().all()
    df = get_user_data_df(users)
    chart_title = request.data
    graph_dict = get_graph_dict(df, chart_title, users)
    return jsonify({'graph_dict': graph_dict})


@main.route('/survey/<username>')
def survey(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('survey.html', user=user, questions=questions_by_category)


@main.route('/edit-survey', methods=['GET', 'POST'])
@login_required
def edit_survey():
    form = EditSurveyForm()
    if form.validate_on_submit():
        current_user.gender = form.gender.data
        current_user.ethnicity = form.ethnicity.data
        current_user.highest_educational_attainment = form.highest_educational_attainment.data
        current_user.undergraduate_major = form.undergraduate_major.data
        current_user.how_you_learned_to_code = '|'.join(form.how_you_learned_to_code.data)
        current_user.primary_programming_languages_used_at_work = '|'.join(form.primary_programming_languages_used_at_work.data)
        current_user.primary_database_technologies_used_at_work = '|'.join(form.primary_database_technologies_used_at_work.data)
        current_user.primary_platforms_used_at_work = '|'.join(form.primary_platforms_used_at_work.data)
        current_user.primary_development_environments_used_at_work = '|'.join(form.primary_development_environments_used_at_work.data)
        current_user.primary_version_control_systems_used_at_work = '|'.join(form.primary_version_control_systems_used_at_work.data)
        current_user.tech_roles = '|'.join(form.tech_roles.data)
        current_user.years_of_professional_experience = form.years_of_professional_experience.data
        current_user.total_compensation = form.total_compensation.data
        current_user.satisfaction_with_compensation = form.satisfaction_with_compensation.data
        current_user.what_you_value_most_in_compensation = '|'.join(form.what_you_value_most_in_compensation.data)
        current_user.how_many_days_per_week_you_work_from_home = form.how_many_days_per_week_you_work_from_home.data
        current_user.company_size = form.company_size.data
        current_user.total_hours_worked_per_week = form.total_hours_worked_per_week.data
        current_user.job_satisfaction = form.job_satisfaction.data
        current_user.a_customer_calls_late_friday_evening = form.a_customer_calls_late_friday_evening.data
        current_user.work_life_balance = form.work_life_balance.data
        current_user.how_you_found_your_current_job = '|'.join(form.how_you_found_your_current_job.data)
        current_user.most_annoying_work_issue = '|'.join(form.most_annoying_work_issue.data)
        current_user.favorite_office_perk = '|'.join(form.favorite_office_perk.data)
        current_user.what_keeps_you_in_cleveland = '|'.join(form.what_keeps_you_in_cleveland.data)
        current_user.favorite_cleveland_pro_sports_team = form.favorite_cleveland_pro_sports_team.data
        current_user.favorite_cleveland_hangout_area = form.favorite_cleveland_hangout_area.data
        current_user.favorite_cleveland_activity = form.favorite_cleveland_activity.data
        current_user.feedback = form.feedback.data
        db.session.add(current_user)
        flash('Thanks for updating your survey responses!')
        return redirect(url_for('.survey', username=current_user.username))
    form.gender.data = current_user.gender
    form.ethnicity.data = current_user.ethnicity
    form.highest_educational_attainment.data = current_user.highest_educational_attainment
    form.undergraduate_major.data = current_user.undergraduate_major
    form.how_you_learned_to_code.data = current_user.how_you_learned_to_code
    form.primary_programming_languages_used_at_work.data = current_user.primary_programming_languages_used_at_work
    form.primary_database_technologies_used_at_work.data = current_user.primary_database_technologies_used_at_work
    form.primary_platforms_used_at_work.data = current_user.primary_platforms_used_at_work
    form.primary_development_environments_used_at_work.data = current_user.primary_development_environments_used_at_work
    form.primary_version_control_systems_used_at_work.data = current_user.primary_version_control_systems_used_at_work
    form.tech_roles.data = current_user.tech_roles
    form.years_of_professional_experience.data = current_user.years_of_professional_experience
    form.total_compensation.data = current_user.total_compensation
    form.satisfaction_with_compensation.data = current_user.satisfaction_with_compensation
    form.what_you_value_most_in_compensation.data = current_user.what_you_value_most_in_compensation
    form.how_many_days_per_week_you_work_from_home.data = current_user.how_many_days_per_week_you_work_from_home
    form.company_size.data = current_user.company_size
    form.total_hours_worked_per_week.data = current_user.total_hours_worked_per_week
    form.job_satisfaction.data = current_user.job_satisfaction
    form.a_customer_calls_late_friday_evening.data = current_user.a_customer_calls_late_friday_evening
    form.work_life_balance.data = current_user.work_life_balance
    form.how_you_found_your_current_job.data = current_user.how_you_found_your_current_job
    form.most_annoying_work_issue.data = current_user.most_annoying_work_issue
    form.favorite_office_perk.data = current_user.favorite_office_perk
    form.what_keeps_you_in_cleveland.data = current_user.what_keeps_you_in_cleveland
    form.favorite_cleveland_pro_sports_team.data = current_user.favorite_cleveland_pro_sports_team
    form.favorite_cleveland_hangout_area.data = current_user.favorite_cleveland_hangout_area
    form.favorite_cleveland_activity.data = current_user.favorite_cleveland_activity
    form.feedback.data = current_user.feedback
    return render_template('edit_survey.html', form=form)

# TODO: add admin-edit-survey
