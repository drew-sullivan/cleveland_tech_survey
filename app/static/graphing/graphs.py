import json
import plotly

from app.static.graphing import graph_tools
from app.static.graphing.graph_tools import COLORS as color


def gender_count(pd_series):
    g = pd_series.value_counts()
    g.sort_index(inplace=True)
    x = g.index
    y = g.values
    graph_type = 'bar'
    title = 'Gender Count'
    return graph_tools.generate_non_pie_chart_dict(title=title, x=x, y=y, graph_type=graph_type,
                                                   color=color['cavaliers']['wine'],
                                                   line_color=color['cavaliers']['gold'])


def gender_by_percent(pd_series):
    title = 'Gender by Percent'
    colors = color['cavaliers'].values() + ['#d3d3d3']
    return graph_tools.generate_pie_chart_percentage_dict(title=title, colors=colors, pd_series=pd_series)


def years_of_pro_experience(pd_series):
    title = 'Range of Experience'
    colors = color['cavaliers'].values() + ['#d3d3d3']
    suffix = ' year(s)'
    return graph_tools.generate_pie_chart_percentage_dict(title=title, colors=colors, pd_series=pd_series,
                                                          suffix=suffix)


def ethnicities(pd_series):
    title = 'Ethnicities'
    colors = color['cavaliers'].values() + ['#d3d3d3']
    return graph_tools.generate_pie_chart_percentage_dict(title=title, colors=colors, pd_series=pd_series)


def salary_for_years_of_exp(pd_series):
    title = 'Compensation for Years of Professional Experience'
    sal_exp = (pd_series.replace('[\$,)]', '', regex=True).replace('[(]', '-', regex=True).astype(float))
    x = sal_exp['annual_amount_earned_from_all_tech_activities_combined']
    y = sal_exp['years_of_professional_experience']
    mode = 'markers'
    xaxis_title = 'Total Compensation'
    yaxis_title = 'Years of Professional Experience'
    return graph_tools.generate_non_pie_chart_dict(title=title, x=x, y=y, mode=mode, xaxis_title=xaxis_title,
                                                   yaxis_title=yaxis_title, color=color['indians']['red'],
                                                   line_color=color['indians']['navy'])


def tech_roles(pd_series):
    title = 'Tech Roles'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def most_common_languages(pd_series):
    title = 'Programming Languages Used'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def most_common_db_technologies(pd_series):
    title = 'Database Technologies Used'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def most_common_platform(pd_series):
    title = 'Platforms Used'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def most_common_dev_env(pd_series):
    title = 'Development Environments Used'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def most_common_version_control(pd_series):
    title = 'Version Control Systems Used'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def educational_attainment(pd_series):
    title = 'Educational Attainment'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def undergraduate_major(pd_series):
    title = 'Undergraduate Major'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def how_you_learned_to_code(pd_series):
    title = 'Learning to Code'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def what_you_value_most_in_compensation(pd_series):
    title = 'Most Valued Compensation'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def how_many_days_per_week_you_work_from_home(pd_series):
    title = 'Remote Work Per Week'
    yaxis_title = 'Days Per Week'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, yaxis_title=yaxis_title)


def company_size(pd_series):
    title = 'Company Size'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def job_satisfaction(pd_series):
    title = 'Job Satisfaction'
    yaxis_title = 'Deeply Unsatisfied --> Extremely Satisfied'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, yaxis_title=yaxis_title)


def work_life_balance(pd_series):
    title = 'Work Life Balance'
    yaxis_title = 'Non-Stop Work --> Extremely Flexible'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, yaxis_title=yaxis_title)


def how_you_found_your_current_job(pd_series):
    title = 'How You Found Your Current Job'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def most_annoying_work_issue(pd_series):
    title = 'Most Annoying Work Issue'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def favorite_office_perk(pd_series):
    title = 'Favorite Office Perk'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def what_keeps_you_in_cleveland(pd_series):
    title = 'What Keeps You in Cleveland'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def favorite_cleveland_pro_sports_team(pd_series):
    title = 'Favorite Cleveland Sports Team'
    colors = color['cavaliers'].values() + ['#d3d3d3']
    return graph_tools.generate_pie_chart_percentage_dict(title=title, colors=colors, pd_series=pd_series)


