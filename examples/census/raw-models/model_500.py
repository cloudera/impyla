def predict_income(data={}):
    """ Predictor for income from model/5360311dffa04466f60007dc

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
                            if (data['education_num'] > 14):
				if (not 'workclass' in data or data['workclass'] is None):
                                    return u'>50K'
                                if (data['workclass'] == 'Local-gov'):
                                    return u'<=50K'
                                if (data['workclass'] != 'Local-gov'):
				    if (not 'occupation' in data or data['occupation'] is None):
                                        return u'>50K'
                                    if (data['occupation'] == 'Sales'):
                                        return u'<=50K'
                                    if (data['occupation'] != 'Sales'):
                                        return u'>50K'
                            if (data['education_num'] <= 14):
                                if (data['hours_per_week'] > 36):
				    if (not 'workclass' in data or data['workclass'] is None):
                                        return u'>50K'
                                    if (data['workclass'] == 'Self-emp-inc'):
                                        return u'>50K'
                                    if (data['workclass'] != 'Self-emp-inc'):
                                        return u'>50K'
                                if (data['hours_per_week'] <= 36):
                                    return u'<=50K'
                        if (data['age'] <= 58):
                            if (data['age'] > 38):
                                if (data['education_num'] > 14):
                                    if (data['hours_per_week'] > 49):
                                        return u'>50K'
                                    if (data['hours_per_week'] <= 49):
                                        return u'>50K'
                                if (data['education_num'] <= 14):
				    if (not 'workclass' in data or data['workclass'] is None):
                                        return u'>50K'
				    if (data['workclass'] == 'Self-emp-not-inc'):
                                        return u'>50K'
				    if (data['workclass'] != 'Self-emp-not-inc'):
                                        return u'>50K'
                            if (data['age'] <= 38):
				if (not 'occupation' in data or data['occupation'] is None):
                                    return u'>50K'
                                if (data['occupation'] == 'Farming-fishing'):
                                    return u'<=50K'
                                if (data['occupation'] != 'Farming-fishing'):
                                    if (data['hours_per_week'] > 42):
                                        return u'>50K'
                                    if (data['hours_per_week'] <= 42):
                                        return u'>50K'
                    if (data['education_num'] <= 13):
			if (not 'occupation' in data or data['occupation'] is None):
                            return u'>50K'
                        if (data['occupation'] == 'Exec-managerial'):
			    if (not 'workclass' in data or data['workclass'] is None):
                                return u'>50K'
                            if (data['workclass'] == 'Self-emp-not-inc'):
				if (not 'final_weight' in data or data['final_weight'] is None):
                                    return u'>50K'
                                if (data['final_weight'] > 90244):
                                    if (data['age'] > 48):
                                        return u'>50K'
                                    if (data['age'] <= 48):
                                        return u'<=50K'
                                if (data['final_weight'] <= 90244):
                                    return u'<=50K'
                            if (data['workclass'] != 'Self-emp-not-inc'):
                                if (data['hours_per_week'] > 67):
                                    if (data['hours_per_week'] > 73):
                                        return u'>50K'
                                    if (data['hours_per_week'] <= 73):
                                        return u'<=50K'
                                if (data['hours_per_week'] <= 67):
				    if (not 'race' in data or data['race'] is None):
                                        return u'>50K'
                                    if (data['race'] == 'Other'):
                                        return u'<=50K'
                                    if (data['race'] != 'Other'):
                                        return u'>50K'
                        if (data['occupation'] != 'Exec-managerial'):
			    if (not 'relationship' in data or data['relationship'] is None):
                                return u'>50K'
                            if (data['relationship'] == 'Other-relative'):
                                return u'<=50K'
                            if (data['relationship'] != 'Other-relative'):
				if (not 'race' in data or data['race'] is None):
                                    return u'>50K'
                                if (data['race'] == 'Other'):
                                    return u'<=50K'
                                if (data['race'] != 'Other'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
                                        return u'>50K'
                                    if (data['final_weight'] > 121061):
                                        return u'>50K'
                                    if (data['final_weight'] <= 121061):
                                        return u'>50K'
                if (data['age'] <= 28):
                    if (data['age'] > 24):
			if (not 'occupation' in data or data['occupation'] is None):
                            return u'<=50K'
                        if (data['occupation'] == 'Tech-support'):
                            return u'>50K'
                        if (data['occupation'] != 'Tech-support'):
                            if (data['hours_per_week'] > 41):
                                if (data['hours_per_week'] > 46):
                                    if (data['education_num'] > 14):
                                        return u'<=50K'
                                    if (data['education_num'] <= 14):
                                        return u'<=50K'
                                if (data['hours_per_week'] <= 46):
                                    if (data['occupation'] == 'Adm-clerical'):
                                        return u'<=50K'
                                    if (data['occupation'] != 'Adm-clerical'):
                                        return u'>50K'
                            if (data['hours_per_week'] <= 41):
				if (not 'final_weight' in data or data['final_weight'] is None):
                                    return u'<=50K'
                                if (data['final_weight'] > 159383):
                                    if (data['final_weight'] > 260996):
                                        return u'>50K'
                                    if (data['final_weight'] <= 260996):
                                        return u'<=50K'
                                if (data['final_weight'] <= 159383):
                                    if (data['final_weight'] > 100631):
                                        return u'>50K'
                                    if (data['final_weight'] <= 100631):
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
                            if (data['age'] > 78):
                                if (data['hours_per_week'] > 9):
                                    return u'>50K'
                                if (data['hours_per_week'] <= 9):
                                    return u'<=50K'
                            if (data['age'] <= 78):
                                if (data['hours_per_week'] > 13):
				    if (not 'race' in data or data['race'] is None):
                                        return u'<=50K'
                                    if (data['race'] == 'White'):
                                        return u'<=50K'
                                    if (data['race'] != 'White'):
                                        return u'>50K'
                                if (data['hours_per_week'] <= 13):
				    if (not 'occupation' in data or data['occupation'] is None):
                                        return u'<=50K'
				    if (data['occupation'] == 'Exec-managerial'):
                                        return u'>50K'
				    if (data['occupation'] != 'Exec-managerial'):
                                        return u'<=50K'
                        if (data['age'] <= 62):
                            if (data['hours_per_week'] > 12):
				if (not 'workclass' in data or data['workclass'] is None):
                                    return u'>50K'
                                if (data['workclass'] == 'State-gov'):
                                    return u'<=50K'
                                if (data['workclass'] != 'State-gov'):
                                    if (data['hours_per_week'] > 21):
                                        return u'<=50K'
                                    if (data['hours_per_week'] <= 21):
                                        return u'>50K'
                            if (data['hours_per_week'] <= 12):
                                if (data['hours_per_week'] > 2):
                                    if (data['education_num'] > 14):
                                        return u'<=50K'
                                    if (data['education_num'] <= 14):
                                        return u'<=50K'
                                if (data['hours_per_week'] <= 2):
                                    return u'>50K'
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
			    if (not 'workclass' in data or data['workclass'] is None):
                                return u'>50K'
                            if (data['workclass'] == 'Self-emp-not-inc'):
                                if (data['hours_per_week'] > 26):
                                    return u'>50K'
                                if (data['hours_per_week'] <= 26):
                                    return u'<=50K'
                            if (data['workclass'] != 'Self-emp-not-inc'):
                                if (data['final_weight'] > 36352):
				    if (not 'occupation' in data or data['occupation'] is None):
                                        return u'>50K'
                                    if (data['occupation'] == 'Other-service'):
                                        return u'<=50K'
                                    if (data['occupation'] != 'Other-service'):
                                        return u'>50K'
                                if (data['final_weight'] <= 36352):
                                    return u'<=50K'
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
			    if (not 'occupation' in data or data['occupation'] is None):
                                return u'>50K'
                            if (data['occupation'] == 'Farming-fishing'):
                                if (data['hours_per_week'] > 71):
                                    return u'<=50K'
                                if (data['hours_per_week'] <= 71):
				    if (not 'final_weight' in data or data['final_weight'] is None):
                                        return u'<=50K'
                                    if (data['final_weight'] > 182378):
                                        return u'<=50K'
                                    if (data['final_weight'] <= 182378):
                                        return u'<=50K'
                            if (data['occupation'] != 'Farming-fishing'):
                                if (data['occupation'] == 'Other-service'):
                                    if (data['age'] > 40):
                                        return u'<=50K'
                                    if (data['age'] <= 40):
                                        return u'<=50K'
                                if (data['occupation'] != 'Other-service'):
				    if (data['occupation'] == 'Exec-managerial'):
                                        return u'>50K'
				    if (data['occupation'] != 'Exec-managerial'):
                                        return u'>50K'
                        if (data['education_num'] <= 9):
			    if (not 'occupation' in data or data['occupation'] is None):
                                return u'<=50K'
                            if (data['occupation'] == 'Exec-managerial'):
				if (not 'workclass' in data or data['workclass'] is None):
                                    return u'>50K'
                                if (data['workclass'] == 'Self-emp-not-inc'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
                                        return u'<=50K'
                                    if (data['final_weight'] > 92214):
                                        return u'<=50K'
                                    if (data['final_weight'] <= 92214):
                                        return u'>50K'
                                if (data['workclass'] != 'Self-emp-not-inc'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
                                        return u'>50K'
                                    if (data['final_weight'] > 189527):
                                        return u'>50K'
                                    if (data['final_weight'] <= 189527):
                                        return u'>50K'
                            if (data['occupation'] != 'Exec-managerial'):
                                if (data['occupation'] == 'Other-service'):
				    if (not 'sex' in data or data['sex'] is None):
                                        return u'<=50K'
                                    if (data['sex'] == 'Male'):
                                        return u'<=50K'
                                    if (data['sex'] != 'Male'):
                                        return u'<=50K'
                                if (data['occupation'] != 'Other-service'):
				    if (data['occupation'] == 'Farming-fishing'):
                                        return u'<=50K'
				    if (data['occupation'] != 'Farming-fishing'):
                                        return u'<=50K'
                    if (data['hours_per_week'] <= 33):
			if (not 'workclass' in data or data['workclass'] is None):
                            return u'<=50K'
                        if (data['workclass'] == 'Self-emp-inc'):
                            if (data['age'] > 54):
				if (not 'final_weight' in data or data['final_weight'] is None):
                                    return u'>50K'
                                if (data['final_weight'] > 181769):
                                    if (data['hours_per_week'] > 27):
                                        return u'>50K'
                                    if (data['hours_per_week'] <= 27):
                                        return u'>50K'
                                if (data['final_weight'] <= 181769):
				    if (not 'sex' in data or data['sex'] is None):
                                        return u'<=50K'
                                    if (data['sex'] == 'Male'):
                                        return u'<=50K'
                                    if (data['sex'] != 'Male'):
                                        return u'>50K'
                            if (data['age'] <= 54):
                                return u'<=50K'
                        if (data['workclass'] != 'Self-emp-inc'):
			    if (not 'relationship' in data or data['relationship'] is None):
                                return u'<=50K'
                            if (data['relationship'] == 'Wife'):
                                if (data['age'] > 59):
                                    return u'<=50K'
                                if (data['age'] <= 59):
                                    if (data['education_num'] > 9):
                                        return u'>50K'
                                    if (data['education_num'] <= 9):
                                        return u'<=50K'
                            if (data['relationship'] != 'Wife'):
				if (not 'occupation' in data or data['occupation'] is None):
                                    return u'<=50K'
                                if (data['occupation'] == 'Tech-support'):
				    if (data['workclass'] == 'Self-emp-not-inc'):
                                        return u'<=50K'
				    if (data['workclass'] != 'Self-emp-not-inc'):
                                        return u'>50K'
                                if (data['occupation'] != 'Tech-support'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
                                        return u'<=50K'
                                    if (data['final_weight'] > 286449):
                                        return u'<=50K'
                                    if (data['final_weight'] <= 286449):
                                        return u'<=50K'
                if (data['age'] <= 35):
                    if (data['age'] > 24):
			if (not 'occupation' in data or data['occupation'] is None):
                            return u'<=50K'
                        if (data['occupation'] == 'Exec-managerial'):
                            if (data['age'] > 27):
				if (not 'workclass' in data or data['workclass'] is None):
                                    return u'<=50K'
                                if (data['workclass'] == 'Self-emp-not-inc'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
                                        return u'<=50K'
                                    if (data['final_weight'] > 237985):
                                        return u'<=50K'
                                    if (data['final_weight'] <= 237985):
                                        return u'<=50K'
                                if (data['workclass'] != 'Self-emp-not-inc'):
                                    if (data['age'] > 32):
                                        return u'>50K'
                                    if (data['age'] <= 32):
                                        return u'<=50K'
                            if (data['age'] <= 27):
				if (not 'final_weight' in data or data['final_weight'] is None):
                                    return u'<=50K'
                                if (data['final_weight'] > 162313):
                                    if (data['final_weight'] > 190463):
                                        return u'<=50K'
                                    if (data['final_weight'] <= 190463):
                                        return u'>50K'
                                if (data['final_weight'] <= 162313):
                                    return u'<=50K'
                        if (data['occupation'] != 'Exec-managerial'):
                            if (data['occupation'] == 'Farming-fishing'):
                                if (data['education_num'] > 10):
				    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
                                        return u'<=50K'
                                    if (data['hours_per_week'] > 57):
                                        return u'<=50K'
                                    if (data['hours_per_week'] <= 57):
                                        return u'<=50K'
                                if (data['education_num'] <= 10):
                                    return u'<=50K'
                            if (data['occupation'] != 'Farming-fishing'):
				if (not 'hours_per_week' in data or data['hours_per_week'] is None):
                                    return u'<=50K'
                                if (data['hours_per_week'] > 46):
                                    if (data['age'] > 31):
                                        return u'<=50K'
                                    if (data['age'] <= 31):
                                        return u'<=50K'
                                if (data['hours_per_week'] <= 46):
				    if (data['occupation'] == 'Prof-specialty'):
                                        return u'<=50K'
				    if (data['occupation'] != 'Prof-specialty'):
                                        return u'<=50K'
                    if (data['age'] <= 24):
			if (not 'hours_per_week' in data or data['hours_per_week'] is None):
                            return u'<=50K'
                        if (data['hours_per_week'] > 45):
			    if (not 'final_weight' in data or data['final_weight'] is None):
                                return u'<=50K'
                            if (data['final_weight'] > 79991):
				if (not 'race' in data or data['race'] is None):
                                    return u'<=50K'
                                if (data['race'] == 'Amer-Indian-Eskimo'):
                                    return u'>50K'
                                if (data['race'] != 'Amer-Indian-Eskimo'):
				    if (not 'workclass' in data or data['workclass'] is None):
                                        return u'<=50K'
                                    if (data['workclass'] == 'State-gov'):
                                        return u'>50K'
                                    if (data['workclass'] != 'State-gov'):
                                        return u'<=50K'
                            if (data['final_weight'] <= 79991):
                                if (data['education_num'] > 9):
                                    return u'>50K'
                                if (data['education_num'] <= 9):
                                    return u'<=50K'
                        if (data['hours_per_week'] <= 45):
			    if (not 'occupation' in data or data['occupation'] is None):
                                return u'<=50K'
                            if (data['occupation'] == 'Prof-specialty'):
                                if (data['hours_per_week'] > 38):
                                    return u'>50K'
                                if (data['hours_per_week'] <= 38):
                                    return u'<=50K'
                            if (data['occupation'] != 'Prof-specialty'):
                                if (data['occupation'] == 'Adm-clerical'):
				    if (not 'sex' in data or data['sex'] is None):
                                        return u'<=50K'
                                    if (data['sex'] == 'Male'):
                                        return u'<=50K'
                                    if (data['sex'] != 'Male'):
                                        return u'<=50K'
                                if (data['occupation'] != 'Adm-clerical'):
				    if (data['occupation'] == 'Handlers-cleaners'):
                                        return u'<=50K'
				    if (data['occupation'] != 'Handlers-cleaners'):
                                        return u'<=50K'
            if (data['education_num'] <= 8):
                if (not 'age' in data or data['age'] is None):
                    return u'<=50K'
                if (data['age'] > 36):
		    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
                        return u'<=50K'
                    if (data['hours_per_week'] > 22):
                        if (data['education_num'] > 5):
                            if (data['age'] > 53):
				if (not 'occupation' in data or data['occupation'] is None):
                                    return u'<=50K'
                                if (data['occupation'] == 'Transport-moving'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
                                        return u'<=50K'
                                    if (data['final_weight'] > 89485):
                                        return u'<=50K'
                                    if (data['final_weight'] <= 89485):
                                        return u'<=50K'
                                if (data['occupation'] != 'Transport-moving'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
                                        return u'<=50K'
                                    if (data['final_weight'] > 162184):
                                        return u'<=50K'
                                    if (data['final_weight'] <= 162184):
                                        return u'<=50K'
                            if (data['age'] <= 53):
				if (not 'occupation' in data or data['occupation'] is None):
                                    return u'<=50K'
                                if (data['occupation'] == 'Sales'):
                                    if (data['hours_per_week'] > 52):
                                        return u'<=50K'
                                    if (data['hours_per_week'] <= 52):
                                        return u'>50K'
                                if (data['occupation'] != 'Sales'):
				    if (not 'workclass' in data or data['workclass'] is None):
                                        return u'<=50K'
                                    if (data['workclass'] == 'Local-gov'):
                                        return u'<=50K'
                                    if (data['workclass'] != 'Local-gov'):
                                        return u'<=50K'
                        if (data['education_num'] <= 5):
			    if (not 'workclass' in data or data['workclass'] is None):
                                return u'<=50K'
                            if (data['workclass'] == 'Private'):
				if (not 'occupation' in data or data['occupation'] is None):
                                    return u'<=50K'
                                if (data['occupation'] == 'Exec-managerial'):
                                    if (data['hours_per_week'] > 46):
                                        return u'<=50K'
                                    if (data['hours_per_week'] <= 46):
                                        return u'>50K'
                                if (data['occupation'] != 'Exec-managerial'):
                                    if (data['occupation'] == 'Sales'):
                                        return u'<=50K'
                                    if (data['occupation'] != 'Sales'):
                                        return u'<=50K'
                            if (data['workclass'] != 'Private'):
                                if (data['hours_per_week'] > 55):
				    if (data['workclass'] == 'Self-emp-not-inc'):
                                        return u'>50K'
				    if (data['workclass'] != 'Self-emp-not-inc'):
                                        return u'<=50K'
                                if (data['hours_per_week'] <= 55):
                                    if (data['workclass'] == 'Self-emp-inc'):
                                        return u'>50K'
                                    if (data['workclass'] != 'Self-emp-inc'):
                                        return u'<=50K'
                    if (data['hours_per_week'] <= 22):
                        return u'<=50K'
                if (data['age'] <= 36):
                    if (not 'workclass' in data or data['workclass'] is None):
                        return u'<=50K'
                    if (data['workclass'] == 'Private'):
                        if (data['age'] > 35):
			    if (not 'occupation' in data or data['occupation'] is None):
                                return u'<=50K'
                            if (data['occupation'] == 'Sales'):
                                return u'>50K'
                            if (data['occupation'] != 'Sales'):
                                if (data['education_num'] > 3):
				    if (not 'final_weight' in data or data['final_weight'] is None):
                                        return u'<=50K'
                                    if (data['final_weight'] > 185266):
                                        return u'<=50K'
                                    if (data['final_weight'] <= 185266):
                                        return u'<=50K'
                                if (data['education_num'] <= 3):
                                    return u'>50K'
                        if (data['age'] <= 35):
			    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
                                return u'<=50K'
                            if (data['hours_per_week'] > 67):
                                if (data['hours_per_week'] > 83):
                                    return u'<=50K'
                                if (data['hours_per_week'] <= 83):
                                    return u'>50K'
                            if (data['hours_per_week'] <= 67):
				if (not 'occupation' in data or data['occupation'] is None):
                                    return u'<=50K'
                                if (data['occupation'] == 'Adm-clerical'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
                                        return u'<=50K'
                                    if (data['final_weight'] > 219946):
                                        return u'<=50K'
                                    if (data['final_weight'] <= 219946):
                                        return u'<=50K'
                                if (data['occupation'] != 'Adm-clerical'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
                                        return u'<=50K'
                                    if (data['final_weight'] > 145325):
                                        return u'<=50K'
                                    if (data['final_weight'] <= 145325):
                                        return u'<=50K'
                    if (data['workclass'] != 'Private'):
			if (not 'occupation' in data or data['occupation'] is None):
                            return u'<=50K'
                        if (data['occupation'] == 'Machine-op-inspct'):
                            return u'>50K'
                        if (data['occupation'] != 'Machine-op-inspct'):
                            if (data['age'] > 29):
                                return u'<=50K'
                            if (data['age'] <= 29):
				if (not 'relationship' in data or data['relationship'] is None):
                                    return u'<=50K'
                                if (data['relationship'] == 'Husband'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
                                        return u'<=50K'
                                    if (data['final_weight'] > 149463):
                                        return u'<=50K'
                                    if (data['final_weight'] <= 149463):
                                        return u'<=50K'
                                if (data['relationship'] != 'Husband'):
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
			    if (not 'final_weight' in data or data['final_weight'] is None):
                                return u'>50K'
                            if (data['final_weight'] > 160393):
                                if (data['hours_per_week'] > 58):
                                    if (data['education_num'] > 13):
                                        return u'>50K'
                                    if (data['education_num'] <= 13):
                                        return u'<=50K'
                                if (data['hours_per_week'] <= 58):
				    if (not 'race' in data or data['race'] is None):
                                        return u'>50K'
                                    if (data['race'] == 'Amer-Indian-Eskimo'):
                                        return u'<=50K'
                                    if (data['race'] != 'Amer-Indian-Eskimo'):
                                        return u'>50K'
                            if (data['final_weight'] <= 160393):
                                if (data['hours_per_week'] > 47):
                                    if (data['final_weight'] > 51818):
                                        return u'>50K'
                                    if (data['final_weight'] <= 51818):
                                        return u'>50K'
                                if (data['hours_per_week'] <= 47):
                                    if (data['age'] > 49):
                                        return u'>50K'
                                    if (data['age'] <= 49):
                                        return u'<=50K'
                        if (data['age'] <= 41):
			    if (not 'final_weight' in data or data['final_weight'] is None):
                                return u'<=50K'
                            if (data['final_weight'] > 307855):
                                return u'<=50K'
                            if (data['final_weight'] <= 307855):
				if (not 'workclass' in data or data['workclass'] is None):
                                    return u'<=50K'
                                if (data['workclass'] == 'Self-emp-not-inc'):
                                    return u'<=50K'
                                if (data['workclass'] != 'Self-emp-not-inc'):
                                    if (data['marital_status'] == 'Separated'):
                                        return u'>50K'
                                    if (data['marital_status'] != 'Separated'):
                                        return u'>50K'
                    if (data['occupation'] != 'Exec-managerial'):
                        if (data['education_num'] > 14):
                            if (data['age'] > 32):
                                if (data['age'] > 52):
                                    if (data['marital_status'] == 'Widowed'):
                                        return u'>50K'
                                    if (data['marital_status'] != 'Widowed'):
                                        return u'<=50K'
                                if (data['age'] <= 52):
                                    if (data['hours_per_week'] > 52):
                                        return u'>50K'
                                    if (data['hours_per_week'] <= 52):
                                        return u'>50K'
                            if (data['age'] <= 32):
                                if (data['age'] > 29):
                                    return u'<=50K'
                                if (data['age'] <= 29):
				    if (data['marital_status'] == 'Never-married'):
                                        return u'<=50K'
				    if (data['marital_status'] != 'Never-married'):
                                        return u'>50K'
                        if (data['education_num'] <= 14):
                            if (not 'sex' in data or data['sex'] is None):
                                return u'<=50K'
                            if (data['sex'] == 'Male'):
                                if (data['hours_per_week'] > 55):
                                    if (data['occupation'] == 'Sales'):
                                        return u'<=50K'
                                    if (data['occupation'] != 'Sales'):
                                        return u'<=50K'
                                if (data['hours_per_week'] <= 55):
				    if (not 'workclass' in data or data['workclass'] is None):
                                        return u'<=50K'
                                    if (data['workclass'] == 'State-gov'):
                                        return u'<=50K'
                                    if (data['workclass'] != 'State-gov'):
                                        return u'<=50K'
                            if (data['sex'] != 'Male'):
				if (not 'final_weight' in data or data['final_weight'] is None):
                                    return u'<=50K'
                                if (data['final_weight'] > 151124):
                                    if (data['final_weight'] > 158605):
                                        return u'<=50K'
                                    if (data['final_weight'] <= 158605):
                                        return u'>50K'
                                if (data['final_weight'] <= 151124):
				    if (not 'workclass' in data or data['workclass'] is None):
                                        return u'<=50K'
                                    if (data['workclass'] == 'Federal-gov'):
                                        return u'>50K'
                                    if (data['workclass'] != 'Federal-gov'):
                                        return u'<=50K'
                if (data['hours_per_week'] <= 43):
                    if (data['education_num'] > 14):
                        if (data['age'] > 32):
                            if (not 'sex' in data or data['sex'] is None):
                                return u'>50K'
                            if (data['sex'] == 'Male'):
                                if (data['hours_per_week'] > 21):
				    if (not 'final_weight' in data or data['final_weight'] is None):
                                        return u'>50K'
                                    if (data['final_weight'] > 107803):
                                        return u'>50K'
                                    if (data['final_weight'] <= 107803):
                                        return u'>50K'
                                if (data['hours_per_week'] <= 21):
                                    if (data['marital_status'] == 'Widowed'):
                                        return u'>50K'
                                    if (data['marital_status'] != 'Widowed'):
                                        return u'<=50K'
                            if (data['sex'] != 'Male'):
                                if (data['marital_status'] == 'Never-married'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
                                        return u'>50K'
                                    if (data['final_weight'] > 386027):
                                        return u'<=50K'
                                    if (data['final_weight'] <= 386027):
                                        return u'>50K'
                                if (data['marital_status'] != 'Never-married'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
                                        return u'<=50K'
                                    if (data['final_weight'] > 170081):
                                        return u'<=50K'
                                    if (data['final_weight'] <= 170081):
                                        return u'<=50K'
                        if (data['age'] <= 32):
                            return u'<=50K'
                    if (data['education_num'] <= 14):
                        if (data['age'] > 45):
                            if (data['hours_per_week'] > 31):
				if (not 'relationship' in data or data['relationship'] is None):
                                    return u'<=50K'
                                if (data['relationship'] == 'Not-in-family'):
				    if (not 'workclass' in data or data['workclass'] is None):
                                        return u'<=50K'
                                    if (data['workclass'] == 'Federal-gov'):
                                        return u'<=50K'
                                    if (data['workclass'] != 'Federal-gov'):
                                        return u'<=50K'
                                if (data['relationship'] != 'Not-in-family'):
                                    if (data['age'] > 49):
                                        return u'<=50K'
                                    if (data['age'] <= 49):
                                        return u'<=50K'
                            if (data['hours_per_week'] <= 31):
                                if (data['marital_status'] == 'Divorced'):
                                    return u'<=50K'
                                if (data['marital_status'] != 'Divorced'):
				    if (not 'occupation' in data or data['occupation'] is None):
                                        return u'<=50K'
                                    if (data['occupation'] == 'Craft-repair'):
                                        return u'>50K'
                                    if (data['occupation'] != 'Craft-repair'):
                                        return u'<=50K'
                        if (data['age'] <= 45):
                            if (data['hours_per_week'] > 34):
				if (not 'workclass' in data or data['workclass'] is None):
                                    return u'<=50K'
                                if (data['workclass'] == 'State-gov'):
                                    return u'<=50K'
                                if (data['workclass'] != 'State-gov'):
                                    if (data['workclass'] == 'Federal-gov'):
                                        return u'<=50K'
                                    if (data['workclass'] != 'Federal-gov'):
                                        return u'<=50K'
                            if (data['hours_per_week'] <= 34):
				if (not 'final_weight' in data or data['final_weight'] is None):
                                    return u'<=50K'
                                if (data['final_weight'] > 391238):
                                    return u'>50K'
                                if (data['final_weight'] <= 391238):
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
			    if (not 'final_weight' in data or data['final_weight'] is None):
                                return u'<=50K'
                            if (data['final_weight'] > 156075):
                                return u'>50K'
                            if (data['final_weight'] <= 156075):
                                return u'<=50K'
                        if (data['hours_per_week'] <= 77):
                            if (not 'race' in data or data['race'] is None):
                                return u'<=50K'
                            if (data['race'] == 'Amer-Indian-Eskimo'):
                                if (data['hours_per_week'] > 41):
                                    return u'<=50K'
                                if (data['hours_per_week'] <= 41):
                                    return u'>50K'
                            if (data['race'] != 'Amer-Indian-Eskimo'):
				if (not 'workclass' in data or data['workclass'] is None):
                                    return u'<=50K'
                                if (data['workclass'] == 'Self-emp-not-inc'):
				    if (data['relationship'] == 'Not-in-family'):
                                        return u'<=50K'
				    if (data['relationship'] != 'Not-in-family'):
                                        return u'>50K'
                                if (data['workclass'] != 'Self-emp-not-inc'):
                                    if (data['workclass'] == 'Private'):
                                        return u'<=50K'
                                    if (data['workclass'] != 'Private'):
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
			    if (not 'occupation' in data or data['occupation'] is None):
                                return u'<=50K'
                            if (data['occupation'] == 'Adm-clerical'):
                                return u'<=50K'
                            if (data['occupation'] != 'Adm-clerical'):
                                if (data['hours_per_week'] > 67):
                                    return u'<=50K'
                                if (data['hours_per_week'] <= 67):
                                    if (data['marital_status'] == 'Separated'):
                                        return u'>50K'
                                    if (data['marital_status'] != 'Separated'):
                                        return u'<=50K'
                        if (data['age'] <= 53):
			    if (not 'relationship' in data or data['relationship'] is None):
                                return u'<=50K'
                            if (data['relationship'] == 'Not-in-family'):
				if (not 'education' in data or data['education'] is None):
                                    return u'<=50K'
                                if (data['education'] == 'HS-grad'):
                                    if (data['hours_per_week'] > 47):
                                        return u'<=50K'
                                    if (data['hours_per_week'] <= 47):
                                        return u'<=50K'
                                if (data['education'] != 'HS-grad'):
				    if (not 'workclass' in data or data['workclass'] is None):
                                        return u'<=50K'
				    if (data['workclass'] == 'Self-emp-not-inc'):
                                        return u'<=50K'
				    if (data['workclass'] != 'Self-emp-not-inc'):
                                        return u'<=50K'
                            if (data['relationship'] != 'Not-in-family'):
                                if (data['age'] > 39):
                                    if (data['age'] > 45):
                                        return u'<=50K'
                                    if (data['age'] <= 45):
                                        return u'<=50K'
                                if (data['age'] <= 39):
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
                            if (data['hours_per_week'] > 32):
                                return u'>50K'
                            if (data['hours_per_week'] <= 32):
                                return u'<=50K'
                        if (data['relationship'] != 'Wife'):
                            if (data['age'] > 59):
				if (not 'workclass' in data or data['workclass'] is None):
                                    return u'<=50K'
                                if (data['workclass'] == 'Private'):
                                    return u'<=50K'
                                if (data['workclass'] != 'Private'):
				    if (not 'education' in data or data['education'] is None):
                                        return u'<=50K'
                                    if (data['education'] == 'Some-college'):
                                        return u'>50K'
                                    if (data['education'] != 'Some-college'):
                                        return u'<=50K'
                            if (data['age'] <= 59):
                                return u'<=50K'
                    if (data['occupation'] != 'Other-service'):
                        if (data['occupation'] == 'Machine-op-inspct'):
			    if (not 'relationship' in data or data['relationship'] is None):
                                return u'<=50K'
                            if (data['relationship'] == 'Unmarried'):
                                if (not 'sex' in data or data['sex'] is None):
                                    return u'<=50K'
                                if (data['sex'] == 'Male'):
                                    if (data['age'] > 37):
                                        return u'<=50K'
                                    if (data['age'] <= 37):
                                        return u'<=50K'
                                if (data['sex'] != 'Male'):
                                    return u'<=50K'
                            if (data['relationship'] != 'Unmarried'):
                                return u'<=50K'
                        if (data['occupation'] != 'Machine-op-inspct'):
			    if (not 'relationship' in data or data['relationship'] is None):
                                return u'<=50K'
                            if (data['relationship'] == 'Not-in-family'):
                                if (data['occupation'] == 'Adm-clerical'):
				    if (data['marital_status'] == 'Married-spouse-absent'):
                                        return u'<=50K'
				    if (data['marital_status'] != 'Married-spouse-absent'):
                                        return u'<=50K'
                                if (data['occupation'] != 'Adm-clerical'):
				    if (not 'workclass' in data or data['workclass'] is None):
                                        return u'<=50K'
                                    if (data['workclass'] == 'Self-emp-inc'):
                                        return u'<=50K'
                                    if (data['workclass'] != 'Self-emp-inc'):
                                        return u'<=50K'
                            if (data['relationship'] != 'Not-in-family'):
                                if (data['occupation'] == 'Prof-specialty'):
				    if (not 'workclass' in data or data['workclass'] is None):
                                        return u'<=50K'
                                    if (data['workclass'] == 'Federal-gov'):
                                        return u'<=50K'
                                    if (data['workclass'] != 'Federal-gov'):
                                        return u'<=50K'
                                if (data['occupation'] != 'Prof-specialty'):
                                    if (data['relationship'] == 'Wife'):
                                        return u'<=50K'
                                    if (data['relationship'] != 'Wife'):
                                        return u'<=50K'
            if (data['age'] <= 31):
                if (data['age'] > 21):
		    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
                        return u'<=50K'
                    if (data['hours_per_week'] > 41):
			if (not 'workclass' in data or data['workclass'] is None):
                            return u'<=50K'
                        if (data['workclass'] == 'Private'):
			    if (not 'relationship' in data or data['relationship'] is None):
                                return u'<=50K'
                            if (data['relationship'] == 'Not-in-family'):
				if (not 'occupation' in data or data['occupation'] is None):
                                    return u'<=50K'
                                if (data['occupation'] == 'Exec-managerial'):
				    if (data['marital_status'] == 'Never-married'):
                                        return u'<=50K'
				    if (data['marital_status'] != 'Never-married'):
                                        return u'>50K'
                                if (data['occupation'] != 'Exec-managerial'):
				    if (not 'education' in data or data['education'] is None):
                                        return u'<=50K'
                                    if (data['education'] == '9th'):
                                        return u'<=50K'
                                    if (data['education'] != '9th'):
                                        return u'<=50K'
                            if (data['relationship'] != 'Not-in-family'):
                                return u'<=50K'
                        if (data['workclass'] != 'Private'):
                            if (not 'sex' in data or data['sex'] is None):
                                return u'<=50K'
                            if (data['sex'] == 'Male'):
                                if (data['hours_per_week'] > 49):
				    if (not 'occupation' in data or data['occupation'] is None):
                                        return u'<=50K'
				    if (data['occupation'] == 'Exec-managerial'):
                                        return u'>50K'
				    if (data['occupation'] != 'Exec-managerial'):
                                        return u'<=50K'
                                if (data['hours_per_week'] <= 49):
                                    if (data['education_num'] > 8):
                                        return u'<=50K'
                                    if (data['education_num'] <= 8):
                                        return u'<=50K'
                            if (data['sex'] != 'Male'):
                                return u'<=50K'
                    if (data['hours_per_week'] <= 41):
                        if (data['education_num'] > 9):
                            if (data['hours_per_week'] > 29):
				if (not 'relationship' in data or data['relationship'] is None):
                                    return u'<=50K'
                                if (data['relationship'] == 'Wife'):
                                    return u'>50K'
                                if (data['relationship'] != 'Wife'):
				    if (not 'occupation' in data or data['occupation'] is None):
                                        return u'<=50K'
				    if (data['occupation'] == 'Protective-serv'):
                                        return u'<=50K'
				    if (data['occupation'] != 'Protective-serv'):
                                        return u'<=50K'
                            if (data['hours_per_week'] <= 29):
                                return u'<=50K'
                        if (data['education_num'] <= 9):
                            if (data['age'] > 27):
				if (not 'final_weight' in data or data['final_weight'] is None):
                                    return u'<=50K'
                                if (data['final_weight'] > 94030):
                                    if (data['final_weight'] > 334106):
                                        return u'<=50K'
                                    if (data['final_weight'] <= 334106):
                                        return u'<=50K'
                                if (data['final_weight'] <= 94030):
                                    if (data['marital_status'] == 'Divorced'):
                                        return u'<=50K'
                                    if (data['marital_status'] != 'Divorced'):
                                        return u'<=50K'
                            if (data['age'] <= 27):
                                return u'<=50K'
                if (data['age'] <= 21):
                    if (not 'education' in data or data['education'] is None):
                        return u'<=50K'
                    if (data['education'] == '7th-8th'):
			if (not 'occupation' in data or data['occupation'] is None):
                            return u'<=50K'
                        if (data['occupation'] == 'Other-service'):
			    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
                                return u'<=50K'
                            if (data['hours_per_week'] > 50):
                                return u'>50K'
                            if (data['hours_per_week'] <= 50):
                                return u'<=50K'
                        if (data['occupation'] != 'Other-service'):
                            return u'<=50K'
                    if (data['education'] != '7th-8th'):
			return u'<=50K'