CAVALIERS_COLORS = ['#6F263D', '#FFB81C', '#041E42']
INDIANS_COLORS = ['#D50032', '#0C2340', '#FFFFFF']
BROWNS_COLORS = ['#EB3300', '#382F2D', '#FFFFFF']
MONSTERS_COLORS = ['#004EA6', '#F8F9FB', '#000000', '#FFBA00', '#FFFFFF']


def generate_non_pie_chart_dict(title='Insert title here', x=None, y=None, mode=None, graph_type=None,
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
            'showlegend': showlegend}
    }
    return pie_chart_dict


def get_values_as_lists(pd_series):
    """
    Turns values from pd_series from |-delimited strings to lists
    :param pd_series:
    :return list of lists:
    """
    values_as_strings = pd_series.dropna().values
    values_as_lists = [item.split('|') for item in values_as_strings]
    return values_as_lists