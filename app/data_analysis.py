import pandas as pd


def analyze_user_data(users):
    user_dict_list = [u.__dict__ for u in users]
    df = pd.DataFrame(user_dict_list)

    data = {}
    data['gender_counts'] = df['gender'].value_counts().to_dict()
    return data




