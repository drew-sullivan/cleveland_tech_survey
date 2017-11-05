import json

import plotly

from app.static.graphing import graph_tools
from app.static.graphing.graph_tools import COLORS as color


def gender_count(df):
    g = df['gender'].value_counts()
    g.sort_index(inplace=True)
    x = g.index
    y = g.values
    graph_type = 'bar'
    title = 'Gender Count'
    return graph_tools.generate_non_pie_chart_dict(title=title, x=x, y=y, graph_type=graph_type,
                                                   color=color['cavaliers']['wine'],
                                                   line_color=color['cavaliers']['gold'])


def gender_by_percent(df):
    title = 'Gender by Percent'
    colors = color['cavaliers'].values() + ['#d3d3d3']
    pd_series = df['gender']
    return graph_tools.generate_pie_chart_percentage_dict(title=title, colors=colors, pd_series=pd_series)


def years_of_pro_experience(df):
    title = 'Range of Experience'
    colors = color['cavaliers'].values() + ['#d3d3d3']
    pd_series = df['years_of_professional_experience']
    suffix = ' year(s)'
    return graph_tools.generate_pie_chart_percentage_dict(title=title, colors=colors, pd_series=pd_series,
                                                          suffix=suffix)


def ethnicities(df):
    title = 'Ethnicities'
    colors = color['cavaliers'].values() + ['#d3d3d3']
    pd_series = df['ethnicity']
    return graph_tools.generate_pie_chart_percentage_dict(title=title, colors=colors, pd_series=pd_series)


def salary_for_years_of_exp(df):
    sal_exp = (df[['annual_amount_earned_from_all_tech_activities_combined', 'years_of_professional_experience']].replace(
                   '[\$,)]', '', regex=True).replace('[(]', '-', regex=True).astype(float))
    x = sal_exp['annual_amount_earned_from_all_tech_activities_combined']
    y = sal_exp['years_of_professional_experience']
    mode = 'markers'
    xaxis_title = 'Total Compensation'
    yaxis_title = 'Years of Professional Experience'
    title = 'Total Compensation for Years of Professional Experience'
    return graph_tools.generate_non_pie_chart_dict(title=title, x=x, y=y, mode=mode, xaxis_title=xaxis_title,
                                                   yaxis_title=yaxis_title, color=color['indians']['red'],
                                                   line_color=color['indians']['navy'])


def tech_roles(df):
    title = 'Percentage of Respondents who Identify with Tech Role'
    pd_series = df['tech_roles']
    color_scheme = 'browns'
    color_1 = 'orange'
    color_2 = 'brown'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def most_common_languages(df):
    title = 'Most Common Programming Languages Used'
    pd_series = df['primary_programming_languages_used_at_work']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def most_common_db_technologies(df):
    title = 'Most Common Database Technologies Used'
    pd_series = df['primary_database_technologies_used_at_work']
    color_scheme = 'browns'
    color_1 = 'brown'
    color_2 = 'orange'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def most_common_platform(df):
    title = 'Most Common Platforms Used'
    pd_series = df['primary_platforms_used_at_work']
    color_scheme = 'monsters'
    color_1 = 'blue'
    color_2 = 'wine'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def most_common_dev_env(df):
    title = 'Most Common Development Environments Used'
    pd_series = df['primary_development_environments_used_at_work']
    color_scheme = 'indians'
    color_1 = 'navy'
    color_2 = 'red'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def most_common_version_control(df):
    title = 'Most Common Version Control Systems Used'
    pd_series = df['primary_version_control_systems_used_at_work']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def educational_attainment(df):
    title = 'Educational Attainment'
    pd_series = df['highest_educational_attainment']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def undergraduate_major(df):
    title = 'Undergraduate Major'
    pd_series = df['undergraduate_major']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def how_you_learned_to_code(df):
    title = 'How You Learned to Code'
    pd_series = df['how_you_learned_to_code']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def what_you_value_most_in_compensation(df):
    title = 'What You Value Most in Compensation'
    pd_series = df['what_you_value_most_in_compensation']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def how_many_days_per_week_you_work_from_home(df):
    title = 'How Many Days Per Week You Work From Home'
    pd_series = df['how_many_days_per_week_you_work_from_home']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    yaxis_title = 'Days Per Week'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2, yaxis_title=yaxis_title)


def company_size(df):
    title = 'Company Size'
    pd_series = df['company_size']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def job_satisfaction(df):
    title = 'Job Satisfaction'
    pd_series = df['job_satisfaction']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    yaxis_title = 'Deeply Unsatisfied --> Extremely Satisfied'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2, yaxis_title=yaxis_title)


def work_life_balance(df):
    title = 'Work Life Balance'
    pd_series = df['work_life_balance']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    yaxis_title = 'Non-Stop Work --> Extremely Flexible'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2, yaxis_title=yaxis_title)


def how_you_found_your_current_job(df):
    title = 'How You Found Your Current Job'
    pd_series = df['how_you_found_your_current_job']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def most_annoying_work_issue(df):
    title = 'Most Annoying Work Issue'
    pd_series = df['most_annoying_work_issue']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def favorite_office_perk(df):
    title = 'Favorite Office Perk'
    pd_series = df['favorite_office_perk']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def what_keeps_you_in_cleveland(df):
    title = 'What Keeps You in Cleveland'
    pd_series = df['what_keeps_you_in_cleveland']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def favorite_cleveland_pro_sports_team(df):
    title = 'Favorite Cleveland Pro Sports Team'
    colors = color['cavaliers'].values() + ['#d3d3d3']
    pd_series = df['favorite_cleveland_pro_sports_team']
    return graph_tools.generate_pie_chart_percentage_dict(title=title, colors=colors, pd_series=pd_series)


def favorite_cleveland_hangout_area(df):
    title = 'Favorite Cleveland Hangout Area'
    pd_series = df['favorite_cleveland_hangout_area']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def favorite_cleveland_activity(df):
    title = 'Favorite Cleveland Activity'
    pd_series = df['favorite_cleveland_activity']
    color_scheme = 'cavaliers'
    color_1 = 'wine'
    color_2 = 'gold'
    return graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, color_scheme=color_scheme,
                                                           color_1=color_1, color_2=color_2)


def compile_graph_data(df):
    graphs = (gender_count(df),
              gender_by_percent(df),
              salary_for_years_of_exp(df),
              tech_roles(df),
              most_common_languages(df),
              most_common_db_technologies(df),
              most_common_platform(df),
              most_common_dev_env(df),
              most_common_version_control(df),
              years_of_pro_experience(df),
              ethnicities(df),
              educational_attainment(df),
              undergraduate_major(df),
              how_you_learned_to_code(df),
              what_you_value_most_in_compensation(df),
              how_many_days_per_week_you_work_from_home(df),
              company_size(df),
              job_satisfaction(df),
              work_life_balance(df),
              how_you_found_your_current_job(df),
              most_annoying_work_issue(df),
              favorite_office_perk(df),
              what_keeps_you_in_cleveland(df),
              favorite_cleveland_pro_sports_team(df),
              favorite_cleveland_hangout_area(df),
              favorite_cleveland_activity(df)
              )

    # Add "ids" to each of the graphing
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return ids, graphJSON
