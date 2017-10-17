import pandas as pd
import numpy as np

from .models import User


def analyze_user_data():
    users = User.query.filter_by().all()
    user_dict_list = [u.__dict__ for u in users]
    df = pd.DataFrame(user_dict_list)

    data = {}
    data['gender_counts'] = df['gender'].value_counts().to_dict()
    return data




