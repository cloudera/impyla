def predict_income(data={}):
    """ Predictor for income from model/536030f60af5e8092c001612

        https://archive.ics.uci.edu/ml/machine-learning-databases/adult/
    """
    if (not 'marital_status' in data or data['marital_status'] is None):
        return u'<=50K'
    if (data['marital_status'] == 'Married-civ-spouse'):
        if (not 'education_num' in data or data['education_num'] is None):
            return u'<=50K'
        if (data['education_num'] > 12):
            if (not 'hours_per_week' in data or data['hours_per_week'] is None):
                return u'>50K'
            if (data['hours_per_week'] > 31):
                if (not 'age' in data or data['age'] is None):
                    return u'>50K'
                if (data['age'] > 28):
                    if (data['education_num'] > 13):
                        if (data['age'] > 58):
                            return u'>50K'
                        if (data['age'] <= 58):
                            return u'>50K'
                    if (data['education_num'] <= 13):
                        if (not 'occupation' in data or data['occupation'] is None):
                            return u'>50K'
                        if (data['occupation'] == 'Exec-managerial'):
                            return u'>50K'
                        if (data['occupation'] != 'Exec-managerial'):
                            return u'>50K'
                if (data['age'] <= 28):
                    if (data['age'] > 24):
                        if (not 'occupation' in data or data['occupation'] is None):
                            return u'<=50K'
                        if (data['occupation'] == 'Tech-support'):
                            return u'>50K'
                        if (data['occupation'] != 'Tech-support'):
                            return u'<=50K'
                    if (data['age'] <= 24):
                        if (not 'final_weight' in data or data['final_weight'] is None):
                            return u'<=50K'
                        if (data['final_weight'] > 492053):
                            return u'>50K'
                        if (data['final_weight'] <= 492053):
                            return u'<=50K'
            if (data['hours_per_week'] <= 31):
                if (not 'sex' in data or data['sex'] is None):
                    return u'<=50K'
                if (data['sex'] == 'Male'):
                    if (not 'age' in data or data['age'] is None):
                        return u'<=50K'
                    if (data['age'] > 29):
                        if (data['age'] > 62):
                            return u'<=50K'
                        if (data['age'] <= 62):
                            return u'<=50K'
                    if (data['age'] <= 29):
                        return u'<=50K'
                if (data['sex'] != 'Male'):
                    if (not 'final_weight' in data or data['final_weight'] is None):
                        return u'>50K'
                    if (data['final_weight'] > 264521):
                        if (data['hours_per_week'] > 7):
                            return u'<=50K'
                        if (data['hours_per_week'] <= 7):
                            return u'>50K'
                    if (data['final_weight'] <= 264521):
                        if (not 'age' in data or data['age'] is None):
                            return u'>50K'
                        if (data['age'] > 26):
                            return u'>50K'
                        if (data['age'] <= 26):
                            return u'<=50K'
        if (data['education_num'] <= 12):
            if (data['education_num'] > 8):
                if (not 'age' in data or data['age'] is None):
                    return u'<=50K'
                if (data['age'] > 35):
                    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
                        return u'<=50K'
                    if (data['hours_per_week'] > 33):
                        if (data['education_num'] > 9):
                            return u'>50K'
                        if (data['education_num'] <= 9):
                            return u'<=50K'
                    if (data['hours_per_week'] <= 33):
                        if (not 'workclass' in data or data['workclass'] is None):
                            return u'<=50K'
                        if (data['workclass'] == 'Self-emp-inc'):
                            return u'>50K'
                        if (data['workclass'] != 'Self-emp-inc'):
                            return u'<=50K'
                if (data['age'] <= 35):
                    if (data['age'] > 24):
                        if (not 'occupation' in data or data['occupation'] is None):
                            return u'<=50K'
                        if (data['occupation'] == 'Exec-managerial'):
                            return u'<=50K'
                        if (data['occupation'] != 'Exec-managerial'):
                            return u'<=50K'
                    if (data['age'] <= 24):
                        if (not 'hours_per_week' in data or data['hours_per_week'] is None):
                            return u'<=50K'
                        if (data['hours_per_week'] > 45):
                            return u'<=50K'
                        if (data['hours_per_week'] <= 45):
                            return u'<=50K'
            if (data['education_num'] <= 8):
                if (not 'age' in data or data['age'] is None):
                    return u'<=50K'
                if (data['age'] > 36):
                    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
                        return u'<=50K'
                    if (data['hours_per_week'] > 22):
                        if (data['education_num'] > 5):
                            return u'<=50K'
                        if (data['education_num'] <= 5):
                            return u'<=50K'
                    if (data['hours_per_week'] <= 22):
                        return u'<=50K'
                if (data['age'] <= 36):
                    if (not 'workclass' in data or data['workclass'] is None):
                        return u'<=50K'
                    if (data['workclass'] == 'Private'):
                        if (data['age'] > 35):
                            return u'<=50K'
                        if (data['age'] <= 35):
                            return u'<=50K'
                    if (data['workclass'] != 'Private'):
                        if (not 'occupation' in data or data['occupation'] is None):
                            return u'<=50K'
                        if (data['occupation'] == 'Machine-op-inspct'):
                            return u'>50K'
                        if (data['occupation'] != 'Machine-op-inspct'):
                            return u'<=50K'
    if (data['marital_status'] != 'Married-civ-spouse'):
        if (not 'education_num' in data or data['education_num'] is None):
            return u'<=50K'
        if (data['education_num'] > 12):
            if (not 'age' in data or data['age'] is None):
                return u'<=50K'
            if (data['age'] > 27):
                if (not 'hours_per_week' in data or data['hours_per_week'] is None):
                    return u'<=50K'
                if (data['hours_per_week'] > 43):
                    if (not 'occupation' in data or data['occupation'] is None):
                        return u'<=50K'
                    if (data['occupation'] == 'Exec-managerial'):
                        if (data['age'] > 41):
                            return u'>50K'
                        if (data['age'] <= 41):
                            return u'<=50K'
                    if (data['occupation'] != 'Exec-managerial'):
                        if (data['education_num'] > 14):
                            return u'>50K'
                        if (data['education_num'] <= 14):
                            return u'<=50K'
                if (data['hours_per_week'] <= 43):
                    if (data['education_num'] > 14):
                        if (data['age'] > 32):
                            return u'>50K'
                        if (data['age'] <= 32):
                            return u'<=50K'
                    if (data['education_num'] <= 14):
                        if (data['age'] > 45):
                            return u'<=50K'
                        if (data['age'] <= 45):
                            return u'<=50K'
            if (data['age'] <= 27):
                if (not 'hours_per_week' in data or data['hours_per_week'] is None):
                    return u'<=50K'
                if (data['hours_per_week'] > 38):
                    if (not 'relationship' in data or data['relationship'] is None):
                        return u'<=50K'
                    if (data['relationship'] == 'Wife'):
                        return u'>50K'
                    if (data['relationship'] != 'Wife'):
                        if (data['hours_per_week'] > 77):
                            return u'<=50K'
                        if (data['hours_per_week'] <= 77):
                            return u'<=50K'
                if (data['hours_per_week'] <= 38):
                    return u'<=50K'
        if (data['education_num'] <= 12):
            if (not 'age' in data or data['age'] is None):
                return u'<=50K'
            if (data['age'] > 31):
                if (not 'hours_per_week' in data or data['hours_per_week'] is None):
                    return u'<=50K'
                if (data['hours_per_week'] > 41):
                    if (data['education_num'] > 5):
                        if (data['age'] > 53):
                            return u'<=50K'
                        if (data['age'] <= 53):
                            return u'<=50K'
                    if (data['education_num'] <= 5):
                        return u'<=50K'
                if (data['hours_per_week'] <= 41):
                    if (not 'occupation' in data or data['occupation'] is None):
                        return u'<=50K'
                    if (data['occupation'] == 'Other-service'):
                        if (not 'relationship' in data or data['relationship'] is None):
                            return u'<=50K'
                        if (data['relationship'] == 'Wife'):
                            return u'<=50K'
                        if (data['relationship'] != 'Wife'):
                            return u'<=50K'
                    if (data['occupation'] != 'Other-service'):
                        if (data['occupation'] == 'Machine-op-inspct'):
                            return u'<=50K'
                        if (data['occupation'] != 'Machine-op-inspct'):
                            return u'<=50K'
            if (data['age'] <= 31):
                if (data['age'] > 21):
                    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
                        return u'<=50K'
                    if (data['hours_per_week'] > 41):
                        if (not 'workclass' in data or data['workclass'] is None):
                            return u'<=50K'
                        if (data['workclass'] == 'Private'):
                            return u'<=50K'
                        if (data['workclass'] != 'Private'):
                            return u'<=50K'
                    if (data['hours_per_week'] <= 41):
                        if (data['education_num'] > 9):
                            return u'<=50K'
                        if (data['education_num'] <= 9):
                            return u'<=50K'
                if (data['age'] <= 21):
                    if (not 'education' in data or data['education'] is None):
                        return u'<=50K'
                    if (data['education'] == '7th-8th'):
                        if (not 'occupation' in data or data['occupation'] is None):
                            return u'<=50K'
                        if (data['occupation'] == 'Other-service'):
                            return u'<=50K'
                        if (data['occupation'] != 'Other-service'):
                            return u'<=50K'
                    if (data['education'] != '7th-8th'):
                        return u'<=50K'