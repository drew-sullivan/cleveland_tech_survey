import itertools

from collections import Counter


COLORS = {
    'cavaliers': {'wine': '#6F263D', 'gold': '#FFB81C', 'navy': '#041E42'},
    'indians': {'red': '#D50032', 'navy': '#0C2340', 'white': '#FFFFFF'},
    'browns': {'orange': '#EB3300', 'brown': '#382F2D', 'white': '#FFFFFF'},
    'monsters': {'wine': '#940033', 'blue': '#004EA6',  'gold': '#FFBA00', 'white': '#FFFFFF', 'black': '#000000'}
}


def generate_non_pie_chart_dict(title='Insert title here', x=None, y=None, mode=None, graph_type=None,
                                orientation=None, xaxis_title=None, yaxis_title=None, color='#FF0000', line_width=2,
                                line_color='#ffba13', left_margin=None, right_margin=None, top_margin=None,
                                bottom_margin=None):
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
            'title': title,
            'margin': {
                'l': left_margin,
                'r': right_margin,
                't': top_margin,
                'b': bottom_margin
            }
        }
    }
    return graph


def generate_pie_chart_dict(title='Insert Title Here', labels=['1st label', '2nd label'], values=[75, 25],
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
            'showlegend': showlegend
        }
    }
    return pie_chart_dict


def generate_horizontal_line_chart_dict(title='Title Here', pd_series=None, color_scheme=None,
                                        color_1=None, color_2=None):
    color_1 = COLORS[color_scheme][color_1]
    color_2 = COLORS[color_scheme][color_2]
    lists_per_user = get_values_as_lists(pd_series)
    num_users = len(lists_per_user)
    flat_list = itertools.chain.from_iterable(lists_per_user)
    c = Counter(flat_list)
    list_of_least_common_elements = c.most_common()
    list_of_most_common_elements = list_of_least_common_elements[::-1]
    left_margin = None
    labels = [item[0] for item in list_of_most_common_elements]
    for item in labels:
        if len(item) > 10:
            left_margin = 180
            break
    percentages = [round(100 * float(item[1]) / float(num_users), 2) for item in list_of_most_common_elements]
    return generate_non_pie_chart_dict(title=title, x=percentages, y=labels, graph_type='bar',
                                       color=color_1, line_color=color_2, orientation='h', left_margin=left_margin)


def get_values_as_lists(pd_series):
    """
    Turns values from pd_series from |-delimited strings to lists
    :param pd_series:
    :return list of lists:
    """
    values_as_strings = pd_series.dropna().values
    values_as_lists = [item.split('|') for item in values_as_strings]
    return values_as_lists