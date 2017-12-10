import pandas as pd
from app.static.survey.survey import questions_by_category


def get_user_data_df(users):
    user_dict_list = [u.__dict__ for u in users]
    df = pd.DataFrame(user_dict_list)
    return df


def clean_df_for_printing(df):
    cleaned_df = df[questions_by_category]
    return cleaned_df



