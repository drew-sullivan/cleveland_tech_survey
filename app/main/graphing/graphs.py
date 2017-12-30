from app.main.graphing.graph_tools import generate_horizontal_line_chart_dict, generate_box_and_whisker_dict


def _get_title_and_df_keys_from_tab_value(chart_title):
    """Remove extra quotes from Jinja template and separate multi-column chart titles"""
    chart_title = chart_title.replace('"', '')
    axes_titles = chart_title.split(' / ')
    df_keys = [item.lower().replace(' ', '_') for item in axes_titles]
    return chart_title, df_keys, axes_titles


def get_graph_dict(df, chart_title, yaxis_title=None):
    title, df_keys, axes_titles = _get_title_and_df_keys_from_tab_value(chart_title)
    pd_series = df[df_keys[0]]
    pd_series = pd_series.dropna()
    if pd_series.dtype == 'float64' or pd_series.dtype == 'int64' or ('$' in list(pd_series.values)[0]):
        return generate_box_and_whisker_dict(pd_series)
    return generate_horizontal_line_chart_dict(title='', pd_series=pd_series, yaxis_title=yaxis_title)
