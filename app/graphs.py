import json
import numpy as np
import pandas as pd
import plotly


rng = pd.date_range('1/1/2011', periods=25, freq='H')
ts = pd.Series(np.random.randn(len(rng)), index=rng)


def generate_graph_dict(x=None, y=None, graph_type=None, title='Insert title here'):
    graph = dict(
                data=[
                    dict(
                        x=x,
                        y=y,
                        type=graph_type
                    ),
                ],
                layout=dict(
                    title=title
                )
            )
    return graph


def gender_count(df):
    g = df['gender'].value_counts()
    g.sort_index(inplace=True)
    x = g.index
    y = g.values
    graph_type = 'bar'
    title = 'Gender Count'
    return generate_graph_dict(x, y, graph_type, title)


def salary_for_years_of_exp(df):
    sal_exp = (df[['annual_amount_earned_from_all_tech_activities_combined', 'years_of_professional_experience']].replace(
                   '[\$,)]', '', regex=True).replace('[(]', '-', regex=True).astype(float))
    x = sal_exp['annual_amount_earned_from_all_tech_activities_combined']
    y = sal_exp['years_of_professional_experience']

    fig = {
        'data': [
            {
                'x': x,
                'y': y,
                'mode': 'markers'}
        ],
        'layout': {
            'xaxis': {'title': 'Total Compensation'},
            'yaxis': {'title': 'Years of Professional Experience'},
            'title': 'Total Compensation for Years of Professional Experience'
        }
    }
    return fig


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




