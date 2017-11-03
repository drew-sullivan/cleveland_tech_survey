import json
import operator

import itertools
import plotly

from collections import Counter


CAVS_COLORS = ['#6F263D', '#FFB81C', '#041E42']
INDIANS_COLORS = ['#D50032', '#0C2340', '#FFFFFF']
BROWNS_COLORS = ['#EB3300', '#382F2D', '#FFFFFF']
MONSTERS_COLORS = ['#004EA6', '#F8F9FB', '#000000', '#FFBA00', '#FFFFFF']


def _get_values_as_lists(pd_series):
    """
    Turns values from pd_series from |-delimited strings to lists
    :param pd_series:
    :return list of lists:
    """
    values_as_strings = pd_series.dropna().values
    values_as_lists = [item.split('|') for item in values_as_strings]
    return values_as_lists


def _generate_non_pie_chart_dict(title='Insert title here', x=None, y=None, mode=None, graph_type=None,
                                 orientation=None, xaxis_title=None, yaxis_title=None, color='#FF0000', line_width=2,
                                 line_color='#ffba13'):
    graph = {
        'data': [
            {
                'x': x,
                'y': y,
                'mode': mode,
                'type': graph_type,
                'orientation': orientation,
                'marker': {
                    'color': color,
                    'line': {
                        'width': line_width,
                        'color': line_color
                    }
                }
            }
        ],
        'layout': {
            'xaxis': {'title': xaxis_title},
            'yaxis': {'title': yaxis_title},
            'title': title
        }
    }
    return graph


def _generate_pie_chart_dict(title='Insert Title Here', labels=['1st label', '2nd label'], values=[75, 25],
                             colors=['rgb(146, 123, 21)', 'rgb(177, 180, 34)'], chart_type='pie',
                             hoverinfo='label+percent', textinfo='none', showlegend=True, line_width=2,
                             line_color='black'):
    pie_chart_dict = {
        'data': [
            {
                'labels': labels,
                'values': values,
                'marker': {
                    'colors': colors,
                    'line': {
                        'width': line_width,
                        'color': line_color
                    }
                },
                'type': chart_type,
                'hoverinfo': hoverinfo,
                'textinfo': textinfo
            }
        ],
        'layout': {
            'title': title,
            'showlegend': showlegend}
    }
    return pie_chart_dict


def gender_count(df):
    g = df['gender'].value_counts()
    g.sort_index(inplace=True)
    x = g.index
    y = g.values
    graph_type = 'bar'
    title = 'Gender Count'
    return _generate_non_pie_chart_dict(title=title, x=x, y=y, graph_type=graph_type,
                                        color=CAVS_COLORS[0], line_color=CAVS_COLORS[1])


def salary_for_years_of_exp(df):
    sal_exp = (df[['annual_amount_earned_from_all_tech_activities_combined', 'years_of_professional_experience']].replace(
                   '[\$,)]', '', regex=True).replace('[(]', '-', regex=True).astype(float))
    x = sal_exp['annual_amount_earned_from_all_tech_activities_combined']
    y = sal_exp['years_of_professional_experience']
    mode = 'markers'
    xaxis_title = 'Total Compensation'
    yaxis_title = 'Years of Professional Experience'
    title = 'Total Compensation for Years of Professional Experience'
    return _generate_non_pie_chart_dict(title=title, x=x, y=y, mode=mode, xaxis_title=xaxis_title,
                                        yaxis_title=yaxis_title, color=INDIANS_COLORS[0], line_color=INDIANS_COLORS[1])


def tech_roles(df):
    roles_as_lists_per_user = _get_values_as_lists(df['tech_roles'])
    num_users = len(roles_as_lists_per_user)
    flat_list = itertools.chain.from_iterable(roles_as_lists_per_user)
    c = Counter(flat_list)
    c = c.most_common()
    tech_role_names = [item[0] for item in c]
    tech_role_percents = [round(100 * float(item[1]) / float(num_users), 2) for item in c]

    return _generate_non_pie_chart_dict(x=tech_role_names, y=tech_role_percents, graph_type='bar', xaxis_title=None,
                                        title='Percentage of Respondents who Identify with Tech Role', yaxis_title=None,
                                        color=BROWNS_COLORS[0], line_color=BROWNS_COLORS[1])


def gender_percent(df):
    gender_data = df['gender'].value_counts(normalize=True)
    labels = gender_data.sort_index().index
    values = gender_data.round(2).sort_index().values
    return _generate_pie_chart_dict(title='Gender Breakdown', labels=labels, values=values,
                                    colors=CAVS_COLORS+['#d3d3d3'])


def compile_graph_data(df):
    graphs = (gender_count(df),
              gender_percent(df),
              salary_for_years_of_exp(df),
              tech_roles(df))


    # Add "ids" to each of the graphs
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return ids, graphJSON




