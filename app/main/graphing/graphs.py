from app.main.graphing.graph_tools import generate_pie_chart_percentage_dict,\
    generate_horizontal_line_chart_dict


def _get_title_and_df_keys_from_tab_value(chart_title):
    """Remove extra quotes from Jinja template and separate multi-column chart titles"""
    chart_title = chart_title.replace('"', '')
    axes_titles = chart_title.split(' / ')
    df_keys = [item.lower().replace(' ', '_') for item in axes_titles]
    return chart_title, df_keys, axes_titles


def get_graph_dict(df, chart_title, suffix='', yaxis_title=None):
    title, df_keys, axes_titles = _get_title_and_df_keys_from_tab_value(chart_title)
    pd_series = df[df_keys[0]]
    return generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, yaxis_title=yaxis_title)
