import itertools
import pandas as pd
import numpy as np

from app.static.survey.survey import cleveland_tech_survey as cts, questions_by_category
from app.main.graphing.graph_tools import transform_strings_to_lists, transform_currency_to_ints
from collections import Counter


def get_user_data_df(users):
    user_dict_list = [u.__dict__ for u in users]
    df = pd.DataFrame(user_dict_list)
    return df


def clean_df_for_printing(df):
    cleaned_df = df[questions_by_category]
    return cleaned_df


def get_community_profile(df):
    community_profile = cts
    categories = cts.keys()
    question_title = ''
    for category in categories:
        questions = cts[category]
        for question in questions:
            question_title = question
            question = question.replace(' ', '_').lower()
            answer = df[question].value_counts().index[0]
            if isinstance(answer, np.integer) or isinstance(answer, np.float):
                average = df[question].mean()
                answer = round(average, 2)
            if isinstance(answer, basestring) and '|' in answer:
                user_responses = transform_strings_to_lists(df[question])
                flat_list = itertools.chain.from_iterable(user_responses)
                c = Counter(flat_list)
                list_of_least_common_elements = c.most_common()
                answer = list_of_least_common_elements[0][0]
            if isinstance(answer, basestring) and '$' in answer:
                transformed_series = transform_currency_to_ints(df[question])
                average = transformed_series.mean()
                answer = '${:,.2f}'.format(average)
            community_profile[category][question_title] = answer
    return community_profile








