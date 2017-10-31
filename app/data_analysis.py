import pandas as pd


def get_user_data_df(users):
    user_dict_list = [u.__dict__ for u in users]
    return pd.DataFrame(user_dict_list)




