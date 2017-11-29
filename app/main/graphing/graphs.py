from app.main.graphing.graph_tools import generate_pie_chart_percentage_dict,\
    generate_horizontal_line_chart_dict, generate_scatter_chart_dict,\
    generate_vertical_bar_chart_dict


def _get_title_and_df_keys_from_tab_value(chart_title):
    """Remove extra quotes from Jinja template and separate multi-column chart titles"""
    chart_title = chart_title.replace('"', '')
    axes_titles = chart_title.split(' / ')
    df_keys = [item.lower().replace(' ', '_') for item in axes_titles]
    return chart_title, df_keys, axes_titles


def get_graph_dict(df, chart_title, users, suffix='', yaxis_title=None):
    title, df_keys, axes_titles = _get_title_and_df_keys_from_tab_value(chart_title)
    if len(df_keys) >= 2:
        xaxis_title = axes_titles[0]
        yaxis_title = axes_titles[1]
        x = df_keys[0]
        y = df_keys[1]
        x_y_data = df[[x, y]]
        x_y_data.iloc[:, 1] = x_y_data[y].replace('[\$,)]', '', regex=True).astype(int)
        data = x_y_data.groupby('gender')['total_compensation'].mean().astype(int)
        x = list(data.index)
        print x
        y = ['${:,}'.format(value) for value in data.values]
        print y
        return generate_vertical_bar_chart_dict(title=title, x=x, y=y, xaxis_title=xaxis_title, yaxis_title=yaxis_title)
    else:
        pd_series = df[df_keys[0]]
        if len(pd_series.unique()) <= 5:
            return generate_pie_chart_percentage_dict(title=title, pd_series=pd_series, suffix=suffix)
        return generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, yaxis_title=yaxis_title)