def favorite_cleveland_hangout_area(pd_series):
    title = 'Favorite Cleveland Hangout Area'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def favorite_cleveland_activity(pd_series):
    title = 'Favorite Cleveland Activity'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series)


def compile_graph_data(df):
    graphs = (tech_roles(df['tech_roles']),
              years_of_pro_experience(df['years_of_professional_experience']),
              gender_count(df['gender']),
              gender_by_percent(df['gender']),
              ethnicities(df['ethnicity']),
              educational_attainment(df['highest_educational_attainment']),
              undergraduate_major(df['undergraduate_major']),
              how_you_learned_to_code(df['how_you_learned_to_code']),
              most_common_languages(df['primary_programming_languages_used_at_work']),
              most_common_db_technologies(df['primary_database_technologies_used_at_work']),
              most_common_platform(df['primary_platforms_used_at_work']),
              most_common_dev_env(df['primary_development_environments_used_at_work']),
              most_common_version_control(df['primary_version_control_systems_used_at_work']),
              salary_for_years_of_exp(df[['annual_amount_earned_from_all_tech_activities_combined',
                                          'years_of_professional_experience']]),
              what_you_value_most_in_compensation(df['what_you_value_most_in_compensation']),
              how_many_days_per_week_you_work_from_home(df['how_many_days_per_week_you_work_from_home']),
              company_size(df['company_size']),
              job_satisfaction(df['job_satisfaction']),
              work_life_balance(df['work_life_balance']),
              how_you_found_your_current_job(df['how_you_found_your_current_job']),
              most_annoying_work_issue(df['most_annoying_work_issue']),
              favorite_office_perk(df['favorite_office_perk']),
              what_keeps_you_in_cleveland(df['what_keeps_you_in_cleveland']),
              favorite_cleveland_pro_sports_team(df['favorite_cleveland_pro_sports_team']),
              favorite_cleveland_hangout_area(df['favorite_cleveland_hangout_area']),
              favorite_cleveland_activity(df['favorite_cleveland_activity']))

    ids = ['{}'.format(i) for i, _ in enumerate(graphs)]

    ids_and_titles = tuple(('{}'.format(i), graph['layout']['title']) for i, graph in enumerate(graphs))

    titles = [graph['layout']['title'] for graph in graphs]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return ids, ids_and_titles, titles, graphJSON


def get_graphs(df):
    graphs = (tech_roles(df['tech_roles']),
              years_of_pro_experience(df['years_of_professional_experience']),
              gender_count(df['gender']),
              gender_by_percent(df['gender']),
              ethnicities(df['ethnicity']),
              educational_attainment(df['highest_educational_attainment']),
              undergraduate_major(df['undergraduate_major']),
              how_you_learned_to_code(df['how_you_learned_to_code']),
              most_common_languages(df['primary_programming_languages_used_at_work']),
              most_common_db_technologies(df['primary_database_technologies_used_at_work']),
              most_common_platform(df['primary_platforms_used_at_work']),
              most_common_dev_env(df['primary_development_environments_used_at_work']),
              most_common_version_control(df['primary_version_control_systems_used_at_work']),
              salary_for_years_of_exp(df[['annual_amount_earned_from_all_tech_activities_combined',
                                          'years_of_professional_experience']]),
              what_you_value_most_in_compensation(df['what_you_value_most_in_compensation']),
              how_many_days_per_week_you_work_from_home(df['how_many_days_per_week_you_work_from_home']),
              company_size(df['company_size']),
              job_satisfaction(df['job_satisfaction']),
              work_life_balance(df['work_life_balance']),
              how_you_found_your_current_job(df['how_you_found_your_current_job']),
              most_annoying_work_issue(df['most_annoying_work_issue']),
              favorite_office_perk(df['favorite_office_perk']),
              what_keeps_you_in_cleveland(df['what_keeps_you_in_cleveland']),
              favorite_cleveland_pro_sports_team(df['favorite_cleveland_pro_sports_team']),
              favorite_cleveland_hangout_area(df['favorite_cleveland_hangout_area']),
              favorite_cleveland_activity(df['favorite_cleveland_activity']))
    return graphs


def get_graph_title(df, graph_id):
    id_as_int = int(filter(str.isdigit, graph_id))
    graphs = get_graphs(df)
    return graphs[id_as_int]['layout']['title']
