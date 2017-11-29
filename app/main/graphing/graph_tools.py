import itertools
import random
from collections import Counter


COLORS = {
    'cavaliers': {'wine': '#6F263D', 'gold': '#FFB81C', 'navy': '#041E42'},
    'indians': {'red': '#D50032', 'navy': '#0C2340', 'white': '#FFFFFF'},
    'browns': {'orange': '#EB3300', 'brown': '#382F2D', 'white': '#FFFFFF'},
    'monsters': {'wine': '#940033', 'blue': '#004EA6',  'gold': '#FFBA00', 'white': '#FFFFFF', 'black': '#000000'}
}


def _get_colors():
    random_team = random.choice(COLORS.keys())
    color_scheme = COLORS[random_team]
    if random_team == 'cavaliers':
        color = color_scheme['wine']
        line_color = color_scheme['gold']
    elif random_team == 'browns':
        color = color_scheme['brown']
        line_color = color_scheme['orange']
    elif random_team == 'indians':
        color = color_scheme['red']
        line_color = color_scheme['navy']
    else:
        color = color_scheme['wine']
        line_color = color_scheme['blue']
    return color, line_color


def generate_non_pie_chart_dict(title='Insert title here', x=None, y=None, mode=None, graph_type=None,
                                orientation=None, xaxis_title=None, yaxis_title=None, text=None,
                                color='#000', line_width=2, line_color='#FFF', left_margin=None,
                                right_margin=None, top_margin=None, bottom_margin=None, xaxis_ticksuffix=None,
                                xaxis_showticksuffix=None, yaxis_side=None, tooltip_labels=None):
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
                },
                'text': tooltip_labels
            }
        ],
        'layout': {
            'xaxis': {
                'title': xaxis_title,
                'ticksuffix': xaxis_ticksuffix,
                'showticksuffix': xaxis_showticksuffix
            },
            'yaxis': {
                'title': yaxis_title,
                'side': yaxis_side
            },
            'title': title,
            'margin': {
                'l': left_margin,
                'r': right_margin,
                't': top_margin,
                'b': bottom_margin
            }
        },
    }
    return graph


def generate_pie_chart_dict(title='Insert Title Here', labels=['1st label', '2nd label'], values=[75, 25],
                             colors=COLORS['cavaliers'].values() + ['#D3D3D3'], chart_type='pie',
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
            'showlegend': showlegend
        },
        'show_link': False
    }
    return pie_chart_dict


def generate_scatter_chart_dict(title, x, y, xaxis_title, yaxis_title):
    chart_colors = _get_colors()
    return generate_non_pie_chart_dict(title=title, x=x, y=y, mode='markers', xaxis_title=xaxis_title,
                                       yaxis_title=yaxis_title, color=chart_colors[0], line_color=chart_colors[1])


def generate_vertical_bar_chart_dict(title='Title Here', x=None, y=None, xaxis_title=None, yaxis_title=None):
    chart_colors = _get_colors()
    return generate_non_pie_chart_dict(title=title, x=x, y=y, graph_type='bar',
                                       color=chart_colors[0], line_color=chart_colors[1],
                                       xaxis_title=xaxis_title, yaxis_title=yaxis_title, left_margin=150)


def generate_horizontal_line_chart_dict(title='Title Here', pd_series=None, xaxis_title='Percentage of Respondents',
                                        yaxis_title=None):
    user_responses = _transform_strings_to_lists(pd_series)
    num_users = len(user_responses)
    flat_list = itertools.chain.from_iterable(user_responses)
    c = Counter(flat_list)
    list_of_least_common_elements = c.most_common()
    list_of_most_common_elements = list_of_least_common_elements[::-1]

    percentages = _get_percentage_list(num_users, list_of_most_common_elements)
    tooltip_labels = _get_tooltip_labels(list_of_most_common_elements)
    yaxis_labels = _get_short_yaxis_labels(tooltip_labels)
    chart_colors = _get_colors()
    return generate_non_pie_chart_dict(title=title, x=percentages, y=yaxis_labels, graph_type='bar',
                                       color=chart_colors[0], line_color=chart_colors[1], orientation='h',
                                       xaxis_title=xaxis_title, yaxis_title=yaxis_title, xaxis_ticksuffix='%',
                                       xaxis_showticksuffix='all', tooltip_labels=tooltip_labels, left_margin=250)


def generate_pie_chart_percentage_dict(title=None, pd_series=None, suffix=''):
    pd_series = pd_series.dropna()
    exp_data = pd_series.value_counts(normalize=True)
    sorted_labels = exp_data.sort_index()
    labels = [str(label) for label in sorted_labels.index]
    labels += suffix
    labels = list(labels)  # changed to list to accommodate json encoding for ajax call
    values = list(exp_data.round(2).sort_index().values)  # changed to list to accommodate json encoding for ajax call
    return generate_pie_chart_dict(title=title, labels=labels, values=values)


def _transform_strings_to_lists(pd_series):
    """
    Turns values from pd_series from |-delimited strings to lists
    :param pd_series:
    :return list of lists:
    """
    values_as_strings = pd_series.dropna().values.astype(str)
    values_as_lists = [item.split('|') for item in values_as_strings]
    return values_as_lists


def _get_percentage_list(num_users, list_of_items):
    return ['{}%'.format(round(100 * float(item[1]) / float(num_users), 2)) for item in list_of_items]


def _get_tooltip_labels(list_of_items):
    return [item[0] for item in list_of_items]


def _get_short_yaxis_labels(labels):
    MAX_LABEL_LEN = 35
    return ['{}...'.format(label[:MAX_LABEL_LEN - 3]) if len(label) >= MAX_LABEL_LEN else label for label in labels]


def _transform_currency_to_ints(pd_series):
    transformed_series = (pd_series.replace('[\$,)]', '', regex=True).astype(float))
    return transformed_series
