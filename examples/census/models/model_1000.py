def predict_income(impala_function_context, age, workclass, final_weight, education, education_num, marital_status, occupation, relationship, race, sex, hours_per_week, native_country, income):
    """ Predictor for income from model/53603152ffa04466f9000e6b

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
                            if (education_num > 14):
                                if (workclass is None):
                                    return '>50K'
                                if (workclass == 'Local-gov'):
                                    return '<=50K'
                                if (workclass != 'Local-gov'):
                                    if (occupation is None):
                                        return '>50K'
                                    if (occupation == 'Sales'):
                                        return '<=50K'
                                    if (occupation != 'Sales'):
                                        if (age > 74):
                                            if (hours_per_week > 45):
                                                return '>50K'
                                            if (hours_per_week <= 45):
                                                if (education_num > 15):
                                                    return '>50K'
                                                if (education_num <= 15):
                                                    return '<=50K'
                                        if (age <= 74):
                                            if (workclass == 'State-gov'):
                                                if (hours_per_week > 47):
                                                    return '<=50K'
                                                if (hours_per_week <= 47):
                                                    return '>50K'
                                            if (workclass != 'State-gov'):
                                                return '>50K'
                            if (education_num <= 14):
                                if (hours_per_week > 36):
                                    if (workclass is None):
                                        return '>50K'
                                    if (workclass == 'Self-emp-inc'):
                                        return '>50K'
                                    if (workclass != 'Self-emp-inc'):
                                        if (occupation is None):
                                            return '>50K'
                                        if (occupation == 'Adm-clerical'):
                                            return '>50K'
                                        if (occupation != 'Adm-clerical'):
                                            if (final_weight is None):
                                                return '>50K'
                                            if (final_weight > 142784):
                                                if (workclass == 'Self-emp-not-inc'):
                                                    return '<=50K'
                                                if (workclass != 'Self-emp-not-inc'):
                                                    return '<=50K'
                                            if (final_weight <= 142784):
                                                if (final_weight > 92181):
                                                    return '>50K'
                                                if (final_weight <= 92181):
                                                    return '<=50K'
                                if (hours_per_week <= 36):
                                    return '<=50K'
                        if (age <= 58):
                            if (age > 38):
                                if (education_num > 14):
                                    if (hours_per_week > 49):
                                        if (occupation is None):
                                            return '>50K'
                                        if (occupation == 'Craft-repair'):
                                            return '<=50K'
                                        if (occupation != 'Craft-repair'):
                                            if (workclass is None):
                                                return '>50K'
                                            if (workclass == 'Private'):
                                                if (race is None):
                                                    return '>50K'
                                                if (race == 'Asian-Pac-Islander'):
                                                    return '<=50K'
                                                if (race != 'Asian-Pac-Islander'):
                                                    return '>50K'
                                            if (workclass != 'Private'):
                                                return '>50K'
                                    if (hours_per_week <= 49):
                                        if (relationship is None):
                                            return '>50K'
                                        if (relationship == 'Not-in-family'):
                                            return '<=50K'
                                        if (relationship != 'Not-in-family'):
                                            if (occupation is None):
                                                return '>50K'
                                            if (occupation == 'Transport-moving'):
                                                return '<=50K'
                                            if (occupation != 'Transport-moving'):
                                                if (age > 57):
                                                    return '<=50K'
                                                if (age <= 57):
                                                    return '>50K'
                                if (education_num <= 14):
                                    if (workclass is None):
                                        return '>50K'
                                    if (workclass == 'Self-emp-not-inc'):
                                        if (final_weight is None):
                                            return '>50K'
                                        if (final_weight > 243112):
                                            return '>50K'
                                        if (final_weight <= 243112):
                                            if (hours_per_week > 57):
                                                if (occupation is None):
                                                    return '<=50K'
                                                if (occupation == 'Exec-managerial'):
                                                    return '>50K'
                                                if (occupation != 'Exec-managerial'):
                                                    return '<=50K'
                                            if (hours_per_week <= 57):
                                                if (hours_per_week > 39):
                                                    return '>50K'
                                                if (hours_per_week <= 39):
                                                    return '>50K'
                                    if (workclass != 'Self-emp-not-inc'):
                                        if (occupation is None):
                                            return '>50K'
                                        if (occupation == 'Adm-clerical'):
                                            if (final_weight is None):
                                                return '>50K'
                                            if (final_weight > 347159):
                                                return '<=50K'
                                            if (final_weight <= 347159):
                                                if (final_weight > 188705):
                                                    return '>50K'
                                                if (final_weight <= 188705):
                                                    return '<=50K'
                                        if (occupation != 'Adm-clerical'):
                                            if (final_weight is None):
                                                return '>50K'
                                            if (final_weight > 323185):
                                                return '>50K'
                                            if (final_weight <= 323185):
                                                if (race is None):
                                                    return '>50K'
                                                if (race == 'Amer-Indian-Eskimo'):
                                                    return '<=50K'
                                                if (race != 'Amer-Indian-Eskimo'):
                                                    return '>50K'
                            if (age <= 38):
                                if (occupation is None):
                                    return '>50K'
                                if (occupation == 'Farming-fishing'):
                                    return '<=50K'
                                if (occupation != 'Farming-fishing'):
                                    if (hours_per_week > 42):
                                        if (occupation == 'Exec-managerial'):
                                            if (final_weight is None):
                                                return '>50K'
                                            if (final_weight > 285656):
                                                if (final_weight > 296849):
                                                    return '>50K'
                                                if (final_weight <= 296849):
                                                    return '<=50K'
                                            if (final_weight <= 285656):
                                                return '>50K'
                                        if (occupation != 'Exec-managerial'):
                                            if (sex is None):
                                                return '>50K'
                                            if (sex == 'Male'):
                                                if (occupation == 'Machine-op-inspct'):
                                                    return '<=50K'
                                                if (occupation != 'Machine-op-inspct'):
                                                    return '>50K'
                                            if (sex != 'Male'):
                                                return '>50K'
                                    if (hours_per_week <= 42):
                                        if (occupation == 'Craft-repair'):
                                            return '<=50K'
                                        if (occupation != 'Craft-repair'):
                                            if (hours_per_week > 39):
                                                if (final_weight is None):
                                                    return '>50K'
                                                if (final_weight > 323491):
                                                    return '>50K'
                                                if (final_weight <= 323491):
                                                    return '>50K'
                                            if (hours_per_week <= 39):
                                                if (hours_per_week > 37):
                                                    return '<=50K'
                                                if (hours_per_week <= 37):
                                                    return '>50K'
                    if (education_num <= 13):
                        if (occupation is None):
                            return '>50K'
                        if (occupation == 'Exec-managerial'):
                            if (workclass is None):
                                return '>50K'
                            if (workclass == 'Self-emp-not-inc'):
                                if (final_weight is None):
                                    return '>50K'
                                if (final_weight > 90244):
                                    if (age > 48):
                                        if (age > 65):
                                            return '<=50K'
                                        if (age <= 65):
                                            return '>50K'
                                    if (age <= 48):
                                        if (age > 35):
                                            if (age > 43):
                                                if (hours_per_week > 42):
                                                    return '>50K'
                                                if (hours_per_week <= 42):
                                                    return '<=50K'
                                            if (age <= 43):
                                                if (final_weight > 187120):
                                                    return '<=50K'
                                                if (final_weight <= 187120):
                                                    return '<=50K'
                                        if (age <= 35):
                                            return '>50K'
                                if (final_weight <= 90244):
                                    return '<=50K'
                            if (workclass != 'Self-emp-not-inc'):
                                if (hours_per_week > 67):
                                    if (hours_per_week > 73):
                                        return '>50K'
                                    if (hours_per_week <= 73):
                                        if (final_weight is None):
                                            return '<=50K'
                                        if (final_weight > 134993):
                                            if (hours_per_week > 71):
                                                if (final_weight > 322085):
                                                    return '<=50K'
                                                if (final_weight <= 322085):
                                                    return '>50K'
                                            if (hours_per_week <= 71):
                                                return '<=50K'
                                        if (final_weight <= 134993):
                                            return '>50K'
                                if (hours_per_week <= 67):
                                    if (race is None):
                                        return '>50K'
                                    if (race == 'Other'):
                                        return '<=50K'
                                    if (race != 'Other'):
                                        if (relationship is None):
                                            return '>50K'
                                        if (relationship == 'Other-relative'):
                                            return '<=50K'
                                        if (relationship != 'Other-relative'):
                                            if (hours_per_week > 41):
                                                if (age > 84):
                                                    return '<=50K'
                                                if (age <= 84):
                                                    return '>50K'
                                            if (hours_per_week <= 41):
                                                if (final_weight is None):
                                                    return '>50K'
                                                if (final_weight > 364614):
                                                    return '>50K'
                                                if (final_weight <= 364614):
                                                    return '>50K'
                        if (occupation != 'Exec-managerial'):
                            if (relationship is None):
                                return '>50K'
                            if (relationship == 'Other-relative'):
                                return '<=50K'
                            if (relationship != 'Other-relative'):
                                if (race is None):
                                    return '>50K'
                                if (race == 'Other'):
                                    return '<=50K'
                                if (race != 'Other'):
                                    if (final_weight is None):
                                        return '>50K'
                                    if (final_weight > 121061):
                                        if (final_weight > 232277):
                                            if (age > 36):
                                                if (occupation == 'Other-service'):
                                                    return '<=50K'
                                                if (occupation != 'Other-service'):
                                                    return '>50K'
                                            if (age <= 36):
                                                if (hours_per_week > 39):
                                                    return '<=50K'
                                                if (hours_per_week <= 39):
                                                    return '>50K'
                                        if (final_weight <= 232277):
                                            if (occupation == 'Transport-moving'):
                                                if (hours_per_week > 42):
                                                    return '>50K'
                                                if (hours_per_week <= 42):
                                                    return '<=50K'
                                            if (occupation != 'Transport-moving'):
                                                if (workclass is None):
                                                    return '>50K'
                                                if (workclass == 'Local-gov'):
                                                    return '>50K'
                                                if (workclass != 'Local-gov'):
                                                    return '>50K'
                                    if (final_weight <= 121061):
                                        if (occupation == 'Machine-op-inspct'):
                                            return '<=50K'
                                        if (occupation != 'Machine-op-inspct'):
                                            if (hours_per_week > 53):
                                                if (occupation == 'Sales'):
                                                    return '<=50K'
                                                if (occupation != 'Sales'):
                                                    return '>50K'
                                            if (hours_per_week <= 53):
                                                if (workclass is None):
                                                    return '>50K'
                                                if (workclass == 'Self-emp-not-inc'):
                                                    return '<=50K'
                                                if (workclass != 'Self-emp-not-inc'):
                                                    return '>50K'
                if (age <= 28):
                    if (age > 24):
                        if (occupation is None):
                            return '<=50K'
                        if (occupation == 'Tech-support'):
                            return '>50K'
                        if (occupation != 'Tech-support'):
                            if (hours_per_week > 41):
                                if (hours_per_week > 46):
                                    if (education_num > 14):
                                        return '<=50K'
                                    if (education_num <= 14):
                                        if (final_weight is None):
                                            return '<=50K'
                                        if (final_weight > 59538):
                                            if (workclass is None):
                                                return '<=50K'
                                            if (workclass == 'Self-emp-inc'):
                                                return '>50K'
                                            if (workclass != 'Self-emp-inc'):
                                                if (final_weight > 165889):
                                                    return '<=50K'
                                                if (final_weight <= 165889):
                                                    return '<=50K'
                                        if (final_weight <= 59538):
                                            return '>50K'
                                if (hours_per_week <= 46):
                                    if (occupation == 'Adm-clerical'):
                                        return '<=50K'
                                    if (occupation != 'Adm-clerical'):
                                        if (final_weight is None):
                                            return '>50K'
                                        if (final_weight > 155506):
                                            return '>50K'
                                        if (final_weight <= 155506):
                                            if (age > 27):
                                                return '<=50K'
                                            if (age <= 27):
                                                return '>50K'
                            if (hours_per_week <= 41):
                                if (final_weight is None):
                                    return '<=50K'
                                if (final_weight > 159383):
                                    if (final_weight > 260996):
                                        if (age > 27):
                                            if (final_weight > 263671):
                                                return '<=50K'
                                            if (final_weight <= 263671):
                                                return '>50K'
                                        if (age <= 27):
                                            return '>50K'
                                    if (final_weight <= 260996):
                                        if (occupation == 'Exec-managerial'):
                                            if (age > 27):
                                                return '>50K'
                                            if (age <= 27):
                                                return '<=50K'
                                        if (occupation != 'Exec-managerial'):
                                            return '<=50K'
                                if (final_weight <= 159383):
                                    if (final_weight > 100631):
                                        if (age > 27):
                                            return '>50K'
                                        if (age <= 27):
                                            if (occupation == 'Sales'):
                                                return '>50K'
                                            if (occupation != 'Sales'):
                                                return '<=50K'
                                    if (final_weight <= 100631):
                                        if (occupation == 'Exec-managerial'):
                                            if (race is None):
                                                return '<=50K'
                                            if (race == 'White'):
                                                return '>50K'
                                            if (race != 'White'):
                                                return '<=50K'
                                        if (occupation != 'Exec-managerial'):
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
                            if (age > 78):
                                if (hours_per_week > 9):
                                    return '>50K'
                                if (hours_per_week <= 9):
                                    return '<=50K'
                            if (age <= 78):
                                if (hours_per_week > 13):
                                    if (race is None):
                                        return '<=50K'
                                    if (race == 'White'):
                                        if (final_weight is None):
                                            return '<=50K'
                                        if (final_weight > 38129):
                                            if (age > 66):
                                                return '<=50K'
                                            if (age <= 66):
                                                if (occupation is None):
                                                    return '<=50K'
                                                if (occupation == 'Sales'):
                                                    return '<=50K'
                                                if (occupation != 'Sales'):
                                                    return '<=50K'
                                        if (final_weight <= 38129):
                                            return '>50K'
                                    if (race != 'White'):
                                        return '>50K'
                                if (hours_per_week <= 13):
                                    if (occupation is None):
                                        return '<=50K'
                                    if (occupation == 'Exec-managerial'):
                                        return '>50K'
                                    if (occupation != 'Exec-managerial'):
                                        if (occupation == 'Prof-specialty'):
                                            return '<=50K'
                                        if (occupation != 'Prof-specialty'):
                                            if (hours_per_week > 11):
                                                return '>50K'
                                            if (hours_per_week <= 11):
                                                if (final_weight is None):
                                                    return '<=50K'
                                                if (final_weight > 180316):
                                                    return '>50K'
                                                if (final_weight <= 180316):
                                                    return '<=50K'
                        if (age <= 62):
                            if (hours_per_week > 12):
                                if (workclass is None):
                                    return '>50K'
                                if (workclass == 'State-gov'):
                                    return '<=50K'
                                if (workclass != 'State-gov'):
                                    if (hours_per_week > 21):
                                        if (education is None):
                                            return '<=50K'
                                        if (education == 'Prof-school'):
                                            return '>50K'
                                        if (education != 'Prof-school'):
                                            if (final_weight is None):
                                                return '<=50K'
                                            if (final_weight > 302817):
                                                return '<=50K'
                                            if (final_weight <= 302817):
                                                if (final_weight > 234356):
                                                    return '>50K'
                                                if (final_weight <= 234356):
                                                    return '<=50K'
                                    if (hours_per_week <= 21):
                                        if (workclass == 'Self-emp-inc'):
                                            return '<=50K'
                                        if (workclass != 'Self-emp-inc'):
                                            if (relationship is None):
                                                return '>50K'
                                            if (relationship == 'Husband'):
                                                if (education_num > 13):
                                                    return '>50K'
                                                if (education_num <= 13):
                                                    return '>50K'
                                            if (relationship != 'Husband'):
                                                return '<=50K'
                            if (hours_per_week <= 12):
                                if (hours_per_week > 2):
                                    if (education_num > 14):
                                        if (hours_per_week > 5):
                                            return '<=50K'
                                        if (hours_per_week <= 5):
                                            return '>50K'
                                    if (education_num <= 14):
                                        return '<=50K'
                                if (hours_per_week <= 2):
                                    return '>50K'
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
                            if (workclass is None):
                                return '>50K'
                            if (workclass == 'Self-emp-not-inc'):
                                if (hours_per_week > 26):
                                    return '>50K'
                                if (hours_per_week <= 26):
                                    return '<=50K'
                            if (workclass != 'Self-emp-not-inc'):
                                if (final_weight > 36352):
                                    if (occupation is None):
                                        return '>50K'
                                    if (occupation == 'Other-service'):
                                        if (hours_per_week > 27):
                                            return '>50K'
                                        if (hours_per_week <= 27):
                                            return '<=50K'
                                    if (occupation != 'Other-service'):
                                        if (workclass == 'Local-gov'):
                                            if (hours_per_week > 23):
                                                if (hours_per_week > 24):
                                                    return '>50K'
                                                if (hours_per_week <= 24):
                                                    return '<=50K'
                                            if (hours_per_week <= 23):
                                                return '>50K'
                                        if (workclass != 'Local-gov'):
                                            return '>50K'
                                if (final_weight <= 36352):
                                    return '<=50K'
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
                            if (occupation is None):
                                return '>50K'
                            if (occupation == 'Farming-fishing'):
                                if (hours_per_week > 71):
                                    return '<=50K'
                                if (hours_per_week <= 71):
                                    if (final_weight is None):
                                        return '<=50K'
                                    if (final_weight > 182378):
                                        return '<=50K'
                                    if (final_weight <= 182378):
                                        if (hours_per_week > 67):
                                            return '>50K'
                                        if (hours_per_week <= 67):
                                            if (age > 49):
                                                if (hours_per_week > 45):
                                                    return '<=50K'
                                                if (hours_per_week <= 45):
                                                    return '>50K'
                                            if (age <= 49):
                                                if (age > 39):
                                                    return '<=50K'
                                                if (age <= 39):
                                                    return '<=50K'
                            if (occupation != 'Farming-fishing'):
                                if (occupation == 'Other-service'):
                                    if (age > 40):
                                        if (final_weight is None):
                                            return '<=50K'
                                        if (final_weight > 196473):
                                            if (hours_per_week > 37):
                                                if (hours_per_week > 46):
                                                    return '<=50K'
                                                if (hours_per_week <= 46):
                                                    return '>50K'
                                            if (hours_per_week <= 37):
                                                return '<=50K'
                                        if (final_weight <= 196473):
                                            if (age > 46):
                                                if (age > 48):
                                                    return '<=50K'
                                                if (age <= 48):
                                                    return '>50K'
                                            if (age <= 46):
                                                return '<=50K'
                                    if (age <= 40):
                                        return '<=50K'
                                if (occupation != 'Other-service'):
                                    if (occupation == 'Exec-managerial'):
                                        if (workclass is None):
                                            return '>50K'
                                        if (workclass == 'State-gov'):
                                            if (sex is None):
                                                return '<=50K'
                                            if (sex == 'Male'):
                                                return '<=50K'
                                            if (sex != 'Male'):
                                                return '>50K'
                                        if (workclass != 'State-gov'):
                                            if (workclass == 'Self-emp-not-inc'):
                                                if (education is None):
                                                    return '<=50K'
                                                if (education == 'Assoc-voc'):
                                                    return '<=50K'
                                                if (education != 'Assoc-voc'):
                                                    return '>50K'
                                            if (workclass != 'Self-emp-not-inc'):
                                                if (hours_per_week > 48):
                                                    return '>50K'
                                                if (hours_per_week <= 48):
                                                    return '>50K'
                                    if (occupation != 'Exec-managerial'):
                                        if (occupation == 'Prof-specialty'):
                                            if (final_weight is None):
                                                return '>50K'
                                            if (final_weight > 133264):
                                                if (workclass is None):
                                                    return '>50K'
                                                if (workclass == 'Self-emp-not-inc'):
                                                    return '<=50K'
                                                if (workclass != 'Self-emp-not-inc'):
                                                    return '>50K'
                                            if (final_weight <= 133264):
                                                if (final_weight > 45882):
                                                    return '<=50K'
                                                if (final_weight <= 45882):
                                                    return '<=50K'
                                        if (occupation != 'Prof-specialty'):
                                            if (occupation == 'Tech-support'):
                                                if (final_weight is None):
                                                    return '>50K'
                                                if (final_weight > 132978):
                                                    return '>50K'
                                                if (final_weight <= 132978):
                                                    return '>50K'
                                            if (occupation != 'Tech-support'):
                                                if (workclass is None):
                                                    return '<=50K'
                                                if (workclass == 'Self-emp-inc'):
                                                    return '>50K'
                                                if (workclass != 'Self-emp-inc'):
                                                    return '<=50K'
                        if (education_num <= 9):
                            if (occupation is None):
                                return '<=50K'
                            if (occupation == 'Exec-managerial'):
                                if (workclass is None):
                                    return '>50K'
                                if (workclass == 'Self-emp-not-inc'):
                                    if (final_weight is None):
                                        return '<=50K'
                                    if (final_weight > 92214):
                                        if (final_weight > 145136):
                                            if (hours_per_week > 51):
                                                return '>50K'
                                            if (hours_per_week <= 51):
                                                if (final_weight > 199146):
                                                    return '<=50K'
                                                if (final_weight <= 199146):
                                                    return '>50K'
                                        if (final_weight <= 145136):
                                            return '<=50K'
                                    if (final_weight <= 92214):
                                        if (hours_per_week > 47):
                                            if (hours_per_week > 55):
                                                return '>50K'
                                            if (hours_per_week <= 55):
                                                return '<=50K'
                                        if (hours_per_week <= 47):
                                            return '>50K'
                                if (workclass != 'Self-emp-not-inc'):
                                    if (final_weight is None):
                                        return '>50K'
                                    if (final_weight > 189527):
                                        if (age > 55):
                                            if (workclass == 'Private'):
                                                if (hours_per_week > 45):
                                                    return '<=50K'
                                                if (hours_per_week <= 45):
                                                    return '>50K'
                                            if (workclass != 'Private'):
                                                return '<=50K'
                                        if (age <= 55):
                                            if (hours_per_week > 47):
                                                return '>50K'
                                            if (hours_per_week <= 47):
                                                if (final_weight > 224226):
                                                    return '>50K'
                                                if (final_weight <= 224226):
                                                    return '>50K'
                                    if (final_weight <= 189527):
                                        if (hours_per_week > 37):
                                            if (age > 63):
                                                return '>50K'
                                            if (age <= 63):
                                                if (age > 54):
                                                    return '<=50K'
                                                if (age <= 54):
                                                    return '>50K'
                                        if (hours_per_week <= 37):
                                            return '>50K'
                            if (occupation != 'Exec-managerial'):
                                if (occupation == 'Other-service'):
                                    if (sex is None):
                                        return '<=50K'
                                    if (sex == 'Male'):
                                        if (age > 47):
                                            if (hours_per_week > 37):
                                                if (final_weight is None):
                                                    return '<=50K'
                                                if (final_weight > 324775):
                                                    return '>50K'
                                                if (final_weight <= 324775):
                                                    return '<=50K'
                                            if (hours_per_week <= 37):
                                                return '>50K'
                                        if (age <= 47):
                                            if (final_weight is None):
                                                return '<=50K'
                                            if (final_weight > 84981):
                                                if (final_weight > 92314):
                                                    return '<=50K'
                                                if (final_weight <= 92314):
                                                    return '>50K'
                                            if (final_weight <= 84981):
                                                return '<=50K'
                                    if (sex != 'Male'):
                                        return '<=50K'
                                if (occupation != 'Other-service'):
                                    if (occupation == 'Farming-fishing'):
                                        if (hours_per_week > 39):
                                            if (age > 65):
                                                return '<=50K'
                                            if (age <= 65):
                                                if (age > 63):
                                                    return '>50K'
                                                if (age <= 63):
                                                    return '<=50K'
                                        if (hours_per_week <= 39):
                                            return '<=50K'
                                    if (occupation != 'Farming-fishing'):
                                        if (race is None):
                                            return '<=50K'
                                        if (race == 'Amer-Indian-Eskimo'):
                                            return '<=50K'
                                        if (race != 'Amer-Indian-Eskimo'):
                                            if (final_weight is None):
                                                return '<=50K'
                                            if (final_weight > 535569):
                                                if (final_weight > 792076):
                                                    return '<=50K'
                                                if (final_weight <= 792076):
                                                    return '>50K'
                                            if (final_weight <= 535569):
                                                if (hours_per_week > 71):
                                                    return '>50K'
                                                if (hours_per_week <= 71):
                                                    return '<=50K'
                    if (hours_per_week <= 33):
                        if (workclass is None):
                            return '<=50K'
                        if (workclass == 'Self-emp-inc'):
                            if (age > 54):
                                if (final_weight is None):
                                    return '>50K'
                                if (final_weight > 181769):
                                    if (hours_per_week > 27):
                                        if (education_num > 9):
                                            return '<=50K'
                                        if (education_num <= 9):
                                            return '>50K'
                                    if (hours_per_week <= 27):
                                        return '>50K'
                                if (final_weight <= 181769):
                                    if (sex is None):
                                        return '<=50K'
                                    if (sex == 'Male'):
                                        return '<=50K'
                                    if (sex != 'Male'):
                                        return '>50K'
                            if (age <= 54):
                                return '<=50K'
                        if (workclass != 'Self-emp-inc'):
                            if (relationship is None):
                                return '<=50K'
                            if (relationship == 'Wife'):
                                if (age > 59):
                                    return '<=50K'
                                if (age <= 59):
                                    if (education_num > 9):
                                        if (workclass == 'Local-gov'):
                                            return '<=50K'
                                        if (workclass != 'Local-gov'):
                                            if (occupation is None):
                                                return '>50K'
                                            if (occupation == 'Adm-clerical'):
                                                return '>50K'
                                            if (occupation != 'Adm-clerical'):
                                                if (race is None):
                                                    return '>50K'
                                                if (race == 'White'):
                                                    return '>50K'
                                                if (race != 'White'):
                                                    return '<=50K'
                                    if (education_num <= 9):
                                        if (age > 57):
                                            return '>50K'
                                        if (age <= 57):
                                            if (hours_per_week > 18):
                                                if (final_weight is None):
                                                    return '<=50K'
                                                if (final_weight > 194378):
                                                    return '<=50K'
                                                if (final_weight <= 194378):
                                                    return '<=50K'
                                            if (hours_per_week <= 18):
                                                return '<=50K'
                            if (relationship != 'Wife'):
                                if (occupation is None):
                                    return '<=50K'
                                if (occupation == 'Tech-support'):
                                    if (workclass == 'Self-emp-not-inc'):
                                        return '<=50K'
                                    if (workclass != 'Self-emp-not-inc'):
                                        return '>50K'
                                if (occupation != 'Tech-support'):
                                    if (final_weight is None):
                                        return '<=50K'
                                    if (final_weight > 286449):
                                        return '<=50K'
                                    if (final_weight <= 286449):
                                        if (age > 41):
                                            if (age > 59):
                                                if (education_num > 9):
                                                    return '<=50K'
                                                if (education_num <= 9):
                                                    return '<=50K'
                                            if (age <= 59):
                                                if (occupation == 'Handlers-cleaners'):
                                                    return '>50K'
                                                if (occupation != 'Handlers-cleaners'):
                                                    return '<=50K'
                                        if (age <= 41):
                                            return '<=50K'
                if (age <= 35):
                    if (age > 24):
                        if (occupation is None):
                            return '<=50K'
                        if (occupation == 'Exec-managerial'):
                            if (age > 27):
                                if (workclass is None):
                                    return '<=50K'
                                if (workclass == 'Self-emp-not-inc'):
                                    if (final_weight is None):
                                        return '<=50K'
                                    if (final_weight > 237985):
                                        return '<=50K'
                                    if (final_weight <= 237985):
                                        if (age > 32):
                                            if (education_num > 10):
                                                return '>50K'
                                            if (education_num <= 10):
                                                return '<=50K'
                                        if (age <= 32):
                                            if (hours_per_week is None):
                                                return '>50K'
                                            if (hours_per_week > 52):
                                                return '<=50K'
                                            if (hours_per_week <= 52):
                                                return '>50K'
                                if (workclass != 'Self-emp-not-inc'):
                                    if (age > 32):
                                        if (sex is None):
                                            return '>50K'
                                        if (sex == 'Male'):
                                            if (hours_per_week is None):
                                                return '>50K'
                                            if (hours_per_week > 59):
                                                if (education_num > 9):
                                                    return '>50K'
                                                if (education_num <= 9):
                                                    return '<=50K'
                                            if (hours_per_week <= 59):
                                                if (education_num > 10):
                                                    return '<=50K'
                                                if (education_num <= 10):
                                                    return '>50K'
                                        if (sex != 'Male'):
                                            return '>50K'
                                    if (age <= 32):
                                        if (education_num > 11):
                                            return '>50K'
                                        if (education_num <= 11):
                                            if (sex is None):
                                                return '<=50K'
                                            if (sex == 'Male'):
                                                if (hours_per_week is None):
                                                    return '<=50K'
                                                if (hours_per_week > 67):
                                                    return '<=50K'
                                                if (hours_per_week <= 67):
                                                    return '<=50K'
                                            if (sex != 'Male'):
                                                return '<=50K'
                            if (age <= 27):
                                if (final_weight is None):
                                    return '<=50K'
                                if (final_weight > 162313):
                                    if (final_weight > 190463):
                                        if (workclass is None):
                                            return '<=50K'
                                        if (workclass == 'Private'):
                                            return '<=50K'
                                        if (workclass != 'Private'):
                                            if (education_num > 9):
                                                return '>50K'
                                            if (education_num <= 9):
                                                return '<=50K'
                                    if (final_weight <= 190463):
                                        return '>50K'
                                if (final_weight <= 162313):
                                    return '<=50K'
                        if (occupation != 'Exec-managerial'):
                            if (occupation == 'Farming-fishing'):
                                if (education_num > 10):
                                    if (hours_per_week is None):
                                        return '<=50K'
                                    if (hours_per_week > 57):
                                        if (final_weight is None):
                                            return '<=50K'
                                        if (final_weight > 133042):
                                            return '>50K'
                                        if (final_weight <= 133042):
                                            return '<=50K'
                                    if (hours_per_week <= 57):
                                        return '<=50K'
                                if (education_num <= 10):
                                    return '<=50K'
                            if (occupation != 'Farming-fishing'):
                                if (hours_per_week is None):
                                    return '<=50K'
                                if (hours_per_week > 46):
                                    if (age > 31):
                                        if (hours_per_week > 73):
                                            return '>50K'
                                        if (hours_per_week <= 73):
                                            if (hours_per_week > 61):
                                                return '<=50K'
                                            if (hours_per_week <= 61):
                                                if (occupation == 'Adm-clerical'):
                                                    return '>50K'
                                                if (occupation != 'Adm-clerical'):
                                                    return '<=50K'
                                    if (age <= 31):
                                        if (occupation == 'Handlers-cleaners'):
                                            return '<=50K'
                                        if (occupation != 'Handlers-cleaners'):
                                            if (final_weight is None):
                                                return '<=50K'
                                            if (final_weight > 131760):
                                                if (education_num > 9):
                                                    return '<=50K'
                                                if (education_num <= 9):
                                                    return '<=50K'
                                            if (final_weight <= 131760):
                                                if (final_weight > 95351):
                                                    return '<=50K'
                                                if (final_weight <= 95351):
                                                    return '<=50K'
                                if (hours_per_week <= 46):
                                    if (occupation == 'Prof-specialty'):
                                        if (hours_per_week > 39):
                                            if (final_weight is None):
                                                return '<=50K'
                                            if (final_weight > 316937):
                                                return '<=50K'
                                            if (final_weight <= 316937):
                                                if (final_weight > 268432):
                                                    return '>50K'
                                                if (final_weight <= 268432):
                                                    return '<=50K'
                                        if (hours_per_week <= 39):
                                            if (hours_per_week > 7):
                                                if (final_weight is None):
                                                    return '>50K'
                                                if (final_weight > 151741):
                                                    return '>50K'
                                                if (final_weight <= 151741):
                                                    return '<=50K'
                                            if (hours_per_week <= 7):
                                                return '<=50K'
                                    if (occupation != 'Prof-specialty'):
                                        if (workclass is None):
                                            return '<=50K'
                                        if (workclass == 'Federal-gov'):
                                            if (age > 30):
                                                if (occupation == 'Tech-support'):
                                                    return '<=50K'
                                                if (occupation != 'Tech-support'):
                                                    return '>50K'
                                            if (age <= 30):
                                                return '>50K'
                                        if (workclass != 'Federal-gov'):
                                            if (relationship is None):
                                                return '<=50K'
                                            if (relationship == 'Own-child'):
                                                return '<=50K'
                                            if (relationship != 'Own-child'):
                                                if (occupation == 'Handlers-cleaners'):
                                                    return '<=50K'
                                                if (occupation != 'Handlers-cleaners'):
                                                    return '<=50K'
                    if (age <= 24):
                        if (hours_per_week is None):
                            return '<=50K'
                        if (hours_per_week > 45):
                            if (final_weight is None):
                                return '<=50K'
                            if (final_weight > 79991):
                                if (race is None):
                                    return '<=50K'
                                if (race == 'Amer-Indian-Eskimo'):
                                    return '>50K'
                                if (race != 'Amer-Indian-Eskimo'):
                                    if (workclass is None):
                                        return '<=50K'
                                    if (workclass == 'State-gov'):
                                        return '>50K'
                                    if (workclass != 'State-gov'):
                                        return '<=50K'
                            if (final_weight <= 79991):
                                if (education_num > 9):
                                    return '>50K'
                                if (education_num <= 9):
                                    return '<=50K'
                        if (hours_per_week <= 45):
                            if (occupation is None):
                                return '<=50K'
                            if (occupation == 'Prof-specialty'):
                                if (hours_per_week > 38):
                                    return '>50K'
                                if (hours_per_week <= 38):
                                    return '<=50K'
                            if (occupation != 'Prof-specialty'):
                                if (occupation == 'Adm-clerical'):
                                    if (sex is None):
                                        return '<=50K'
                                    if (sex == 'Male'):
                                        if (final_weight is None):
                                            return '<=50K'
                                        if (final_weight > 339707):
                                            return '>50K'
                                        if (final_weight <= 339707):
                                            if (education is None):
                                                return '<=50K'
                                            if (education == 'Some-college'):
                                                if (race is None):
                                                    return '<=50K'
                                                if (race == 'White'):
                                                    return '<=50K'
                                                if (race != 'White'):
                                                    return '<=50K'
                                            if (education != 'Some-college'):
                                                return '<=50K'
                                    if (sex != 'Male'):
                                        return '<=50K'
                                if (occupation != 'Adm-clerical'):
                                    if (occupation == 'Handlers-cleaners'):
                                        if (final_weight is None):
                                            return '<=50K'
                                        if (final_weight > 154988):
                                            return '<=50K'
                                        if (final_weight <= 154988):
                                            return '>50K'
                                    if (occupation != 'Handlers-cleaners'):
                                        return '<=50K'
            if (education_num <= 8):
                if (age is None):
                    return '<=50K'
                if (age > 36):
                    if (hours_per_week is None):
                        return '<=50K'
                    if (hours_per_week > 22):
                        if (education_num > 5):
                            if (age > 53):
                                if (occupation is None):
                                    return '<=50K'
                                if (occupation == 'Transport-moving'):
                                    if (final_weight is None):
                                        return '<=50K'
                                    if (final_weight > 89485):
                                        if (hours_per_week > 37):
                                            if (final_weight > 190475):
                                                if (final_weight > 226535):
                                                    return '<=50K'
                                                if (final_weight <= 226535):
                                                    return '>50K'
                                            if (final_weight <= 190475):
                                                if (final_weight > 181878):
                                                    return '<=50K'
                                                if (final_weight <= 181878):
                                                    return '<=50K'
                                        if (hours_per_week <= 37):
                                            return '<=50K'
                                    if (final_weight <= 89485):
                                        return '<=50K'
                                if (occupation != 'Transport-moving'):
                                    if (final_weight is None):
                                        return '<=50K'
                                    if (final_weight > 162184):
                                        if (age > 62):
                                            if (workclass is None):
                                                return '<=50K'
                                            if (workclass == 'Local-gov'):
                                                return '>50K'
                                            if (workclass != 'Local-gov'):
                                                if (occupation == 'Sales'):
                                                    return '<=50K'
                                                if (occupation != 'Sales'):
                                                    return '<=50K'
                                        if (age <= 62):
                                            return '<=50K'
                                    if (final_weight <= 162184):
                                        if (final_weight > 151824):
                                            if (occupation == 'Machine-op-inspct'):
                                                return '<=50K'
                                            if (occupation != 'Machine-op-inspct'):
                                                return '>50K'
                                        if (final_weight <= 151824):
                                            if (final_weight > 118909):
                                                return '<=50K'
                                            if (final_weight <= 118909):
                                                if (final_weight > 65018):
                                                    return '<=50K'
                                                if (final_weight <= 65018):
                                                    return '<=50K'
                            if (age <= 53):
                                if (occupation is None):
                                    return '<=50K'
                                if (occupation == 'Sales'):
                                    if (hours_per_week > 52):
                                        return '<=50K'
                                    if (hours_per_week <= 52):
                                        if (sex is None):
                                            return '>50K'
                                        if (sex == 'Male'):
                                            return '>50K'
                                        if (sex != 'Male'):
                                            return '<=50K'
                                if (occupation != 'Sales'):
                                    if (workclass is None):
                                        return '<=50K'
                                    if (workclass == 'Local-gov'):
                                        return '<=50K'
                                    if (workclass != 'Local-gov'):
                                        if (occupation == 'Exec-managerial'):
                                            if (hours_per_week > 55):
                                                return '<=50K'
                                            if (hours_per_week <= 55):
                                                if (final_weight is None):
                                                    return '>50K'
                                                if (final_weight > 340151):
                                                    return '<=50K'
                                                if (final_weight <= 340151):
                                                    return '>50K'
                                        if (occupation != 'Exec-managerial'):
                                            if (race is None):
                                                return '<=50K'
                                            if (race == 'Other'):
                                                return '>50K'
                                            if (race != 'Other'):
                                                if (hours_per_week > 39):
                                                    return '<=50K'
                                                if (hours_per_week <= 39):
                                                    return '<=50K'
                        if (education_num <= 5):
                            if (workclass is None):
                                return '<=50K'
                            if (workclass == 'Private'):
                                if (occupation is None):
                                    return '<=50K'
                                if (occupation == 'Exec-managerial'):
                                    if (hours_per_week > 46):
                                        return '<=50K'
                                    if (hours_per_week <= 46):
                                        if (final_weight is None):
                                            return '>50K'
                                        if (final_weight > 99690):
                                            return '>50K'
                                        if (final_weight <= 99690):
                                            return '<=50K'
                                if (occupation != 'Exec-managerial'):
                                    if (occupation == 'Sales'):
                                        if (age > 53):
                                            if (final_weight is None):
                                                return '>50K'
                                            if (final_weight > 104904):
                                                return '>50K'
                                            if (final_weight <= 104904):
                                                return '<=50K'
                                        if (age <= 53):
                                            return '<=50K'
                                    if (occupation != 'Sales'):
                                        if (hours_per_week > 39):
                                            if (hours_per_week > 51):
                                                return '<=50K'
                                            if (hours_per_week <= 51):
                                                if (hours_per_week > 49):
                                                    return '<=50K'
                                                if (hours_per_week <= 49):
                                                    return '<=50K'
                                        if (hours_per_week <= 39):
                                            return '<=50K'
                            if (workclass != 'Private'):
                                if (hours_per_week > 55):
                                    if (workclass == 'Self-emp-not-inc'):
                                        if (occupation is None):
                                            return '>50K'
                                        if (occupation == 'Farming-fishing'):
                                            if (age > 61):
                                                if (education_num > 3):
                                                    return '>50K'
                                                if (education_num <= 3):
                                                    return '<=50K'
                                            if (age <= 61):
                                                return '<=50K'
                                        if (occupation != 'Farming-fishing'):
                                            return '>50K'
                                    if (workclass != 'Self-emp-not-inc'):
                                        return '<=50K'
                                if (hours_per_week <= 55):
                                    if (workclass == 'Self-emp-inc'):
                                        if (occupation is None):
                                            return '>50K'
                                        if (occupation == 'Craft-repair'):
                                            return '>50K'
                                        if (occupation != 'Craft-repair'):
                                            if (occupation == 'Sales'):
                                                return '>50K'
                                            if (occupation != 'Sales'):
                                                if (occupation == 'Machine-op-inspct'):
                                                    return '>50K'
                                                if (occupation != 'Machine-op-inspct'):
                                                    return '<=50K'
                                    if (workclass != 'Self-emp-inc'):
                                        if (age > 40):
                                            if (final_weight is None):
                                                return '<=50K'
                                            if (final_weight > 35109):
                                                if (hours_per_week > 27):
                                                    return '<=50K'
                                                if (hours_per_week <= 27):
                                                    return '<=50K'
                                            if (final_weight <= 35109):
                                                if (final_weight > 33892):
                                                    return '>50K'
                                                if (final_weight <= 33892):
                                                    return '<=50K'
                                        if (age <= 40):
                                            if (education is None):
                                                return '>50K'
                                            if (education == '7th-8th'):
                                                return '>50K'
                                            if (education != '7th-8th'):
                                                if (occupation is None):
                                                    return '<=50K'
                                                if (occupation == 'Craft-repair'):
                                                    return '<=50K'
                                                if (occupation != 'Craft-repair'):
                                                    return '>50K'
                    if (hours_per_week <= 22):
                        return '<=50K'
                if (age <= 36):
                    if (workclass is None):
                        return '<=50K'
                    if (workclass == 'Private'):
                        if (age > 35):
                            if (occupation is None):
                                return '<=50K'
                            if (occupation == 'Sales'):
                                return '>50K'
                            if (occupation != 'Sales'):
                                if (education_num > 3):
                                    if (final_weight is None):
                                        return '<=50K'
                                    if (final_weight > 185266):
                                        if (education_num > 6):
                                            return '>50K'
                                        if (education_num <= 6):
                                            return '<=50K'
                                    if (final_weight <= 185266):
                                        return '<=50K'
                                if (education_num <= 3):
                                    return '>50K'
                        if (age <= 35):
                            if (hours_per_week is None):
                                return '<=50K'
                            if (hours_per_week > 67):
                                if (hours_per_week > 83):
                                    return '<=50K'
                                if (hours_per_week <= 83):
                                    return '>50K'
                            if (hours_per_week <= 67):
                                if (occupation is None):
                                    return '<=50K'
                                if (occupation == 'Adm-clerical'):
                                    if (final_weight is None):
                                        return '<=50K'
                                    if (final_weight > 219946):
                                        if (sex is None):
                                            return '<=50K'
                                        if (sex == 'Male'):
                                            return '>50K'
                                        if (sex != 'Male'):
                                            return '<=50K'
                                    if (final_weight <= 219946):
                                        return '<=50K'
                                if (occupation != 'Adm-clerical'):
                                    if (final_weight is None):
                                        return '<=50K'
                                    if (final_weight > 145325):
                                        return '<=50K'
                                    if (final_weight <= 145325):
                                        if (age > 28):
                                            if (age > 29):
                                                if (education is None):
                                                    return '<=50K'
                                                if (education == '7th-8th'):
                                                    return '<=50K'
                                                if (education != '7th-8th'):
                                                    return '<=50K'
                                            if (age <= 29):
                                                if (occupation == 'Other-service'):
                                                    return '<=50K'
                                                if (occupation != 'Other-service'):
                                                    return '>50K'
                                        if (age <= 28):
                                            return '<=50K'
                    if (workclass != 'Private'):
                        if (occupation is None):
                            return '<=50K'
                        if (occupation == 'Machine-op-inspct'):
                            return '>50K'
                        if (occupation != 'Machine-op-inspct'):
                            if (age > 29):
                                return '<=50K'
                            if (age <= 29):
                                if (relationship is None):
                                    return '<=50K'
                                if (relationship == 'Husband'):
                                    if (final_weight is None):
                                        return '<=50K'
                                    if (final_weight > 149463):
                                        if (age > 27):
                                            if (hours_per_week is None):
                                                return '>50K'
                                            if (hours_per_week > 30):
                                                return '>50K'
                                            if (hours_per_week <= 30):
                                                return '<=50K'
                                        if (age <= 27):
                                            if (occupation == 'Transport-moving'):
                                                return '>50K'
                                            if (occupation != 'Transport-moving'):
                                                return '<=50K'
                                    if (final_weight <= 149463):
                                        return '<=50K'
                                if (relationship != 'Husband'):
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
                            if (final_weight is None):
                                return '>50K'
                            if (final_weight > 160393):
                                if (hours_per_week > 58):
                                    if (education_num > 13):
                                        if (workclass is None):
                                            return '>50K'
                                        if (workclass == 'Local-gov'):
                                            return '<=50K'
                                        if (workclass != 'Local-gov'):
                                            return '>50K'
                                    if (education_num <= 13):
                                        return '<=50K'
                                if (hours_per_week <= 58):
                                    if (race is None):
                                        return '>50K'
                                    if (race == 'Amer-Indian-Eskimo'):
                                        return '<=50K'
                                    if (race != 'Amer-Indian-Eskimo'):
                                        if (marital_status == 'Never-married'):
                                            if (age > 48):
                                                return '>50K'
                                            if (age <= 48):
                                                if (age > 46):
                                                    return '<=50K'
                                                if (age <= 46):
                                                    return '>50K'
                                        if (marital_status != 'Never-married'):
                                            return '>50K'
                            if (final_weight <= 160393):
                                if (hours_per_week > 47):
                                    if (final_weight > 51818):
                                        if (workclass is None):
                                            return '>50K'
                                        if (workclass == 'Private'):
                                            if (marital_status == 'Separated'):
                                                return '<=50K'
                                            if (marital_status != 'Separated'):
                                                return '>50K'
                                        if (workclass != 'Private'):
                                            if (hours_per_week > 62):
                                                if (hours_per_week > 85):
                                                    return '<=50K'
                                                if (hours_per_week <= 85):
                                                    return '>50K'
                                            if (hours_per_week <= 62):
                                                return '<=50K'
                                    if (final_weight <= 51818):
                                        return '>50K'
                                if (hours_per_week <= 47):
                                    if (age > 49):
                                        return '>50K'
                                    if (age <= 49):
                                        return '<=50K'
                        if (age <= 41):
                            if (final_weight is None):
                                return '<=50K'
                            if (final_weight > 307855):
                                return '<=50K'
                            if (final_weight <= 307855):
                                if (workclass is None):
                                    return '<=50K'
                                if (workclass == 'Self-emp-not-inc'):
                                    return '<=50K'
                                if (workclass != 'Self-emp-not-inc'):
                                    if (marital_status == 'Separated'):
                                        return '>50K'
                                    if (marital_status != 'Separated'):
                                        if (final_weight > 259049):
                                            return '<=50K'
                                        if (final_weight <= 259049):
                                            if (race is None):
                                                return '>50K'
                                            if (race == 'Black'):
                                                return '<=50K'
                                            if (race != 'Black'):
                                                if (final_weight > 40926):
                                                    return '>50K'
                                                if (final_weight <= 40926):
                                                    return '<=50K'
                    if (occupation != 'Exec-managerial'):
                        if (education_num > 14):
                            if (age > 32):
                                if (age > 52):
                                    if (marital_status == 'Widowed'):
                                        return '>50K'
                                    if (marital_status != 'Widowed'):
                                        if (workclass is None):
                                            return '<=50K'
                                        if (workclass == 'Private'):
                                            return '<=50K'
                                        if (workclass != 'Private'):
                                            if (hours_per_week > 55):
                                                return '<=50K'
                                            if (hours_per_week <= 55):
                                                if (marital_status == 'Never-married'):
                                                    return '>50K'
                                                if (marital_status != 'Never-married'):
                                                    return '<=50K'
                                if (age <= 52):
                                    if (hours_per_week > 52):
                                        if (hours_per_week > 75):
                                            return '<=50K'
                                        if (hours_per_week <= 75):
                                            return '>50K'
                                    if (hours_per_week <= 52):
                                        if (relationship is None):
                                            return '>50K'
                                        if (relationship == 'Not-in-family'):
                                            if (final_weight is None):
                                                return '>50K'
                                            if (final_weight > 215668):
                                                return '<=50K'
                                            if (final_weight <= 215668):
                                                if (workclass is None):
                                                    return '>50K'
                                                if (workclass == 'State-gov'):
                                                    return '<=50K'
                                                if (workclass != 'State-gov'):
                                                    return '>50K'
                                        if (relationship != 'Not-in-family'):
                                            return '>50K'
                            if (age <= 32):
                                if (age > 29):
                                    return '<=50K'
                                if (age <= 29):
                                    if (marital_status == 'Never-married'):
                                        if (final_weight is None):
                                            return '<=50K'
                                        if (final_weight > 92062):
                                            return '<=50K'
                                        if (final_weight <= 92062):
                                            if (sex is None):
                                                return '<=50K'
                                            if (sex == 'Male'):
                                                return '>50K'
                                            if (sex != 'Male'):
                                                return '<=50K'
                                    if (marital_status != 'Never-married'):
                                        return '>50K'
                        if (education_num <= 14):
                            if (sex is None):
                                return '<=50K'
                            if (sex == 'Male'):
                                if (hours_per_week > 55):
                                    if (occupation == 'Sales'):
                                        if (relationship is None):
                                            return '<=50K'
                                        if (relationship == 'Own-child'):
                                            return '<=50K'
                                        if (relationship != 'Own-child'):
                                            if (workclass is None):
                                                return '>50K'
                                            if (workclass == 'Self-emp-not-inc'):
                                                return '<=50K'
                                            if (workclass != 'Self-emp-not-inc'):
                                                if (race is None):
                                                    return '>50K'
                                                if (race == 'White'):
                                                    return '>50K'
                                                if (race != 'White'):
                                                    return '>50K'
                                    if (occupation != 'Sales'):
                                        if (race is None):
                                            return '<=50K'
                                        if (race == 'Asian-Pac-Islander'):
                                            return '>50K'
                                        if (race != 'Asian-Pac-Islander'):
                                            if (occupation == 'Adm-clerical'):
                                                if (marital_status == 'Never-married'):
                                                    return '>50K'
                                                if (marital_status != 'Never-married'):
                                                    return '<=50K'
                                            if (occupation != 'Adm-clerical'):
                                                if (hours_per_week > 87):
                                                    return '<=50K'
                                                if (hours_per_week <= 87):
                                                    return '<=50K'
                                if (hours_per_week <= 55):
                                    if (workclass is None):
                                        return '<=50K'
                                    if (workclass == 'State-gov'):
                                        return '<=50K'
                                    if (workclass != 'State-gov'):
                                        if (age > 32):
                                            if (workclass == 'Self-emp-inc'):
                                                return '<=50K'
                                            if (workclass != 'Self-emp-inc'):
                                                if (marital_status == 'Separated'):
                                                    return '<=50K'
                                                if (marital_status != 'Separated'):
                                                    return '>50K'
                                        if (age <= 32):
                                            if (race is None):
                                                return '<=50K'
                                            if (race == 'Black'):
                                                return '>50K'
                                            if (race != 'Black'):
                                                if (workclass == 'Private'):
                                                    return '<=50K'
                                                if (workclass != 'Private'):
                                                    return '<=50K'
                            if (sex != 'Male'):
                                if (final_weight is None):
                                    return '<=50K'
                                if (final_weight > 151124):
                                    if (final_weight > 158605):
                                        if (marital_status == 'Married-spouse-absent'):
                                            return '>50K'
                                        if (marital_status != 'Married-spouse-absent'):
                                            if (race is None):
                                                return '<=50K'
                                            if (race == 'Asian-Pac-Islander'):
                                                return '>50K'
                                            if (race != 'Asian-Pac-Islander'):
                                                if (age > 43):
                                                    return '<=50K'
                                                if (age <= 43):
                                                    return '<=50K'
                                    if (final_weight <= 158605):
                                        if (final_weight > 157227):
                                            return '<=50K'
                                        if (final_weight <= 157227):
                                            return '>50K'
                                if (final_weight <= 151124):
                                    if (workclass is None):
                                        return '<=50K'
                                    if (workclass == 'Federal-gov'):
                                        return '>50K'
                                    if (workclass != 'Federal-gov'):
                                        if (relationship is None):
                                            return '<=50K'
                                        if (relationship == 'Not-in-family'):
                                            if (hours_per_week > 61):
                                                if (hours_per_week > 67):
                                                    return '<=50K'
                                                if (hours_per_week <= 67):
                                                    return '>50K'
                                            if (hours_per_week <= 61):
                                                if (final_weight > 107801):
                                                    return '<=50K'
                                                if (final_weight <= 107801):
                                                    return '<=50K'
                                        if (relationship != 'Not-in-family'):
                                            return '<=50K'
                if (hours_per_week <= 43):
                    if (education_num > 14):
                        if (age > 32):
                            if (sex is None):
                                return '>50K'
                            if (sex == 'Male'):
                                if (hours_per_week > 21):
                                    if (final_weight is None):
                                        return '>50K'
                                    if (final_weight > 107803):
                                        return '>50K'
                                    if (final_weight <= 107803):
                                        if (education_num > 15):
                                            return '<=50K'
                                        if (education_num <= 15):
                                            if (workclass is None):
                                                return '>50K'
                                            if (workclass == 'State-gov'):
                                                return '<=50K'
                                            if (workclass != 'State-gov'):
                                                return '>50K'
                                if (hours_per_week <= 21):
                                    if (marital_status == 'Widowed'):
                                        return '>50K'
                                    if (marital_status != 'Widowed'):
                                        return '<=50K'
                            if (sex != 'Male'):
                                if (marital_status == 'Never-married'):
                                    if (final_weight is None):
                                        return '>50K'
                                    if (final_weight > 386027):
                                        return '<=50K'
                                    if (final_weight <= 386027):
                                        if (education_num > 15):
                                            return '>50K'
                                        if (education_num <= 15):
                                            if (hours_per_week > 37):
                                                if (occupation is None):
                                                    return '<=50K'
                                                if (occupation == 'Prof-specialty'):
                                                    return '<=50K'
                                                if (occupation != 'Prof-specialty'):
                                                    return '<=50K'
                                            if (hours_per_week <= 37):
                                                return '>50K'
                                if (marital_status != 'Never-married'):
                                    if (final_weight is None):
                                        return '<=50K'
                                    if (final_weight > 170081):
                                        if (final_weight > 227385):
                                            return '<=50K'
                                        if (final_weight <= 227385):
                                            if (age > 40):
                                                if (age > 47):
                                                    return '<=50K'
                                                if (age <= 47):
                                                    return '>50K'
                                            if (age <= 40):
                                                return '<=50K'
                                    if (final_weight <= 170081):
                                        return '<=50K'
                        if (age <= 32):
                            return '<=50K'
                    if (education_num <= 14):
                        if (age > 45):
                            if (hours_per_week > 31):
                                if (relationship is None):
                                    return '<=50K'
                                if (relationship == 'Not-in-family'):
                                    if (workclass is None):
                                        return '<=50K'
                                    if (workclass == 'Federal-gov'):
                                        return '<=50K'
                                    if (workclass != 'Federal-gov'):
                                        if (marital_status == 'Never-married'):
                                            if (age > 54):
                                                return '<=50K'
                                            if (age <= 54):
                                                if (education_num > 13):
                                                    return '>50K'
                                                if (education_num <= 13):
                                                    return '<=50K'
                                        if (marital_status != 'Never-married'):
                                            if (age > 59):
                                                if (age > 64):
                                                    return '<=50K'
                                                if (age <= 64):
                                                    return '>50K'
                                            if (age <= 59):
                                                if (age > 55):
                                                    return '<=50K'
                                                if (age <= 55):
                                                    return '<=50K'
                                if (relationship != 'Not-in-family'):
                                    if (age > 49):
                                        if (sex is None):
                                            return '<=50K'
                                        if (sex == 'Male'):
                                            if (occupation is None):
                                                return '<=50K'
                                            if (occupation == 'Prof-specialty'):
                                                return '>50K'
                                            if (occupation != 'Prof-specialty'):
                                                return '<=50K'
                                        if (sex != 'Male'):
                                            return '<=50K'
                                    if (age <= 49):
                                        if (age > 46):
                                            if (sex is None):
                                                return '<=50K'
                                            if (sex == 'Male'):
                                                return '>50K'
                                            if (sex != 'Male'):
                                                if (education_num > 13):
                                                    return '<=50K'
                                                if (education_num <= 13):
                                                    return '<=50K'
                                        if (age <= 46):
                                            return '<=50K'
                            if (hours_per_week <= 31):
                                if (marital_status == 'Divorced'):
                                    return '<=50K'
                                if (marital_status != 'Divorced'):
                                    if (occupation is None):
                                        return '<=50K'
                                    if (occupation == 'Craft-repair'):
                                        return '>50K'
                                    if (occupation != 'Craft-repair'):
                                        if (hours_per_week > 18):
                                            if (age > 77):
                                                return '>50K'
                                            if (age <= 77):
                                                if (final_weight is None):
                                                    return '<=50K'
                                                if (final_weight > 154955):
                                                    return '<=50K'
                                                if (final_weight <= 154955):
                                                    return '<=50K'
                                        if (hours_per_week <= 18):
                                            return '<=50K'
                        if (age <= 45):
                            if (hours_per_week > 34):
                                if (workclass is None):
                                    return '<=50K'
                                if (workclass == 'State-gov'):
                                    return '<=50K'
                                if (workclass != 'State-gov'):
                                    if (workclass == 'Federal-gov'):
                                        if (sex is None):
                                            return '<=50K'
                                        if (sex == 'Male'):
                                            if (age > 40):
                                                return '>50K'
                                            if (age <= 40):
                                                if (marital_status == 'Widowed'):
                                                    return '>50K'
                                                if (marital_status != 'Widowed'):
                                                    return '<=50K'
                                        if (sex != 'Male'):
                                            return '<=50K'
                                    if (workclass != 'Federal-gov'):
                                        if (final_weight is None):
                                            return '<=50K'
                                        if (final_weight > 101112):
                                            if (age > 34):
                                                if (marital_status == 'Never-married'):
                                                    return '<=50K'
                                                if (marital_status != 'Never-married'):
                                                    return '<=50K'
                                            if (age <= 34):
                                                if (occupation is None):
                                                    return '<=50K'
                                                if (occupation == 'Adm-clerical'):
                                                    return '<=50K'
                                                if (occupation != 'Adm-clerical'):
                                                    return '<=50K'
                                        if (final_weight <= 101112):
                                            if (age > 28):
                                                return '<=50K'
                                            if (age <= 28):
                                                if (sex is None):
                                                    return '<=50K'
                                                if (sex == 'Male'):
                                                    return '<=50K'
                                                if (sex != 'Male'):
                                                    return '<=50K'
                            if (hours_per_week <= 34):
                                if (final_weight is None):
                                    return '<=50K'
                                if (final_weight > 391238):
                                    return '>50K'
                                if (final_weight <= 391238):
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
                            if (final_weight is None):
                                return '<=50K'
                            if (final_weight > 156075):
                                return '>50K'
                            if (final_weight <= 156075):
                                return '<=50K'
                        if (hours_per_week <= 77):
                            if (race is None):
                                return '<=50K'
                            if (race == 'Amer-Indian-Eskimo'):
                                if (hours_per_week > 41):
                                    return '<=50K'
                                if (hours_per_week <= 41):
                                    return '>50K'
                            if (race != 'Amer-Indian-Eskimo'):
                                if (workclass is None):
                                    return '<=50K'
                                if (workclass == 'Self-emp-not-inc'):
                                    if (relationship == 'Not-in-family'):
                                        return '<=50K'
                                    if (relationship != 'Not-in-family'):
                                        return '>50K'
                                if (workclass != 'Self-emp-not-inc'):
                                    if (workclass == 'Private'):
                                        if (occupation is None):
                                            return '<=50K'
                                        if (occupation == 'Prof-specialty'):
                                            if (final_weight is None):
                                                return '<=50K'
                                            if (final_weight > 187971):
                                                if (final_weight > 318115):
                                                    return '<=50K'
                                                if (final_weight <= 318115):
                                                    return '<=50K'
                                            if (final_weight <= 187971):
                                                if (final_weight > 36821):
                                                    return '<=50K'
                                                if (final_weight <= 36821):
                                                    return '>50K'
                                        if (occupation != 'Prof-specialty'):
                                            if (relationship == 'Unmarried'):
                                                if (race == 'White'):
                                                    return '<=50K'
                                                if (race != 'White'):
                                                    return '<=50K'
                                            if (relationship != 'Unmarried'):
                                                if (occupation == 'Exec-managerial'):
                                                    return '<=50K'
                                                if (occupation != 'Exec-managerial'):
                                                    return '<=50K'
                                    if (workclass != 'Private'):
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
                            if (occupation is None):
                                return '<=50K'
                            if (occupation == 'Adm-clerical'):
                                return '<=50K'
                            if (occupation != 'Adm-clerical'):
                                if (hours_per_week > 67):
                                    return '<=50K'
                                if (hours_per_week <= 67):
                                    if (marital_status == 'Separated'):
                                        return '>50K'
                                    if (marital_status != 'Separated'):
                                        if (workclass is None):
                                            return '<=50K'
                                        if (workclass == 'Self-emp-inc'):
                                            if (marital_status == 'Widowed'):
                                                return '>50K'
                                            if (marital_status != 'Widowed'):
                                                return '<=50K'
                                        if (workclass != 'Self-emp-inc'):
                                            if (hours_per_week > 61):
                                                return '>50K'
                                            if (hours_per_week <= 61):
                                                if (occupation == 'Tech-support'):
                                                    return '>50K'
                                                if (occupation != 'Tech-support'):
                                                    return '<=50K'
                        if (age <= 53):
                            if (relationship is None):
                                return '<=50K'
                            if (relationship == 'Not-in-family'):
                                if (education is None):
                                    return '<=50K'
                                if (education == 'HS-grad'):
                                    if (hours_per_week > 47):
                                        if (final_weight is None):
                                            return '<=50K'
                                        if (final_weight > 30779):
                                            if (race is None):
                                                return '<=50K'
                                            if (race == 'White'):
                                                if (final_weight > 521347):
                                                    return '>50K'
                                                if (final_weight <= 521347):
                                                    return '<=50K'
                                            if (race != 'White'):
                                                return '<=50K'
                                        if (final_weight <= 30779):
                                            if (age > 40):
                                                return '<=50K'
                                            if (age <= 40):
                                                return '>50K'
                                    if (hours_per_week <= 47):
                                        if (workclass is None):
                                            return '<=50K'
                                        if (workclass == 'Federal-gov'):
                                            if (marital_status == 'Never-married'):
                                                return '>50K'
                                            if (marital_status != 'Never-married'):
                                                return '<=50K'
                                        if (workclass != 'Federal-gov'):
                                            return '<=50K'
                                if (education != 'HS-grad'):
                                    if (workclass is None):
                                        return '<=50K'
                                    if (workclass == 'Self-emp-not-inc'):
                                        return '<=50K'
                                    if (workclass != 'Self-emp-not-inc'):
                                        if (age > 52):
                                            if (hours_per_week > 52):
                                                return '<=50K'
                                            if (hours_per_week <= 52):
                                                return '>50K'
                                        if (age <= 52):
                                            if (occupation is None):
                                                return '<=50K'
                                            if (occupation == 'Other-service'):
                                                return '<=50K'
                                            if (occupation != 'Other-service'):
                                                if (age > 35):
                                                    return '<=50K'
                                                if (age <= 35):
                                                    return '<=50K'
                            if (relationship != 'Not-in-family'):
                                if (age > 39):
                                    if (age > 45):
                                        if (education is None):
                                            return '<=50K'
                                        if (education == 'Some-college'):
                                            if (final_weight is None):
                                                return '<=50K'
                                            if (final_weight > 162003):
                                                if (final_weight > 182557):
                                                    return '<=50K'
                                                if (final_weight <= 182557):
                                                    return '>50K'
                                            if (final_weight <= 162003):
                                                return '<=50K'
                                        if (education != 'Some-college'):
                                            return '<=50K'
                                    if (age <= 45):
                                        if (final_weight is None):
                                            return '<=50K'
                                        if (final_weight > 63827):
                                            if (occupation is None):
                                                return '<=50K'
                                            if (occupation == 'Adm-clerical'):
                                                if (final_weight > 187713):
                                                    return '<=50K'
                                                if (final_weight <= 187713):
                                                    return '>50K'
                                            if (occupation != 'Adm-clerical'):
                                                if (relationship == 'Wife'):
                                                    return '>50K'
                                                if (relationship != 'Wife'):
                                                    return '<=50K'
                                        if (final_weight <= 63827):
                                            return '<=50K'
                                if (age <= 39):
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
                            if (hours_per_week > 32):
                                return '>50K'
                            if (hours_per_week <= 32):
                                return '<=50K'
                        if (relationship != 'Wife'):
                            if (age > 59):
                                if (workclass is None):
                                    return '<=50K'
                                if (workclass == 'Private'):
                                    return '<=50K'
                                if (workclass != 'Private'):
                                    if (education is None):
                                        return '<=50K'
                                    if (education == 'Some-college'):
                                        return '>50K'
                                    if (education != 'Some-college'):
                                        if (education == '11th'):
                                            return '>50K'
                                        if (education != '11th'):
                                            return '<=50K'
                            if (age <= 59):
                                return '<=50K'
                    if (occupation != 'Other-service'):
                        if (occupation == 'Machine-op-inspct'):
                            if (relationship is None):
                                return '<=50K'
                            if (relationship == 'Unmarried'):
                                if (sex is None):
                                    return '<=50K'
                                if (sex == 'Male'):
                                    if (age > 37):
                                        return '<=50K'
                                    if (age <= 37):
                                        if (age > 36):
                                            return '>50K'
                                        if (age <= 36):
                                            return '<=50K'
                                if (sex != 'Male'):
                                    return '<=50K'
                            if (relationship != 'Unmarried'):
                                return '<=50K'
                        if (occupation != 'Machine-op-inspct'):
                            if (relationship is None):
                                return '<=50K'
                            if (relationship == 'Not-in-family'):
                                if (occupation == 'Adm-clerical'):
                                    if (marital_status == 'Married-spouse-absent'):
                                        if (education is None):
                                            return '<=50K'
                                        if (education == 'HS-grad'):
                                            return '<=50K'
                                        if (education != 'HS-grad'):
                                            return '>50K'
                                    if (marital_status != 'Married-spouse-absent'):
                                        if (sex is None):
                                            return '<=50K'
                                        if (sex == 'Male'):
                                            if (marital_status == 'Never-married'):
                                                return '<=50K'
                                            if (marital_status != 'Never-married'):
                                                if (final_weight is None):
                                                    return '<=50K'
                                                if (final_weight > 126659):
                                                    return '<=50K'
                                                if (final_weight <= 126659):
                                                    return '<=50K'
                                        if (sex != 'Male'):
                                            if (final_weight is None):
                                                return '<=50K'
                                            if (final_weight > 61433):
                                                if (hours_per_week > 18):
                                                    return '<=50K'
                                                if (hours_per_week <= 18):
                                                    return '<=50K'
                                            if (final_weight <= 61433):
                                                if (final_weight > 20997):
                                                    return '<=50K'
                                                if (final_weight <= 20997):
                                                    return '>50K'
                                if (occupation != 'Adm-clerical'):
                                    if (workclass is None):
                                        return '<=50K'
                                    if (workclass == 'Self-emp-inc'):
                                        if (marital_status == 'Widowed'):
                                            if (education_num > 8):
                                                return '>50K'
                                            if (education_num <= 8):
                                                return '<=50K'
                                        if (marital_status != 'Widowed'):
                                            if (final_weight is None):
                                                return '<=50K'
                                            if (final_weight > 101318):
                                                return '<=50K'
                                            if (final_weight <= 101318):
                                                return '>50K'
                                    if (workclass != 'Self-emp-inc'):
                                        if (occupation == 'Protective-serv'):
                                            if (age > 47):
                                                return '<=50K'
                                            if (age <= 47):
                                                if (education_num > 10):
                                                    return '<=50K'
                                                if (education_num <= 10):
                                                    return '>50K'
                                        if (occupation != 'Protective-serv'):
                                            if (occupation == 'Transport-moving'):
                                                if (education is None):
                                                    return '<=50K'
                                                if (education == 'Some-college'):
                                                    return '<=50K'
                                                if (education != 'Some-college'):
                                                    return '<=50K'
                                            if (occupation != 'Transport-moving'):
                                                if (occupation == 'Sales'):
                                                    return '<=50K'
                                                if (occupation != 'Sales'):
                                                    return '<=50K'
                            if (relationship != 'Not-in-family'):
                                if (occupation == 'Prof-specialty'):
                                    if (workclass is None):
                                        return '<=50K'
                                    if (workclass == 'Federal-gov'):
                                        if (final_weight is None):
                                            return '<=50K'
                                        if (final_weight > 94417):
                                            return '>50K'
                                        if (final_weight <= 94417):
                                            return '<=50K'
                                    if (workclass != 'Federal-gov'):
                                        if (final_weight is None):
                                            return '<=50K'
                                        if (final_weight > 338432):
                                            return '>50K'
                                        if (final_weight <= 338432):
                                            if (final_weight > 175915):
                                                return '<=50K'
                                            if (final_weight <= 175915):
                                                if (final_weight > 175017):
                                                    return '>50K'
                                                if (final_weight <= 175017):
                                                    return '<=50K'
                                if (occupation != 'Prof-specialty'):
                                    if (relationship == 'Wife'):
                                        if (education_num > 11):
                                            return '<=50K'
                                        if (education_num <= 11):
                                            return '>50K'
                                    if (relationship != 'Wife'):
                                        if (marital_status == 'Separated'):
                                            return '<=50K'
                                        if (marital_status != 'Separated'):
                                            if (education is None):
                                                return '<=50K'
                                            if (education == 'Assoc-voc'):
                                                if (workclass is None):
                                                    return '<=50K'
                                                if (workclass == 'Federal-gov'):
                                                    return '<=50K'
                                                if (workclass != 'Federal-gov'):
                                                    return '<=50K'
                                            if (education != 'Assoc-voc'):
                                                if (occupation == 'Adm-clerical'):
                                                    return '<=50K'
                                                if (occupation != 'Adm-clerical'):
                                                    return '<=50K'
            if (age <= 31):
                if (age > 21):
                    if (hours_per_week is None):
                        return '<=50K'
                    if (hours_per_week > 41):
                        if (workclass is None):
                            return '<=50K'
                        if (workclass == 'Private'):
                            if (relationship is None):
                                return '<=50K'
                            if (relationship == 'Not-in-family'):
                                if (occupation is None):
                                    return '<=50K'
                                if (occupation == 'Exec-managerial'):
                                    if (marital_status == 'Never-married'):
                                        if (hours_per_week > 62):
                                            return '>50K'
                                        if (hours_per_week <= 62):
                                            return '<=50K'
                                    if (marital_status != 'Never-married'):
                                        if (final_weight is None):
                                            return '>50K'
                                        if (final_weight > 111019):
                                            return '>50K'
                                        if (final_weight <= 111019):
                                            return '<=50K'
                                if (occupation != 'Exec-managerial'):
                                    if (education is None):
                                        return '<=50K'
                                    if (education == '9th'):
                                        if (hours_per_week > 44):
                                            return '<=50K'
                                        if (hours_per_week <= 44):
                                            return '>50K'
                                    if (education != '9th'):
                                        if (occupation == 'Transport-moving'):
                                            if (hours_per_week > 51):
                                                return '<=50K'
                                            if (hours_per_week <= 51):
                                                if (final_weight is None):
                                                    return '<=50K'
                                                if (final_weight > 81673):
                                                    return '<=50K'
                                                if (final_weight <= 81673):
                                                    return '>50K'
                                        if (occupation != 'Transport-moving'):
                                            if (race is None):
                                                return '<=50K'
                                            if (race == 'Asian-Pac-Islander'):
                                                if (sex is None):
                                                    return '<=50K'
                                                if (sex == 'Male'):
                                                    return '>50K'
                                                if (sex != 'Male'):
                                                    return '<=50K'
                                            if (race != 'Asian-Pac-Islander'):
                                                return '<=50K'
                            if (relationship != 'Not-in-family'):
                                return '<=50K'
                        if (workclass != 'Private'):
                            if (sex is None):
                                return '<=50K'
                            if (sex == 'Male'):
                                if (hours_per_week > 49):
                                    if (occupation is None):
                                        return '<=50K'
                                    if (occupation == 'Exec-managerial'):
                                        return '>50K'
                                    if (occupation != 'Exec-managerial'):
                                        if (final_weight is None):
                                            return '<=50K'
                                        if (final_weight > 378259):
                                            return '>50K'
                                        if (final_weight <= 378259):
                                            if (race is None):
                                                return '<=50K'
                                            if (race == 'Asian-Pac-Islander'):
                                                return '>50K'
                                            if (race != 'Asian-Pac-Islander'):
                                                if (final_weight > 174056):
                                                    return '<=50K'
                                                if (final_weight <= 174056):
                                                    return '<=50K'
                                if (hours_per_week <= 49):
                                    if (education_num > 8):
                                        return '<=50K'
                                    if (education_num <= 8):
                                        if (race is None):
                                            return '<=50K'
                                        if (race == 'White'):
                                            return '>50K'
                                        if (race != 'White'):
                                            return '<=50K'
                            if (sex != 'Male'):
                                return '<=50K'
                    if (hours_per_week <= 41):
                        if (education_num > 9):
                            if (hours_per_week > 29):
                                if (relationship is None):
                                    return '<=50K'
                                if (relationship == 'Wife'):
                                    return '>50K'
                                if (relationship != 'Wife'):
                                    if (occupation is None):
                                        return '<=50K'
                                    if (occupation == 'Protective-serv'):
                                        if (final_weight is None):
                                            return '<=50K'
                                        if (final_weight > 199791):
                                            return '<=50K'
                                        if (final_weight <= 199791):
                                            if (relationship == 'Own-child'):
                                                return '>50K'
                                            if (relationship != 'Own-child'):
                                                if (final_weight > 95966):
                                                    return '<=50K'
                                                if (final_weight <= 95966):
                                                    return '<=50K'
                                    if (occupation != 'Protective-serv'):
                                        if (relationship == 'Own-child'):
                                            if (age > 29):
                                                if (occupation == 'Craft-repair'):
                                                    return '<=50K'
                                                if (occupation != 'Craft-repair'):
                                                    return '<=50K'
                                            if (age <= 29):
                                                return '<=50K'
                                        if (relationship != 'Own-child'):
                                            if (age > 30):
                                                return '<=50K'
                                            if (age <= 30):
                                                if (education_num > 10):
                                                    return '<=50K'
                                                if (education_num <= 10):
                                                    return '<=50K'
                            if (hours_per_week <= 29):
                                return '<=50K'
                        if (education_num <= 9):
                            if (age > 27):
                                if (final_weight is None):
                                    return '<=50K'
                                if (final_weight > 94030):
                                    if (final_weight > 334106):
                                        if (occupation is None):
                                            return '<=50K'
                                        if (occupation == 'Craft-repair'):
                                            if (marital_status == 'Never-married'):
                                                if (relationship is None):
                                                    return '<=50K'
                                                if (relationship == 'Not-in-family'):
                                                    return '<=50K'
                                                if (relationship != 'Not-in-family'):
                                                    return '>50K'
                                            if (marital_status != 'Never-married'):
                                                return '<=50K'
                                        if (occupation != 'Craft-repair'):
                                            return '<=50K'
                                    if (final_weight <= 334106):
                                        return '<=50K'
                                if (final_weight <= 94030):
                                    if (marital_status == 'Divorced'):
                                        if (race is None):
                                            return '<=50K'
                                        if (race == 'Amer-Indian-Eskimo'):
                                            return '>50K'
                                        if (race != 'Amer-Indian-Eskimo'):
                                            if (occupation is None):
                                                return '<=50K'
                                            if (occupation == 'Other-service'):
                                                return '>50K'
                                            if (occupation != 'Other-service'):
                                                return '<=50K'
                                    if (marital_status != 'Divorced'):
                                        return '<=50K'
                            if (age <= 27):
                                return '<=50K'
                if (age <= 21):
                    if (education is None):
                        return '<=50K'
                    if (education == '7th-8th'):
                        if (occupation is None):
                            return '<=50K'
                        if (occupation == 'Other-service'):
                            if (hours_per_week is None):
                                return '<=50K'
                            if (hours_per_week > 50):
                                return '>50K'
                            if (hours_per_week <= 50):
                                return '<=50K'
                        if (occupation != 'Other-service'):
                            return '<=50K'
                    if (education != '7th-8th'):
                        return '<=50K'
