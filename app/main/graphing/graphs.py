from app.main.graphing.graph_tools import COLORS, generate_pie_chart_percentage_dict,\
    generate_horizontal_line_chart_dict, generate_non_pie_chart_dict


def get_title_and_df_key_from_tab_value(tab_values):
    title = tab_values.replace('"', '')
    df_keys = [tab_value.replace('"', '').lower().replace(' ', '_') for tab_value in tab_values.split(' / ')]
    return title, df_keys


def get_graph_dict(title, df, df_keys, users, suffix='', yaxis_title=None):
    if len(df_keys) >= 2:
        xaxis_title = df_keys[0]
        yaxis_title = df_keys[1]
        x = [getattr(u, xaxis_title) for u in users]
        y = [getattr(u, yaxis_title) for u in users]
        mode = 'markers'
        xaxis_title = xaxis_title.replace('_', ' ').title()
        yaxis_title = yaxis_title.replace('_', ' ').title()
        return generate_non_pie_chart_dict(title=title, x=x, y=y, mode=mode, xaxis_title=xaxis_title, yaxis_title=yaxis_title)
    else:
        pd_series = df[df_keys[0]]
        if len(pd_series.unique()) <= 5:
            return generate_pie_chart_percentage_dict(title=title, pd_series=pd_series, suffix=suffix)
        return generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, yaxis_title=yaxis_title)
