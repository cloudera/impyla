

def predict_income(impala_function_context, age, workclass, final_weight,
                   education, education_num,
                   marital_status, occupation, relationship, race, sex,
                   hours_per_week, native_country, income):
    """ Predictor for income from model/536030f60af5e8092c001612

        https://archive.ics.uci.edu/ml/machine-learning-databases/adult/
    """
    if (marital_status is None):
        return '<=50K'
    if (marital_status == 'Married-civ-spouse'):
        if (education_num is None):
            return '<=50K'
        if (education_num > 12):
            if (hours_per_week is None):
                return '>50K'
            if (hours_per_week > 31):
                if (age is None):
                    return '>50K'
                if (age > 28):
                    if (education_num > 13):
                        if (age > 58):
                            return '>50K'
                        if (age <= 58):
                            return '>50K'
                    if (education_num <= 13):
                        if (occupation is None):
                            return '>50K'
                        if (occupation == 'Exec-managerial'):
                            return '>50K'
                        if (occupation != 'Exec-managerial'):
                            return '>50K'
                if (age <= 28):
                    if (age > 24):
                        if (occupation is None):
                            return '<=50K'
                        if (occupation == 'Tech-support'):
                            return '>50K'
                        if (occupation != 'Tech-support'):
                            return '<=50K'
                    if (age <= 24):
                        if (final_weight is None):
                            return '<=50K'
                        if (final_weight > 492053):
                            return '>50K'
                        if (final_weight <= 492053):
                            return '<=50K'
            if (hours_per_week <= 31):
                if (sex is None):
                    return '<=50K'
                if (sex == 'Male'):
                    if (age is None):
                        return '<=50K'
                    if (age > 29):
                        if (age > 62):
                            return '<=50K'
                        if (age <= 62):
                            return '<=50K'
                    if (age <= 29):
                        return '<=50K'
                if (sex != 'Male'):
                    if (final_weight is None):
                        return '>50K'
                    if (final_weight > 264521):
                        if (hours_per_week > 7):
                            return '<=50K'
                        if (hours_per_week <= 7):
                            return '>50K'
                    if (final_weight <= 264521):
                        if (age is None):
                            return '>50K'
                        if (age > 26):
                            return '>50K'
                        if (age <= 26):
                            return '<=50K'
        if (education_num <= 12):
            if (education_num > 8):
                if (age is None):
                    return '<=50K'
                if (age > 35):
                    if (hours_per_week is None):
                        return '<=50K'
                    if (hours_per_week > 33):
                        if (education_num > 9):
                            return '>50K'
                        if (education_num <= 9):
                            return '<=50K'
                    if (hours_per_week <= 33):
                        if (workclass is None):
                            return '<=50K'
                        if (workclass == 'Self-emp-inc'):
                            return '>50K'
                        if (workclass != 'Self-emp-inc'):
                            return '<=50K'
                if (age <= 35):
                    if (age > 24):
                        if (occupation is None):
                            return '<=50K'
                        if (occupation == 'Exec-managerial'):
                            return '<=50K'
                        if (occupation != 'Exec-managerial'):
                            return '<=50K'
                    if (age <= 24):
                        if (hours_per_week is None):
                            return '<=50K'
                        if (hours_per_week > 45):
                            return '<=50K'
                        if (hours_per_week <= 45):
                            return '<=50K'
            if (education_num <= 8):
                if (age is None):
                    return '<=50K'
                if (age > 36):
                    if (hours_per_week is None):
                        return '<=50K'
                    if (hours_per_week > 22):
                        if (education_num > 5):
                            return '<=50K'
                        if (education_num <= 5):
                            return '<=50K'
                    if (hours_per_week <= 22):
                        return '<=50K'
                if (age <= 36):
                    if (workclass is None):
                        return '<=50K'
                    if (workclass == 'Private'):
                        if (age > 35):
                            return '<=50K'
                        if (age <= 35):
                            return '<=50K'
                    if (workclass != 'Private'):
                        if (occupation is None):
                            return '<=50K'
                        if (occupation == 'Machine-op-inspct'):
                            return '>50K'
                        if (occupation != 'Machine-op-inspct'):
                            return '<=50K'
    if (marital_status != 'Married-civ-spouse'):
        if (education_num is None):
            return '<=50K'
        if (education_num > 12):
            if (age is None):
                return '<=50K'
            if (age > 27):
                if (hours_per_week is None):
                    return '<=50K'
                if (hours_per_week > 43):
                    if (occupation is None):
                        return '<=50K'
                    if (occupation == 'Exec-managerial'):
                        if (age > 41):
                            return '>50K'
                        if (age <= 41):
                            return '<=50K'
                    if (occupation != 'Exec-managerial'):
                        if (education_num > 14):
                            return '>50K'
                        if (education_num <= 14):
                            return '<=50K'
                if (hours_per_week <= 43):
                    if (education_num > 14):
                        if (age > 32):
                            return '>50K'
                        if (age <= 32):
                            return '<=50K'
                    if (education_num <= 14):
                        if (age > 45):
                            return '<=50K'
                        if (age <= 45):
                            return '<=50K'
            if (age <= 27):
                if (hours_per_week is None):
                    return '<=50K'
                if (hours_per_week > 38):
                    if (relationship is None):
                        return '<=50K'
                    if (relationship == 'Wife'):
                        return '>50K'
                    if (relationship != 'Wife'):
                        if (hours_per_week > 77):
                            return '<=50K'
                        if (hours_per_week <= 77):
                            return '<=50K'
                if (hours_per_week <= 38):
                    return '<=50K'
        if (education_num <= 12):
            if (age is None):
                return '<=50K'
            if (age > 31):
                if (hours_per_week is None):
                    return '<=50K'
                if (hours_per_week > 41):
                    if (education_num > 5):
                        if (age > 53):
                            return '<=50K'
                        if (age <= 53):
                            return '<=50K'
                    if (education_num <= 5):
                        return '<=50K'
                if (hours_per_week <= 41):
                    if (occupation is None):
                        return '<=50K'
                    if (occupation == 'Other-service'):
                        if (relationship is None):
                            return '<=50K'
                        if (relationship == 'Wife'):
                            return '<=50K'
                        if (relationship != 'Wife'):
                            return '<=50K'
                    if (occupation != 'Other-service'):
                        if (occupation == 'Machine-op-inspct'):
                            return '<=50K'
                        if (occupation != 'Machine-op-inspct'):
                            return '<=50K'
            if (age <= 31):
                if (age > 21):
                    if (hours_per_week is None):
                        return '<=50K'
                    if (hours_per_week > 41):
                        if (workclass is None):
                            return '<=50K'
                        if (workclass == 'Private'):
                            return '<=50K'
                        if (workclass != 'Private'):
                            return '<=50K'
                    if (hours_per_week <= 41):
                        if (education_num > 9):
                            return '<=50K'
                        if (education_num <= 9):
                            return '<=50K'
                if (age <= 21):
                    if (education is None):
                        return '<=50K'
                    if (education == '7th-8th'):
                        if (occupation is None):
                            return '<=50K'
                        if (occupation == 'Other-service'):
                            return '<=50K'
                        if (occupation != 'Other-service'):
                            return '<=50K'
                    if (education != '7th-8th'):
                        return '<=50K'
