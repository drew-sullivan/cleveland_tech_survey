from flask import render_template, redirect, url_for, abort, flash
from flask_login import login_required, current_user

from app.static.graphing.data_analysis import get_user_data_df
from app.static.graphing.graphs import compile_graph_data
from app.static.survey.survey_questions_and_answers import labels
from . import main
from .forms import EditProfileForm, EditProfileAdminForm, EditSurveyForm
from .. import db
from ..decorators import admin_required
from ..models import Role, User


@main.route('/')
def index():
    users = User.query.filter_by().all()
    num_respondents = len(users)
    df = get_user_data_df(users)
    ids, graphJSON = compile_graph_data(df)
    return render_template('index.html', ids=ids, graphJSON=graphJSON, num_respondents=num_respondents)


@main.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)


@main.route('/survey/<username>')
def survey(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('survey.html', user=user, questions=labels)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        flash('The profile has been updated.')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form, user=user)


@main.route('/edit-survey', methods=['GET', 'POST'])
@login_required
def edit_survey():
    form = EditSurveyForm()
    if form.validate_on_submit():
        current_user.tech_roles = '|'.join(form.tech_roles.data)
        current_user.years_of_professional_experience = form.years_of_professional_experience.data
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
        current_user.annual_amount_earned_from_all_tech_activities_combined = form.annual_amount_earned_from_all_tech_activities_combined.data
        current_user.what_you_value_most_in_compensation = '|'.join(form.what_you_value_most_in_compensation.data)
        current_user.how_many_days_per_week_you_work_from_home = form.how_many_days_per_week_you_work_from_home.data
        current_user.company_size = form.company_size.data
        current_user.job_satisfaction = form.job_satisfaction.data
        current_user.work_life_balance = form.work_life_balance.data
        current_user.how_you_found_your_current_job = '|'.join(form.how_you_found_your_current_job.data)
        current_user.most_annoying_work_issue = '|'.join(form.most_annoying_work_issue.data)
        current_user.favorite_office_perk = '|'.join(form.favorite_office_perk.data)
        current_user.what_keeps_you_in_cleveland = '|'.join(form.what_keeps_you_in_cleveland.data)
        current_user.favorite_cleveland_pro_sports_team = form.favorite_cleveland_pro_sports_team.data
        current_user.favorite_cleveland_hangout_area = form.favorite_cleveland_hangout_area.data
        current_user.favorite_cleveland_activity = form.favorite_cleveland_activity.data
        db.session.add(current_user)
        flash('Thanks for updating your survey responses!')
        return redirect(url_for('.survey', username=current_user.username))
    form.tech_roles.data = current_user.tech_roles
    form.years_of_professional_experience.data = current_user.years_of_professional_experience
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
    form.annual_amount_earned_from_all_tech_activities_combined.data = current_user.annual_amount_earned_from_all_tech_activities_combined
    form.what_you_value_most_in_compensation.data = current_user.what_you_value_most_in_compensation
    form.how_many_days_per_week_you_work_from_home.data = current_user.how_many_days_per_week_you_work_from_home
    form.company_size.data = current_user.company_size
    form.job_satisfaction.data = current_user.job_satisfaction
    form.work_life_balance.data = current_user.work_life_balance
    form.how_you_found_your_current_job.data = current_user.how_you_found_your_current_job
    form.most_annoying_work_issue.data = current_user.most_annoying_work_issue
    form.favorite_office_perk.data = current_user.favorite_office_perk
    form.what_keeps_you_in_cleveland.data = current_user.what_keeps_you_in_cleveland
    form.favorite_cleveland_pro_sports_team.data = current_user.favorite_cleveland_pro_sports_team
    form.favorite_cleveland_hangout_area.data = current_user.favorite_cleveland_hangout_area
    form.favorite_cleveland_activity.data = current_user.favorite_cleveland_activity
    return render_template('edit_survey.html', form=form)


# TODO: add admin-edit-survey
