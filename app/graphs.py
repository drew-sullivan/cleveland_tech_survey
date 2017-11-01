import json
import plotly


def generate_graph_dict(title='Insert title here', x=None, y=None, mode=None, graph_type=None, xaxis_title=None, yaxis_title=None):
    graph = {
        'data': [
            {
                'x': x,
                'y': y,
                'mode': mode,
                'type': graph_type}
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
    return generate_graph_dict(title=title, x=x, y=y, graph_type=graph_type)


def salary_for_years_of_exp(df):
    sal_exp = (df[['annual_amount_earned_from_all_tech_activities_combined', 'years_of_professional_experience']].replace(
                   '[\$,)]', '', regex=True).replace('[(]', '-', regex=True).astype(float))
    x = sal_exp['annual_amount_earned_from_all_tech_activities_combined']
    y = sal_exp['years_of_professional_experience']
    mode = 'markers'
    xaxis_title = 'Total Compensation'
    yaxis_title = 'Years of Professional Experience'
    title = 'Total Compensation for Years of Professional Experience'
    return generate_graph_dict(title=title, x=x, y=y, mode=mode, xaxis_title=xaxis_title, yaxis_title=yaxis_title)


def compile_graph_data(df):
    graphs = (gender_count(df),
              salary_for_years_of_exp(df))


    # Add "ids" to each of the graphs
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return ids, graphJSON




