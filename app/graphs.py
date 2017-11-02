import json
import operator
import plotly


def _get_list_from_multiple_field_entry(pd_series):
    pd_series = pd_series.dropna()
    return pd_series.str.split('|')


def _generate_graph_dict(title='Insert title here', x=None, y=None, mode=None, graph_type=None, orientation=None,
                         xaxis_title='Insert xaxis title here', yaxis_title='Insert yaxis title here', color='#FF0000',
                         line_width=2, line_color='#ffba13'):
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


def gender_count(df):
    g = df['gender'].value_counts()
    g.sort_index(inplace=True)
    x = g.index
    y = g.values
    graph_type = 'bar'
    title = 'Gender Count'
    return _generate_graph_dict(title=title, x=x, y=y, graph_type=graph_type, color='#7e113a', line_color='#ffba13')


def salary_for_years_of_exp(df):
    sal_exp = (df[['annual_amount_earned_from_all_tech_activities_combined', 'years_of_professional_experience']].replace(
                   '[\$,)]', '', regex=True).replace('[(]', '-', regex=True).astype(float))
    x = sal_exp['annual_amount_earned_from_all_tech_activities_combined']
    y = sal_exp['years_of_professional_experience']
    mode = 'markers'
    xaxis_title = 'Total Compensation'
    yaxis_title = 'Years of Professional Experience'
    title = 'Total Compensation for Years of Professional Experience'
    return _generate_graph_dict(title=title, x=x, y=y, mode=mode, xaxis_title=xaxis_title, yaxis_title=yaxis_title,
                                color='#fb000f', line_color='#042755')


def tech_roles(df):
    roles = _get_list_from_multiple_field_entry(df['tech_roles'])
    num_users = len(roles)

    counter = {}
    for index, role_list in roles.iteritems():
        for item in role_list:
            counter[item] = counter.get(item, 0) + 1

    for k, v in counter.iteritems():
        counter[k] = round(100 * (float(counter[k]) / float(num_users)), 2)

    sorted_role_pct_list = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)

    y = [item[1] for item in sorted_role_pct_list]
    x = [item[0] for item in sorted_role_pct_list]

    return _generate_graph_dict(x=x, y=y, graph_type='bar', xaxis_title=None,
                                title='Percentage of Respondents who Identify with Tech Role', yaxis_title=None,
                                color='#ff0900', line_color='#341b00')


def compile_graph_data(df):
    graphs = (gender_count(df),
              salary_for_years_of_exp(df),
              tech_roles(df))


    # Add "ids" to each of the graphs
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return ids, graphJSON




