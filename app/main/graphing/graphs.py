from app.main.graphing.graph_tools import COLORS, generate_pie_chart_percentage_dict,\
    generate_horizontal_line_chart_dict, generate_non_pie_chart_dict


def salary_for_years_of_exp(pd_series):
    title = 'Compensation for Years of Professional Experience'
    sal_exp = (pd_series.replace('[\$,)]', '', regex=True).replace('[(]', '-', regex=True).astype(float))
    x = sal_exp['annual_amount_earned_from_all_tech_activities_combined']
    y = sal_exp['years_of_professional_experience']
    mode = 'markers'
    xaxis_title = 'Total Compensation'
    yaxis_title = 'Years of Professional Experience'
    return generate_non_pie_chart_dict(title=title, x=x, y=y, mode=mode, xaxis_title=xaxis_title,
                                                   yaxis_title=yaxis_title, color=COLORS['indians']['red'],
                                                   line_color=COLORS['indians']['navy'])


def get_title_and_df_key_from_tab_value(tab_values):
    title = tab_values.replace('"', '')
    df_keys = [tab_value.replace('"', '').lower().replace(' ', '_') for tab_value in tab_values.split(' / ')]
    return title, df_keys


def get_graph_dict(title, df, df_keys, suffix='', yaxis_title=None):
    if len(df_keys) >= 2:
        print '{} df_keys were passed in'.format(len(df_keys))
        xaxis_title = df_keys[0]
        yaxis_title = df_keys[1]
        pd_series_1 = df[xaxis_title]
        pd_series_2 = df[yaxis_title]
        color = COLORS['indians']['red']
        line_color = COLORS['indians']['navy']
        return generate_non_pie_chart_dict(title=title, x=pd_series_1, y=pd_series_2, mode='markers',
                                           xaxis_title=xaxis_title, yaxis_title=yaxis_title, color=color,
                                           line_color=line_color)
    else:
        pd_series = df[df_keys[0]]
        if len(pd_series.unique()) <= 5:
            return generate_pie_chart_percentage_dict(title=title, pd_series=pd_series, suffix=suffix)
        return generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, yaxis_title=yaxis_title)
