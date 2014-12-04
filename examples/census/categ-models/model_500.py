def predict_income(impala_function_context, age, workclass, final_weight, education, education_num, marital_status, occupation, relationship, race, sex, hours_per_week, native_country, income):
    """ Predictor for income from model/5360311dffa04466f60007dc

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
                            if (education_num > 14):
                                if (workclass is None):
                                    return -671483940756762216
                                if (workclass == -857656620414700721):
                                    return -7811984082516642400
                                if (workclass != -857656620414700721):
                                    if (occupation is None):
                                        return -671483940756762216
                                    if (occupation == -5484833051640498835):
                                        return -7811984082516642400
                                    if (occupation != -5484833051640498835):
                                        return -671483940756762216
                            if (education_num <= 14):
                                if (hours_per_week > 36):
                                    if (workclass is None):
                                        return -671483940756762216
                                    if (workclass == -7197995106135439896):
                                        return -671483940756762216
                                    if (workclass != -7197995106135439896):
                                        return -671483940756762216
                                if (hours_per_week <= 36):
                                    return -7811984082516642400
                        if (age <= 58):
                            if (age > 38):
                                if (education_num > 14):
                                    if (hours_per_week > 49):
                                        return -671483940756762216
                                    if (hours_per_week <= 49):
                                        return -671483940756762216
                                if (education_num <= 14):
                                    if (workclass is None):
                                        return -671483940756762216
                                    if (workclass == -1136074064918994416):
                                        return -671483940756762216
                                    if (workclass != -1136074064918994416):
                                        return -671483940756762216
                            if (age <= 38):
                                if (occupation is None):
                                    return -671483940756762216
                                if (occupation == 3088227676756162338):
                                    return -7811984082516642400
                                if (occupation != 3088227676756162338):
                                    if (hours_per_week > 42):
                                        return -671483940756762216
                                    if (hours_per_week <= 42):
                                        return -671483940756762216
                    if (education_num <= 13):
                        if (occupation is None):
                            return -671483940756762216
                        if (occupation == -6990906632015037778):
                            if (workclass is None):
                                return -671483940756762216
                            if (workclass == -1136074064918994416):
                                if (final_weight is None):
                                    return -671483940756762216
                                if (final_weight > 90244):
                                    if (age > 48):
                                        return -671483940756762216
                                    if (age <= 48):
                                        return -7811984082516642400
                                if (final_weight <= 90244):
                                    return -7811984082516642400
                            if (workclass != -1136074064918994416):
                                if (hours_per_week > 67):
                                    if (hours_per_week > 73):
                                        return -671483940756762216
                                    if (hours_per_week <= 73):
                                        return -7811984082516642400
                                if (hours_per_week <= 67):
                                    if (race is None):
                                        return -671483940756762216
                                    if (race == 3939476748445039507):
                                        return -7811984082516642400
                                    if (race != 3939476748445039507):
                                        return -671483940756762216
                        if (occupation != -6990906632015037778):
                            if (relationship is None):
                                return -671483940756762216
                            if (relationship == 8744150760759310329):
                                return -7811984082516642400
                            if (relationship != 8744150760759310329):
                                if (race is None):
                                    return -671483940756762216
                                if (race == 3939476748445039507):
                                    return -7811984082516642400
                                if (race != 3939476748445039507):
                                    if (final_weight is None):
                                        return -671483940756762216
                                    if (final_weight > 121061):
                                        return -671483940756762216
                                    if (final_weight <= 121061):
                                        return -671483940756762216
                if (age <= 28):
                    if (age > 24):
                        if (occupation is None):
                            return -7811984082516642400
                        if (occupation == 4779842868628447834):
                            return -671483940756762216
                        if (occupation != 4779842868628447834):
                            if (hours_per_week > 41):
                                if (hours_per_week > 46):
                                    if (education_num > 14):
                                        return -7811984082516642400
                                    if (education_num <= 14):
                                        return -7811984082516642400
                                if (hours_per_week <= 46):
                                    if (occupation == 5332362397248960598):
                                        return -7811984082516642400
                                    if (occupation != 5332362397248960598):
                                        return -671483940756762216
                            if (hours_per_week <= 41):
                                if (final_weight is None):
                                    return -7811984082516642400
                                if (final_weight > 159383):
                                    if (final_weight > 260996):
                                        return -671483940756762216
                                    if (final_weight <= 260996):
                                        return -7811984082516642400
                                if (final_weight <= 159383):
                                    if (final_weight > 100631):
                                        return -671483940756762216
                                    if (final_weight <= 100631):
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
                            if (age > 78):
                                if (hours_per_week > 9):
                                    return -671483940756762216
                                if (hours_per_week <= 9):
                                    return -7811984082516642400
                            if (age <= 78):
                                if (hours_per_week > 13):
                                    if (race is None):
                                        return -7811984082516642400
                                    if (race == -1569537633132385766):
                                        return -7811984082516642400
                                    if (race != -1569537633132385766):
                                        return -671483940756762216
                                if (hours_per_week <= 13):
                                    if (occupation is None):
                                        return -7811984082516642400
                                    if (occupation == -6990906632015037778):
                                        return -671483940756762216
                                    if (occupation != -6990906632015037778):
                                        return -7811984082516642400
                        if (age <= 62):
                            if (hours_per_week > 12):
                                if (workclass is None):
                                    return -671483940756762216
                                if (workclass == -4284295320506787287):
                                    return -7811984082516642400
                                if (workclass != -4284295320506787287):
                                    if (hours_per_week > 21):
                                        return -7811984082516642400
                                    if (hours_per_week <= 21):
                                        return -671483940756762216
                            if (hours_per_week <= 12):
                                if (hours_per_week > 2):
                                    if (education_num > 14):
                                        return -7811984082516642400
                                    if (education_num <= 14):
                                        return -7811984082516642400
                                if (hours_per_week <= 2):
                                    return -671483940756762216
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
                            if (workclass is None):
                                return -671483940756762216
                            if (workclass == -1136074064918994416):
                                if (hours_per_week > 26):
                                    return -671483940756762216
                                if (hours_per_week <= 26):
                                    return -7811984082516642400
                            if (workclass != -1136074064918994416):
                                if (final_weight > 36352):
                                    if (occupation is None):
                                        return -671483940756762216
                                    if (occupation == 8618684898378336489):
                                        return -7811984082516642400
                                    if (occupation != 8618684898378336489):
                                        return -671483940756762216
                                if (final_weight <= 36352):
                                    return -7811984082516642400
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
                            if (occupation is None):
                                return -671483940756762216
                            if (occupation == 3088227676756162338):
                                if (hours_per_week > 71):
                                    return -7811984082516642400
                                if (hours_per_week <= 71):
                                    if (final_weight is None):
                                        return -7811984082516642400
                                    if (final_weight > 182378):
                                        return -7811984082516642400
                                    if (final_weight <= 182378):
                                        return -7811984082516642400
                            if (occupation != 3088227676756162338):
                                if (occupation == 8618684898378336489):
                                    if (age > 40):
                                        return -7811984082516642400
                                    if (age <= 40):
                                        return -7811984082516642400
                                if (occupation != 8618684898378336489):
                                    if (occupation == -6990906632015037778):
                                        return -671483940756762216
                                    if (occupation != -6990906632015037778):
                                        return -671483940756762216
                        if (education_num <= 9):
                            if (occupation is None):
                                return -7811984082516642400
                            if (occupation == -6990906632015037778):
                                if (workclass is None):
                                    return -671483940756762216
                                if (workclass == -1136074064918994416):
                                    if (final_weight is None):
                                        return -7811984082516642400
                                    if (final_weight > 92214):
                                        return -7811984082516642400
                                    if (final_weight <= 92214):
                                        return -671483940756762216
                                if (workclass != -1136074064918994416):
                                    if (final_weight is None):
                                        return -671483940756762216
                                    if (final_weight > 189527):
                                        return -671483940756762216
                                    if (final_weight <= 189527):
                                        return -671483940756762216
                            if (occupation != -6990906632015037778):
                                if (occupation == 8618684898378336489):
                                    if (sex is None):
                                        return -7811984082516642400
                                    if (sex == 6306819796163687131):
                                        return -7811984082516642400
                                    if (sex != 6306819796163687131):
                                        return -7811984082516642400
                                if (occupation != 8618684898378336489):
                                    if (occupation == 3088227676756162338):
                                        return -7811984082516642400
                                    if (occupation != 3088227676756162338):
                                        return -7811984082516642400
                    if (hours_per_week <= 33):
                        if (workclass is None):
                            return -7811984082516642400
                        if (workclass == -7197995106135439896):
                            if (age > 54):
                                if (final_weight is None):
                                    return -671483940756762216
                                if (final_weight > 181769):
                                    if (hours_per_week > 27):
                                        return -671483940756762216
                                    if (hours_per_week <= 27):
                                        return -671483940756762216
                                if (final_weight <= 181769):
                                    if (sex is None):
                                        return -7811984082516642400
                                    if (sex == 6306819796163687131):
                                        return -7811984082516642400
                                    if (sex != 6306819796163687131):
                                        return -671483940756762216
                            if (age <= 54):
                                return -7811984082516642400
                        if (workclass != -7197995106135439896):
                            if (relationship is None):
                                return -7811984082516642400
                            if (relationship == -7487827120114232249):
                                if (age > 59):
                                    return -7811984082516642400
                                if (age <= 59):
                                    if (education_num > 9):
                                        return -671483940756762216
                                    if (education_num <= 9):
                                        return -7811984082516642400
                            if (relationship != -7487827120114232249):
                                if (occupation is None):
                                    return -7811984082516642400
                                if (occupation == 4779842868628447834):
                                    if (workclass == -1136074064918994416):
                                        return -7811984082516642400
                                    if (workclass != -1136074064918994416):
                                        return -671483940756762216
                                if (occupation != 4779842868628447834):
                                    if (final_weight is None):
                                        return -7811984082516642400
                                    if (final_weight > 286449):
                                        return -7811984082516642400
                                    if (final_weight <= 286449):
                                        return -7811984082516642400
                if (age <= 35):
                    if (age > 24):
                        if (occupation is None):
                            return -7811984082516642400
                        if (occupation == -6990906632015037778):
                            if (age > 27):
                                if (workclass is None):
                                    return -7811984082516642400
                                if (workclass == -1136074064918994416):
                                    if (final_weight is None):
                                        return -7811984082516642400
                                    if (final_weight > 237985):
                                        return -7811984082516642400
                                    if (final_weight <= 237985):
                                        return -7811984082516642400
                                if (workclass != -1136074064918994416):
                                    if (age > 32):
                                        return -671483940756762216
                                    if (age <= 32):
                                        return -7811984082516642400
                            if (age <= 27):
                                if (final_weight is None):
                                    return -7811984082516642400
                                if (final_weight > 162313):
                                    if (final_weight > 190463):
                                        return -7811984082516642400
                                    if (final_weight <= 190463):
                                        return -671483940756762216
                                if (final_weight <= 162313):
                                    return -7811984082516642400
                        if (occupation != -6990906632015037778):
                            if (occupation == 3088227676756162338):
                                if (education_num > 10):
                                    if (hours_per_week is None):
                                        return -7811984082516642400
                                    if (hours_per_week > 57):
                                        return -7811984082516642400
                                    if (hours_per_week <= 57):
                                        return -7811984082516642400
                                if (education_num <= 10):
                                    return -7811984082516642400
                            if (occupation != 3088227676756162338):
                                if (hours_per_week is None):
                                    return -7811984082516642400
                                if (hours_per_week > 46):
                                    if (age > 31):
                                        return -7811984082516642400
                                    if (age <= 31):
                                        return -7811984082516642400
                                if (hours_per_week <= 46):
                                    if (occupation == 1581590029918088140):
                                        return -7811984082516642400
                                    if (occupation != 1581590029918088140):
                                        return -7811984082516642400
                    if (age <= 24):
                        if (hours_per_week is None):
                            return -7811984082516642400
                        if (hours_per_week > 45):
                            if (final_weight is None):
                                return -7811984082516642400
                            if (final_weight > 79991):
                                if (race is None):
                                    return -7811984082516642400
                                if (race == -681598405395175136):
                                    return -671483940756762216
                                if (race != -681598405395175136):
                                    if (workclass is None):
                                        return -7811984082516642400
                                    if (workclass == -4284295320506787287):
                                        return -671483940756762216
                                    if (workclass != -4284295320506787287):
                                        return -7811984082516642400
                            if (final_weight <= 79991):
                                if (education_num > 9):
                                    return -671483940756762216
                                if (education_num <= 9):
                                    return -7811984082516642400
                        if (hours_per_week <= 45):
                            if (occupation is None):
                                return -7811984082516642400
                            if (occupation == 1581590029918088140):
                                if (hours_per_week > 38):
                                    return -671483940756762216
                                if (hours_per_week <= 38):
                                    return -7811984082516642400
                            if (occupation != 1581590029918088140):
                                if (occupation == 5332362397248960598):
                                    if (sex is None):
                                        return -7811984082516642400
                                    if (sex == 6306819796163687131):
                                        return -7811984082516642400
                                    if (sex != 6306819796163687131):
                                        return -7811984082516642400
                                if (occupation != 5332362397248960598):
                                    if (occupation == -6951104699562914960):
                                        return -7811984082516642400
                                    if (occupation != -6951104699562914960):
                                        return -7811984082516642400
            if (education_num <= 8):
                if (age is None):
                    return -7811984082516642400
                if (age > 36):
                    if (hours_per_week is None):
                        return -7811984082516642400
                    if (hours_per_week > 22):
                        if (education_num > 5):
                            if (age > 53):
                                if (occupation is None):
                                    return -7811984082516642400
                                if (occupation == 2812191937831880778):
                                    if (final_weight is None):
                                        return -7811984082516642400
                                    if (final_weight > 89485):
                                        return -7811984082516642400
                                    if (final_weight <= 89485):
                                        return -7811984082516642400
                                if (occupation != 2812191937831880778):
                                    if (final_weight is None):
                                        return -7811984082516642400
                                    if (final_weight > 162184):
                                        return -7811984082516642400
                                    if (final_weight <= 162184):
                                        return -7811984082516642400
                            if (age <= 53):
                                if (occupation is None):
                                    return -7811984082516642400
                                if (occupation == -5484833051640498835):
                                    if (hours_per_week > 52):
                                        return -7811984082516642400
                                    if (hours_per_week <= 52):
                                        return -671483940756762216
                                if (occupation != -5484833051640498835):
                                    if (workclass is None):
                                        return -7811984082516642400
                                    if (workclass == -857656620414700721):
                                        return -7811984082516642400
                                    if (workclass != -857656620414700721):
                                        return -7811984082516642400
                        if (education_num <= 5):
                            if (workclass is None):
                                return -7811984082516642400
                            if (workclass == 8585012838816931822):
                                if (occupation is None):
                                    return -7811984082516642400
                                if (occupation == -6990906632015037778):
                                    if (hours_per_week > 46):
                                        return -7811984082516642400
                                    if (hours_per_week <= 46):
                                        return -671483940756762216
                                if (occupation != -6990906632015037778):
                                    if (occupation == -5484833051640498835):
                                        return -7811984082516642400
                                    if (occupation != -5484833051640498835):
                                        return -7811984082516642400
                            if (workclass != 8585012838816931822):
                                if (hours_per_week > 55):
                                    if (workclass == -1136074064918994416):
                                        return -671483940756762216
                                    if (workclass != -1136074064918994416):
                                        return -7811984082516642400
                                if (hours_per_week <= 55):
                                    if (workclass == -7197995106135439896):
                                        return -671483940756762216
                                    if (workclass != -7197995106135439896):
                                        return -7811984082516642400
                    if (hours_per_week <= 22):
                        return -7811984082516642400
                if (age <= 36):
                    if (workclass is None):
                        return -7811984082516642400
                    if (workclass == 8585012838816931822):
                        if (age > 35):
                            if (occupation is None):
                                return -7811984082516642400
                            if (occupation == -5484833051640498835):
                                return -671483940756762216
                            if (occupation != -5484833051640498835):
                                if (education_num > 3):
                                    if (final_weight is None):
                                        return -7811984082516642400
                                    if (final_weight > 185266):
                                        return -7811984082516642400
                                    if (final_weight <= 185266):
                                        return -7811984082516642400
                                if (education_num <= 3):
                                    return -671483940756762216
                        if (age <= 35):
                            if (hours_per_week is None):
                                return -7811984082516642400
                            if (hours_per_week > 67):
                                if (hours_per_week > 83):
                                    return -7811984082516642400
                                if (hours_per_week <= 83):
                                    return -671483940756762216
                            if (hours_per_week <= 67):
                                if (occupation is None):
                                    return -7811984082516642400
                                if (occupation == 5332362397248960598):
                                    if (final_weight is None):
                                        return -7811984082516642400
                                    if (final_weight > 219946):
                                        return -7811984082516642400
                                    if (final_weight <= 219946):
                                        return -7811984082516642400
                                if (occupation != 5332362397248960598):
                                    if (final_weight is None):
                                        return -7811984082516642400
                                    if (final_weight > 145325):
                                        return -7811984082516642400
                                    if (final_weight <= 145325):
                                        return -7811984082516642400
                    if (workclass != 8585012838816931822):
                        if (occupation is None):
                            return -7811984082516642400
                        if (occupation == -8227066636055033186):
                            return -671483940756762216
                        if (occupation != -8227066636055033186):
                            if (age > 29):
                                return -7811984082516642400
                            if (age <= 29):
                                if (relationship is None):
                                    return -7811984082516642400
                                if (relationship == -408487193273916322):
                                    if (final_weight is None):
                                        return -7811984082516642400
                                    if (final_weight > 149463):
                                        return -7811984082516642400
                                    if (final_weight <= 149463):
                                        return -7811984082516642400
                                if (relationship != -408487193273916322):
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
                            if (final_weight is None):
                                return -671483940756762216
                            if (final_weight > 160393):
                                if (hours_per_week > 58):
                                    if (education_num > 13):
                                        return -671483940756762216
                                    if (education_num <= 13):
                                        return -7811984082516642400
                                if (hours_per_week <= 58):
                                    if (race is None):
                                        return -671483940756762216
                                    if (race == -681598405395175136):
                                        return -7811984082516642400
                                    if (race != -681598405395175136):
                                        return -671483940756762216
                            if (final_weight <= 160393):
                                if (hours_per_week > 47):
                                    if (final_weight > 51818):
                                        return -671483940756762216
                                    if (final_weight <= 51818):
                                        return -671483940756762216
                                if (hours_per_week <= 47):
                                    if (age > 49):
                                        return -671483940756762216
                                    if (age <= 49):
                                        return -7811984082516642400
                        if (age <= 41):
                            if (final_weight is None):
                                return -7811984082516642400
                            if (final_weight > 307855):
                                return -7811984082516642400
                            if (final_weight <= 307855):
                                if (workclass is None):
                                    return -7811984082516642400
                                if (workclass == -1136074064918994416):
                                    return -7811984082516642400
                                if (workclass != -1136074064918994416):
                                    if (marital_status == 7568786824864426784):
                                        return -671483940756762216
                                    if (marital_status != 7568786824864426784):
                                        return -671483940756762216
                    if (occupation != -6990906632015037778):
                        if (education_num > 14):
                            if (age > 32):
                                if (age > 52):
                                    if (marital_status == -5485661916787442206):
                                        return -671483940756762216
                                    if (marital_status != -5485661916787442206):
                                        return -7811984082516642400
                                if (age <= 52):
                                    if (hours_per_week > 52):
                                        return -671483940756762216
                                    if (hours_per_week <= 52):
                                        return -671483940756762216
                            if (age <= 32):
                                if (age > 29):
                                    return -7811984082516642400
                                if (age <= 29):
                                    if (marital_status == -2843050270188924016):
                                        return -7811984082516642400
                                    if (marital_status != -2843050270188924016):
                                        return -671483940756762216
                        if (education_num <= 14):
                            if (sex is None):
                                return -7811984082516642400
                            if (sex == 6306819796163687131):
                                if (hours_per_week > 55):
                                    if (occupation == -5484833051640498835):
                                        return -7811984082516642400
                                    if (occupation != -5484833051640498835):
                                        return -7811984082516642400
                                if (hours_per_week <= 55):
                                    if (workclass is None):
                                        return -7811984082516642400
                                    if (workclass == -4284295320506787287):
                                        return -7811984082516642400
                                    if (workclass != -4284295320506787287):
                                        return -7811984082516642400
                            if (sex != 6306819796163687131):
                                if (final_weight is None):
                                    return -7811984082516642400
                                if (final_weight > 151124):
                                    if (final_weight > 158605):
                                        return -7811984082516642400
                                    if (final_weight <= 158605):
                                        return -671483940756762216
                                if (final_weight <= 151124):
                                    if (workclass is None):
                                        return -7811984082516642400
                                    if (workclass == 8161495398349361779):
                                        return -671483940756762216
                                    if (workclass != 8161495398349361779):
                                        return -7811984082516642400
                if (hours_per_week <= 43):
                    if (education_num > 14):
                        if (age > 32):
                            if (sex is None):
                                return -671483940756762216
                            if (sex == 6306819796163687131):
                                if (hours_per_week > 21):
                                    if (final_weight is None):
                                        return -671483940756762216
                                    if (final_weight > 107803):
                                        return -671483940756762216
                                    if (final_weight <= 107803):
                                        return -671483940756762216
                                if (hours_per_week <= 21):
                                    if (marital_status == -5485661916787442206):
                                        return -671483940756762216
                                    if (marital_status != -5485661916787442206):
                                        return -7811984082516642400
                            if (sex != 6306819796163687131):
                                if (marital_status == -2843050270188924016):
                                    if (final_weight is None):
                                        return -671483940756762216
                                    if (final_weight > 386027):
                                        return -7811984082516642400
                                    if (final_weight <= 386027):
                                        return -671483940756762216
                                if (marital_status != -2843050270188924016):
                                    if (final_weight is None):
                                        return -7811984082516642400
                                    if (final_weight > 170081):
                                        return -7811984082516642400
                                    if (final_weight <= 170081):
                                        return -7811984082516642400
                        if (age <= 32):
                            return -7811984082516642400
                    if (education_num <= 14):
                        if (age > 45):
                            if (hours_per_week > 31):
                                if (relationship is None):
                                    return -7811984082516642400
                                if (relationship == 5722155880036500383):
                                    if (workclass is None):
                                        return -7811984082516642400
                                    if (workclass == 8161495398349361779):
                                        return -7811984082516642400
                                    if (workclass != 8161495398349361779):
                                        return -7811984082516642400
                                if (relationship != 5722155880036500383):
                                    if (age > 49):
                                        return -7811984082516642400
                                    if (age <= 49):
                                        return -7811984082516642400
                            if (hours_per_week <= 31):
                                if (marital_status == -8271725530730535226):
                                    return -7811984082516642400
                                if (marital_status != -8271725530730535226):
                                    if (occupation is None):
                                        return -7811984082516642400
                                    if (occupation == -8005258492814722552):
                                        return -671483940756762216
                                    if (occupation != -8005258492814722552):
                                        return -7811984082516642400
                        if (age <= 45):
                            if (hours_per_week > 34):
                                if (workclass is None):
                                    return -7811984082516642400
                                if (workclass == -4284295320506787287):
                                    return -7811984082516642400
                                if (workclass != -4284295320506787287):
                                    if (workclass == 8161495398349361779):
                                        return -7811984082516642400
                                    if (workclass != 8161495398349361779):
                                        return -7811984082516642400
                            if (hours_per_week <= 34):
                                if (final_weight is None):
                                    return -7811984082516642400
                                if (final_weight > 391238):
                                    return -671483940756762216
                                if (final_weight <= 391238):
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
                            if (final_weight is None):
                                return -7811984082516642400
                            if (final_weight > 156075):
                                return -671483940756762216
                            if (final_weight <= 156075):
                                return -7811984082516642400
                        if (hours_per_week <= 77):
                            if (race is None):
                                return -7811984082516642400
                            if (race == -681598405395175136):
                                if (hours_per_week > 41):
                                    return -7811984082516642400
                                if (hours_per_week <= 41):
                                    return -671483940756762216
                            if (race != -681598405395175136):
                                if (workclass is None):
                                    return -7811984082516642400
                                if (workclass == -1136074064918994416):
                                    if (relationship == 5722155880036500383):
                                        return -7811984082516642400
                                    if (relationship != 5722155880036500383):
                                        return -671483940756762216
                                if (workclass != -1136074064918994416):
                                    if (workclass == 8585012838816931822):
                                        return -7811984082516642400
                                    if (workclass != 8585012838816931822):
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
                            if (occupation is None):
                                return -7811984082516642400
                            if (occupation == 5332362397248960598):
                                return -7811984082516642400
                            if (occupation != 5332362397248960598):
                                if (hours_per_week > 67):
                                    return -7811984082516642400
                                if (hours_per_week <= 67):
                                    if (marital_status == 7568786824864426784):
                                        return -671483940756762216
                                    if (marital_status != 7568786824864426784):
                                        return -7811984082516642400
                        if (age <= 53):
                            if (relationship is None):
                                return -7811984082516642400
                            if (relationship == 5722155880036500383):
                                if (education is None):
                                    return -7811984082516642400
                                if (education == 4595982442865070163):
                                    if (hours_per_week > 47):
                                        return -7811984082516642400
                                    if (hours_per_week <= 47):
                                        return -7811984082516642400
                                if (education != 4595982442865070163):
                                    if (workclass is None):
                                        return -7811984082516642400
                                    if (workclass == -1136074064918994416):
                                        return -7811984082516642400
                                    if (workclass != -1136074064918994416):
                                        return -7811984082516642400
                            if (relationship != 5722155880036500383):
                                if (age > 39):
                                    if (age > 45):
                                        return -7811984082516642400
                                    if (age <= 45):
                                        return -7811984082516642400
                                if (age <= 39):
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
                            if (hours_per_week > 32):
                                return -671483940756762216
                            if (hours_per_week <= 32):
                                return -7811984082516642400
                        if (relationship != -7487827120114232249):
                            if (age > 59):
                                if (workclass is None):
                                    return -7811984082516642400
                                if (workclass == 8585012838816931822):
                                    return -7811984082516642400
                                if (workclass != 8585012838816931822):
                                    if (education is None):
                                        return -7811984082516642400
                                    if (education == -1620783280160849416):
                                        return -671483940756762216
                                    if (education != -1620783280160849416):
                                        return -7811984082516642400
                            if (age <= 59):
                                return -7811984082516642400
                    if (occupation != 8618684898378336489):
                        if (occupation == -8227066636055033186):
                            if (relationship is None):
                                return -7811984082516642400
                            if (relationship == -7729121122090457494):
                                if (sex is None):
                                    return -7811984082516642400
                                if (sex == 6306819796163687131):
                                    if (age > 37):
                                        return -7811984082516642400
                                    if (age <= 37):
                                        return -7811984082516642400
                                if (sex != 6306819796163687131):
                                    return -7811984082516642400
                            if (relationship != -7729121122090457494):
                                return -7811984082516642400
                        if (occupation != -8227066636055033186):
                            if (relationship is None):
                                return -7811984082516642400
                            if (relationship == 5722155880036500383):
                                if (occupation == 5332362397248960598):
                                    if (marital_status == -1035125786006291861):
                                        return -7811984082516642400
                                    if (marital_status != -1035125786006291861):
                                        return -7811984082516642400
                                if (occupation != 5332362397248960598):
                                    if (workclass is None):
                                        return -7811984082516642400
                                    if (workclass == -7197995106135439896):
                                        return -7811984082516642400
                                    if (workclass != -7197995106135439896):
                                        return -7811984082516642400
                            if (relationship != 5722155880036500383):
                                if (occupation == 1581590029918088140):
                                    if (workclass is None):
                                        return -7811984082516642400
                                    if (workclass == 8161495398349361779):
                                        return -7811984082516642400
                                    if (workclass != 8161495398349361779):
                                        return -7811984082516642400
                                if (occupation != 1581590029918088140):
                                    if (relationship == -7487827120114232249):
                                        return -7811984082516642400
                                    if (relationship != -7487827120114232249):
                                        return -7811984082516642400
            if (age <= 31):
                if (age > 21):
                    if (hours_per_week is None):
                        return -7811984082516642400
                    if (hours_per_week > 41):
                        if (workclass is None):
                            return -7811984082516642400
                        if (workclass == 8585012838816931822):
                            if (relationship is None):
                                return -7811984082516642400
                            if (relationship == 5722155880036500383):
                                if (occupation is None):
                                    return -7811984082516642400
                                if (occupation == -6990906632015037778):
                                    if (marital_status == -2843050270188924016):
                                        return -7811984082516642400
                                    if (marital_status != -2843050270188924016):
                                        return -671483940756762216
                                if (occupation != -6990906632015037778):
                                    if (education is None):
                                        return -7811984082516642400
                                    if (education == -8844931991724242570):
                                        return -7811984082516642400
                                    if (education != -8844931991724242570):
                                        return -7811984082516642400
                            if (relationship != 5722155880036500383):
                                return -7811984082516642400
                        if (workclass != 8585012838816931822):
                            if (sex is None):
                                return -7811984082516642400
                            if (sex == 6306819796163687131):
                                if (hours_per_week > 49):
                                    if (occupation is None):
                                        return -7811984082516642400
                                    if (occupation == -6990906632015037778):
                                        return -671483940756762216
                                    if (occupation != -6990906632015037778):
                                        return -7811984082516642400
                                if (hours_per_week <= 49):
                                    if (education_num > 8):
                                        return -7811984082516642400
                                    if (education_num <= 8):
                                        return -7811984082516642400
                            if (sex != 6306819796163687131):
                                return -7811984082516642400
                    if (hours_per_week <= 41):
                        if (education_num > 9):
                            if (hours_per_week > 29):
                                if (relationship is None):
                                    return -7811984082516642400
                                if (relationship == -7487827120114232249):
                                    return -671483940756762216
                                if (relationship != -7487827120114232249):
                                    if (occupation is None):
                                        return -7811984082516642400
                                    if (occupation == -3959269231467008119):
                                        return -7811984082516642400
                                    if (occupation != -3959269231467008119):
                                        return -7811984082516642400
                            if (hours_per_week <= 29):
                                return -7811984082516642400
                        if (education_num <= 9):
                            if (age > 27):
                                if (final_weight is None):
                                    return -7811984082516642400
                                if (final_weight > 94030):
                                    if (final_weight > 334106):
                                        return -7811984082516642400
                                    if (final_weight <= 334106):
                                        return -7811984082516642400
                                if (final_weight <= 94030):
                                    if (marital_status == -8271725530730535226):
                                        return -7811984082516642400
                                    if (marital_status != -8271725530730535226):
                                        return -7811984082516642400
                            if (age <= 27):
                                return -7811984082516642400
                if (age <= 21):
                    if (education is None):
                        return -7811984082516642400
                    if (education == -3305009427453673313):
                        if (occupation is None):
                            return -7811984082516642400
                        if (occupation == 8618684898378336489):
                            if (hours_per_week is None):
                                return -7811984082516642400
                            if (hours_per_week > 50):
                                return -671483940756762216
                            if (hours_per_week <= 50):
                                return -7811984082516642400
                        if (occupation != 8618684898378336489):
                            return -7811984082516642400
                    if (education != -3305009427453673313):
                        return -7811984082516642400
