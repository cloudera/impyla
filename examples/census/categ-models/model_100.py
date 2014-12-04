def predict_income(impala_function_context, age, workclass, final_weight, education, education_num, marital_status, occupation, relationship, race, sex, hours_per_week, native_country, income):
    """ Predictor for income from model/536030f60af5e8092c001612

        https://archive.ics.uci.edu/ml/machine-learning-databases/adult/
    """
    if (marital_status is None):
        return -7811984082516642400
    if (marital_status == -7213454403760958791):
        if (education_num is None):
            return -7811984082516642400
        if (education_num > 12):
            if (hours_per_week is None):
                return -671483940756762216
            if (hours_per_week > 31):
                if (age is None):
                    return -671483940756762216
                if (age > 28):
                    if (education_num > 13):
                        if (age > 58):
                            return -671483940756762216
                        if (age <= 58):
                            return -671483940756762216
                    if (education_num <= 13):
                        if (occupation is None):
                            return -671483940756762216
                        if (occupation == -6990906632015037778):
                            return -671483940756762216
                        if (occupation != -6990906632015037778):
                            return -671483940756762216
                if (age <= 28):
                    if (age > 24):
                        if (occupation is None):
                            return -7811984082516642400
                        if (occupation == 4779842868628447834):
                            return -671483940756762216
                        if (occupation != 4779842868628447834):
                            return -7811984082516642400
                    if (age <= 24):
                        if (final_weight is None):
                            return -7811984082516642400
                        if (final_weight > 492053):
                            return -671483940756762216
                        if (final_weight <= 492053):
                            return -7811984082516642400
            if (hours_per_week <= 31):
                if (sex is None):
                    return -7811984082516642400
                if (sex == 6306819796163687131):
                    if (age is None):
                        return -7811984082516642400
                    if (age > 29):
                        if (age > 62):
                            return -7811984082516642400
                        if (age <= 62):
                            return -7811984082516642400
                    if (age <= 29):
                        return -7811984082516642400
                if (sex != 6306819796163687131):
                    if (final_weight is None):
                        return -671483940756762216
                    if (final_weight > 264521):
                        if (hours_per_week > 7):
                            return -7811984082516642400
                        if (hours_per_week <= 7):
                            return -671483940756762216
                    if (final_weight <= 264521):
                        if (age is None):
                            return -671483940756762216
                        if (age > 26):
                            return -671483940756762216
                        if (age <= 26):
                            return -7811984082516642400
        if (education_num <= 12):
            if (education_num > 8):
                if (age is None):
                    return -7811984082516642400
                if (age > 35):
                    if (hours_per_week is None):
                        return -7811984082516642400
                    if (hours_per_week > 33):
                        if (education_num > 9):
                            return -671483940756762216
                        if (education_num <= 9):
                            return -7811984082516642400
                    if (hours_per_week <= 33):
                        if (workclass is None):
                            return -7811984082516642400
                        if (workclass == -7197995106135439896):
                            return -671483940756762216
                        if (workclass != -7197995106135439896):
                            return -7811984082516642400
                if (age <= 35):
                    if (age > 24):
                        if (occupation is None):
                            return -7811984082516642400
                        if (occupation == -6990906632015037778):
                            return -7811984082516642400
                        if (occupation != -6990906632015037778):
                            return -7811984082516642400
                    if (age <= 24):
                        if (hours_per_week is None):
                            return -7811984082516642400
                        if (hours_per_week > 45):
                            return -7811984082516642400
                        if (hours_per_week <= 45):
                            return -7811984082516642400
            if (education_num <= 8):
                if (age is None):
                    return -7811984082516642400
                if (age > 36):
                    if (hours_per_week is None):
                        return -7811984082516642400
                    if (hours_per_week > 22):
                        if (education_num > 5):
                            return -7811984082516642400
                        if (education_num <= 5):
                            return -7811984082516642400
                    if (hours_per_week <= 22):
                        return -7811984082516642400
                if (age <= 36):
                    if (workclass is None):
                        return -7811984082516642400
                    if (workclass == 8585012838816931822):
                        if (age > 35):
                            return -7811984082516642400
                        if (age <= 35):
                            return -7811984082516642400
                    if (workclass != 8585012838816931822):
                        if (occupation is None):
                            return -7811984082516642400
                        if (occupation == -8227066636055033186):
                            return -671483940756762216
                        if (occupation != -8227066636055033186):
                            return -7811984082516642400
    if (marital_status != -7213454403760958791):
        if (education_num is None):
            return -7811984082516642400
        if (education_num > 12):
            if (age is None):
                return -7811984082516642400
            if (age > 27):
                if (hours_per_week is None):
                    return -7811984082516642400
                if (hours_per_week > 43):
                    if (occupation is None):
                        return -7811984082516642400
                    if (occupation == -6990906632015037778):
                        if (age > 41):
                            return -671483940756762216
                        if (age <= 41):
                            return -7811984082516642400
                    if (occupation != -6990906632015037778):
                        if (education_num > 14):
                            return -671483940756762216
                        if (education_num <= 14):
                            return -7811984082516642400
                if (hours_per_week <= 43):
                    if (education_num > 14):
                        if (age > 32):
                            return -671483940756762216
                        if (age <= 32):
                            return -7811984082516642400
                    if (education_num <= 14):
                        if (age > 45):
                            return -7811984082516642400
                        if (age <= 45):
                            return -7811984082516642400
            if (age <= 27):
                if (hours_per_week is None):
                    return -7811984082516642400
                if (hours_per_week > 38):
                    if (relationship is None):
                        return -7811984082516642400
                    if (relationship == -7487827120114232249):
                        return -671483940756762216
                    if (relationship != -7487827120114232249):
                        if (hours_per_week > 77):
                            return -7811984082516642400
                        if (hours_per_week <= 77):
                            return -7811984082516642400
                if (hours_per_week <= 38):
                    return -7811984082516642400
        if (education_num <= 12):
            if (age is None):
                return -7811984082516642400
            if (age > 31):
                if (hours_per_week is None):
                    return -7811984082516642400
                if (hours_per_week > 41):
                    if (education_num > 5):
                        if (age > 53):
                            return -7811984082516642400
                        if (age <= 53):
                            return -7811984082516642400
                    if (education_num <= 5):
                        return -7811984082516642400
                if (hours_per_week <= 41):
                    if (occupation is None):
                        return -7811984082516642400
                    if (occupation == 8618684898378336489):
                        if (relationship is None):
                            return -7811984082516642400
                        if (relationship == -7487827120114232249):
                            return -7811984082516642400
                        if (relationship != -7487827120114232249):
                            return -7811984082516642400
                    if (occupation != 8618684898378336489):
                        if (occupation == -8227066636055033186):
                            return -7811984082516642400
                        if (occupation != -8227066636055033186):
                            return -7811984082516642400
            if (age <= 31):
                if (age > 21):
                    if (hours_per_week is None):
                        return -7811984082516642400
                    if (hours_per_week > 41):
                        if (workclass is None):
                            return -7811984082516642400
                        if (workclass == 8585012838816931822):
                            return -7811984082516642400
                        if (workclass != 8585012838816931822):
                            return -7811984082516642400
                    if (hours_per_week <= 41):
                        if (education_num > 9):
                            return -7811984082516642400
                        if (education_num <= 9):
                            return -7811984082516642400
                if (age <= 21):
                    if (education is None):
                        return -7811984082516642400
                    if (education == -3305009427453673313):
                        if (occupation is None):
                            return -7811984082516642400
                        if (occupation == 8618684898378336489):
                            return -7811984082516642400
                        if (occupation != 8618684898378336489):
                            return -7811984082516642400
                    if (education != -3305009427453673313):
                        return -7811984082516642400
