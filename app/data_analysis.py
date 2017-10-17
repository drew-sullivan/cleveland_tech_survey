import pandas as pd
import numpy as np

from .models import User
from collections import Counter


def get_ratio_of_genders_among_users():
    users = User.query.filter_by().all()
    responses = Counter()
    for user in users:
        if user.gender is not None:
            gender = user.gender.lower()
            if gender == 'male':
                responses['male'] += 1
            elif gender == 'female':
                responses['female'] += 1
            elif gender == 'other':
                responses['other'] += 1
            else:
                responses['prefer_not_to_says'] += 1
        else:
            responses['None'] += 1
    return responses


def print_it_all():
    users = User.query.filter_by().all()
    l = [u.__dict__ for u in users]
    df = pd.DataFrame(l)
    return df
