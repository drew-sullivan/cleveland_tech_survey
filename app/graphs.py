import json
import numpy as np
import pandas as pd
import plotly


rng = pd.date_range('1/1/2011', periods=25, freq='H')
ts = pd.Series(np.random.randn(len(rng)), index=rng)


def get_graph_dict(x=None, y=None, graph_type=None, title='Insert title here'):
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


def compile_graph_data(df):
    graphs = (get_graph_dict([1, 2, 3], [10, 20, 30], 'scatter', 'first graph'),
              get_graph_dict([1, 3, 5], [10, 20, 30], 'bar', 'second graph'),
              get_graph_dict(df['gender'].sort_values().dropna().unique(),
                             df['gender'].sort_values().value_counts(),
                             'bar', 'third graph'),
              get_graph_dict(ts.index, ts, title='fourth graph'))


    # Add "ids" to each of the graphs
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return ids, graphJSON




