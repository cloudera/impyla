

def predict_income(impala_function_context, age, workclass, final_weight,
                   education, education_num,
                   marital_status, occupation, relationship, race, sex,
                   hours_per_week, native_country, income):
    """ Predictor for income from model/536031d6ffa04466f3001b49

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
                                        if (age > 74):
                                            if (hours_per_week > 45):
                                                return -671483940756762216
                                            if (hours_per_week <= 45):
                                                if (education_num > 15):
                                                    return -671483940756762216
                                                if (education_num <= 15):
                                                    return -7811984082516642400
                                        if (age <= 74):
                                            if (workclass == -
                                                    4284295320506787287):
                                                if (hours_per_week > 47):
                                                    if (hours_per_week > 57):
                                                        return - \
                                                            671483940756762216
                                                    if (hours_per_week <= 57):
                                                        return - \
                                                            7811984082516642400
                                                if (hours_per_week <= 47):
                                                    return -671483940756762216
                                            if (workclass != -
                                                    4284295320506787287):
                                                return -671483940756762216
                            if (education_num <= 14):
                                if (hours_per_week > 36):
                                    if (workclass is None):
                                        return -671483940756762216
                                    if (workclass == -7197995106135439896):
                                        return -671483940756762216
                                    if (workclass != -7197995106135439896):
                                        if (occupation is None):
                                            return -671483940756762216
                                        if (occupation == 5332362397248960598):
                                            return -671483940756762216
                                        if (occupation != 5332362397248960598):
                                            if (final_weight is None):
                                                return -671483940756762216
                                            if (final_weight > 142784):
                                                if (workclass == -
                                                        1136074064918994416):
                                                    return -7811984082516642400
                                                if (workclass != -
                                                        1136074064918994416):
                                                    if (occupation == -
                                                            6990906632015037778):
                                                        return - \
                                                            671483940756762216
                                                    if (occupation != -
                                                            6990906632015037778):
                                                        if (final_weight >
                                                                195635):
                                                            return - \
                                                                671483940756762216
                                                        if (final_weight <=
                                                                195635):
                                                            return - \
                                                                7811984082516642400
                                            if (final_weight <= 142784):
                                                if (final_weight > 92181):
                                                    return -671483940756762216
                                                if (final_weight <= 92181):
                                                    if (age > 59):
                                                        if (workclass == -
                                                                857656620414700721):
                                                            return - \
                                                                7811984082516642400
                                                        if (workclass != -
                                                                857656620414700721):
                                                            return - \
                                                                671483940756762216
                                                    if (age <= 59):
                                                        return - \
                                                            7811984082516642400
                                if (hours_per_week <= 36):
                                    return -7811984082516642400
                        if (age <= 58):
                            if (age > 38):
                                if (education_num > 14):
                                    if (hours_per_week > 49):
                                        if (occupation is None):
                                            return -671483940756762216
                                        if (occupation == -
                                                8005258492814722552):
                                            return -7811984082516642400
                                        if (occupation != -
                                                8005258492814722552):
                                            if (workclass is None):
                                                return -671483940756762216
                                            if (workclass ==
                                                    8585012838816931822):
                                                if (race is None):
                                                    return -671483940756762216
                                                if (race ==
                                                        3632794867504857096):
                                                    return -7811984082516642400
                                                if (race !=
                                                        3632794867504857096):
                                                    if (age > 42):
                                                        return - \
                                                            671483940756762216
                                                    if (age <= 42):
                                                        if (age > 41):
                                                            if (
                                                                    hours_per_week >
                                                                    55):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                    hours_per_week <=
                                                                    55):
                                                                return - \
                                                                    7811984082516642400
                                                        if (age <= 41):
                                                            return - \
                                                                671483940756762216
                                            if (workclass !=
                                                    8585012838816931822):
                                                return -671483940756762216
                                    if (hours_per_week <= 49):
                                        if (relationship is None):
                                            return -671483940756762216
                                        if (relationship ==
                                                5722155880036500383):
                                            return -7811984082516642400
                                        if (relationship !=
                                                5722155880036500383):
                                            if (occupation is None):
                                                return -671483940756762216
                                            if (occupation ==
                                                    2812191937831880778):
                                                return -7811984082516642400
                                            if (occupation !=
                                                    2812191937831880778):
                                                if (age > 57):
                                                    return -7811984082516642400
                                                if (age <= 57):
                                                    if (final_weight is None):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight > 95223):
                                                        if (final_weight >
                                                                317314):
                                                            return - \
                                                                671483940756762216
                                                        if (final_weight <=
                                                                317314):
                                                            if (
                                                                    hours_per_week >
                                                                    47):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                    hours_per_week <=
                                                                    47):
                                                                return - \
                                                                    671483940756762216
                                                    if (final_weight <= 95223):
                                                        return - \
                                                            671483940756762216
                                if (education_num <= 14):
                                    if (workclass is None):
                                        return -671483940756762216
                                    if (workclass == -1136074064918994416):
                                        if (final_weight is None):
                                            return -671483940756762216
                                        if (final_weight > 243112):
                                            return -671483940756762216
                                        if (final_weight <= 243112):
                                            if (hours_per_week > 57):
                                                if (occupation is None):
                                                    return -7811984082516642400
                                                if (occupation == -
                                                        6990906632015037778):
                                                    return -671483940756762216
                                                if (occupation != -
                                                        6990906632015037778):
                                                    return -7811984082516642400
                                            if (hours_per_week <= 57):
                                                if (hours_per_week > 39):
                                                    if (final_weight > 226073):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight <=
                                                            226073):
                                                        if (final_weight >
                                                                211455):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight <=
                                                                211455):
                                                            if (age > 53):
                                                                return - \
                                                                    7811984082516642400
                                                            if (age <= 53):
                                                                return - \
                                                                    671483940756762216
                                                if (hours_per_week <= 39):
                                                    return -671483940756762216
                                    if (workclass != -1136074064918994416):
                                        if (occupation is None):
                                            return -671483940756762216
                                        if (occupation == 5332362397248960598):
                                            if (final_weight is None):
                                                return -671483940756762216
                                            if (final_weight > 347159):
                                                return -7811984082516642400
                                            if (final_weight <= 347159):
                                                if (final_weight > 188705):
                                                    return -671483940756762216
                                                if (final_weight <= 188705):
                                                    if (hours_per_week > 39):
                                                        if (final_weight >
                                                                63143):
                                                            if (
                                                                    hours_per_week >
                                                                    42):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                    hours_per_week <=
                                                                    42):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                63143):
                                                            return - \
                                                                671483940756762216
                                                    if (hours_per_week <= 39):
                                                        return - \
                                                            671483940756762216
                                        if (occupation != 5332362397248960598):
                                            if (final_weight is None):
                                                return -671483940756762216
                                            if (final_weight > 323185):
                                                return -671483940756762216
                                            if (final_weight <= 323185):
                                                if (race is None):
                                                    return -671483940756762216
                                                if (race == -
                                                        681598405395175136):
                                                    return -7811984082516642400
                                                if (race != -
                                                        681598405395175136):
                                                    if (occupation ==
                                                            8618684898378336489):
                                                        return - \
                                                            7811984082516642400
                                                    if (occupation !=
                                                            8618684898378336489):
                                                        if (final_weight >
                                                                151676):
                                                            if (
                                                                    hours_per_week >
                                                                    62):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    hours_per_week <=
                                                                    62):
                                                                return - \
                                                                    671483940756762216
                                                        if (final_weight <=
                                                                151676):
                                                            if (final_weight >
                                                                    73703):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    73703):
                                                                return - \
                                                                    671483940756762216
                            if (age <= 38):
                                if (occupation is None):
                                    return -671483940756762216
                                if (occupation == 3088227676756162338):
                                    return -7811984082516642400
                                if (occupation != 3088227676756162338):
                                    if (hours_per_week > 42):
                                        if (occupation == -
                                                6990906632015037778):
                                            if (final_weight is None):
                                                return -671483940756762216
                                            if (final_weight > 285656):
                                                if (final_weight > 296849):
                                                    return -671483940756762216
                                                if (final_weight <= 296849):
                                                    return -7811984082516642400
                                            if (final_weight <= 285656):
                                                return -671483940756762216
                                        if (occupation != -
                                                6990906632015037778):
                                            if (sex is None):
                                                return -671483940756762216
                                            if (sex == 6306819796163687131):
                                                if (occupation == -
                                                        8227066636055033186):
                                                    return -7811984082516642400
                                                if (occupation != -
                                                        8227066636055033186):
                                                    if (workclass is None):
                                                        return - \
                                                            671483940756762216
                                                    if (workclass ==
                                                            8585012838816931822):
                                                        if (
                                                                final_weight is None):
                                                            return - \
                                                                671483940756762216
                                                        if (final_weight >
                                                                35814):
                                                            if (final_weight >
                                                                    344743):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    344743):
                                                                return - \
                                                                    671483940756762216
                                                        if (final_weight <=
                                                                35814):
                                                            return - \
                                                                7811984082516642400
                                                    if (workclass !=
                                                            8585012838816931822):
                                                        if (
                                                                final_weight is None):
                                                            return - \
                                                                671483940756762216
                                                        if (final_weight >
                                                                252034):
                                                            return - \
                                                                671483940756762216
                                                        if (final_weight <=
                                                                252034):
                                                            if (age > 37):
                                                                return - \
                                                                    671483940756762216
                                                            if (age <= 37):
                                                                return - \
                                                                    7811984082516642400
                                            if (sex != 6306819796163687131):
                                                return -671483940756762216
                                    if (hours_per_week <= 42):
                                        if (occupation == -
                                                8005258492814722552):
                                            return -7811984082516642400
                                        if (occupation != -
                                                8005258492814722552):
                                            if (hours_per_week > 39):
                                                if (final_weight is None):
                                                    return -671483940756762216
                                                if (final_weight > 323491):
                                                    return -671483940756762216
                                                if (final_weight <= 323491):
                                                    if (workclass is None):
                                                        return - \
                                                            671483940756762216
                                                    if (workclass == -
                                                            7197995106135439896):
                                                        return - \
                                                            671483940756762216
                                                    if (workclass != -
                                                            7197995106135439896):
                                                        if (final_weight >
                                                                270317):
                                                            if (final_weight >
                                                                    321197):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    321197):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                270317):
                                                            if (final_weight >
                                                                    203903):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    203903):
                                                                return - \
                                                                    671483940756762216
                                            if (hours_per_week <= 39):
                                                if (hours_per_week > 37):
                                                    return -7811984082516642400
                                                if (hours_per_week <= 37):
                                                    if (relationship is None):
                                                        return - \
                                                            671483940756762216
                                                    if (relationship ==
                                                            8744150760759310329):
                                                        return - \
                                                            7811984082516642400
                                                    if (relationship !=
                                                            8744150760759310329):
                                                        if (education_num >
                                                                15):
                                                            if (
                                                                    hours_per_week >
                                                                    35):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    hours_per_week <=
                                                                    35):
                                                                return - \
                                                                    7811984082516642400
                                                        if (education_num <=
                                                                15):
                                                            return - \
                                                                671483940756762216
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
                                        if (age > 65):
                                            return -7811984082516642400
                                        if (age <= 65):
                                            return -671483940756762216
                                    if (age <= 48):
                                        if (age > 35):
                                            if (age > 43):
                                                if (hours_per_week > 42):
                                                    if (hours_per_week > 55):
                                                        return - \
                                                            7811984082516642400
                                                    if (hours_per_week <= 55):
                                                        return - \
                                                            671483940756762216
                                                if (hours_per_week <= 42):
                                                    return -7811984082516642400
                                            if (age <= 43):
                                                if (final_weight > 187120):
                                                    return -7811984082516642400
                                                if (final_weight <= 187120):
                                                    if (final_weight > 152625):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight <=
                                                            152625):
                                                        return - \
                                                            7811984082516642400
                                        if (age <= 35):
                                            return -671483940756762216
                                if (final_weight <= 90244):
                                    return -7811984082516642400
                            if (workclass != -1136074064918994416):
                                if (hours_per_week > 67):
                                    if (hours_per_week > 73):
                                        return -671483940756762216
                                    if (hours_per_week <= 73):
                                        if (final_weight is None):
                                            return -7811984082516642400
                                        if (final_weight > 134993):
                                            if (hours_per_week > 71):
                                                if (final_weight > 322085):
                                                    return -7811984082516642400
                                                if (final_weight <= 322085):
                                                    return -671483940756762216
                                            if (hours_per_week <= 71):
                                                return -7811984082516642400
                                        if (final_weight <= 134993):
                                            return -671483940756762216
                                if (hours_per_week <= 67):
                                    if (race is None):
                                        return -671483940756762216
                                    if (race == 3939476748445039507):
                                        return -7811984082516642400
                                    if (race != 3939476748445039507):
                                        if (relationship is None):
                                            return -671483940756762216
                                        if (relationship ==
                                                8744150760759310329):
                                            return -7811984082516642400
                                        if (relationship !=
                                                8744150760759310329):
                                            if (hours_per_week > 41):
                                                if (age > 84):
                                                    return -7811984082516642400
                                                if (age <= 84):
                                                    if (age > 51):
                                                        if (workclass == -
                                                                857656620414700721):
                                                            return - \
                                                                7811984082516642400
                                                        if (workclass != -
                                                                857656620414700721):
                                                            if (age > 58):
                                                                return - \
                                                                    671483940756762216
                                                            if (age <= 58):
                                                                return - \
                                                                    671483940756762216
                                                    if (age <= 51):
                                                        if (age > 32):
                                                            if (age > 33):
                                                                return - \
                                                                    671483940756762216
                                                            if (age <= 33):
                                                                return - \
                                                                    7811984082516642400
                                                        if (age <= 32):
                                                            if (
                                                                    final_weight is None):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight >
                                                                    81292):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    81292):
                                                                return - \
                                                                    7811984082516642400
                                            if (hours_per_week <= 41):
                                                if (final_weight is None):
                                                    return -671483940756762216
                                                if (final_weight > 364614):
                                                    return -671483940756762216
                                                if (final_weight <= 364614):
                                                    if (final_weight > 337643):
                                                        return - \
                                                            7811984082516642400
                                                    if (final_weight <=
                                                            337643):
                                                        if (workclass == -
                                                                4284295320506787287):
                                                            if (age > 55):
                                                                return - \
                                                                    7811984082516642400
                                                            if (age <= 55):
                                                                return - \
                                                                    671483940756762216
                                                        if (workclass != -
                                                                4284295320506787287):
                                                            if (final_weight >
                                                                    202813):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    202813):
                                                                return - \
                                                                    671483940756762216
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
                                        if (final_weight > 232277):
                                            if (age > 36):
                                                if (occupation ==
                                                        8618684898378336489):
                                                    return -7811984082516642400
                                                if (occupation !=
                                                        8618684898378336489):
                                                    if (workclass is None):
                                                        return - \
                                                            671483940756762216
                                                    if (workclass == -
                                                            857656620414700721):
                                                        if (final_weight >
                                                                308865):
                                                            if (race == -
                                                                    5895194357237003500):
                                                                return - \
                                                                    7811984082516642400
                                                            if (race != -
                                                                    5895194357237003500):
                                                                return - \
                                                                    671483940756762216
                                                        if (final_weight <=
                                                                308865):
                                                            return - \
                                                                7811984082516642400
                                                    if (workclass != -
                                                            857656620414700721):
                                                        if (occupation ==
                                                                3088227676756162338):
                                                            return - \
                                                                7811984082516642400
                                                        if (occupation !=
                                                                3088227676756162338):
                                                            if (final_weight >
                                                                    407546):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    407546):
                                                                return - \
                                                                    671483940756762216
                                            if (age <= 36):
                                                if (hours_per_week > 39):
                                                    if (occupation ==
                                                            8618684898378336489):
                                                        return - \
                                                            7811984082516642400
                                                    if (occupation !=
                                                            8618684898378336489):
                                                        if (age > 35):
                                                            if (final_weight >
                                                                    326016):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    326016):
                                                                return - \
                                                                    7811984082516642400
                                                        if (age <= 35):
                                                            if (final_weight >
                                                                    365060):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    365060):
                                                                return - \
                                                                    7811984082516642400
                                                if (hours_per_week <= 39):
                                                    return -671483940756762216
                                        if (final_weight <= 232277):
                                            if (occupation ==
                                                    2812191937831880778):
                                                if (hours_per_week > 42):
                                                    if (final_weight > 191925):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight <=
                                                            191925):
                                                        if (age > 43):
                                                            if (final_weight >
                                                                    184791):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    184791):
                                                                return - \
                                                                    671483940756762216
                                                        if (age <= 43):
                                                            return - \
                                                                7811984082516642400
                                                if (hours_per_week <= 42):
                                                    return -7811984082516642400
                                            if (occupation !=
                                                    2812191937831880778):
                                                if (workclass is None):
                                                    return -671483940756762216
                                                if (workclass == -
                                                        857656620414700721):
                                                    if (age > 29):
                                                        if (final_weight >
                                                                192388):
                                                            if (age > 38):
                                                                return - \
                                                                    671483940756762216
                                                            if (age <= 38):
                                                                return - \
                                                                    671483940756762216
                                                        if (final_weight <=
                                                                192388):
                                                            if (age > 47):
                                                                return - \
                                                                    671483940756762216
                                                            if (age <= 47):
                                                                return - \
                                                                    671483940756762216
                                                    if (age <= 29):
                                                        return - \
                                                            7811984082516642400
                                                if (workclass != -
                                                        857656620414700721):
                                                    if (age > 42):
                                                        if (race ==
                                                                3632794867504857096):
                                                            return - \
                                                                7811984082516642400
                                                        if (race !=
                                                                3632794867504857096):
                                                            if (final_weight >
                                                                    201359):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    201359):
                                                                return - \
                                                                    671483940756762216
                                                    if (age <= 42):
                                                        if (race ==
                                                                3632794867504857096):
                                                            if (workclass ==
                                                                    8161495398349361779):
                                                                return - \
                                                                    7811984082516642400
                                                            if (workclass !=
                                                                    8161495398349361779):
                                                                return - \
                                                                    671483940756762216
                                                        if (race !=
                                                                3632794867504857096):
                                                            if (age > 37):
                                                                return - \
                                                                    671483940756762216
                                                            if (age <= 37):
                                                                return - \
                                                                    671483940756762216
                                    if (final_weight <= 121061):
                                        if (occupation == -
                                                8227066636055033186):
                                            return -7811984082516642400
                                        if (occupation != -
                                                8227066636055033186):
                                            if (hours_per_week > 53):
                                                if (occupation == -
                                                        5484833051640498835):
                                                    if (sex is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (sex ==
                                                            6306819796163687131):
                                                        if (age > 46):
                                                            if (
                                                                    hours_per_week >
                                                                    57):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    hours_per_week <=
                                                                    57):
                                                                return - \
                                                                    7811984082516642400
                                                        if (age <= 46):
                                                            return - \
                                                                7811984082516642400
                                                    if (sex !=
                                                            6306819796163687131):
                                                        return - \
                                                            671483940756762216
                                                if (occupation != -
                                                        5484833051640498835):
                                                    if (relationship == -
                                                            408487193273916322):
                                                        if (final_weight >
                                                                86725):
                                                            if (final_weight >
                                                                    98678):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    98678):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                86725):
                                                            if (
                                                                    workclass is None):
                                                                return - \
                                                                    671483940756762216
                                                            if (workclass == -
                                                                    7197995106135439896):
                                                                return - \
                                                                    7811984082516642400
                                                            if (workclass != -
                                                                    7197995106135439896):
                                                                return - \
                                                                    671483940756762216
                                                    if (relationship != -
                                                            408487193273916322):
                                                        return - \
                                                            7811984082516642400
                                            if (hours_per_week <= 53):
                                                if (workclass is None):
                                                    return -671483940756762216
                                                if (workclass == -
                                                        1136074064918994416):
                                                    if (age > 40):
                                                        if (hours_per_week >
                                                                44):
                                                            if (final_weight >
                                                                    110239):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    110239):
                                                                return - \
                                                                    7811984082516642400
                                                        if (hours_per_week <=
                                                                44):
                                                            if (occupation == -
                                                                    5484833051640498835):
                                                                return - \
                                                                    671483940756762216
                                                            if (occupation != -
                                                                    5484833051640498835):
                                                                return - \
                                                                    7811984082516642400
                                                    if (age <= 40):
                                                        return - \
                                                            7811984082516642400
                                                if (workclass != -
                                                        1136074064918994416):
                                                    if (hours_per_week > 44):
                                                        if (hours_per_week >
                                                                49):
                                                            if (age > 36):
                                                                return - \
                                                                    671483940756762216
                                                            if (age <= 36):
                                                                return - \
                                                                    7811984082516642400
                                                        if (hours_per_week <=
                                                                49):
                                                            return - \
                                                                671483940756762216
                                                    if (hours_per_week <= 44):
                                                        if (final_weight >
                                                                117105):
                                                            return - \
                                                                671483940756762216
                                                        if (final_weight <=
                                                                117105):
                                                            if (final_weight >
                                                                    110039):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    110039):
                                                                return - \
                                                                    671483940756762216
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
                                        if (final_weight is None):
                                            return -7811984082516642400
                                        if (final_weight > 59538):
                                            if (workclass is None):
                                                return -7811984082516642400
                                            if (workclass == -
                                                    7197995106135439896):
                                                return -671483940756762216
                                            if (workclass != -
                                                    7197995106135439896):
                                                if (final_weight > 165889):
                                                    if (final_weight > 179942):
                                                        if (age > 25):
                                                            if (age > 26):
                                                                return - \
                                                                    7811984082516642400
                                                            if (age <= 26):
                                                                return - \
                                                                    671483940756762216
                                                        if (age <= 25):
                                                            return - \
                                                                7811984082516642400
                                                    if (final_weight <=
                                                            179942):
                                                        return - \
                                                            671483940756762216
                                                if (final_weight <= 165889):
                                                    if (hours_per_week > 52):
                                                        if (hours_per_week >
                                                                57):
                                                            return - \
                                                                7811984082516642400
                                                        if (hours_per_week <=
                                                                57):
                                                            return - \
                                                                671483940756762216
                                                    if (hours_per_week <= 52):
                                                        return - \
                                                            7811984082516642400
                                        if (final_weight <= 59538):
                                            return -671483940756762216
                                if (hours_per_week <= 46):
                                    if (occupation == 5332362397248960598):
                                        return -7811984082516642400
                                    if (occupation != 5332362397248960598):
                                        if (final_weight is None):
                                            return -671483940756762216
                                        if (final_weight > 155506):
                                            return -671483940756762216
                                        if (final_weight <= 155506):
                                            if (age > 27):
                                                return -7811984082516642400
                                            if (age <= 27):
                                                return -671483940756762216
                            if (hours_per_week <= 41):
                                if (final_weight is None):
                                    return -7811984082516642400
                                if (final_weight > 159383):
                                    if (final_weight > 260996):
                                        if (age > 27):
                                            if (final_weight > 263671):
                                                return -7811984082516642400
                                            if (final_weight <= 263671):
                                                return -671483940756762216
                                        if (age <= 27):
                                            return -671483940756762216
                                    if (final_weight <= 260996):
                                        if (occupation == -
                                                6990906632015037778):
                                            if (age > 27):
                                                return -671483940756762216
                                            if (age <= 27):
                                                return -7811984082516642400
                                        if (occupation != -
                                                6990906632015037778):
                                            return -7811984082516642400
                                if (final_weight <= 159383):
                                    if (final_weight > 100631):
                                        if (age > 27):
                                            return -671483940756762216
                                        if (age <= 27):
                                            if (occupation == -
                                                    5484833051640498835):
                                                return -671483940756762216
                                            if (occupation != -
                                                    5484833051640498835):
                                                return -7811984082516642400
                                    if (final_weight <= 100631):
                                        if (occupation == -
                                                6990906632015037778):
                                            if (race is None):
                                                return -7811984082516642400
                                            if (race == -1569537633132385766):
                                                return -671483940756762216
                                            if (race != -1569537633132385766):
                                                return -7811984082516642400
                                        if (occupation != -
                                                6990906632015037778):
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
                                        if (final_weight is None):
                                            return -7811984082516642400
                                        if (final_weight > 38129):
                                            if (age > 66):
                                                return -7811984082516642400
                                            if (age <= 66):
                                                if (occupation is None):
                                                    return -7811984082516642400
                                                if (occupation == -
                                                        5484833051640498835):
                                                    if (final_weight > 196834):
                                                        return - \
                                                            7811984082516642400
                                                    if (final_weight <=
                                                            196834):
                                                        return - \
                                                            671483940756762216
                                                if (occupation != -
                                                        5484833051640498835):
                                                    return -7811984082516642400
                                        if (final_weight <= 38129):
                                            return -671483940756762216
                                    if (race != -1569537633132385766):
                                        return -671483940756762216
                                if (hours_per_week <= 13):
                                    if (occupation is None):
                                        return -7811984082516642400
                                    if (occupation == -6990906632015037778):
                                        return -671483940756762216
                                    if (occupation != -6990906632015037778):
                                        if (occupation == 1581590029918088140):
                                            return -7811984082516642400
                                        if (occupation != 1581590029918088140):
                                            if (hours_per_week > 11):
                                                return -671483940756762216
                                            if (hours_per_week <= 11):
                                                if (final_weight is None):
                                                    return -7811984082516642400
                                                if (final_weight > 180316):
                                                    return -671483940756762216
                                                if (final_weight <= 180316):
                                                    return -7811984082516642400
                        if (age <= 62):
                            if (hours_per_week > 12):
                                if (workclass is None):
                                    return -671483940756762216
                                if (workclass == -4284295320506787287):
                                    return -7811984082516642400
                                if (workclass != -4284295320506787287):
                                    if (hours_per_week > 21):
                                        if (education is None):
                                            return -7811984082516642400
                                        if (education == 109636874712401733):
                                            return -671483940756762216
                                        if (education != 109636874712401733):
                                            if (final_weight is None):
                                                return -7811984082516642400
                                            if (final_weight > 302817):
                                                return -7811984082516642400
                                            if (final_weight <= 302817):
                                                if (final_weight > 234356):
                                                    if (workclass == -
                                                            7197995106135439896):
                                                        return - \
                                                            7811984082516642400
                                                    if (workclass != -
                                                            7197995106135439896):
                                                        return - \
                                                            671483940756762216
                                                if (final_weight <= 234356):
                                                    if (workclass == -
                                                            7197995106135439896):
                                                        return - \
                                                            671483940756762216
                                                    if (workclass != -
                                                            7197995106135439896):
                                                        if (final_weight >
                                                                120839):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight <=
                                                                120839):
                                                            if (final_weight >
                                                                    101625):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    101625):
                                                                return - \
                                                                    7811984082516642400
                                    if (hours_per_week <= 21):
                                        if (workclass == -7197995106135439896):
                                            return -7811984082516642400
                                        if (workclass != -7197995106135439896):
                                            if (relationship is None):
                                                return -671483940756762216
                                            if (relationship == -
                                                    408487193273916322):
                                                if (education_num > 13):
                                                    if (occupation is None):
                                                        return - \
                                                            671483940756762216
                                                    if (occupation == -
                                                            6990906632015037778):
                                                        return - \
                                                            7811984082516642400
                                                    if (occupation != -
                                                            6990906632015037778):
                                                        if (
                                                                final_weight is None):
                                                            return - \
                                                                671483940756762216
                                                        if (final_weight >
                                                                217428):
                                                            if (
                                                                    hours_per_week >
                                                                    17):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    hours_per_week <=
                                                                    17):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                217428):
                                                            return - \
                                                                671483940756762216
                                                if (education_num <= 13):
                                                    return -671483940756762216
                                            if (relationship != -
                                                    408487193273916322):
                                                return -7811984082516642400
                            if (hours_per_week <= 12):
                                if (hours_per_week > 2):
                                    if (education_num > 14):
                                        if (hours_per_week > 5):
                                            return -7811984082516642400
                                        if (hours_per_week <= 5):
                                            return -671483940756762216
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
                                        if (hours_per_week > 27):
                                            return -671483940756762216
                                        if (hours_per_week <= 27):
                                            return -7811984082516642400
                                    if (occupation != 8618684898378336489):
                                        if (workclass == -857656620414700721):
                                            if (hours_per_week > 23):
                                                if (hours_per_week > 24):
                                                    return -671483940756762216
                                                if (hours_per_week <= 24):
                                                    return -7811984082516642400
                                            if (hours_per_week <= 23):
                                                return -671483940756762216
                                        if (workclass != -857656620414700721):
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
                                        if (hours_per_week > 67):
                                            return -671483940756762216
                                        if (hours_per_week <= 67):
                                            if (age > 49):
                                                if (hours_per_week > 45):
                                                    if (final_weight > 155617):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight <=
                                                            155617):
                                                        return - \
                                                            7811984082516642400
                                                if (hours_per_week <= 45):
                                                    return -671483940756762216
                                            if (age <= 49):
                                                if (age > 39):
                                                    return -7811984082516642400
                                                if (age <= 39):
                                                    if (hours_per_week > 47):
                                                        return - \
                                                            671483940756762216
                                                    if (hours_per_week <= 47):
                                                        return - \
                                                            7811984082516642400
                            if (occupation != 3088227676756162338):
                                if (occupation == 8618684898378336489):
                                    if (age > 40):
                                        if (final_weight is None):
                                            return -7811984082516642400
                                        if (final_weight > 196473):
                                            if (hours_per_week > 37):
                                                if (hours_per_week > 46):
                                                    return -7811984082516642400
                                                if (hours_per_week <= 46):
                                                    return -671483940756762216
                                            if (hours_per_week <= 37):
                                                return -7811984082516642400
                                        if (final_weight <= 196473):
                                            if (age > 46):
                                                if (age > 48):
                                                    if (sex is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (sex ==
                                                            6306819796163687131):
                                                        return - \
                                                            7811984082516642400
                                                    if (sex !=
                                                            6306819796163687131):
                                                        return - \
                                                            671483940756762216
                                                if (age <= 48):
                                                    return -671483940756762216
                                            if (age <= 46):
                                                return -7811984082516642400
                                    if (age <= 40):
                                        return -7811984082516642400
                                if (occupation != 8618684898378336489):
                                    if (occupation == -6990906632015037778):
                                        if (workclass is None):
                                            return -671483940756762216
                                        if (workclass == -4284295320506787287):
                                            if (sex is None):
                                                return -7811984082516642400
                                            if (sex == 6306819796163687131):
                                                return -7811984082516642400
                                            if (sex != 6306819796163687131):
                                                return -671483940756762216
                                        if (workclass != -4284295320506787287):
                                            if (workclass == -
                                                    1136074064918994416):
                                                if (education is None):
                                                    return -7811984082516642400
                                                if (education ==
                                                        6401768215868355915):
                                                    return -7811984082516642400
                                                if (education !=
                                                        6401768215868355915):
                                                    if (age > 44):
                                                        if (age > 50):
                                                            if (
                                                                    hours_per_week >
                                                                    37):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    hours_per_week <=
                                                                    37):
                                                                return - \
                                                                    7811984082516642400
                                                        if (age <= 50):
                                                            return - \
                                                                7811984082516642400
                                                    if (age <= 44):
                                                        return - \
                                                            671483940756762216
                                            if (workclass != -
                                                    1136074064918994416):
                                                if (hours_per_week > 48):
                                                    if (hours_per_week > 91):
                                                        return - \
                                                            7811984082516642400
                                                    if (hours_per_week <= 91):
                                                        if (age > 44):
                                                            if (age > 60):
                                                                return - \
                                                                    7811984082516642400
                                                            if (age <= 60):
                                                                return - \
                                                                    671483940756762216
                                                        if (age <= 44):
                                                            if (education_num >
                                                                    10):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    education_num <=
                                                                    10):
                                                                return - \
                                                                    671483940756762216
                                                if (hours_per_week <= 48):
                                                    if (final_weight is None):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight > 137265):
                                                        if (age > 68):
                                                            return - \
                                                                671483940756762216
                                                        if (age <= 68):
                                                            if (age > 64):
                                                                return - \
                                                                    7811984082516642400
                                                            if (age <= 64):
                                                                return - \
                                                                    671483940756762216
                                                    if (final_weight <=
                                                            137265):
                                                        if (final_weight >
                                                                133255):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight <=
                                                                133255):
                                                            if (workclass ==
                                                                    8161495398349361779):
                                                                return - \
                                                                    671483940756762216
                                                            if (workclass !=
                                                                    8161495398349361779):
                                                                return - \
                                                                    7811984082516642400
                                    if (occupation != -6990906632015037778):
                                        if (occupation == 1581590029918088140):
                                            if (final_weight is None):
                                                return -671483940756762216
                                            if (final_weight > 133264):
                                                if (workclass is None):
                                                    return -671483940756762216
                                                if (workclass == -
                                                        1136074064918994416):
                                                    return -7811984082516642400
                                                if (workclass != -
                                                        1136074064918994416):
                                                    if (age > 57):
                                                        if (hours_per_week >
                                                                46):
                                                            return - \
                                                                671483940756762216
                                                        if (hours_per_week <=
                                                                46):
                                                            return - \
                                                                7811984082516642400
                                                    if (age <= 57):
                                                        if (final_weight >
                                                                304409):
                                                            if (
                                                                    hours_per_week >
                                                                    38):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    hours_per_week <=
                                                                    38):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                304409):
                                                            if (final_weight >
                                                                    202429):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    202429):
                                                                return - \
                                                                    671483940756762216
                                            if (final_weight <= 133264):
                                                if (final_weight > 45882):
                                                    if (final_weight > 56857):
                                                        if (race is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (race == -
                                                                681598405395175136):
                                                            return - \
                                                                671483940756762216
                                                        if (race != -
                                                                681598405395175136):
                                                            if (final_weight >
                                                                    101705):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    101705):
                                                                return - \
                                                                    7811984082516642400
                                                    if (final_weight <= 56857):
                                                        return - \
                                                            671483940756762216
                                                if (final_weight <= 45882):
                                                    return -7811984082516642400
                                        if (occupation != 1581590029918088140):
                                            if (occupation ==
                                                    4779842868628447834):
                                                if (final_weight is None):
                                                    return -671483940756762216
                                                if (final_weight > 132978):
                                                    if (age > 53):
                                                        return - \
                                                            671483940756762216
                                                    if (age <= 53):
                                                        if (final_weight >
                                                                183597):
                                                            if (final_weight >
                                                                    343751):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    343751):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                183597):
                                                            if (age > 52):
                                                                return - \
                                                                    7811984082516642400
                                                            if (age <= 52):
                                                                return - \
                                                                    671483940756762216
                                                if (final_weight <= 132978):
                                                    if (hours_per_week > 41):
                                                        if (final_weight >
                                                                117485):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight <=
                                                                117485):
                                                            return - \
                                                                671483940756762216
                                                    if (hours_per_week <= 41):
                                                        if (education is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (education ==
                                                                6401768215868355915):
                                                            return - \
                                                                7811984082516642400
                                                        if (education !=
                                                                6401768215868355915):
                                                            if (final_weight >
                                                                    51969):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    51969):
                                                                return - \
                                                                    671483940756762216
                                            if (occupation !=
                                                    4779842868628447834):
                                                if (workclass is None):
                                                    return -7811984082516642400
                                                if (workclass == -
                                                        7197995106135439896):
                                                    if (final_weight is None):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight > 92178):
                                                        if (hours_per_week >
                                                                64):
                                                            if (final_weight >
                                                                    189582):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    189582):
                                                                return - \
                                                                    7811984082516642400
                                                        if (hours_per_week <=
                                                                64):
                                                            if (final_weight >
                                                                    194045):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    194045):
                                                                return - \
                                                                    671483940756762216
                                                    if (final_weight <= 92178):
                                                        return - \
                                                            671483940756762216
                                                if (workclass != -
                                                        7197995106135439896):
                                                    if (relationship is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (relationship ==
                                                            8744150760759310329):
                                                        return - \
                                                            7811984082516642400
                                                    if (relationship !=
                                                            8744150760759310329):
                                                        if (
                                                                final_weight is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight >
                                                                62494):
                                                            if (occupation == -
                                                                    6951104699562914960):
                                                                return - \
                                                                    7811984082516642400
                                                            if (occupation != -
                                                                    6951104699562914960):
                                                                return - \
                                                                    671483940756762216
                                                        if (final_weight <=
                                                                62494):
                                                            if (final_weight >
                                                                    27834):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    27834):
                                                                return - \
                                                                    671483940756762216
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
                                        if (final_weight > 145136):
                                            if (hours_per_week > 51):
                                                return -671483940756762216
                                            if (hours_per_week <= 51):
                                                if (final_weight > 199146):
                                                    if (final_weight > 297876):
                                                        if (race is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (race == -
                                                                1569537633132385766):
                                                            return - \
                                                                671483940756762216
                                                        if (race != -
                                                                1569537633132385766):
                                                            return - \
                                                                7811984082516642400
                                                    if (final_weight <=
                                                            297876):
                                                        return - \
                                                            7811984082516642400
                                                if (final_weight <= 199146):
                                                    if (hours_per_week > 42):
                                                        return - \
                                                            671483940756762216
                                                    if (hours_per_week <= 42):
                                                        if (final_weight >
                                                                170195):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight <=
                                                                170195):
                                                            if (
                                                                    hours_per_week >
                                                                    37):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                    hours_per_week <=
                                                                    37):
                                                                return - \
                                                                    671483940756762216
                                        if (final_weight <= 145136):
                                            return -7811984082516642400
                                    if (final_weight <= 92214):
                                        if (hours_per_week > 47):
                                            if (hours_per_week > 55):
                                                return -671483940756762216
                                            if (hours_per_week <= 55):
                                                return -7811984082516642400
                                        if (hours_per_week <= 47):
                                            return -671483940756762216
                                if (workclass != -1136074064918994416):
                                    if (final_weight is None):
                                        return -671483940756762216
                                    if (final_weight > 189527):
                                        if (age > 55):
                                            if (workclass ==
                                                    8585012838816931822):
                                                if (hours_per_week > 45):
                                                    return -7811984082516642400
                                                if (hours_per_week <= 45):
                                                    if (final_weight > 263581):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight <=
                                                            263581):
                                                        if (final_weight >
                                                                211118):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight <=
                                                                211118):
                                                            return - \
                                                                671483940756762216
                                            if (workclass !=
                                                    8585012838816931822):
                                                return -7811984082516642400
                                        if (age <= 55):
                                            if (hours_per_week > 47):
                                                return -671483940756762216
                                            if (hours_per_week <= 47):
                                                if (final_weight > 224226):
                                                    if (final_weight > 278979):
                                                        if (age > 42):
                                                            return - \
                                                                671483940756762216
                                                        if (age <= 42):
                                                            return - \
                                                                7811984082516642400
                                                    if (final_weight <=
                                                            278979):
                                                        return - \
                                                            7811984082516642400
                                                if (final_weight <= 224226):
                                                    if (sex is None):
                                                        return - \
                                                            671483940756762216
                                                    if (sex ==
                                                            6306819796163687131):
                                                        return - \
                                                            671483940756762216
                                                    if (sex !=
                                                            6306819796163687131):
                                                        if (final_weight >
                                                                204133):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight <=
                                                                204133):
                                                            return - \
                                                                671483940756762216
                                    if (final_weight <= 189527):
                                        if (hours_per_week > 37):
                                            if (age > 63):
                                                return -671483940756762216
                                            if (age <= 63):
                                                if (age > 54):
                                                    if (final_weight > 116610):
                                                        if (age > 61):
                                                            return - \
                                                                671483940756762216
                                                        if (age <= 61):
                                                            if (
                                                                    hours_per_week >
                                                                    39):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                    hours_per_week <=
                                                                    39):
                                                                return - \
                                                                    7811984082516642400
                                                    if (final_weight <=
                                                            116610):
                                                        if (workclass == -
                                                                7197995106135439896):
                                                            if (final_weight >
                                                                    59224):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    59224):
                                                                return - \
                                                                    671483940756762216
                                                        if (workclass != -
                                                                7197995106135439896):
                                                            return - \
                                                                7811984082516642400
                                                if (age <= 54):
                                                    if (age > 53):
                                                        return - \
                                                            671483940756762216
                                                    if (age <= 53):
                                                        if (race is None):
                                                            return - \
                                                                671483940756762216
                                                        if (race == -
                                                                681598405395175136):
                                                            return - \
                                                                7811984082516642400
                                                        if (race != -
                                                                681598405395175136):
                                                            if (final_weight >
                                                                    31851):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    31851):
                                                                return - \
                                                                    671483940756762216
                                        if (hours_per_week <= 37):
                                            return -671483940756762216
                            if (occupation != -6990906632015037778):
                                if (occupation == 8618684898378336489):
                                    if (sex is None):
                                        return -7811984082516642400
                                    if (sex == 6306819796163687131):
                                        if (age > 47):
                                            if (hours_per_week > 37):
                                                if (final_weight is None):
                                                    return -7811984082516642400
                                                if (final_weight > 324775):
                                                    return -671483940756762216
                                                if (final_weight <= 324775):
                                                    if (age > 52):
                                                        return - \
                                                            7811984082516642400
                                                    if (age <= 52):
                                                        if (age > 50):
                                                            return - \
                                                                671483940756762216
                                                        if (age <= 50):
                                                            return - \
                                                                7811984082516642400
                                            if (hours_per_week <= 37):
                                                return -671483940756762216
                                        if (age <= 47):
                                            if (final_weight is None):
                                                return -7811984082516642400
                                            if (final_weight > 84981):
                                                if (final_weight > 92314):
                                                    if (final_weight > 121238):
                                                        if (final_weight >
                                                                167547):
                                                            if (age > 42):
                                                                return - \
                                                                    7811984082516642400
                                                            if (age <= 42):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                167547):
                                                            if (race is None):
                                                                return - \
                                                                    671483940756762216
                                                            if (race ==
                                                                    3632794867504857096):
                                                                return - \
                                                                    7811984082516642400
                                                            if (race !=
                                                                    3632794867504857096):
                                                                return - \
                                                                    671483940756762216
                                                    if (final_weight <=
                                                            121238):
                                                        return - \
                                                            7811984082516642400
                                                if (final_weight <= 92314):
                                                    return -671483940756762216
                                            if (final_weight <= 84981):
                                                return -7811984082516642400
                                    if (sex != 6306819796163687131):
                                        return -7811984082516642400
                                if (occupation != 8618684898378336489):
                                    if (occupation == 3088227676756162338):
                                        if (hours_per_week > 39):
                                            if (age > 65):
                                                return -7811984082516642400
                                            if (age <= 65):
                                                if (age > 63):
                                                    return -671483940756762216
                                                if (age <= 63):
                                                    if (hours_per_week > 71):
                                                        return - \
                                                            7811984082516642400
                                                    if (hours_per_week <= 71):
                                                        if (
                                                                final_weight is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight >
                                                                243348):
                                                            if (
                                                                    workclass is None):
                                                                return - \
                                                                    671483940756762216
                                                            if (workclass ==
                                                                    8585012838816931822):
                                                                return - \
                                                                    671483940756762216
                                                            if (workclass !=
                                                                    8585012838816931822):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                243348):
                                                            if (
                                                                    workclass is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (workclass ==
                                                                    8585012838816931822):
                                                                return - \
                                                                    7811984082516642400
                                                            if (workclass !=
                                                                    8585012838816931822):
                                                                return - \
                                                                    7811984082516642400
                                        if (hours_per_week <= 39):
                                            return -7811984082516642400
                                    if (occupation != 3088227676756162338):
                                        if (race is None):
                                            return -7811984082516642400
                                        if (race == -681598405395175136):
                                            return -7811984082516642400
                                        if (race != -681598405395175136):
                                            if (final_weight is None):
                                                return -7811984082516642400
                                            if (final_weight > 535569):
                                                if (final_weight > 792076):
                                                    return -7811984082516642400
                                                if (final_weight <= 792076):
                                                    return -671483940756762216
                                            if (final_weight <= 535569):
                                                if (hours_per_week > 71):
                                                    if (hours_per_week > 87):
                                                        if (final_weight >
                                                                234866):
                                                            return - \
                                                                671483940756762216
                                                        if (final_weight <=
                                                                234866):
                                                            return - \
                                                                7811984082516642400
                                                    if (hours_per_week <= 87):
                                                        if (age > 49):
                                                            if (
                                                                    hours_per_week >
                                                                    82):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    hours_per_week <=
                                                                    82):
                                                                return - \
                                                                    7811984082516642400
                                                        if (age <= 49):
                                                            return - \
                                                                671483940756762216
                                                if (hours_per_week <= 71):
                                                    if (occupation ==
                                                            1581590029918088140):
                                                        if (final_weight >
                                                                71716):
                                                            if (age > 41):
                                                                return - \
                                                                    7811984082516642400
                                                            if (age <= 41):
                                                                return - \
                                                                    671483940756762216
                                                        if (final_weight <=
                                                                71716):
                                                            return - \
                                                                671483940756762216
                                                    if (occupation !=
                                                            1581590029918088140):
                                                        if (age > 43):
                                                            if (
                                                                    workclass is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (workclass ==
                                                                    8161495398349361779):
                                                                return - \
                                                                    671483940756762216
                                                            if (workclass !=
                                                                    8161495398349361779):
                                                                return - \
                                                                    7811984082516642400
                                                        if (age <= 43):
                                                            if (
                                                                    workclass is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (workclass == -
                                                                    1136074064918994416):
                                                                return - \
                                                                    7811984082516642400
                                                            if (workclass != -
                                                                    1136074064918994416):
                                                                return - \
                                                                    7811984082516642400
                    if (hours_per_week <= 33):
                        if (workclass is None):
                            return -7811984082516642400
                        if (workclass == -7197995106135439896):
                            if (age > 54):
                                if (final_weight is None):
                                    return -671483940756762216
                                if (final_weight > 181769):
                                    if (hours_per_week > 27):
                                        if (education_num > 9):
                                            return -7811984082516642400
                                        if (education_num <= 9):
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
                                        if (workclass == -857656620414700721):
                                            return -7811984082516642400
                                        if (workclass != -857656620414700721):
                                            if (occupation is None):
                                                return -671483940756762216
                                            if (occupation ==
                                                    5332362397248960598):
                                                return -671483940756762216
                                            if (occupation !=
                                                    5332362397248960598):
                                                if (race is None):
                                                    return -671483940756762216
                                                if (race == -
                                                        1569537633132385766):
                                                    if (age > 52):
                                                        if (occupation == -
                                                                5484833051640498835):
                                                            return - \
                                                                671483940756762216
                                                        if (occupation != -
                                                                5484833051640498835):
                                                            return - \
                                                                7811984082516642400
                                                    if (age <= 52):
                                                        if (
                                                                final_weight is None):
                                                            return - \
                                                                671483940756762216
                                                        if (final_weight >
                                                                93252):
                                                            if (final_weight >
                                                                    301988):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    301988):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                93252):
                                                            return - \
                                                                671483940756762216
                                                if (race != -
                                                        1569537633132385766):
                                                    return -7811984082516642400
                                    if (education_num <= 9):
                                        if (age > 57):
                                            return -671483940756762216
                                        if (age <= 57):
                                            if (hours_per_week > 18):
                                                if (final_weight is None):
                                                    return -7811984082516642400
                                                if (final_weight > 194378):
                                                    return -7811984082516642400
                                                if (final_weight <= 194378):
                                                    if (final_weight > 151718):
                                                        if (hours_per_week >
                                                                22):
                                                            return - \
                                                                671483940756762216
                                                        if (hours_per_week <=
                                                                22):
                                                            if (
                                                                    occupation is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (occupation ==
                                                                    8618684898378336489):
                                                                return - \
                                                                    7811984082516642400
                                                            if (occupation !=
                                                                    8618684898378336489):
                                                                return - \
                                                                    671483940756762216
                                                    if (final_weight <=
                                                            151718):
                                                        if (race is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (race == -
                                                                681598405395175136):
                                                            return - \
                                                                671483940756762216
                                                        if (race != -
                                                                681598405395175136):
                                                            if (
                                                                    occupation is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (occupation == -
                                                                    6990906632015037778):
                                                                return - \
                                                                    7811984082516642400
                                                            if (occupation != -
                                                                    6990906632015037778):
                                                                return - \
                                                                    7811984082516642400
                                            if (hours_per_week <= 18):
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
                                        if (age > 41):
                                            if (age > 59):
                                                if (education_num > 9):
                                                    if (hours_per_week > 3):
                                                        if (final_weight >
                                                                265692):
                                                            return - \
                                                                671483940756762216
                                                        if (final_weight <=
                                                                265692):
                                                            if (final_weight >
                                                                    114061):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    114061):
                                                                return - \
                                                                    7811984082516642400
                                                    if (hours_per_week <= 3):
                                                        return - \
                                                            671483940756762216
                                                if (education_num <= 9):
                                                    return -7811984082516642400
                                            if (age <= 59):
                                                if (occupation == -
                                                        6951104699562914960):
                                                    return -671483940756762216
                                                if (occupation != -
                                                        6951104699562914960):
                                                    if (occupation == -
                                                            5484833051640498835):
                                                        if (hours_per_week >
                                                                22):
                                                            return - \
                                                                671483940756762216
                                                        if (hours_per_week <=
                                                                22):
                                                            return - \
                                                                7811984082516642400
                                                    if (occupation != -
                                                            5484833051640498835):
                                                        if (final_weight >
                                                                184287):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight <=
                                                                184287):
                                                            if (final_weight >
                                                                    100729):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    100729):
                                                                return - \
                                                                    7811984082516642400
                                        if (age <= 41):
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
                                        if (age > 32):
                                            if (education_num > 10):
                                                return -671483940756762216
                                            if (education_num <= 10):
                                                return -7811984082516642400
                                        if (age <= 32):
                                            if (hours_per_week is None):
                                                return -671483940756762216
                                            if (hours_per_week > 52):
                                                return -7811984082516642400
                                            if (hours_per_week <= 52):
                                                return -671483940756762216
                                if (workclass != -1136074064918994416):
                                    if (age > 32):
                                        if (sex is None):
                                            return -671483940756762216
                                        if (sex == 6306819796163687131):
                                            if (hours_per_week is None):
                                                return -671483940756762216
                                            if (hours_per_week > 59):
                                                if (education_num > 9):
                                                    return -671483940756762216
                                                if (education_num <= 9):
                                                    if (final_weight is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (final_weight > 156615):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight <=
                                                            156615):
                                                        return - \
                                                            7811984082516642400
                                            if (hours_per_week <= 59):
                                                if (education_num > 10):
                                                    return -7811984082516642400
                                                if (education_num <= 10):
                                                    if (hours_per_week > 46):
                                                        if (
                                                                final_weight is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight >
                                                                337190):
                                                            return - \
                                                                671483940756762216
                                                        if (final_weight <=
                                                                337190):
                                                            if (
                                                                    hours_per_week >
                                                                    52):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    hours_per_week <=
                                                                    52):
                                                                return - \
                                                                    7811984082516642400
                                                    if (hours_per_week <= 46):
                                                        if (hours_per_week >
                                                                38):
                                                            if (
                                                                    final_weight is None):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight >
                                                                    210417):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    210417):
                                                                return - \
                                                                    671483940756762216
                                                        if (hours_per_week <=
                                                                38):
                                                            return - \
                                                                7811984082516642400
                                        if (sex != 6306819796163687131):
                                            return -671483940756762216
                                    if (age <= 32):
                                        if (education_num > 11):
                                            return -671483940756762216
                                        if (education_num <= 11):
                                            if (sex is None):
                                                return -7811984082516642400
                                            if (sex == 6306819796163687131):
                                                if (hours_per_week is None):
                                                    return -7811984082516642400
                                                if (hours_per_week > 67):
                                                    return -7811984082516642400
                                                if (hours_per_week <= 67):
                                                    if (workclass == -
                                                            857656620414700721):
                                                        return - \
                                                            7811984082516642400
                                                    if (workclass != -
                                                            857656620414700721):
                                                        if (race is None):
                                                            return - \
                                                                671483940756762216
                                                        if (race == -
                                                                5895194357237003500):
                                                            return - \
                                                                7811984082516642400
                                                        if (race != -
                                                                5895194357237003500):
                                                            if (
                                                                    education is None):
                                                                return - \
                                                                    671483940756762216
                                                            if (education == -
                                                                    1620783280160849416):
                                                                return - \
                                                                    671483940756762216
                                                            if (education != -
                                                                    1620783280160849416):
                                                                return - \
                                                                    7811984082516642400
                                            if (sex != 6306819796163687131):
                                                return -7811984082516642400
                            if (age <= 27):
                                if (final_weight is None):
                                    return -7811984082516642400
                                if (final_weight > 162313):
                                    if (final_weight > 190463):
                                        if (workclass is None):
                                            return -7811984082516642400
                                        if (workclass == 8585012838816931822):
                                            return -7811984082516642400
                                        if (workclass != 8585012838816931822):
                                            if (education_num > 9):
                                                return -671483940756762216
                                            if (education_num <= 9):
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
                                        if (final_weight is None):
                                            return -7811984082516642400
                                        if (final_weight > 133042):
                                            return -671483940756762216
                                        if (final_weight <= 133042):
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
                                        if (hours_per_week > 73):
                                            return -671483940756762216
                                        if (hours_per_week <= 73):
                                            if (hours_per_week > 61):
                                                return -7811984082516642400
                                            if (hours_per_week <= 61):
                                                if (occupation ==
                                                        5332362397248960598):
                                                    return -671483940756762216
                                                if (occupation !=
                                                        5332362397248960598):
                                                    if (occupation ==
                                                            8618684898378336489):
                                                        return - \
                                                            7811984082516642400
                                                    if (occupation !=
                                                            8618684898378336489):
                                                        if (occupation == -
                                                                3959269231467008119):
                                                            if (
                                                                    workclass is None):
                                                                return - \
                                                                    671483940756762216
                                                            if (workclass == -
                                                                    857656620414700721):
                                                                return - \
                                                                    671483940756762216
                                                            if (workclass != -
                                                                    857656620414700721):
                                                                return - \
                                                                    7811984082516642400
                                                        if (occupation != -
                                                                3959269231467008119):
                                                            if (
                                                                    workclass is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (workclass == -
                                                                    857656620414700721):
                                                                return - \
                                                                    7811984082516642400
                                                            if (workclass != -
                                                                    857656620414700721):
                                                                return - \
                                                                    7811984082516642400
                                    if (age <= 31):
                                        if (occupation == -
                                                6951104699562914960):
                                            return -7811984082516642400
                                        if (occupation != -
                                                6951104699562914960):
                                            if (final_weight is None):
                                                return -7811984082516642400
                                            if (final_weight > 131760):
                                                if (education_num > 9):
                                                    if (hours_per_week > 57):
                                                        if (occupation == -
                                                                8005258492814722552):
                                                            if (
                                                                    hours_per_week >
                                                                    59):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    hours_per_week <=
                                                                    59):
                                                                return - \
                                                                    7811984082516642400
                                                        if (occupation != -
                                                                8005258492814722552):
                                                            return - \
                                                                7811984082516642400
                                                    if (hours_per_week <= 57):
                                                        if (final_weight >
                                                                166656):
                                                            if (occupation == -
                                                                    8005258492814722552):
                                                                return - \
                                                                    671483940756762216
                                                            if (occupation != -
                                                                    8005258492814722552):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                166656):
                                                            return - \
                                                                671483940756762216
                                                if (education_num <= 9):
                                                    if (relationship is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (relationship ==
                                                            8744150760759310329):
                                                        return - \
                                                            671483940756762216
                                                    if (relationship !=
                                                            8744150760759310329):
                                                        if (occupation ==
                                                                1581590029918088140):
                                                            return - \
                                                                671483940756762216
                                                        if (occupation !=
                                                                1581590029918088140):
                                                            if (final_weight >
                                                                    410231):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    410231):
                                                                return - \
                                                                    7811984082516642400
                                            if (final_weight <= 131760):
                                                if (final_weight > 95351):
                                                    return -7811984082516642400
                                                if (final_weight <= 95351):
                                                    if (occupation ==
                                                            2812191937831880778):
                                                        if (hours_per_week >
                                                                51):
                                                            return - \
                                                                671483940756762216
                                                        if (hours_per_week <=
                                                                51):
                                                            return - \
                                                                7811984082516642400
                                                    if (occupation !=
                                                            2812191937831880778):
                                                        if (occupation == -
                                                                5484833051640498835):
                                                            if (education_num >
                                                                    9):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                    education_num <=
                                                                    9):
                                                                return - \
                                                                    671483940756762216
                                                        if (occupation != -
                                                                5484833051640498835):
                                                            if (occupation ==
                                                                    5332362397248960598):
                                                                return - \
                                                                    7811984082516642400
                                                            if (occupation !=
                                                                    5332362397248960598):
                                                                return - \
                                                                    7811984082516642400
                                if (hours_per_week <= 46):
                                    if (occupation == 1581590029918088140):
                                        if (hours_per_week > 39):
                                            if (final_weight is None):
                                                return -7811984082516642400
                                            if (final_weight > 316937):
                                                return -7811984082516642400
                                            if (final_weight <= 316937):
                                                if (final_weight > 268432):
                                                    return -671483940756762216
                                                if (final_weight <= 268432):
                                                    if (workclass is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (workclass == -
                                                            4284295320506787287):
                                                        return - \
                                                            671483940756762216
                                                    if (workclass != -
                                                            4284295320506787287):
                                                        if (education is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (education == -
                                                                1620783280160849416):
                                                            if (final_weight >
                                                                    66920):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    66920):
                                                                return - \
                                                                    671483940756762216
                                                        if (education != -
                                                                1620783280160849416):
                                                            if (final_weight >
                                                                    82745):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    82745):
                                                                return - \
                                                                    7811984082516642400
                                        if (hours_per_week <= 39):
                                            if (hours_per_week > 7):
                                                if (final_weight is None):
                                                    return -671483940756762216
                                                if (final_weight > 151741):
                                                    return -671483940756762216
                                                if (final_weight <= 151741):
                                                    if (hours_per_week > 17):
                                                        if (final_weight >
                                                                71976):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight <=
                                                                71976):
                                                            return - \
                                                                671483940756762216
                                                    if (hours_per_week <= 17):
                                                        return - \
                                                            671483940756762216
                                            if (hours_per_week <= 7):
                                                return -7811984082516642400
                                    if (occupation != 1581590029918088140):
                                        if (workclass is None):
                                            return -7811984082516642400
                                        if (workclass == 8161495398349361779):
                                            if (age > 30):
                                                if (occupation ==
                                                        4779842868628447834):
                                                    return -7811984082516642400
                                                if (occupation !=
                                                        4779842868628447834):
                                                    if (occupation == -
                                                            8005258492814722552):
                                                        return - \
                                                            7811984082516642400
                                                    if (occupation != -
                                                            8005258492814722552):
                                                        if (race is None):
                                                            return - \
                                                                671483940756762216
                                                        if (race == -
                                                                1569537633132385766):
                                                            return - \
                                                                671483940756762216
                                                        if (race != -
                                                                1569537633132385766):
                                                            if (education_num >
                                                                    9):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    education_num <=
                                                                    9):
                                                                return - \
                                                                    7811984082516642400
                                            if (age <= 30):
                                                return -671483940756762216
                                        if (workclass != 8161495398349361779):
                                            if (relationship is None):
                                                return -7811984082516642400
                                            if (relationship == -
                                                    6190047399745113596):
                                                return -7811984082516642400
                                            if (relationship != -
                                                    6190047399745113596):
                                                if (occupation == -
                                                        6951104699562914960):
                                                    if (education is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (education == -
                                                            1620783280160849416):
                                                        if (
                                                                final_weight is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight >
                                                                186571):
                                                            if (final_weight >
                                                                    214492):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    214492):
                                                                return - \
                                                                    671483940756762216
                                                        if (final_weight <=
                                                                186571):
                                                            if (final_weight >
                                                                    37583):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    37583):
                                                                return - \
                                                                    7811984082516642400
                                                    if (education != -
                                                            1620783280160849416):
                                                        if (age > 30):
                                                            return - \
                                                                7811984082516642400
                                                        if (age <= 30):
                                                            if (age > 29):
                                                                return - \
                                                                    7811984082516642400
                                                            if (age <= 29):
                                                                return - \
                                                                    7811984082516642400
                                                if (occupation != -
                                                        6951104699562914960):
                                                    if (relationship == -
                                                            7487827120114232249):
                                                        if (
                                                                final_weight is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight >
                                                                66306):
                                                            if (final_weight >
                                                                    202819):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    202819):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                66306):
                                                            if (final_weight >
                                                                    47362):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    47362):
                                                                return - \
                                                                    671483940756762216
                                                    if (relationship != -
                                                            7487827120114232249):
                                                        if (
                                                                final_weight is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight >
                                                                170446):
                                                            if (final_weight >
                                                                    274418):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    274418):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                170446):
                                                            if (
                                                                    education is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (education == -
                                                                    1620783280160849416):
                                                                return - \
                                                                    7811984082516642400
                                                            if (education != -
                                                                    1620783280160849416):
                                                                return - \
                                                                    7811984082516642400
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
                                        if (final_weight is None):
                                            return -7811984082516642400
                                        if (final_weight > 339707):
                                            return -671483940756762216
                                        if (final_weight <= 339707):
                                            if (education is None):
                                                return -7811984082516642400
                                            if (education == -
                                                    1620783280160849416):
                                                if (race is None):
                                                    return -7811984082516642400
                                                if (race == -
                                                        1569537633132385766):
                                                    if (final_weight > 121186):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight <=
                                                            121186):
                                                        return - \
                                                            7811984082516642400
                                                if (race != -
                                                        1569537633132385766):
                                                    return -7811984082516642400
                                            if (education != -
                                                    1620783280160849416):
                                                return -7811984082516642400
                                    if (sex != 6306819796163687131):
                                        return -7811984082516642400
                                if (occupation != 5332362397248960598):
                                    if (occupation == -6951104699562914960):
                                        if (final_weight is None):
                                            return -7811984082516642400
                                        if (final_weight > 154988):
                                            return -7811984082516642400
                                        if (final_weight <= 154988):
                                            return -671483940756762216
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
                                        if (hours_per_week > 37):
                                            if (final_weight > 190475):
                                                if (final_weight > 226535):
                                                    if (hours_per_week > 45):
                                                        return - \
                                                            671483940756762216
                                                    if (hours_per_week <= 45):
                                                        if (race is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (race == -
                                                                1569537633132385766):
                                                            return - \
                                                                7811984082516642400
                                                        if (race != -
                                                                1569537633132385766):
                                                            return - \
                                                                671483940756762216
                                                if (final_weight <= 226535):
                                                    return -671483940756762216
                                            if (final_weight <= 190475):
                                                if (final_weight > 181878):
                                                    return -7811984082516642400
                                                if (final_weight <= 181878):
                                                    if (hours_per_week > 55):
                                                        return - \
                                                            7811984082516642400
                                                    if (hours_per_week <= 55):
                                                        if (final_weight >
                                                                156702):
                                                            if (final_weight >
                                                                    177866):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    177866):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                156702):
                                                            return - \
                                                                671483940756762216
                                        if (hours_per_week <= 37):
                                            return -7811984082516642400
                                    if (final_weight <= 89485):
                                        return -7811984082516642400
                                if (occupation != 2812191937831880778):
                                    if (final_weight is None):
                                        return -7811984082516642400
                                    if (final_weight > 162184):
                                        if (age > 62):
                                            if (workclass is None):
                                                return -7811984082516642400
                                            if (workclass == -
                                                    857656620414700721):
                                                return -671483940756762216
                                            if (workclass != -
                                                    857656620414700721):
                                                if (occupation == -
                                                        5484833051640498835):
                                                    if (hours_per_week > 33):
                                                        return - \
                                                            671483940756762216
                                                    if (hours_per_week <= 33):
                                                        return - \
                                                            7811984082516642400
                                                if (occupation != -
                                                        5484833051640498835):
                                                    return -7811984082516642400
                                        if (age <= 62):
                                            return -7811984082516642400
                                    if (final_weight <= 162184):
                                        if (final_weight > 151824):
                                            if (occupation == -
                                                    8227066636055033186):
                                                return -7811984082516642400
                                            if (occupation != -
                                                    8227066636055033186):
                                                return -671483940756762216
                                        if (final_weight <= 151824):
                                            if (final_weight > 118909):
                                                return -7811984082516642400
                                            if (final_weight <= 118909):
                                                if (final_weight > 65018):
                                                    if (age > 55):
                                                        if (occupation == -
                                                                6990906632015037778):
                                                            return - \
                                                                671483940756762216
                                                        if (occupation != -
                                                                6990906632015037778):
                                                            if (race is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (race == -
                                                                    1569537633132385766):
                                                                return - \
                                                                    7811984082516642400
                                                            if (race != -
                                                                    1569537633132385766):
                                                                return - \
                                                                    671483940756762216
                                                    if (age <= 55):
                                                        return - \
                                                            7811984082516642400
                                                if (final_weight <= 65018):
                                                    return -7811984082516642400
                            if (age <= 53):
                                if (occupation is None):
                                    return -7811984082516642400
                                if (occupation == -5484833051640498835):
                                    if (hours_per_week > 52):
                                        return -7811984082516642400
                                    if (hours_per_week <= 52):
                                        if (sex is None):
                                            return -671483940756762216
                                        if (sex == 6306819796163687131):
                                            return -671483940756762216
                                        if (sex != 6306819796163687131):
                                            return -7811984082516642400
                                if (occupation != -5484833051640498835):
                                    if (workclass is None):
                                        return -7811984082516642400
                                    if (workclass == -857656620414700721):
                                        return -7811984082516642400
                                    if (workclass != -857656620414700721):
                                        if (occupation == -
                                                6990906632015037778):
                                            if (hours_per_week > 55):
                                                return -7811984082516642400
                                            if (hours_per_week <= 55):
                                                if (final_weight is None):
                                                    return -671483940756762216
                                                if (final_weight > 340151):
                                                    return -7811984082516642400
                                                if (final_weight <= 340151):
                                                    return -671483940756762216
                                        if (occupation != -
                                                6990906632015037778):
                                            if (race is None):
                                                return -7811984082516642400
                                            if (race == 3939476748445039507):
                                                return -671483940756762216
                                            if (race != 3939476748445039507):
                                                if (hours_per_week > 39):
                                                    if (race ==
                                                            3632794867504857096):
                                                        return - \
                                                            7811984082516642400
                                                    if (race !=
                                                            3632794867504857096):
                                                        if (occupation ==
                                                                8618684898378336489):
                                                            if (race == -
                                                                    1569537633132385766):
                                                                return - \
                                                                    7811984082516642400
                                                            if (race != -
                                                                    1569537633132385766):
                                                                return - \
                                                                    7811984082516642400
                                                        if (occupation !=
                                                                8618684898378336489):
                                                            if (education_num >
                                                                    7):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                    education_num <=
                                                                    7):
                                                                return - \
                                                                    7811984082516642400
                                                if (hours_per_week <= 39):
                                                    if (race == -
                                                            1569537633132385766):
                                                        return - \
                                                            7811984082516642400
                                                    if (race != -
                                                            1569537633132385766):
                                                        if (hours_per_week >
                                                                36):
                                                            return - \
                                                                7811984082516642400
                                                        if (hours_per_week <=
                                                                36):
                                                            return - \
                                                                671483940756762216
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
                                        if (final_weight is None):
                                            return -671483940756762216
                                        if (final_weight > 99690):
                                            return -671483940756762216
                                        if (final_weight <= 99690):
                                            return -7811984082516642400
                                if (occupation != -6990906632015037778):
                                    if (occupation == -5484833051640498835):
                                        if (age > 53):
                                            if (final_weight is None):
                                                return -671483940756762216
                                            if (final_weight > 104904):
                                                return -671483940756762216
                                            if (final_weight <= 104904):
                                                return -7811984082516642400
                                        if (age <= 53):
                                            return -7811984082516642400
                                    if (occupation != -5484833051640498835):
                                        if (hours_per_week > 39):
                                            if (hours_per_week > 51):
                                                return -7811984082516642400
                                            if (hours_per_week <= 51):
                                                if (hours_per_week > 49):
                                                    if (final_weight is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (final_weight > 216613):
                                                        return - \
                                                            7811984082516642400
                                                    if (final_weight <=
                                                            216613):
                                                        if (final_weight >
                                                                194761):
                                                            return - \
                                                                671483940756762216
                                                        if (final_weight <=
                                                                194761):
                                                            if (sex is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (sex ==
                                                                    6306819796163687131):
                                                                return - \
                                                                    7811984082516642400
                                                            if (sex !=
                                                                    6306819796163687131):
                                                                return - \
                                                                    671483940756762216
                                                if (hours_per_week <= 49):
                                                    if (age > 53):
                                                        if (
                                                                final_weight is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight >
                                                                60233):
                                                            if (age > 56):
                                                                return - \
                                                                    7811984082516642400
                                                            if (age <= 56):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                60233):
                                                            return - \
                                                                671483940756762216
                                                    if (age <= 53):
                                                        if (
                                                                final_weight is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight >
                                                                221011):
                                                            if (final_weight >
                                                                    237838):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    237838):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                221011):
                                                            return - \
                                                                7811984082516642400
                                        if (hours_per_week <= 39):
                                            return -7811984082516642400
                            if (workclass != 8585012838816931822):
                                if (hours_per_week > 55):
                                    if (workclass == -1136074064918994416):
                                        if (occupation is None):
                                            return -671483940756762216
                                        if (occupation == 3088227676756162338):
                                            if (age > 61):
                                                if (education_num > 3):
                                                    return -671483940756762216
                                                if (education_num <= 3):
                                                    return -7811984082516642400
                                            if (age <= 61):
                                                return -7811984082516642400
                                        if (occupation != 3088227676756162338):
                                            return -671483940756762216
                                    if (workclass != -1136074064918994416):
                                        return -7811984082516642400
                                if (hours_per_week <= 55):
                                    if (workclass == -7197995106135439896):
                                        if (occupation is None):
                                            return -671483940756762216
                                        if (occupation == -
                                                8005258492814722552):
                                            return -671483940756762216
                                        if (occupation != -
                                                8005258492814722552):
                                            if (occupation == -
                                                    5484833051640498835):
                                                return -671483940756762216
                                            if (occupation != -
                                                    5484833051640498835):
                                                if (occupation == -
                                                        8227066636055033186):
                                                    return -671483940756762216
                                                if (occupation != -
                                                        8227066636055033186):
                                                    return -7811984082516642400
                                    if (workclass != -7197995106135439896):
                                        if (age > 40):
                                            if (final_weight is None):
                                                return -7811984082516642400
                                            if (final_weight > 35109):
                                                if (hours_per_week > 27):
                                                    return -7811984082516642400
                                                if (hours_per_week <= 27):
                                                    if (final_weight > 220800):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight <=
                                                            220800):
                                                        return - \
                                                            7811984082516642400
                                            if (final_weight <= 35109):
                                                if (final_weight > 33892):
                                                    return -671483940756762216
                                                if (final_weight <= 33892):
                                                    return -7811984082516642400
                                        if (age <= 40):
                                            if (education is None):
                                                return -671483940756762216
                                            if (education == -
                                                    3305009427453673313):
                                                return -671483940756762216
                                            if (education != -
                                                    3305009427453673313):
                                                if (occupation is None):
                                                    return -7811984082516642400
                                                if (occupation == -
                                                        8005258492814722552):
                                                    return -7811984082516642400
                                                if (occupation != -
                                                        8005258492814722552):
                                                    if (relationship is None):
                                                        return - \
                                                            671483940756762216
                                                    if (relationship ==
                                                            8744150760759310329):
                                                        return - \
                                                            7811984082516642400
                                                    if (relationship !=
                                                            8744150760759310329):
                                                        return - \
                                                            671483940756762216
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
                                        if (education_num > 6):
                                            return -671483940756762216
                                        if (education_num <= 6):
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
                                        if (sex is None):
                                            return -7811984082516642400
                                        if (sex == 6306819796163687131):
                                            return -671483940756762216
                                        if (sex != 6306819796163687131):
                                            return -7811984082516642400
                                    if (final_weight <= 219946):
                                        return -7811984082516642400
                                if (occupation != 5332362397248960598):
                                    if (final_weight is None):
                                        return -7811984082516642400
                                    if (final_weight > 145325):
                                        return -7811984082516642400
                                    if (final_weight <= 145325):
                                        if (age > 28):
                                            if (age > 29):
                                                if (education is None):
                                                    return -7811984082516642400
                                                if (education == -
                                                        3305009427453673313):
                                                    if (occupation == -
                                                            8227066636055033186):
                                                        return - \
                                                            671483940756762216
                                                    if (occupation != -
                                                            8227066636055033186):
                                                        return - \
                                                            7811984082516642400
                                                if (education != -
                                                        3305009427453673313):
                                                    return -7811984082516642400
                                            if (age <= 29):
                                                if (occupation ==
                                                        8618684898378336489):
                                                    return -7811984082516642400
                                                if (occupation !=
                                                        8618684898378336489):
                                                    return -671483940756762216
                                        if (age <= 28):
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
                                        if (age > 27):
                                            if (hours_per_week is None):
                                                return -671483940756762216
                                            if (hours_per_week > 30):
                                                return -671483940756762216
                                            if (hours_per_week <= 30):
                                                return -7811984082516642400
                                        if (age <= 27):
                                            if (occupation ==
                                                    2812191937831880778):
                                                return -671483940756762216
                                            if (occupation !=
                                                    2812191937831880778):
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
                                        if (workclass is None):
                                            return -671483940756762216
                                        if (workclass == -857656620414700721):
                                            return -7811984082516642400
                                        if (workclass != -857656620414700721):
                                            return -671483940756762216
                                    if (education_num <= 13):
                                        return -7811984082516642400
                                if (hours_per_week <= 58):
                                    if (race is None):
                                        return -671483940756762216
                                    if (race == -681598405395175136):
                                        return -7811984082516642400
                                    if (race != -681598405395175136):
                                        if (marital_status == -
                                                2843050270188924016):
                                            if (age > 48):
                                                return -671483940756762216
                                            if (age <= 48):
                                                if (age > 46):
                                                    return -7811984082516642400
                                                if (age <= 46):
                                                    return -671483940756762216
                                        if (marital_status != -
                                                2843050270188924016):
                                            return -671483940756762216
                            if (final_weight <= 160393):
                                if (hours_per_week > 47):
                                    if (final_weight > 51818):
                                        if (workclass is None):
                                            return -671483940756762216
                                        if (workclass == 8585012838816931822):
                                            if (marital_status ==
                                                    7568786824864426784):
                                                return -7811984082516642400
                                            if (marital_status !=
                                                    7568786824864426784):
                                                return -671483940756762216
                                        if (workclass != 8585012838816931822):
                                            if (hours_per_week > 62):
                                                if (hours_per_week > 85):
                                                    return -7811984082516642400
                                                if (hours_per_week <= 85):
                                                    return -671483940756762216
                                            if (hours_per_week <= 62):
                                                return -7811984082516642400
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
                                        if (final_weight > 259049):
                                            return -7811984082516642400
                                        if (final_weight <= 259049):
                                            if (race is None):
                                                return -671483940756762216
                                            if (race == -5895194357237003500):
                                                return -7811984082516642400
                                            if (race != -5895194357237003500):
                                                if (final_weight > 40926):
                                                    if (workclass == -
                                                            4284295320506787287):
                                                        return - \
                                                            7811984082516642400
                                                    if (workclass != -
                                                            4284295320506787287):
                                                        if (age > 31):
                                                            if (
                                                                    hours_per_week >
                                                                    49):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    hours_per_week <=
                                                                    49):
                                                                return - \
                                                                    671483940756762216
                                                        if (age <= 31):
                                                            if (education_num >
                                                                    13):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                    education_num <=
                                                                    13):
                                                                return - \
                                                                    671483940756762216
                                                if (final_weight <= 40926):
                                                    return -7811984082516642400
                    if (occupation != -6990906632015037778):
                        if (education_num > 14):
                            if (age > 32):
                                if (age > 52):
                                    if (marital_status == -
                                            5485661916787442206):
                                        return -671483940756762216
                                    if (marital_status != -
                                            5485661916787442206):
                                        if (workclass is None):
                                            return -7811984082516642400
                                        if (workclass == 8585012838816931822):
                                            return -7811984082516642400
                                        if (workclass != 8585012838816931822):
                                            if (hours_per_week > 55):
                                                return -7811984082516642400
                                            if (hours_per_week <= 55):
                                                if (marital_status == -
                                                        2843050270188924016):
                                                    return -671483940756762216
                                                if (marital_status != -
                                                        2843050270188924016):
                                                    if (hours_per_week > 47):
                                                        return - \
                                                            7811984082516642400
                                                    if (hours_per_week <= 47):
                                                        return - \
                                                            671483940756762216
                                if (age <= 52):
                                    if (hours_per_week > 52):
                                        if (hours_per_week > 75):
                                            return -7811984082516642400
                                        if (hours_per_week <= 75):
                                            return -671483940756762216
                                    if (hours_per_week <= 52):
                                        if (relationship is None):
                                            return -671483940756762216
                                        if (relationship ==
                                                5722155880036500383):
                                            if (final_weight is None):
                                                return -671483940756762216
                                            if (final_weight > 215668):
                                                return -7811984082516642400
                                            if (final_weight <= 215668):
                                                if (workclass is None):
                                                    return -671483940756762216
                                                if (workclass == -
                                                        4284295320506787287):
                                                    return -7811984082516642400
                                                if (workclass != -
                                                        4284295320506787287):
                                                    if (final_weight > 67253):
                                                        if (age > 45):
                                                            if (
                                                                    hours_per_week >
                                                                    47):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    hours_per_week <=
                                                                    47):
                                                                return - \
                                                                    7811984082516642400
                                                        if (age <= 45):
                                                            return - \
                                                                671483940756762216
                                                    if (final_weight <= 67253):
                                                        return - \
                                                            7811984082516642400
                                        if (relationship !=
                                                5722155880036500383):
                                            return -671483940756762216
                            if (age <= 32):
                                if (age > 29):
                                    return -7811984082516642400
                                if (age <= 29):
                                    if (marital_status == -
                                            2843050270188924016):
                                        if (final_weight is None):
                                            return -7811984082516642400
                                        if (final_weight > 92062):
                                            return -7811984082516642400
                                        if (final_weight <= 92062):
                                            if (sex is None):
                                                return -7811984082516642400
                                            if (sex == 6306819796163687131):
                                                return -671483940756762216
                                            if (sex != 6306819796163687131):
                                                return -7811984082516642400
                                    if (marital_status != -
                                            2843050270188924016):
                                        return -671483940756762216
                        if (education_num <= 14):
                            if (sex is None):
                                return -7811984082516642400
                            if (sex == 6306819796163687131):
                                if (hours_per_week > 55):
                                    if (occupation == -5484833051640498835):
                                        if (relationship is None):
                                            return -7811984082516642400
                                        if (relationship == -
                                                6190047399745113596):
                                            return -7811984082516642400
                                        if (relationship != -
                                                6190047399745113596):
                                            if (workclass is None):
                                                return -671483940756762216
                                            if (workclass == -
                                                    1136074064918994416):
                                                return -7811984082516642400
                                            if (workclass != -
                                                    1136074064918994416):
                                                if (race is None):
                                                    return -671483940756762216
                                                if (race == -
                                                        1569537633132385766):
                                                    if (age > 39):
                                                        if (age > 51):
                                                            return - \
                                                                7811984082516642400
                                                        if (age <= 51):
                                                            if (
                                                                marital_status == -
                                                                    2843050270188924016):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                marital_status != -
                                                                    2843050270188924016):
                                                                return - \
                                                                    671483940756762216
                                                    if (age <= 39):
                                                        if (education_num >
                                                                13):
                                                            return - \
                                                                7811984082516642400
                                                        if (education_num <=
                                                                13):
                                                            if (
                                                                marital_status == -
                                                                    2843050270188924016):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                marital_status != -
                                                                    2843050270188924016):
                                                                return - \
                                                                    7811984082516642400
                                                if (race != -
                                                        1569537633132385766):
                                                    return -671483940756762216
                                    if (occupation != -5484833051640498835):
                                        if (race is None):
                                            return -7811984082516642400
                                        if (race == 3632794867504857096):
                                            return -671483940756762216
                                        if (race != 3632794867504857096):
                                            if (occupation ==
                                                    5332362397248960598):
                                                if (marital_status == -
                                                        2843050270188924016):
                                                    return -671483940756762216
                                                if (marital_status != -
                                                        2843050270188924016):
                                                    return -7811984082516642400
                                            if (occupation !=
                                                    5332362397248960598):
                                                if (hours_per_week > 87):
                                                    if (hours_per_week > 94):
                                                        return - \
                                                            7811984082516642400
                                                    if (hours_per_week <= 94):
                                                        return - \
                                                            671483940756762216
                                                if (hours_per_week <= 87):
                                                    return -7811984082516642400
                                if (hours_per_week <= 55):
                                    if (workclass is None):
                                        return -7811984082516642400
                                    if (workclass == -4284295320506787287):
                                        return -7811984082516642400
                                    if (workclass != -4284295320506787287):
                                        if (age > 32):
                                            if (workclass == -
                                                    7197995106135439896):
                                                return -7811984082516642400
                                            if (workclass != -
                                                    7197995106135439896):
                                                if (marital_status ==
                                                        7568786824864426784):
                                                    return -7811984082516642400
                                                if (marital_status !=
                                                        7568786824864426784):
                                                    if (occupation == -
                                                            8005258492814722552):
                                                        return - \
                                                            671483940756762216
                                                    if (occupation != -
                                                            8005258492814722552):
                                                        if (age > 55):
                                                            if (
                                                                marital_status == -
                                                                    5485661916787442206):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                marital_status != -
                                                                    5485661916787442206):
                                                                return - \
                                                                    7811984082516642400
                                                        if (age <= 55):
                                                            if (age > 41):
                                                                return - \
                                                                    671483940756762216
                                                            if (age <= 41):
                                                                return - \
                                                                    7811984082516642400
                                        if (age <= 32):
                                            if (race is None):
                                                return -7811984082516642400
                                            if (race == -5895194357237003500):
                                                return -671483940756762216
                                            if (race != -5895194357237003500):
                                                if (workclass ==
                                                        8585012838816931822):
                                                    if (final_weight is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (final_weight > 286123):
                                                        if (age > 29):
                                                            if (
                                                                    hours_per_week >
                                                                    47):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                    hours_per_week <=
                                                                    47):
                                                                return - \
                                                                    671483940756762216
                                                        if (age <= 29):
                                                            return - \
                                                                671483940756762216
                                                    if (final_weight <=
                                                            286123):
                                                        if (final_weight >
                                                                222378):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight <=
                                                                222378):
                                                            if (final_weight >
                                                                    204109):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    204109):
                                                                return - \
                                                                    7811984082516642400
                                                if (workclass !=
                                                        8585012838816931822):
                                                    return -7811984082516642400
                            if (sex != 6306819796163687131):
                                if (final_weight is None):
                                    return -7811984082516642400
                                if (final_weight > 151124):
                                    if (final_weight > 158605):
                                        if (marital_status == -
                                                1035125786006291861):
                                            return -671483940756762216
                                        if (marital_status != -
                                                1035125786006291861):
                                            if (race is None):
                                                return -7811984082516642400
                                            if (race == 3632794867504857096):
                                                return -671483940756762216
                                            if (race != 3632794867504857096):
                                                if (age > 43):
                                                    if (workclass is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (workclass == -
                                                            4284295320506787287):
                                                        return - \
                                                            671483940756762216
                                                    if (workclass != -
                                                            4284295320506787287):
                                                        if (workclass == -
                                                                857656620414700721):
                                                            if (age > 57):
                                                                return - \
                                                                    671483940756762216
                                                            if (age <= 57):
                                                                return - \
                                                                    7811984082516642400
                                                        if (workclass != -
                                                                857656620414700721):
                                                            return - \
                                                                7811984082516642400
                                                if (age <= 43):
                                                    if (age > 29):
                                                        if (age > 32):
                                                            if (
                                                                marital_status == -
                                                                    2843050270188924016):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                marital_status != -
                                                                    2843050270188924016):
                                                                return - \
                                                                    7811984082516642400
                                                        if (age <= 32):
                                                            if (final_weight >
                                                                    241978):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    241978):
                                                                return - \
                                                                    671483940756762216
                                                    if (age <= 29):
                                                        if (
                                                                relationship is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (relationship == -
                                                                7729121122090457494):
                                                            return - \
                                                                671483940756762216
                                                        if (relationship != -
                                                                7729121122090457494):
                                                            return - \
                                                                7811984082516642400
                                    if (final_weight <= 158605):
                                        if (final_weight > 157227):
                                            return -7811984082516642400
                                        if (final_weight <= 157227):
                                            return -671483940756762216
                                if (final_weight <= 151124):
                                    if (workclass is None):
                                        return -7811984082516642400
                                    if (workclass == 8161495398349361779):
                                        return -671483940756762216
                                    if (workclass != 8161495398349361779):
                                        if (relationship is None):
                                            return -7811984082516642400
                                        if (relationship ==
                                                5722155880036500383):
                                            if (hours_per_week > 61):
                                                if (hours_per_week > 67):
                                                    return -7811984082516642400
                                                if (hours_per_week <= 67):
                                                    return -671483940756762216
                                            if (hours_per_week <= 61):
                                                if (final_weight > 107801):
                                                    if (final_weight > 127548):
                                                        if (hours_per_week >
                                                                52):
                                                            return - \
                                                                671483940756762216
                                                        if (hours_per_week <=
                                                                52):
                                                            return - \
                                                                7811984082516642400
                                                    if (final_weight <=
                                                            127548):
                                                        if (education_num >
                                                                13):
                                                            return - \
                                                                7811984082516642400
                                                        if (education_num <=
                                                                13):
                                                            return - \
                                                                671483940756762216
                                                if (final_weight <= 107801):
                                                    return -7811984082516642400
                                        if (relationship !=
                                                5722155880036500383):
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
                                        if (education_num > 15):
                                            return -7811984082516642400
                                        if (education_num <= 15):
                                            if (workclass is None):
                                                return -671483940756762216
                                            if (workclass == -
                                                    4284295320506787287):
                                                return -7811984082516642400
                                            if (workclass != -
                                                    4284295320506787287):
                                                return -671483940756762216
                                if (hours_per_week <= 21):
                                    if (marital_status == -
                                            5485661916787442206):
                                        return -671483940756762216
                                    if (marital_status != -
                                            5485661916787442206):
                                        return -7811984082516642400
                            if (sex != 6306819796163687131):
                                if (marital_status == -2843050270188924016):
                                    if (final_weight is None):
                                        return -671483940756762216
                                    if (final_weight > 386027):
                                        return -7811984082516642400
                                    if (final_weight <= 386027):
                                        if (education_num > 15):
                                            return -671483940756762216
                                        if (education_num <= 15):
                                            if (hours_per_week > 37):
                                                if (occupation is None):
                                                    return -7811984082516642400
                                                if (occupation ==
                                                        1581590029918088140):
                                                    if (final_weight > 174189):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight <=
                                                            174189):
                                                        return - \
                                                            7811984082516642400
                                                if (occupation !=
                                                        1581590029918088140):
                                                    return -7811984082516642400
                                            if (hours_per_week <= 37):
                                                return -671483940756762216
                                if (marital_status != -2843050270188924016):
                                    if (final_weight is None):
                                        return -7811984082516642400
                                    if (final_weight > 170081):
                                        if (final_weight > 227385):
                                            return -7811984082516642400
                                        if (final_weight <= 227385):
                                            if (age > 40):
                                                if (age > 47):
                                                    if (workclass is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (workclass == -
                                                            857656620414700721):
                                                        return - \
                                                            671483940756762216
                                                    if (workclass != -
                                                            857656620414700721):
                                                        return - \
                                                            7811984082516642400
                                                if (age <= 47):
                                                    return -671483940756762216
                                            if (age <= 40):
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
                                        if (marital_status == -
                                                2843050270188924016):
                                            if (age > 54):
                                                return -7811984082516642400
                                            if (age <= 54):
                                                if (education_num > 13):
                                                    if (sex is None):
                                                        return - \
                                                            671483940756762216
                                                    if (sex ==
                                                            6306819796163687131):
                                                        return - \
                                                            671483940756762216
                                                    if (sex !=
                                                            6306819796163687131):
                                                        return - \
                                                            7811984082516642400
                                                if (education_num <= 13):
                                                    if (workclass == -
                                                            857656620414700721):
                                                        if (race is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (race == -
                                                                1569537633132385766):
                                                            return - \
                                                                671483940756762216
                                                        if (race != -
                                                                1569537633132385766):
                                                            return - \
                                                                7811984082516642400
                                                    if (workclass != -
                                                            857656620414700721):
                                                        return - \
                                                            7811984082516642400
                                        if (marital_status != -
                                                2843050270188924016):
                                            if (age > 59):
                                                if (age > 64):
                                                    if (marital_status == -
                                                            5485661916787442206):
                                                        if (sex is None):
                                                            return - \
                                                                671483940756762216
                                                        if (sex ==
                                                                6306819796163687131):
                                                            return - \
                                                                671483940756762216
                                                        if (sex !=
                                                                6306819796163687131):
                                                            return - \
                                                                7811984082516642400
                                                    if (marital_status != -
                                                            5485661916787442206):
                                                        return - \
                                                            7811984082516642400
                                                if (age <= 64):
                                                    if (hours_per_week > 41):
                                                        return - \
                                                            7811984082516642400
                                                    if (hours_per_week <= 41):
                                                        return - \
                                                            671483940756762216
                                            if (age <= 59):
                                                if (age > 55):
                                                    if (workclass == -
                                                            1136074064918994416):
                                                        return - \
                                                            671483940756762216
                                                    if (workclass != -
                                                            1136074064918994416):
                                                        return - \
                                                            7811984082516642400
                                                if (age <= 55):
                                                    if (final_weight is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (final_weight > 212626):
                                                        if (sex is None):
                                                            return - \
                                                                671483940756762216
                                                        if (sex ==
                                                                6306819796163687131):
                                                            return - \
                                                                671483940756762216
                                                        if (sex !=
                                                                6306819796163687131):
                                                            if (final_weight >
                                                                    233333):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    233333):
                                                                return - \
                                                                    671483940756762216
                                                    if (final_weight <=
                                                            212626):
                                                        if (final_weight >
                                                                38663):
                                                            if (final_weight >
                                                                    126205):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    126205):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                38663):
                                                            return - \
                                                                671483940756762216
                                if (relationship != 5722155880036500383):
                                    if (age > 49):
                                        if (sex is None):
                                            return -7811984082516642400
                                        if (sex == 6306819796163687131):
                                            if (occupation is None):
                                                return -7811984082516642400
                                            if (occupation ==
                                                    1581590029918088140):
                                                return -671483940756762216
                                            if (occupation !=
                                                    1581590029918088140):
                                                return -7811984082516642400
                                        if (sex != 6306819796163687131):
                                            return -7811984082516642400
                                    if (age <= 49):
                                        if (age > 46):
                                            if (sex is None):
                                                return -7811984082516642400
                                            if (sex == 6306819796163687131):
                                                return -671483940756762216
                                            if (sex != 6306819796163687131):
                                                if (education_num > 13):
                                                    if (occupation is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (occupation == -
                                                            6990906632015037778):
                                                        return - \
                                                            671483940756762216
                                                    if (occupation != -
                                                            6990906632015037778):
                                                        if (race is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (race == -
                                                                5895194357237003500):
                                                            return - \
                                                                671483940756762216
                                                        if (race != -
                                                                5895194357237003500):
                                                            return - \
                                                                7811984082516642400
                                                if (education_num <= 13):
                                                    if (occupation is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (occupation ==
                                                            3356618344216796218):
                                                        return - \
                                                            671483940756762216
                                                    if (occupation !=
                                                            3356618344216796218):
                                                        if (occupation ==
                                                                1581590029918088140):
                                                            if (race is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (race == -
                                                                    1569537633132385766):
                                                                return - \
                                                                    671483940756762216
                                                            if (race != -
                                                                    1569537633132385766):
                                                                return - \
                                                                    7811984082516642400
                                                        if (occupation !=
                                                                1581590029918088140):
                                                            return - \
                                                                7811984082516642400
                                        if (age <= 46):
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
                                        if (hours_per_week > 18):
                                            if (age > 77):
                                                return -671483940756762216
                                            if (age <= 77):
                                                if (final_weight is None):
                                                    return -7811984082516642400
                                                if (final_weight > 154955):
                                                    return -7811984082516642400
                                                if (final_weight <= 154955):
                                                    if (marital_status == -
                                                            2843050270188924016):
                                                        return - \
                                                            7811984082516642400
                                                    if (marital_status != -
                                                            2843050270188924016):
                                                        return - \
                                                            671483940756762216
                                        if (hours_per_week <= 18):
                                            return -7811984082516642400
                        if (age <= 45):
                            if (hours_per_week > 34):
                                if (workclass is None):
                                    return -7811984082516642400
                                if (workclass == -4284295320506787287):
                                    return -7811984082516642400
                                if (workclass != -4284295320506787287):
                                    if (workclass == 8161495398349361779):
                                        if (sex is None):
                                            return -7811984082516642400
                                        if (sex == 6306819796163687131):
                                            if (age > 40):
                                                return -671483940756762216
                                            if (age <= 40):
                                                if (marital_status == -
                                                        5485661916787442206):
                                                    return -671483940756762216
                                                if (marital_status != -
                                                        5485661916787442206):
                                                    if (occupation is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (occupation ==
                                                            5332362397248960598):
                                                        return - \
                                                            7811984082516642400
                                                    if (occupation !=
                                                            5332362397248960598):
                                                        if (race is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (race == -
                                                                1569537633132385766):
                                                            if (occupation ==
                                                                    1581590029918088140):
                                                                return - \
                                                                    7811984082516642400
                                                            if (occupation !=
                                                                    1581590029918088140):
                                                                return - \
                                                                    671483940756762216
                                                        if (race != -
                                                                1569537633132385766):
                                                            return - \
                                                                7811984082516642400
                                        if (sex != 6306819796163687131):
                                            return -7811984082516642400
                                    if (workclass != 8161495398349361779):
                                        if (final_weight is None):
                                            return -7811984082516642400
                                        if (final_weight > 101112):
                                            if (age > 34):
                                                if (marital_status == -
                                                        2843050270188924016):
                                                    if (workclass ==
                                                            8585012838816931822):
                                                        if (
                                                                occupation is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (occupation == -
                                                                6990906632015037778):
                                                            if (final_weight >
                                                                    183320):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    183320):
                                                                return - \
                                                                    671483940756762216
                                                        if (occupation != -
                                                                6990906632015037778):
                                                            if (final_weight >
                                                                    136616):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    136616):
                                                                return - \
                                                                    7811984082516642400
                                                    if (workclass !=
                                                            8585012838816931822):
                                                        if (final_weight >
                                                                183395):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight <=
                                                                183395):
                                                            if (final_weight >
                                                                    166429):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    166429):
                                                                return - \
                                                                    7811984082516642400
                                                if (marital_status != -
                                                        2843050270188924016):
                                                    if (age > 35):
                                                        if (final_weight >
                                                                172291):
                                                            if (workclass == -
                                                                    1136074064918994416):
                                                                return - \
                                                                    7811984082516642400
                                                            if (workclass != -
                                                                    1136074064918994416):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                172291):
                                                            if (final_weight >
                                                                    155329):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    155329):
                                                                return - \
                                                                    7811984082516642400
                                                    if (age <= 35):
                                                        if (
                                                                occupation is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (occupation ==
                                                                4779842868628447834):
                                                            return - \
                                                                671483940756762216
                                                        if (occupation !=
                                                                4779842868628447834):
                                                            if (
                                                                    marital_status ==
                                                                    7568786824864426784):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    marital_status !=
                                                                    7568786824864426784):
                                                                return - \
                                                                    7811984082516642400
                                            if (age <= 34):
                                                if (occupation is None):
                                                    return -7811984082516642400
                                                if (occupation ==
                                                        5332362397248960598):
                                                    return -7811984082516642400
                                                if (occupation !=
                                                        5332362397248960598):
                                                    if (occupation == -
                                                            6990906632015037778):
                                                        return - \
                                                            7811984082516642400
                                                    if (occupation != -
                                                            6990906632015037778):
                                                        if (final_weight >
                                                                137961):
                                                            if (education_num >
                                                                    13):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                    education_num <=
                                                                    13):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                137961):
                                                            if (occupation == -
                                                                    5484833051640498835):
                                                                return - \
                                                                    671483940756762216
                                                            if (occupation != -
                                                                    5484833051640498835):
                                                                return - \
                                                                    7811984082516642400
                                        if (final_weight <= 101112):
                                            if (age > 28):
                                                return -7811984082516642400
                                            if (age <= 28):
                                                if (sex is None):
                                                    return -7811984082516642400
                                                if (sex ==
                                                        6306819796163687131):
                                                    if (relationship is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (relationship ==
                                                            5722155880036500383):
                                                        return - \
                                                            671483940756762216
                                                    if (relationship !=
                                                            5722155880036500383):
                                                        if (
                                                                occupation is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (occupation == -
                                                                8005258492814722552):
                                                            return - \
                                                                671483940756762216
                                                        if (occupation != -
                                                                8005258492814722552):
                                                            return - \
                                                                7811984082516642400
                                                if (sex !=
                                                        6306819796163687131):
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
                                        if (occupation is None):
                                            return -7811984082516642400
                                        if (occupation == 1581590029918088140):
                                            if (final_weight is None):
                                                return -7811984082516642400
                                            if (final_weight > 187971):
                                                if (final_weight > 318115):
                                                    if (final_weight > 364262):
                                                        return - \
                                                            7811984082516642400
                                                    if (final_weight <=
                                                            364262):
                                                        return - \
                                                            671483940756762216
                                                if (final_weight <= 318115):
                                                    return -7811984082516642400
                                            if (final_weight <= 187971):
                                                if (final_weight > 36821):
                                                    if (final_weight > 184988):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight <=
                                                            184988):
                                                        if (education is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (education ==
                                                                1163700071921914946):
                                                            if (
                                                                    hours_per_week >
                                                                    50):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    hours_per_week <=
                                                                    50):
                                                                return - \
                                                                    7811984082516642400
                                                        if (education !=
                                                                1163700071921914946):
                                                            if (age > 26):
                                                                return - \
                                                                    7811984082516642400
                                                            if (age <= 26):
                                                                return - \
                                                                    7811984082516642400
                                                if (final_weight <= 36821):
                                                    return -671483940756762216
                                        if (occupation != 1581590029918088140):
                                            if (relationship == -
                                                    7729121122090457494):
                                                if (race == -
                                                        1569537633132385766):
                                                    if (final_weight is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (final_weight > 205660):
                                                        return - \
                                                            7811984082516642400
                                                    if (final_weight <=
                                                            205660):
                                                        return - \
                                                            671483940756762216
                                                if (race != -
                                                        1569537633132385766):
                                                    return -7811984082516642400
                                            if (relationship != -
                                                    7729121122090457494):
                                                if (occupation == -
                                                        6990906632015037778):
                                                    return -7811984082516642400
                                                if (occupation != -
                                                        6990906632015037778):
                                                    if (hours_per_week > 43):
                                                        if (occupation == -
                                                                8005258492814722552):
                                                            if (
                                                                    hours_per_week >
                                                                    50):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    hours_per_week <=
                                                                    50):
                                                                return - \
                                                                    7811984082516642400
                                                        if (occupation != -
                                                                8005258492814722552):
                                                            if (occupation ==
                                                                    3088227676756162338):
                                                                return - \
                                                                    7811984082516642400
                                                            if (occupation !=
                                                                    3088227676756162338):
                                                                return - \
                                                                    7811984082516642400
                                                    if (hours_per_week <= 43):
                                                        if (occupation ==
                                                                5332362397248960598):
                                                            if (
                                                                    final_weight is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight >
                                                                    199150):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    199150):
                                                                return - \
                                                                    7811984082516642400
                                                        if (occupation !=
                                                                5332362397248960598):
                                                            return - \
                                                                7811984082516642400
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
                                        if (workclass is None):
                                            return -7811984082516642400
                                        if (workclass == -7197995106135439896):
                                            if (marital_status == -
                                                    5485661916787442206):
                                                return -671483940756762216
                                            if (marital_status != -
                                                    5485661916787442206):
                                                return -7811984082516642400
                                        if (workclass != -7197995106135439896):
                                            if (hours_per_week > 61):
                                                return -671483940756762216
                                            if (hours_per_week <= 61):
                                                if (occupation ==
                                                        4779842868628447834):
                                                    return -671483940756762216
                                                if (occupation !=
                                                        4779842868628447834):
                                                    if (occupation ==
                                                            8618684898378336489):
                                                        return - \
                                                            7811984082516642400
                                                    if (occupation !=
                                                            8618684898378336489):
                                                        if (education_num > 8):
                                                            if (sex is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (sex ==
                                                                    6306819796163687131):
                                                                return - \
                                                                    7811984082516642400
                                                            if (sex !=
                                                                    6306819796163687131):
                                                                return - \
                                                                    7811984082516642400
                                                        if (education_num <=
                                                                8):
                                                            return - \
                                                                7811984082516642400
                        if (age <= 53):
                            if (relationship is None):
                                return -7811984082516642400
                            if (relationship == 5722155880036500383):
                                if (education is None):
                                    return -7811984082516642400
                                if (education == 4595982442865070163):
                                    if (hours_per_week > 47):
                                        if (final_weight is None):
                                            return -7811984082516642400
                                        if (final_weight > 30779):
                                            if (race is None):
                                                return -7811984082516642400
                                            if (race == -1569537633132385766):
                                                if (final_weight > 521347):
                                                    return -671483940756762216
                                                if (final_weight <= 521347):
                                                    if (marital_status == -
                                                            8271725530730535226):
                                                        if (hours_per_week >
                                                                51):
                                                            if (final_weight >
                                                                    33674):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    33674):
                                                                return - \
                                                                    671483940756762216
                                                        if (hours_per_week <=
                                                                51):
                                                            if (
                                                                    occupation is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (occupation ==
                                                                    4779842868628447834):
                                                                return - \
                                                                    671483940756762216
                                                            if (occupation !=
                                                                    4779842868628447834):
                                                                return - \
                                                                    7811984082516642400
                                                    if (marital_status != -
                                                            8271725530730535226):
                                                        if (age > 39):
                                                            return - \
                                                                7811984082516642400
                                                        if (age <= 39):
                                                            if (final_weight >
                                                                    35599):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    35599):
                                                                return - \
                                                                    671483940756762216
                                            if (race != -1569537633132385766):
                                                return -7811984082516642400
                                        if (final_weight <= 30779):
                                            if (age > 40):
                                                return -7811984082516642400
                                            if (age <= 40):
                                                return -671483940756762216
                                    if (hours_per_week <= 47):
                                        if (workclass is None):
                                            return -7811984082516642400
                                        if (workclass == 8161495398349361779):
                                            if (marital_status == -
                                                    2843050270188924016):
                                                return -671483940756762216
                                            if (marital_status != -
                                                    2843050270188924016):
                                                return -7811984082516642400
                                        if (workclass != 8161495398349361779):
                                            return -7811984082516642400
                                if (education != 4595982442865070163):
                                    if (workclass is None):
                                        return -7811984082516642400
                                    if (workclass == -1136074064918994416):
                                        return -7811984082516642400
                                    if (workclass != -1136074064918994416):
                                        if (age > 52):
                                            if (hours_per_week > 52):
                                                return -7811984082516642400
                                            if (hours_per_week <= 52):
                                                return -671483940756762216
                                        if (age <= 52):
                                            if (occupation is None):
                                                return -7811984082516642400
                                            if (occupation ==
                                                    8618684898378336489):
                                                return -7811984082516642400
                                            if (occupation !=
                                                    8618684898378336489):
                                                if (age > 35):
                                                    if (workclass == -
                                                            4284295320506787287):
                                                        return - \
                                                            671483940756762216
                                                    if (workclass != -
                                                            4284295320506787287):
                                                        if (age > 41):
                                                            if (
                                                                    final_weight is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight >
                                                                    147347):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    147347):
                                                                return - \
                                                                    7811984082516642400
                                                        if (age <= 41):
                                                            if (
                                                                    marital_status ==
                                                                    7568786824864426784):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    marital_status !=
                                                                    7568786824864426784):
                                                                return - \
                                                                    7811984082516642400
                                                if (age <= 35):
                                                    if (hours_per_week > 51):
                                                        return - \
                                                            7811984082516642400
                                                    if (hours_per_week <= 51):
                                                        if (education_num >
                                                                11):
                                                            return - \
                                                                7811984082516642400
                                                        if (education_num <=
                                                                11):
                                                            if (occupation == -
                                                                    3959269231467008119):
                                                                return - \
                                                                    671483940756762216
                                                            if (occupation != -
                                                                    3959269231467008119):
                                                                return - \
                                                                    7811984082516642400
                            if (relationship != 5722155880036500383):
                                if (age > 39):
                                    if (age > 45):
                                        if (education is None):
                                            return -7811984082516642400
                                        if (education == -1620783280160849416):
                                            if (final_weight is None):
                                                return -7811984082516642400
                                            if (final_weight > 162003):
                                                if (final_weight > 182557):
                                                    if (sex is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (sex ==
                                                            6306819796163687131):
                                                        if (final_weight >
                                                                294443):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight <=
                                                                294443):
                                                            return - \
                                                                671483940756762216
                                                    if (sex !=
                                                            6306819796163687131):
                                                        return - \
                                                            7811984082516642400
                                                if (final_weight <= 182557):
                                                    return -671483940756762216
                                            if (final_weight <= 162003):
                                                return -7811984082516642400
                                        if (education != -1620783280160849416):
                                            return -7811984082516642400
                                    if (age <= 45):
                                        if (final_weight is None):
                                            return -7811984082516642400
                                        if (final_weight > 63827):
                                            if (occupation is None):
                                                return -7811984082516642400
                                            if (occupation ==
                                                    5332362397248960598):
                                                if (final_weight > 187713):
                                                    if (hours_per_week > 44):
                                                        return - \
                                                            7811984082516642400
                                                    if (hours_per_week <= 44):
                                                        return - \
                                                            671483940756762216
                                                if (final_weight <= 187713):
                                                    if (marital_status ==
                                                            7568786824864426784):
                                                        return - \
                                                            7811984082516642400
                                                    if (marital_status !=
                                                            7568786824864426784):
                                                        return - \
                                                            671483940756762216
                                            if (occupation !=
                                                    5332362397248960598):
                                                if (relationship == -
                                                        7487827120114232249):
                                                    return -671483940756762216
                                                if (relationship != -
                                                        7487827120114232249):
                                                    if (marital_status == -
                                                            1035125786006291861):
                                                        return - \
                                                            671483940756762216
                                                    if (marital_status != -
                                                            1035125786006291861):
                                                        if (sex is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (sex ==
                                                                6306819796163687131):
                                                            if (occupation == -
                                                                    6990906632015037778):
                                                                return - \
                                                                    671483940756762216
                                                            if (occupation != -
                                                                    6990906632015037778):
                                                                return - \
                                                                    7811984082516642400
                                                        if (sex !=
                                                                6306819796163687131):
                                                            return - \
                                                                7811984082516642400
                                        if (final_weight <= 63827):
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
                                        if (education == 659472584185336986):
                                            return -671483940756762216
                                        if (education != 659472584185336986):
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
                                        if (age > 36):
                                            return -671483940756762216
                                        if (age <= 36):
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
                                    if (marital_status == -
                                            1035125786006291861):
                                        if (education is None):
                                            return -7811984082516642400
                                        if (education == 4595982442865070163):
                                            return -7811984082516642400
                                        if (education != 4595982442865070163):
                                            return -671483940756762216
                                    if (marital_status != -
                                            1035125786006291861):
                                        if (sex is None):
                                            return -7811984082516642400
                                        if (sex == 6306819796163687131):
                                            if (marital_status == -
                                                    2843050270188924016):
                                                return -7811984082516642400
                                            if (marital_status != -
                                                    2843050270188924016):
                                                if (final_weight is None):
                                                    return -7811984082516642400
                                                if (final_weight > 126659):
                                                    if (race is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (race == -
                                                            1569537633132385766):
                                                        if (education_num > 8):
                                                            if (age > 40):
                                                                return - \
                                                                    7811984082516642400
                                                            if (age <= 40):
                                                                return - \
                                                                    671483940756762216
                                                        if (education_num <=
                                                                8):
                                                            return - \
                                                                671483940756762216
                                                    if (race != -
                                                            1569537633132385766):
                                                        return - \
                                                            7811984082516642400
                                                if (final_weight <= 126659):
                                                    return -7811984082516642400
                                        if (sex != 6306819796163687131):
                                            if (final_weight is None):
                                                return -7811984082516642400
                                            if (final_weight > 61433):
                                                if (hours_per_week > 18):
                                                    return -7811984082516642400
                                                if (hours_per_week <= 18):
                                                    if (hours_per_week > 15):
                                                        if (marital_status == -
                                                                5485661916787442206):
                                                            return - \
                                                                671483940756762216
                                                        if (marital_status != -
                                                                5485661916787442206):
                                                            return - \
                                                                7811984082516642400
                                                    if (hours_per_week <= 15):
                                                        return - \
                                                            7811984082516642400
                                            if (final_weight <= 61433):
                                                if (final_weight > 20997):
                                                    if (final_weight > 48143):
                                                        if (race is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (race == -
                                                                1569537633132385766):
                                                            return - \
                                                                671483940756762216
                                                        if (race != -
                                                                1569537633132385766):
                                                            return - \
                                                                7811984082516642400
                                                    if (final_weight <= 48143):
                                                        return - \
                                                            7811984082516642400
                                                if (final_weight <= 20997):
                                                    return -671483940756762216
                                if (occupation != 5332362397248960598):
                                    if (workclass is None):
                                        return -7811984082516642400
                                    if (workclass == -7197995106135439896):
                                        if (marital_status == -
                                                5485661916787442206):
                                            if (education_num > 8):
                                                return -671483940756762216
                                            if (education_num <= 8):
                                                return -7811984082516642400
                                        if (marital_status != -
                                                5485661916787442206):
                                            if (final_weight is None):
                                                return -7811984082516642400
                                            if (final_weight > 101318):
                                                return -7811984082516642400
                                            if (final_weight <= 101318):
                                                return -671483940756762216
                                    if (workclass != -7197995106135439896):
                                        if (occupation == -
                                                3959269231467008119):
                                            if (age > 47):
                                                return -7811984082516642400
                                            if (age <= 47):
                                                if (education_num > 10):
                                                    return -7811984082516642400
                                                if (education_num <= 10):
                                                    if (final_weight is None):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight > 305044):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight <=
                                                            305044):
                                                        if (marital_status == -
                                                                2843050270188924016):
                                                            if (final_weight >
                                                                    132195):
                                                                return - \
                                                                    671483940756762216
                                                            if (final_weight <=
                                                                    132195):
                                                                return - \
                                                                    7811984082516642400
                                                        if (marital_status != -
                                                                2843050270188924016):
                                                            return - \
                                                                7811984082516642400
                                        if (occupation != -
                                                3959269231467008119):
                                            if (occupation ==
                                                    2812191937831880778):
                                                if (education is None):
                                                    return -7811984082516642400
                                                if (education == -
                                                        1620783280160849416):
                                                    if (final_weight is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (final_weight > 157875):
                                                        return - \
                                                            7811984082516642400
                                                    if (final_weight <=
                                                            157875):
                                                        if (hours_per_week >
                                                                29):
                                                            return - \
                                                                671483940756762216
                                                        if (hours_per_week <=
                                                                29):
                                                            return - \
                                                                7811984082516642400
                                                if (education != -
                                                        1620783280160849416):
                                                    return -7811984082516642400
                                            if (occupation !=
                                                    2812191937831880778):
                                                if (occupation == -
                                                        5484833051640498835):
                                                    if (marital_status == -
                                                            5485661916787442206):
                                                        if (
                                                                final_weight is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight >
                                                                171202):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight <=
                                                                171202):
                                                            if (
                                                                    hours_per_week >
                                                                    32):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                    hours_per_week <=
                                                                    32):
                                                                return - \
                                                                    7811984082516642400
                                                    if (marital_status != -
                                                            5485661916787442206):
                                                        return - \
                                                            7811984082516642400
                                                if (occupation != -
                                                        5484833051640498835):
                                                    if (education_num > 3):
                                                        if (race is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (race ==
                                                                3939476748445039507):
                                                            return - \
                                                                671483940756762216
                                                        if (race !=
                                                                3939476748445039507):
                                                            if (occupation == -
                                                                    6951104699562914960):
                                                                return - \
                                                                    7811984082516642400
                                                            if (occupation != -
                                                                    6951104699562914960):
                                                                return - \
                                                                    7811984082516642400
                                                    if (education_num <= 3):
                                                        return - \
                                                            7811984082516642400
                            if (relationship != 5722155880036500383):
                                if (occupation == 1581590029918088140):
                                    if (workclass is None):
                                        return -7811984082516642400
                                    if (workclass == 8161495398349361779):
                                        if (final_weight is None):
                                            return -7811984082516642400
                                        if (final_weight > 94417):
                                            return -671483940756762216
                                        if (final_weight <= 94417):
                                            return -7811984082516642400
                                    if (workclass != 8161495398349361779):
                                        if (final_weight is None):
                                            return -7811984082516642400
                                        if (final_weight > 338432):
                                            return -671483940756762216
                                        if (final_weight <= 338432):
                                            if (final_weight > 175915):
                                                return -7811984082516642400
                                            if (final_weight <= 175915):
                                                if (final_weight > 175017):
                                                    return -671483940756762216
                                                if (final_weight <= 175017):
                                                    if (age > 46):
                                                        if (education is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (education == -
                                                                1620783280160849416):
                                                            return - \
                                                                7811984082516642400
                                                        if (education != -
                                                                1620783280160849416):
                                                            if (
                                                                    hours_per_week >
                                                                    35):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                    hours_per_week <=
                                                                    35):
                                                                return - \
                                                                    7811984082516642400
                                                    if (age <= 46):
                                                        return - \
                                                            7811984082516642400
                                if (occupation != 1581590029918088140):
                                    if (relationship == -7487827120114232249):
                                        if (education_num > 11):
                                            return -7811984082516642400
                                        if (education_num <= 11):
                                            return -671483940756762216
                                    if (relationship != -7487827120114232249):
                                        if (marital_status ==
                                                7568786824864426784):
                                            return -7811984082516642400
                                        if (marital_status !=
                                                7568786824864426784):
                                            if (education is None):
                                                return -7811984082516642400
                                            if (education ==
                                                    6401768215868355915):
                                                if (workclass is None):
                                                    return -7811984082516642400
                                                if (workclass ==
                                                        8161495398349361779):
                                                    if (relationship == -
                                                            6190047399745113596):
                                                        return - \
                                                            7811984082516642400
                                                    if (relationship != -
                                                            6190047399745113596):
                                                        return - \
                                                            671483940756762216
                                                if (workclass !=
                                                        8161495398349361779):
                                                    if (relationship == -
                                                            6190047399745113596):
                                                        if (occupation ==
                                                                5332362397248960598):
                                                            if (
                                                                    final_weight is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight >
                                                                    178700):
                                                                return - \
                                                                    7811984082516642400
                                                            if (final_weight <=
                                                                    178700):
                                                                return - \
                                                                    671483940756762216
                                                        if (occupation !=
                                                                5332362397248960598):
                                                            return - \
                                                                7811984082516642400
                                                    if (relationship != -
                                                            6190047399745113596):
                                                        return - \
                                                            7811984082516642400
                                            if (education !=
                                                    6401768215868355915):
                                                if (occupation ==
                                                        5332362397248960598):
                                                    if (final_weight is None):
                                                        return - \
                                                            7811984082516642400
                                                    if (final_weight > 157742):
                                                        return - \
                                                            7811984082516642400
                                                    if (final_weight <=
                                                            157742):
                                                        if (final_weight >
                                                                119355):
                                                            if (age > 43):
                                                                return - \
                                                                    7811984082516642400
                                                            if (age <= 43):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                119355):
                                                            return - \
                                                                7811984082516642400
                                                if (occupation !=
                                                        5332362397248960598):
                                                    if (age > 45):
                                                        if (
                                                                final_weight is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight >
                                                                322450):
                                                            if (
                                                                marital_status == -
                                                                    2843050270188924016):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                marital_status != -
                                                                    2843050270188924016):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                322450):
                                                            if (age > 48):
                                                                return - \
                                                                    7811984082516642400
                                                            if (age <= 48):
                                                                return - \
                                                                    7811984082516642400
                                                    if (age <= 45):
                                                        if (hours_per_week >
                                                                39):
                                                            if (
                                                                marital_status == -
                                                                    1035125786006291861):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                marital_status != -
                                                                    1035125786006291861):
                                                                return - \
                                                                    7811984082516642400
                                                        if (hours_per_week <=
                                                                39):
                                                            return - \
                                                                7811984082516642400
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
                                    if (marital_status == -
                                            2843050270188924016):
                                        if (hours_per_week > 62):
                                            return -671483940756762216
                                        if (hours_per_week <= 62):
                                            return -7811984082516642400
                                    if (marital_status != -
                                            2843050270188924016):
                                        if (final_weight is None):
                                            return -671483940756762216
                                        if (final_weight > 111019):
                                            return -671483940756762216
                                        if (final_weight <= 111019):
                                            return -7811984082516642400
                                if (occupation != -6990906632015037778):
                                    if (education is None):
                                        return -7811984082516642400
                                    if (education == -8844931991724242570):
                                        if (hours_per_week > 44):
                                            return -7811984082516642400
                                        if (hours_per_week <= 44):
                                            return -671483940756762216
                                    if (education != -8844931991724242570):
                                        if (occupation == 2812191937831880778):
                                            if (hours_per_week > 51):
                                                return -7811984082516642400
                                            if (hours_per_week <= 51):
                                                if (final_weight is None):
                                                    return -7811984082516642400
                                                if (final_weight > 81673):
                                                    if (hours_per_week > 49):
                                                        if (marital_status == -
                                                                2843050270188924016):
                                                            return - \
                                                                671483940756762216
                                                        if (marital_status != -
                                                                2843050270188924016):
                                                            return - \
                                                                7811984082516642400
                                                    if (hours_per_week <= 49):
                                                        return - \
                                                            7811984082516642400
                                                if (final_weight <= 81673):
                                                    return -671483940756762216
                                        if (occupation != 2812191937831880778):
                                            if (race is None):
                                                return -7811984082516642400
                                            if (race == 3632794867504857096):
                                                if (sex is None):
                                                    return -7811984082516642400
                                                if (sex ==
                                                        6306819796163687131):
                                                    return -671483940756762216
                                                if (sex !=
                                                        6306819796163687131):
                                                    return -7811984082516642400
                                            if (race != 3632794867504857096):
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
                                        if (final_weight is None):
                                            return -7811984082516642400
                                        if (final_weight > 378259):
                                            return -671483940756762216
                                        if (final_weight <= 378259):
                                            if (race is None):
                                                return -7811984082516642400
                                            if (race == 3632794867504857096):
                                                return -671483940756762216
                                            if (race != 3632794867504857096):
                                                if (final_weight > 174056):
                                                    if (age > 28):
                                                        if (hours_per_week >
                                                                58):
                                                            if (
                                                                    relationship is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                relationship == -
                                                                    6190047399745113596):
                                                                return - \
                                                                    671483940756762216
                                                            if (
                                                                relationship != -
                                                                    6190047399745113596):
                                                                return - \
                                                                    7811984082516642400
                                                        if (hours_per_week <=
                                                                58):
                                                            return - \
                                                                671483940756762216
                                                    if (age <= 28):
                                                        if (race == -
                                                                1569537633132385766):
                                                            return - \
                                                                7811984082516642400
                                                        if (race != -
                                                                1569537633132385766):
                                                            return - \
                                                                671483940756762216
                                                if (final_weight <= 174056):
                                                    return -7811984082516642400
                                if (hours_per_week <= 49):
                                    if (education_num > 8):
                                        return -7811984082516642400
                                    if (education_num <= 8):
                                        if (race is None):
                                            return -7811984082516642400
                                        if (race == -1569537633132385766):
                                            return -671483940756762216
                                        if (race != -1569537633132385766):
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
                                        if (final_weight is None):
                                            return -7811984082516642400
                                        if (final_weight > 199791):
                                            return -7811984082516642400
                                        if (final_weight <= 199791):
                                            if (relationship == -
                                                    6190047399745113596):
                                                return -671483940756762216
                                            if (relationship != -
                                                    6190047399745113596):
                                                if (final_weight > 95966):
                                                    return -7811984082516642400
                                                if (final_weight <= 95966):
                                                    if (final_weight > 85301):
                                                        return - \
                                                            671483940756762216
                                                    if (final_weight <= 85301):
                                                        return - \
                                                            7811984082516642400
                                    if (occupation != -3959269231467008119):
                                        if (relationship == -
                                                6190047399745113596):
                                            if (age > 29):
                                                if (occupation == -
                                                        8005258492814722552):
                                                    if (education_num > 11):
                                                        return - \
                                                            7811984082516642400
                                                    if (education_num <= 11):
                                                        return - \
                                                            671483940756762216
                                                if (occupation != -
                                                        8005258492814722552):
                                                    return -7811984082516642400
                                            if (age <= 29):
                                                return -7811984082516642400
                                        if (relationship != -
                                                6190047399745113596):
                                            if (age > 30):
                                                return -7811984082516642400
                                            if (age <= 30):
                                                if (education_num > 10):
                                                    if (relationship ==
                                                            5722155880036500383):
                                                        if (
                                                                final_weight is None):
                                                            return - \
                                                                7811984082516642400
                                                        if (final_weight >
                                                                25105):
                                                            if (occupation == -
                                                                    5484833051640498835):
                                                                return - \
                                                                    7811984082516642400
                                                            if (occupation != -
                                                                    5484833051640498835):
                                                                return - \
                                                                    7811984082516642400
                                                        if (final_weight <=
                                                                25105):
                                                            if (
                                                                    hours_per_week >
                                                                    35):
                                                                return - \
                                                                    7811984082516642400
                                                            if (
                                                                    hours_per_week <=
                                                                    35):
                                                                return - \
                                                                    671483940756762216
                                                    if (relationship !=
                                                            5722155880036500383):
                                                        return - \
                                                            7811984082516642400
                                                if (education_num <= 10):
                                                    if (age > 27):
                                                        if (occupation ==
                                                                5332362397248960598):
                                                            return - \
                                                                7811984082516642400
                                                        if (occupation !=
                                                                5332362397248960598):
                                                            if (
                                                                    workclass is None):
                                                                return - \
                                                                    7811984082516642400
                                                            if (workclass ==
                                                                    8161495398349361779):
                                                                return - \
                                                                    671483940756762216
                                                            if (workclass !=
                                                                    8161495398349361779):
                                                                return - \
                                                                    7811984082516642400
                                                    if (age <= 27):
                                                        if (marital_status ==
                                                                7568786824864426784):
                                                            if (occupation ==
                                                                    8618684898378336489):
                                                                return - \
                                                                    7811984082516642400
                                                            if (occupation !=
                                                                    8618684898378336489):
                                                                return - \
                                                                    7811984082516642400
                                                        if (marital_status !=
                                                                7568786824864426784):
                                                            return - \
                                                                7811984082516642400
                            if (hours_per_week <= 29):
                                return -7811984082516642400
                        if (education_num <= 9):
                            if (age > 27):
                                if (final_weight is None):
                                    return -7811984082516642400
                                if (final_weight > 94030):
                                    if (final_weight > 334106):
                                        if (occupation is None):
                                            return -7811984082516642400
                                        if (occupation == -
                                                8005258492814722552):
                                            if (marital_status == -
                                                    2843050270188924016):
                                                if (relationship is None):
                                                    return -7811984082516642400
                                                if (relationship ==
                                                        5722155880036500383):
                                                    return -7811984082516642400
                                                if (relationship !=
                                                        5722155880036500383):
                                                    return -671483940756762216
                                            if (marital_status != -
                                                    2843050270188924016):
                                                return -7811984082516642400
                                        if (occupation != -
                                                8005258492814722552):
                                            return -7811984082516642400
                                    if (final_weight <= 334106):
                                        return -7811984082516642400
                                if (final_weight <= 94030):
                                    if (marital_status == -
                                            8271725530730535226):
                                        if (race is None):
                                            return -7811984082516642400
                                        if (race == -681598405395175136):
                                            return -671483940756762216
                                        if (race != -681598405395175136):
                                            if (occupation is None):
                                                return -7811984082516642400
                                            if (occupation ==
                                                    8618684898378336489):
                                                return -671483940756762216
                                            if (occupation !=
                                                    8618684898378336489):
                                                return -7811984082516642400
                                    if (marital_status != -
                                            8271725530730535226):
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
