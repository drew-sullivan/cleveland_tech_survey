import itertools
import json
import plotly

from . import graph_tools
from graph_tools import COLORS as color
from collections import Counter


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


def salary_for_language(df):
    sal_lang = df[
        ['annual_amount_earned_from_all_tech_activities_combined', 'primary_programming_languages_used_at_work']].dropna()
    salaries = sal_lang['annual_amount_earned_from_all_tech_activities_combined'].replace(
        '[\$,)]', '', regex=True).replace('[(]', '-', regex=True).astype(float)
    languages = sal_lang['primary_programming_languages_used_at_work']
    languages_as_lists = graph_tools.get_values_as_lists(languages)
    flat_list = itertools.chain.from_iterable(languages_as_lists)
    c = Counter(flat_list)


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
              ethnicities(df))

    # Add "ids" to each of the graphs
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return ids, graphJSON
