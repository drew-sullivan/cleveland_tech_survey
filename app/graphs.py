import itertools
import json
import plotly

from . import graph_tools
from collections import Counter


def gender_count(df):
    g = df['gender'].value_counts()
    g.sort_index(inplace=True)
    x = g.index
    y = g.values
    graph_type = 'bar'
    title = 'Gender Count'
    return graph_tools.generate_non_pie_chart_dict(title=title, x=x, y=y, graph_type=graph_type,
                                                   color=graph_tools.CAVALIERS_COLORS[0],
                                                   line_color=graph_tools.CAVALIERS_COLORS[1])


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
                                                   yaxis_title=yaxis_title, color=graph_tools.INDIANS_COLORS[0],
                                                   line_color=graph_tools.INDIANS_COLORS[1])


def tech_roles(df):
    roles_as_lists_per_user = graph_tools.get_values_as_lists(df['tech_roles'])
    num_users = len(roles_as_lists_per_user)
    flat_list = itertools.chain.from_iterable(roles_as_lists_per_user)
    c = Counter(flat_list)
    c = c.most_common()
    tech_role_names = [item[0] for item in c]
    tech_role_percents = [round(100 * float(item[1]) / float(num_users), 2) for item in c]
    return graph_tools.generate_non_pie_chart_dict(x=tech_role_names, y=tech_role_percents, graph_type='bar',
                                                   xaxis_title=None,
                                                   title='Percentage of Respondents who Identify with Tech Role',
                                                   yaxis_title=None, color=graph_tools.BROWNS_COLORS[0],
                                                   line_color=graph_tools.BROWNS_COLORS[1])


def gender_by_percent(df):
    gender_data = df['gender'].value_counts(normalize=True)
    labels = gender_data.sort_index().index
    values = gender_data.round(2).sort_index().values
    return graph_tools.generate_pie_chart_dict(title='Gender by Percent', labels=labels, values=values,
                                               colors=graph_tools.CAVALIERS_COLORS + ['#d3d3d3'])


def compile_graph_data(df):
    graphs = (gender_count(df),
              gender_by_percent(df),
              salary_for_years_of_exp(df),
              tech_roles(df))

    # Add "ids" to each of the graphs
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return ids, graphJSON




