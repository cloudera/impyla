def predict_income(data={}):
    """ Predictor for income from model/5316accd0af5e8143f003c2e

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
		if (data['age'] > 25):
		    if (data['education_num'] > 13):
			if (data['age'] > 32):
			    if (not 'occupation' in data or data['occupation'] is None):
				return u'>50K'
			    if (data['occupation'] == 'Other-service'):
				return u'<=50K'
			    if (data['occupation'] != 'Other-service'):
				if (data['education_num'] > 14):
				    if (data['age'] > 74):
					if (data['hours_per_week'] > 45):
					    return u'>50K'
					if (data['hours_per_week'] <= 45):
					    if (data['education_num'] > 15):
						return u'>50K'
					    if (data['education_num'] <= 15):
						return u'<=50K'
				    if (data['age'] <= 74):
					if (data['age'] > 38):
					    if (not 'relationship' in data or data['relationship'] is None):
						return u'>50K'
					    if (data['relationship'] == 'Not-in-family'):
						return u'<=50K'
					    if (data['relationship'] != 'Not-in-family'):
						if (data['relationship'] == 'Other-relative'):
						    return u'<=50K'
						if (data['relationship'] != 'Other-relative'):
						    if (data['occupation'] == 'Machine-op-inspct'):
							return u'<=50K'
						    if (data['occupation'] != 'Machine-op-inspct'):
							if (data['occupation'] == 'Sales'):
							    return u'>50K'
							if (data['occupation'] != 'Sales'):
							    return u'>50K'
					if (data['age'] <= 38):
					    if (data['hours_per_week'] > 62):
						return u'>50K'
					    if (data['hours_per_week'] <= 62):
						if (not 'race' in data or data['race'] is None):
						    return u'>50K'
						if (data['race'] == 'White'):
						    if (data['occupation'] == 'Craft-repair'):
							return u'<=50K'
						    if (data['occupation'] != 'Craft-repair'):
							if (data['age'] > 34):
							    return u'>50K'
							if (data['age'] <= 34):
							    return u'>50K'
						if (data['race'] != 'White'):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'<=50K'
						    if (data['workclass'] == 'State-gov'):
							return u'<=50K'
						    if (data['workclass'] != 'State-gov'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'>50K'
							if (data['final_weight'] > 175106):
							    return u'<=50K'
							if (data['final_weight'] <= 175106):
							    return u'>50K'
				if (data['education_num'] <= 14):
				    if (data['occupation'] == 'Exec-managerial'):
					if (data['hours_per_week'] > 45):
					    if (data['age'] > 54):
						if (data['age'] > 58):
						    return u'>50K'
						if (data['age'] <= 58):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'>50K'
						    if (data['final_weight'] > 109795):
							if (data['final_weight'] > 143342):
							    return u'>50K'
							if (data['final_weight'] <= 143342):
							    return u'<=50K'
						    if (data['final_weight'] <= 109795):
							return u'>50K'
					    if (data['age'] <= 54):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'>50K'
						if (data['final_weight'] > 233607):
						    if (data['age'] > 34):
							if (data['final_weight'] > 250230):
							    return u'>50K'
							if (data['final_weight'] <= 250230):
							    return u'>50K'
						    if (data['age'] <= 34):
							if (data['final_weight'] > 296849):
							    return u'>50K'
							if (data['final_weight'] <= 296849):
							    return u'<=50K'
						if (data['final_weight'] <= 233607):
						    return u'>50K'
					if (data['hours_per_week'] <= 45):
					    if (data['age'] > 39):
						if (not 'workclass' in data or data['workclass'] is None):
						    return u'>50K'
						if (data['workclass'] == 'Self-emp-not-inc'):
						    if (data['age'] > 51):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'White'):
							    return u'<=50K'
							if (data['race'] != 'White'):
							    return u'<=50K'
						    if (data['age'] <= 51):
							return u'>50K'
						if (data['workclass'] != 'Self-emp-not-inc'):
						    if (data['age'] > 56):
							return u'>50K'
						    if (data['age'] <= 56):
							if (data['workclass'] == 'Private'):
							    return u'>50K'
							if (data['workclass'] != 'Private'):
							    return u'>50K'
					    if (data['age'] <= 39):
						if (not 'workclass' in data or data['workclass'] is None):
						    return u'>50K'
						if (data['workclass'] == 'State-gov'):
						    return u'<=50K'
						if (data['workclass'] != 'State-gov'):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'>50K'
						    if (data['final_weight'] > 262417):
							if (data['final_weight'] > 361253):
							    return u'>50K'
							if (data['final_weight'] <= 361253):
							    return u'<=50K'
						    if (data['final_weight'] <= 262417):
							if (data['age'] > 37):
							    return u'>50K'
							if (data['age'] <= 37):
							    return u'>50K'
				    if (data['occupation'] != 'Exec-managerial'):
					if (data['occupation'] == 'Prof-specialty'):
					    if (data['hours_per_week'] > 57):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'>50K'
						if (data['final_weight'] > 195529):
						    if (not 'race' in data or data['race'] is None):
							return u'<=50K'
						    if (data['race'] == 'White'):
							return u'<=50K'
						    if (data['race'] != 'White'):
							return u'>50K'
						if (data['final_weight'] <= 195529):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'>50K'
						    if (data['workclass'] == 'Private'):
							if (data['final_weight'] > 185433):
							    return u'>50K'
							if (data['final_weight'] <= 185433):
							    return u'<=50K'
						    if (data['workclass'] != 'Private'):
							if (data['age'] > 34):
							    return u'>50K'
							if (data['age'] <= 34):
							    return u'<=50K'
					    if (data['hours_per_week'] <= 57):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'>50K'
						if (data['final_weight'] > 153876):
						    if (data['final_weight'] > 178901):
							if (not 'race' in data or data['race'] is None):
							    return u'>50K'
							if (data['race'] == 'Black'):
							    return u'<=50K'
							if (data['race'] != 'Black'):
							    return u'>50K'
						    if (data['final_weight'] <= 178901):
							if (data['final_weight'] > 158610):
							    return u'>50K'
							if (data['final_weight'] <= 158610):
							    return u'>50K'
						if (data['final_weight'] <= 153876):
						    if (data['age'] > 41):
							if (data['age'] > 58):
							    return u'>50K'
							if (data['age'] <= 58):
							    return u'>50K'
						    if (data['age'] <= 41):
							if (not 'race' in data or data['race'] is None):
							    return u'>50K'
							if (data['race'] == 'White'):
							    return u'>50K'
							if (data['race'] != 'White'):
							    return u'>50K'
					if (data['occupation'] != 'Prof-specialty'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'>50K'
					    if (data['final_weight'] > 440464):
						return u'<=50K'
					    if (data['final_weight'] <= 440464):
						if (data['occupation'] == 'Farming-fishing'):
						    if (data['final_weight'] > 28920):
							return u'<=50K'
						    if (data['final_weight'] <= 28920):
							return u'>50K'
						if (data['occupation'] != 'Farming-fishing'):
						    if (data['occupation'] == 'Sales'):
							if (data['final_weight'] > 246134):
							    return u'>50K'
							if (data['final_weight'] <= 246134):
							    return u'>50K'
						    if (data['occupation'] != 'Sales'):
							if (not 'workclass' in data or data['workclass'] is None):
							    return u'>50K'
							if (data['workclass'] == 'Self-emp-inc'):
							    return u'<=50K'
							if (data['workclass'] != 'Self-emp-inc'):
							    return u'>50K'
			if (data['age'] <= 32):
			    if (not 'workclass' in data or data['workclass'] is None):
				return u'>50K'
			    if (data['workclass'] == 'Local-gov'):
				if (not 'sex' in data or data['sex'] is None):
				    return u'<=50K'
				if (data['sex'] == 'Male'):
				    if (data['hours_per_week'] > 70):
					return u'>50K'
				    if (data['hours_per_week'] <= 70):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 206273):
					    if (data['hours_per_week'] > 45):
						return u'<=50K'
					    if (data['hours_per_week'] <= 45):
						return u'>50K'
					if (data['final_weight'] <= 206273):
					    return u'<=50K'
				if (data['sex'] != 'Male'):
				    if (data['hours_per_week'] > 47):
					return u'<=50K'
				    if (data['hours_per_week'] <= 47):
					return u'>50K'
			    if (data['workclass'] != 'Local-gov'):
				if (data['age'] > 28):
				    if (not 'race' in data or data['race'] is None):
					return u'>50K'
				    if (data['race'] == 'White'):
					if (data['hours_per_week'] > 78):
					    if (data['hours_per_week'] > 94):
						return u'>50K'
					    if (data['hours_per_week'] <= 94):
						return u'<=50K'
					if (data['hours_per_week'] <= 78):
					    if (data['hours_per_week'] > 52):
						return u'>50K'
					    if (data['hours_per_week'] <= 52):
						if (data['age'] > 29):
						    if (data['hours_per_week'] > 47):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 74071):
							    return u'<=50K'
							if (data['final_weight'] <= 74071):
							    return u'>50K'
						    if (data['hours_per_week'] <= 47):
							if (data['age'] > 31):
							    return u'>50K'
							if (data['age'] <= 31):
							    return u'>50K'
						if (data['age'] <= 29):
						    return u'>50K'
				    if (data['race'] != 'White'):
					if (not 'sex' in data or data['sex'] is None):
					    return u'<=50K'
					if (data['sex'] == 'Male'):
					    if (data['education_num'] > 14):
						return u'<=50K'
					    if (data['education_num'] <= 14):
						if (data['hours_per_week'] > 45):
						    return u'>50K'
						if (data['hours_per_week'] <= 45):
						    if (not 'occupation' in data or data['occupation'] is None):
							return u'<=50K'
						    if (data['occupation'] == 'Prof-specialty'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 107255):
							    return u'>50K'
							if (data['final_weight'] <= 107255):
							    return u'<=50K'
						    if (data['occupation'] != 'Prof-specialty'):
							return u'<=50K'
					if (data['sex'] != 'Male'):
					    return u'>50K'
				if (data['age'] <= 28):
				    if (not 'final_weight' in data or data['final_weight'] is None):
					return u'<=50K'
				    if (data['final_weight'] > 97150):
					if (data['final_weight'] > 210842):
					    if (data['hours_per_week'] > 52):
						if (data['final_weight'] > 279203):
						    return u'<=50K'
						if (data['final_weight'] <= 279203):
						    return u'>50K'
					    if (data['hours_per_week'] <= 52):
						return u'>50K'
					if (data['final_weight'] <= 210842):
					    if (data['final_weight'] > 183164):
						return u'<=50K'
					    if (data['final_weight'] <= 183164):
						if (data['final_weight'] > 146194):
						    return u'>50K'
						if (data['final_weight'] <= 146194):
						    if (data['hours_per_week'] > 42):
							return u'>50K'
						    if (data['hours_per_week'] <= 42):
							return u'<=50K'
				    if (data['final_weight'] <= 97150):
					return u'<=50K'
		    if (data['education_num'] <= 13):
			if (not 'occupation' in data or data['occupation'] is None):
			    return u'>50K'
			if (data['occupation'] == 'Exec-managerial'):
			    if (data['hours_per_week'] > 47):
				if (data['hours_per_week'] > 68):
				    if (not 'final_weight' in data or data['final_weight'] is None):
					return u'>50K'
				    if (data['final_weight'] > 138316):
					if (data['final_weight'] > 198053):
					    if (data['final_weight'] > 396555):
						return u'<=50K'
					    if (data['final_weight'] <= 396555):
						if (data['final_weight'] > 258306):
						    if (data['final_weight'] > 303370):
							return u'>50K'
						    if (data['final_weight'] <= 303370):
							return u'<=50K'
						if (data['final_weight'] <= 258306):
						    return u'>50K'
					if (data['final_weight'] <= 198053):
					    if (data['final_weight'] > 178928):
						return u'<=50K'
					    if (data['final_weight'] <= 178928):
						if (data['final_weight'] > 168162):
						    return u'>50K'
						if (data['final_weight'] <= 168162):
						    return u'<=50K'
				    if (data['final_weight'] <= 138316):
					if (data['final_weight'] > 94919):
					    return u'>50K'
					if (data['final_weight'] <= 94919):
					    if (data['final_weight'] > 85112):
						return u'<=50K'
					    if (data['final_weight'] <= 85112):
						return u'>50K'
				if (data['hours_per_week'] <= 68):
				    if (not 'workclass' in data or data['workclass'] is None):
					return u'>50K'
				    if (data['workclass'] == 'Self-emp-not-inc'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'>50K'
					if (data['final_weight'] > 79839):
					    if (data['final_weight'] > 150546):
						if (data['final_weight'] > 312227):
						    return u'<=50K'
						if (data['final_weight'] <= 312227):
						    if (data['final_weight'] > 261160):
							return u'>50K'
						    if (data['final_weight'] <= 261160):
							if (data['final_weight'] > 232813):
							    return u'<=50K'
							if (data['final_weight'] <= 232813):
							    return u'>50K'
					    if (data['final_weight'] <= 150546):
						return u'>50K'
					if (data['final_weight'] <= 79839):
					    return u'<=50K'
				    if (data['workclass'] != 'Self-emp-not-inc'):
					if (not 'relationship' in data or data['relationship'] is None):
					    return u'>50K'
					if (data['relationship'] == 'Own-child'):
					    return u'<=50K'
					if (data['relationship'] != 'Own-child'):
					    if (data['age'] > 26):
						if (data['workclass'] == 'Self-emp-inc'):
						    if (data['hours_per_week'] > 57):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'>50K'
							if (data['final_weight'] > 157822):
							    return u'>50K'
							if (data['final_weight'] <= 157822):
							    return u'>50K'
						    if (data['hours_per_week'] <= 57):
							return u'>50K'
						if (data['workclass'] != 'Self-emp-inc'):
						    if (not 'sex' in data or data['sex'] is None):
							return u'>50K'
						    if (data['sex'] == 'Male'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'>50K'
							if (data['final_weight'] > 353733):
							    return u'>50K'
							if (data['final_weight'] <= 353733):
							    return u'>50K'
						    if (data['sex'] != 'Male'):
							return u'>50K'
					    if (data['age'] <= 26):
						return u'<=50K'
			    if (data['hours_per_week'] <= 47):
				if (data['age'] > 44):
				    if (not 'final_weight' in data or data['final_weight'] is None):
					return u'>50K'
				    if (data['final_weight'] > 297715):
					return u'>50K'
				    if (data['final_weight'] <= 297715):
					if (data['age'] > 47):
					    if (data['final_weight'] > 81627):
						if (data['age'] > 61):
						    if (data['age'] > 72):
							if (data['age'] > 77):
							    return u'>50K'
							if (data['age'] <= 77):
							    return u'<=50K'
						    if (data['age'] <= 72):
							return u'>50K'
						if (data['age'] <= 61):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'>50K'
						    if (data['workclass'] == 'Federal-gov'):
							return u'>50K'
						    if (data['workclass'] != 'Federal-gov'):
							if (data['age'] > 55):
							    return u'>50K'
							if (data['age'] <= 55):
							    return u'>50K'
					    if (data['final_weight'] <= 81627):
						if (data['final_weight'] > 39419):
						    return u'<=50K'
						if (data['final_weight'] <= 39419):
						    if (data['age'] > 58):
							return u'<=50K'
						    if (data['age'] <= 58):
							return u'>50K'
					if (data['age'] <= 47):
					    if (data['hours_per_week'] > 33):
						if (data['final_weight'] > 270323):
						    if (data['final_weight'] > 283954):
							return u'>50K'
						    if (data['final_weight'] <= 283954):
							return u'<=50K'
						if (data['final_weight'] <= 270323):
						    return u'>50K'
					    if (data['hours_per_week'] <= 33):
						return u'<=50K'
				if (data['age'] <= 44):
				    if (not 'race' in data or data['race'] is None):
					return u'>50K'
				    if (data['race'] == 'Asian-Pac-Islander'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 263291):
					    return u'>50K'
					if (data['final_weight'] <= 263291):
					    if (not 'workclass' in data or data['workclass'] is None):
						return u'<=50K'
					    if (data['workclass'] == 'Federal-gov'):
						return u'>50K'
					    if (data['workclass'] != 'Federal-gov'):
						if (data['final_weight'] > 149280):
						    if (data['final_weight'] > 194841):
							return u'<=50K'
						    if (data['final_weight'] <= 194841):
							return u'>50K'
						if (data['final_weight'] <= 149280):
						    return u'<=50K'
				    if (data['race'] != 'Asian-Pac-Islander'):
					if (not 'workclass' in data or data['workclass'] is None):
					    return u'>50K'
					if (data['workclass'] == 'Self-emp-not-inc'):
					    if (not 'sex' in data or data['sex'] is None):
						return u'<=50K'
					    if (data['sex'] == 'Male'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 198062):
						    return u'<=50K'
						if (data['final_weight'] <= 198062):
						    if (data['final_weight'] > 122888):
							return u'>50K'
						    if (data['final_weight'] <= 122888):
							return u'<=50K'
					    if (data['sex'] != 'Male'):
						return u'>50K'
					if (data['workclass'] != 'Self-emp-not-inc'):
					    if (data['hours_per_week'] > 36):
						if (data['race'] == 'Other'):
						    return u'<=50K'
						if (data['race'] != 'Other'):
						    if (data['age'] > 43):
							if (data['hours_per_week'] > 42):
							    return u'>50K'
							if (data['hours_per_week'] <= 42):
							    return u'>50K'
						    if (data['age'] <= 43):
							if (not 'relationship' in data or data['relationship'] is None):
							    return u'>50K'
							if (data['relationship'] == 'Other-relative'):
							    return u'<=50K'
							if (data['relationship'] != 'Other-relative'):
							    return u'>50K'
					    if (data['hours_per_week'] <= 36):
						return u'>50K'
			if (data['occupation'] != 'Exec-managerial'):
			    if (data['occupation'] == 'Other-service'):
				if (not 'final_weight' in data or data['final_weight'] is None):
				    return u'<=50K'
				if (data['final_weight'] > 190394):
				    return u'<=50K'
				if (data['final_weight'] <= 190394):
				    if (data['hours_per_week'] > 47):
					if (data['final_weight'] > 74673):
					    return u'>50K'
					if (data['final_weight'] <= 74673):
					    return u'<=50K'
				    if (data['hours_per_week'] <= 47):
					if (data['final_weight'] > 66031):
					    if (data['final_weight'] > 178776):
						if (not 'sex' in data or data['sex'] is None):
						    return u'>50K'
						if (data['sex'] == 'Male'):
						    if (data['final_weight'] > 181259):
							return u'<=50K'
						    if (data['final_weight'] <= 181259):
							return u'>50K'
						if (data['sex'] != 'Male'):
						    return u'>50K'
					    if (data['final_weight'] <= 178776):
						if (data['age'] > 60):
						    return u'>50K'
						if (data['age'] <= 60):
						    return u'<=50K'
					if (data['final_weight'] <= 66031):
					    return u'>50K'
			    if (data['occupation'] != 'Other-service'):
				if (data['occupation'] == 'Farming-fishing'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
					return u'<=50K'
				    if (data['final_weight'] > 34366):
					if (not 'workclass' in data or data['workclass'] is None):
					    return u'<=50K'
					if (data['workclass'] == 'Self-emp-not-inc'):
					    if (data['hours_per_week'] > 78):
						if (data['final_weight'] > 155091):
						    return u'>50K'
						if (data['final_weight'] <= 155091):
						    return u'<=50K'
					    if (data['hours_per_week'] <= 78):
						return u'<=50K'
					if (data['workclass'] != 'Self-emp-not-inc'):
					    if (data['age'] > 42):
						if (data['hours_per_week'] > 55):
						    if (data['hours_per_week'] > 62):
							return u'>50K'
						    if (data['hours_per_week'] <= 62):
							return u'<=50K'
						if (data['hours_per_week'] <= 55):
						    return u'>50K'
					    if (data['age'] <= 42):
						if (data['hours_per_week'] > 62):
						    return u'>50K'
						if (data['hours_per_week'] <= 62):
						    return u'<=50K'
				    if (data['final_weight'] <= 34366):
					return u'>50K'
				if (data['occupation'] != 'Farming-fishing'):
				    if (not 'relationship' in data or data['relationship'] is None):
					return u'>50K'
				    if (data['relationship'] == 'Other-relative'):
					if (data['age'] > 29):
					    return u'<=50K'
					if (data['age'] <= 29):
					    if (data['hours_per_week'] > 45):
						return u'<=50K'
					    if (data['hours_per_week'] <= 45):
						return u'>50K'
				    if (data['relationship'] != 'Other-relative'):
					if (data['occupation'] == 'Craft-repair'):
					    if (not 'workclass' in data or data['workclass'] is None):
						return u'>50K'
					    if (data['workclass'] == 'Private'):
						if (data['age'] > 33):
						    if (data['age'] > 46):
							if (not 'race' in data or data['race'] is None):
							    return u'>50K'
							if (data['race'] == 'Asian-Pac-Islander'):
							    return u'<=50K'
							if (data['race'] != 'Asian-Pac-Islander'):
							    return u'>50K'
						    if (data['age'] <= 46):
							if (data['age'] > 44):
							    return u'>50K'
							if (data['age'] <= 44):
							    return u'>50K'
						if (data['age'] <= 33):
						    if (data['age'] > 26):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 138282):
							    return u'<=50K'
							if (data['final_weight'] <= 138282):
							    return u'<=50K'
						    if (data['age'] <= 26):
							return u'>50K'
					    if (data['workclass'] != 'Private'):
						if (data['hours_per_week'] > 42):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 285975):
							return u'>50K'
						    if (data['final_weight'] <= 285975):
							if (data['final_weight'] > 204728):
							    return u'<=50K'
							if (data['final_weight'] <= 204728):
							    return u'>50K'
						if (data['hours_per_week'] <= 42):
						    if (data['age'] > 42):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 82887):
							    return u'<=50K'
							if (data['final_weight'] <= 82887):
							    return u'<=50K'
						    if (data['age'] <= 42):
							return u'<=50K'
					if (data['occupation'] != 'Craft-repair'):
					    if (not 'race' in data or data['race'] is None):
						return u'>50K'
					    if (data['race'] == 'Other'):
						if (data['hours_per_week'] > 47):
						    return u'>50K'
						if (data['hours_per_week'] <= 47):
						    return u'<=50K'
					    if (data['race'] != 'Other'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'>50K'
						if (data['final_weight'] > 109774):
						    if (data['occupation'] == 'Transport-moving'):
							if (not 'workclass' in data or data['workclass'] is None):
							    return u'<=50K'
							if (data['workclass'] == 'Private'):
							    return u'<=50K'
							if (data['workclass'] != 'Private'):
							    return u'<=50K'
						    if (data['occupation'] != 'Transport-moving'):
							if (data['age'] > 41):
							    return u'>50K'
							if (data['age'] <= 41):
							    return u'>50K'
						if (data['final_weight'] <= 109774):
						    if (data['final_weight'] > 38448):
							if (data['age'] > 27):
							    return u'>50K'
							if (data['age'] <= 27):
							    return u'<=50K'
						    if (data['final_weight'] <= 38448):
							if (data['hours_per_week'] > 43):
							    return u'>50K'
							if (data['hours_per_week'] <= 43):
							    return u'>50K'
		if (data['age'] <= 25):
		    if (not 'final_weight' in data or data['final_weight'] is None):
			return u'<=50K'
		    if (data['final_weight'] > 401760):
			return u'>50K'
		    if (data['final_weight'] <= 401760):
			if (not 'workclass' in data or data['workclass'] is None):
			    return u'<=50K'
			if (data['workclass'] == 'Self-emp-inc'):
			    return u'>50K'
			if (data['workclass'] != 'Self-emp-inc'):
			    if (data['age'] > 24):
				if (data['final_weight'] > 260521):
				    if (data['hours_per_week'] > 47):
					return u'<=50K'
				    if (data['hours_per_week'] <= 47):
					return u'>50K'
				if (data['final_weight'] <= 260521):
				    if (data['final_weight'] > 200628):
					return u'<=50K'
				    if (data['final_weight'] <= 200628):
					if (data['final_weight'] > 196137):
					    return u'>50K'
					if (data['final_weight'] <= 196137):
					    if (data['final_weight'] > 168467):
						return u'<=50K'
					    if (data['final_weight'] <= 168467):
						if (data['final_weight'] > 66173):
						    if (data['final_weight'] > 90741):
							if (data['final_weight'] > 132562):
							    return u'>50K'
							if (data['final_weight'] <= 132562):
							    return u'<=50K'
						    if (data['final_weight'] <= 90741):
							return u'>50K'
						if (data['final_weight'] <= 66173):
						    return u'<=50K'
			    if (data['age'] <= 24):
				if (data['final_weight'] > 58428):
				    return u'<=50K'
				if (data['final_weight'] <= 58428):
				    if (data['final_weight'] > 38469):
					return u'>50K'
				    if (data['final_weight'] <= 38469):
					return u'<=50K'
	    if (data['hours_per_week'] <= 31):
		if (not 'relationship' in data or data['relationship'] is None):
		    return u'<=50K'
		if (data['relationship'] == 'Wife'):
		    if (not 'final_weight' in data or data['final_weight'] is None):
			return u'>50K'
		    if (data['final_weight'] > 374053):
			return u'<=50K'
		    if (data['final_weight'] <= 374053):
			if (not 'age' in data or data['age'] is None):
			    return u'>50K'
			if (data['age'] > 53):
			    if (not 'workclass' in data or data['workclass'] is None):
				return u'<=50K'
			    if (data['workclass'] == 'Self-emp-not-inc'):
				return u'<=50K'
			    if (data['workclass'] != 'Self-emp-not-inc'):
				if (data['final_weight'] > 274689):
				    return u'<=50K'
				if (data['final_weight'] <= 274689):
				    return u'>50K'
			if (data['age'] <= 53):
			    if (data['age'] > 26):
				if (data['hours_per_week'] > 1):
				    if (data['education_num'] > 13):
					return u'>50K'
				    if (data['education_num'] <= 13):
					if (not 'occupation' in data or data['occupation'] is None):
					    return u'>50K'
					if (data['occupation'] == 'Exec-managerial'):
					    return u'>50K'
					if (data['occupation'] != 'Exec-managerial'):
					    if (data['final_weight'] > 260685):
						if (data['occupation'] == 'Prof-specialty'):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'>50K'
						    if (data['workclass'] == 'Local-gov'):
							return u'<=50K'
						    if (data['workclass'] != 'Local-gov'):
							return u'>50K'
						if (data['occupation'] != 'Prof-specialty'):
						    return u'<=50K'
					    if (data['final_weight'] <= 260685):
						if (data['hours_per_week'] > 24):
						    return u'>50K'
						if (data['hours_per_week'] <= 24):
						    if (data['final_weight'] > 179922):
							return u'>50K'
						    if (data['final_weight'] <= 179922):
							if (data['hours_per_week'] > 6):
							    return u'>50K'
							if (data['hours_per_week'] <= 6):
							    return u'<=50K'
				if (data['hours_per_week'] <= 1):
				    return u'<=50K'
			    if (data['age'] <= 26):
				if (data['hours_per_week'] > 27):
				    return u'>50K'
				if (data['hours_per_week'] <= 27):
				    return u'<=50K'
		if (data['relationship'] != 'Wife'):
		    if (not 'age' in data or data['age'] is None):
			return u'<=50K'
		    if (data['age'] > 28):
			if (not 'workclass' in data or data['workclass'] is None):
			    return u'<=50K'
			if (data['workclass'] == 'State-gov'):
			    if (not 'sex' in data or data['sex'] is None):
				return u'<=50K'
			    if (data['sex'] == 'Male'):
				return u'<=50K'
			    if (data['sex'] != 'Male'):
				return u'>50K'
			if (data['workclass'] != 'State-gov'):
			    if (data['hours_per_week'] > 4):
				if (not 'education' in data or data['education'] is None):
				    return u'<=50K'
				if (data['education'] == 'Prof-school'):
				    if (data['age'] > 58):
					if (data['hours_per_week'] > 14):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 132179):
						if (data['age'] > 68):
						    return u'<=50K'
						if (data['age'] <= 68):
						    if (data['hours_per_week'] > 27):
							if (data['final_weight'] > 164095):
							    return u'<=50K'
							if (data['final_weight'] <= 164095):
							    return u'>50K'
						    if (data['hours_per_week'] <= 27):
							return u'>50K'
					    if (data['final_weight'] <= 132179):
						return u'<=50K'
					if (data['hours_per_week'] <= 14):
					    return u'>50K'
				    if (data['age'] <= 58):
					return u'>50K'
				if (data['education'] != 'Prof-school'):
				    if (not 'occupation' in data or data['occupation'] is None):
					return u'<=50K'
				    if (data['occupation'] == 'Transport-moving'):
					return u'<=50K'
				    if (data['occupation'] != 'Transport-moving'):
					if (data['age'] > 52):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 331480):
						return u'>50K'
					    if (data['final_weight'] <= 331480):
						if (data['occupation'] == 'Tech-support'):
						    return u'>50K'
						if (data['occupation'] != 'Tech-support'):
						    if (data['education'] == 'Masters'):
							if (data['hours_per_week'] > 27):
							    return u'>50K'
							if (data['hours_per_week'] <= 27):
							    return u'<=50K'
						    if (data['education'] != 'Masters'):
							if (data['occupation'] == 'Prof-specialty'):
							    return u'<=50K'
							if (data['occupation'] != 'Prof-specialty'):
							    return u'<=50K'
					if (data['age'] <= 52):
					    if (data['workclass'] == 'Private'):
						if (data['occupation'] == 'Other-service'):
						    if (not 'race' in data or data['race'] is None):
							return u'>50K'
						    if (data['race'] == 'Asian-Pac-Islander'):
							return u'<=50K'
						    if (data['race'] != 'Asian-Pac-Islander'):
							return u'>50K'
						if (data['occupation'] != 'Other-service'):
						    if (data['hours_per_week'] > 15):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 212111):
							    return u'>50K'
							if (data['final_weight'] <= 212111):
							    return u'<=50K'
						    if (data['hours_per_week'] <= 15):
							return u'<=50K'
					    if (data['workclass'] != 'Private'):
						if (not 'race' in data or data['race'] is None):
						    return u'<=50K'
						if (data['race'] == 'White'):
						    if (data['age'] > 37):
							return u'<=50K'
						    if (data['age'] <= 37):
							if (data['age'] > 35):
							    return u'>50K'
							if (data['age'] <= 35):
							    return u'<=50K'
						if (data['race'] != 'White'):
						    return u'>50K'
			    if (data['hours_per_week'] <= 4):
				return u'<=50K'
		    if (data['age'] <= 28):
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
			    if (not 'workclass' in data or data['workclass'] is None):
				return u'>50K'
			    if (data['workclass'] == 'Self-emp-not-inc'):
				if (not 'occupation' in data or data['occupation'] is None):
				    return u'<=50K'
				if (data['occupation'] == 'Machine-op-inspct'):
				    return u'>50K'
				if (data['occupation'] != 'Machine-op-inspct'):
				    if (data['occupation'] == 'Adm-clerical'):
					return u'>50K'
				    if (data['occupation'] != 'Adm-clerical'):
					if (data['occupation'] == 'Farming-fishing'):
					    if (data['education_num'] > 10):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 47382):
						    if (data['final_weight'] > 179718):
							return u'<=50K'
						    if (data['final_weight'] <= 179718):
							if (data['hours_per_week'] > 45):
							    return u'>50K'
							if (data['hours_per_week'] <= 45):
							    return u'<=50K'
						if (data['final_weight'] <= 47382):
						    return u'<=50K'
					    if (data['education_num'] <= 10):
						if (data['age'] > 49):
						    if (data['hours_per_week'] > 42):
							if (data['hours_per_week'] > 89):
							    return u'>50K'
							if (data['hours_per_week'] <= 89):
							    return u'<=50K'
						    if (data['hours_per_week'] <= 42):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'>50K'
							if (data['final_weight'] > 162658):
							    return u'<=50K'
							if (data['final_weight'] <= 162658):
							    return u'>50K'
						if (data['age'] <= 49):
						    return u'<=50K'
					if (data['occupation'] != 'Farming-fishing'):
					    if (data['occupation'] == 'Tech-support'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'>50K'
						if (data['final_weight'] > 84688):
						    return u'>50K'
						if (data['final_weight'] <= 84688):
						    return u'<=50K'
					    if (data['occupation'] != 'Tech-support'):
						if (data['hours_per_week'] > 37):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 338299):
							if (data['hours_per_week'] > 42):
							    return u'<=50K'
							if (data['hours_per_week'] <= 42):
							    return u'>50K'
						    if (data['final_weight'] <= 338299):
							if (data['final_weight'] > 250454):
							    return u'<=50K'
							if (data['final_weight'] <= 250454):
							    return u'<=50K'
						if (data['hours_per_week'] <= 37):
						    return u'<=50K'
			    if (data['workclass'] != 'Self-emp-not-inc'):
				if (not 'occupation' in data or data['occupation'] is None):
				    return u'>50K'
				if (data['occupation'] == 'Exec-managerial'):
				    if (data['hours_per_week'] > 41):
					if (not 'race' in data or data['race'] is None):
					    return u'>50K'
					if (data['race'] == 'Asian-Pac-Islander'):
					    if (data['hours_per_week'] > 67):
						return u'>50K'
					    if (data['hours_per_week'] <= 67):
						return u'<=50K'
					if (data['race'] != 'Asian-Pac-Islander'):
					    if (data['education_num'] > 10):
						if (data['age'] > 49):
						    if (data['hours_per_week'] > 79):
							return u'<=50K'
						    if (data['hours_per_week'] <= 79):
							if (data['workclass'] == 'Private'):
							    return u'>50K'
							if (data['workclass'] != 'Private'):
							    return u'<=50K'
						if (data['age'] <= 49):
						    if (data['hours_per_week'] > 54):
							if (data['education_num'] > 11):
							    return u'>50K'
							if (data['education_num'] <= 11):
							    return u'>50K'
						    if (data['hours_per_week'] <= 54):
							return u'>50K'
					    if (data['education_num'] <= 10):
						if (data['age'] > 48):
						    if (data['age'] > 64):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 81733):
							    return u'<=50K'
							if (data['final_weight'] <= 81733):
							    return u'>50K'
						    if (data['age'] <= 64):
							if (data['workclass'] == 'Private'):
							    return u'>50K'
							if (data['workclass'] != 'Private'):
							    return u'>50K'
						if (data['age'] <= 48):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'>50K'
						    if (data['final_weight'] > 93120):
							if (data['final_weight'] > 397773):
							    return u'<=50K'
							if (data['final_weight'] <= 397773):
							    return u'>50K'
						    if (data['final_weight'] <= 93120):
							if (data['final_weight'] > 64054):
							    return u'<=50K'
							if (data['final_weight'] <= 64054):
							    return u'<=50K'
				    if (data['hours_per_week'] <= 41):
					if (data['workclass'] == 'State-gov'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 75581):
						if (not 'sex' in data or data['sex'] is None):
						    return u'<=50K'
						if (data['sex'] == 'Male'):
						    return u'<=50K'
						if (data['sex'] != 'Male'):
						    if (not 'race' in data or data['race'] is None):
							return u'<=50K'
						    if (data['race'] == 'White'):
							return u'>50K'
						    if (data['race'] != 'White'):
							return u'<=50K'
					    if (data['final_weight'] <= 75581):
						if (data['final_weight'] > 27280):
						    return u'>50K'
						if (data['final_weight'] <= 27280):
						    return u'<=50K'
					if (data['workclass'] != 'State-gov'):
					    if (data['education_num'] > 11):
						if (data['hours_per_week'] > 38):
						    if (data['age'] > 44):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'>50K'
							if (data['final_weight'] > 144233):
							    return u'<=50K'
							if (data['final_weight'] <= 144233):
							    return u'>50K'
						    if (data['age'] <= 44):
							return u'>50K'
						if (data['hours_per_week'] <= 38):
						    return u'<=50K'
					    if (data['education_num'] <= 11):
						if (not 'sex' in data or data['sex'] is None):
						    return u'>50K'
						if (data['sex'] == 'Male'):
						    if (data['age'] > 43):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'>50K'
							if (data['final_weight'] > 39591):
							    return u'>50K'
							if (data['final_weight'] <= 39591):
							    return u'>50K'
						    if (data['age'] <= 43):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'White'):
							    return u'<=50K'
							if (data['race'] != 'White'):
							    return u'>50K'
						if (data['sex'] != 'Male'):
						    if (data['age'] > 59):
							return u'<=50K'
						    if (data['age'] <= 59):
							return u'>50K'
				if (data['occupation'] != 'Exec-managerial'):
				    if (data['occupation'] == 'Other-service'):
					if (data['hours_per_week'] > 55):
					    if (data['workclass'] == 'Private'):
						return u'>50K'
					    if (data['workclass'] != 'Private'):
						return u'<=50K'
					if (data['hours_per_week'] <= 55):
					    if (not 'relationship' in data or data['relationship'] is None):
						return u'<=50K'
					    if (data['relationship'] == 'Own-child'):
						return u'>50K'
					    if (data['relationship'] != 'Own-child'):
						if (data['age'] > 46):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 86584):
							if (data['workclass'] == 'Federal-gov'):
							    return u'>50K'
							if (data['workclass'] != 'Federal-gov'):
							    return u'<=50K'
						    if (data['final_weight'] <= 86584):
							return u'<=50K'
						if (data['age'] <= 46):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 83464):
							if (data['final_weight'] > 194412):
							    return u'<=50K'
							if (data['final_weight'] <= 194412):
							    return u'<=50K'
						    if (data['final_weight'] <= 83464):
							if (data['hours_per_week'] > 42):
							    return u'<=50K'
							if (data['hours_per_week'] <= 42):
							    return u'>50K'
				    if (data['occupation'] != 'Other-service'):
					if (data['occupation'] == 'Handlers-cleaners'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 163740):
						if (data['workclass'] == 'Federal-gov'):
						    return u'>50K'
						if (data['workclass'] != 'Federal-gov'):
						    if (data['age'] > 48):
							if (data['education_num'] > 10):
							    return u'>50K'
							if (data['education_num'] <= 10):
							    return u'<=50K'
						    if (data['age'] <= 48):
							if (data['education_num'] > 10):
							    return u'<=50K'
							if (data['education_num'] <= 10):
							    return u'<=50K'
					    if (data['final_weight'] <= 163740):
						return u'<=50K'
					if (data['occupation'] != 'Handlers-cleaners'):
					    if (data['occupation'] == 'Machine-op-inspct'):
						if (data['education_num'] > 10):
						    if (data['age'] > 49):
							return u'>50K'
						    if (data['age'] <= 49):
							if (data['age'] > 38):
							    return u'<=50K'
							if (data['age'] <= 38):
							    return u'>50K'
						if (data['education_num'] <= 10):
						    if (not 'race' in data or data['race'] is None):
							return u'<=50K'
						    if (data['race'] == 'Asian-Pac-Islander'):
							return u'>50K'
						    if (data['race'] != 'Asian-Pac-Islander'):
							if (data['age'] > 51):
							    return u'<=50K'
							if (data['age'] <= 51):
							    return u'<=50K'
					    if (data['occupation'] != 'Machine-op-inspct'):
						if (data['occupation'] == 'Transport-moving'):
						    if (data['workclass'] == 'Self-emp-inc'):
							return u'>50K'
						    if (data['workclass'] != 'Self-emp-inc'):
							if (data['education_num'] > 11):
							    return u'<=50K'
							if (data['education_num'] <= 11):
							    return u'<=50K'
						if (data['occupation'] != 'Transport-moving'):
						    if (data['occupation'] == 'Farming-fishing'):
							if (data['age'] > 44):
							    return u'<=50K'
							if (data['age'] <= 44):
							    return u'<=50K'
						    if (data['occupation'] != 'Farming-fishing'):
							if (data['occupation'] == 'Craft-repair'):
							    return u'>50K'
							if (data['occupation'] != 'Craft-repair'):
							    return u'>50K'
			if (data['education_num'] <= 9):
			    if (not 'occupation' in data or data['occupation'] is None):
				return u'<=50K'
			    if (data['occupation'] == 'Exec-managerial'):
				if (not 'workclass' in data or data['workclass'] is None):
				    return u'>50K'
				if (data['workclass'] == 'Self-emp-not-inc'):
				    if (data['age'] > 46):
					if (data['age'] > 50):
					    if (data['hours_per_week'] > 42):
						if (data['age'] > 53):
						    if (data['hours_per_week'] > 51):
							if (data['hours_per_week'] > 59):
							    return u'<=50K'
							if (data['hours_per_week'] <= 59):
							    return u'>50K'
						    if (data['hours_per_week'] <= 51):
							return u'<=50K'
						if (data['age'] <= 53):
						    return u'>50K'
					    if (data['hours_per_week'] <= 42):
						if (data['age'] > 60):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 171735):
							if (data['final_weight'] > 208778):
							    return u'>50K'
							if (data['final_weight'] <= 208778):
							    return u'<=50K'
						    if (data['final_weight'] <= 171735):
							return u'>50K'
						if (data['age'] <= 60):
						    return u'<=50K'
					if (data['age'] <= 50):
					    return u'>50K'
				    if (data['age'] <= 46):
					if (data['age'] > 44):
					    return u'<=50K'
					if (data['age'] <= 44):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 145136):
						if (data['final_weight'] > 259555):
						    return u'<=50K'
						if (data['final_weight'] <= 259555):
						    if (data['age'] > 42):
							return u'>50K'
						    if (data['age'] <= 42):
							if (data['hours_per_week'] > 55):
							    return u'>50K'
							if (data['hours_per_week'] <= 55):
							    return u'<=50K'
					    if (data['final_weight'] <= 145136):
						if (data['hours_per_week'] > 45):
						    return u'<=50K'
						if (data['hours_per_week'] <= 45):
						    if (data['final_weight'] > 76096):
							if (data['final_weight'] > 98311):
							    return u'<=50K'
							if (data['final_weight'] <= 98311):
							    return u'>50K'
						    if (data['final_weight'] <= 76096):
							return u'<=50K'
				if (data['workclass'] != 'Self-emp-not-inc'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
					return u'>50K'
				    if (data['final_weight'] > 199214):
					if (data['hours_per_week'] > 75):
					    return u'<=50K'
					if (data['hours_per_week'] <= 75):
					    if (data['final_weight'] > 425345):
						return u'>50K'
					    if (data['final_weight'] <= 425345):
						if (data['final_weight'] > 337575):
						    if (data['workclass'] == 'Self-emp-inc'):
							return u'>50K'
						    if (data['workclass'] != 'Self-emp-inc'):
							return u'<=50K'
						if (data['final_weight'] <= 337575):
						    if (data['final_weight'] > 304899):
							return u'>50K'
						    if (data['final_weight'] <= 304899):
							if (data['final_weight'] > 224412):
							    return u'>50K'
							if (data['final_weight'] <= 224412):
							    return u'>50K'
				    if (data['final_weight'] <= 199214):
					if (data['hours_per_week'] > 71):
					    return u'>50K'
					if (data['hours_per_week'] <= 71):
					    if (not 'race' in data or data['race'] is None):
						return u'>50K'
					    if (data['race'] == 'Amer-Indian-Eskimo'):
						return u'<=50K'
					    if (data['race'] != 'Amer-Indian-Eskimo'):
						if (data['final_weight'] > 29957):
						    if (data['final_weight'] > 53488):
							if (data['workclass'] == 'State-gov'):
							    return u'>50K'
							if (data['workclass'] != 'State-gov'):
							    return u'>50K'
						    if (data['final_weight'] <= 53488):
							if (data['final_weight'] > 36212):
							    return u'<=50K'
							if (data['final_weight'] <= 36212):
							    return u'>50K'
						if (data['final_weight'] <= 29957):
						    return u'>50K'
			    if (data['occupation'] != 'Exec-managerial'):
				if (not 'workclass' in data or data['workclass'] is None):
				    return u'<=50K'
				if (data['workclass'] == 'Federal-gov'):
				    if (data['age'] > 40):
					if (data['age'] > 46):
					    if (data['hours_per_week'] > 60):
						return u'<=50K'
					    if (data['hours_per_week'] <= 60):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'>50K'
						if (data['final_weight'] > 121309):
						    if (data['final_weight'] > 142970):
							if (data['occupation'] == 'Tech-support'):
							    return u'>50K'
							if (data['occupation'] != 'Tech-support'):
							    return u'>50K'
						    if (data['final_weight'] <= 142970):
							return u'<=50K'
						if (data['final_weight'] <= 121309):
						    if (data['age'] > 53):
							return u'>50K'
						    if (data['age'] <= 53):
							if (data['age'] > 49):
							    return u'<=50K'
							if (data['age'] <= 49):
							    return u'>50K'
					if (data['age'] <= 46):
					    if (data['occupation'] == 'Machine-op-inspct'):
						return u'<=50K'
					    if (data['occupation'] != 'Machine-op-inspct'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'>50K'
						if (data['final_weight'] > 183034):
						    return u'>50K'
						if (data['final_weight'] <= 183034):
						    if (data['final_weight'] > 177138):
							return u'<=50K'
						    if (data['final_weight'] <= 177138):
							return u'>50K'
				    if (data['age'] <= 40):
					if (data['hours_per_week'] > 51):
					    return u'>50K'
					if (data['hours_per_week'] <= 51):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 49922):
						if (data['final_weight'] > 272530):
						    if (data['hours_per_week'] > 45):
							return u'>50K'
						    if (data['hours_per_week'] <= 45):
							if (data['occupation'] == 'Craft-repair'):
							    return u'>50K'
							if (data['occupation'] != 'Craft-repair'):
							    return u'<=50K'
						if (data['final_weight'] <= 272530):
						    if (data['final_weight'] > 131943):
							return u'<=50K'
						    if (data['final_weight'] <= 131943):
							if (data['final_weight'] > 108824):
							    return u'>50K'
							if (data['final_weight'] <= 108824):
							    return u'<=50K'
					    if (data['final_weight'] <= 49922):
						return u'>50K'
				if (data['workclass'] != 'Federal-gov'):
				    if (data['hours_per_week'] > 41):
					if (not 'relationship' in data or data['relationship'] is None):
					    return u'<=50K'
					if (data['relationship'] == 'Husband'):
					    if (data['workclass'] == 'Self-emp-not-inc'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 278420):
						    if (data['final_weight'] > 363350):
							return u'<=50K'
						    if (data['final_weight'] <= 363350):
							if (data['hours_per_week'] > 55):
							    return u'<=50K'
							if (data['hours_per_week'] <= 55):
							    return u'>50K'
						if (data['final_weight'] <= 278420):
						    if (not 'race' in data or data['race'] is None):
							return u'<=50K'
						    if (data['race'] == 'White'):
							if (data['hours_per_week'] > 51):
							    return u'<=50K'
							if (data['hours_per_week'] <= 51):
							    return u'<=50K'
						    if (data['race'] != 'White'):
							return u'<=50K'
					    if (data['workclass'] != 'Self-emp-not-inc'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 437313):
						    if (data['final_weight'] > 665871):
							if (data['hours_per_week'] > 58):
							    return u'>50K'
							if (data['hours_per_week'] <= 58):
							    return u'<=50K'
						    if (data['final_weight'] <= 665871):
							return u'>50K'
						if (data['final_weight'] <= 437313):
						    if (not 'race' in data or data['race'] is None):
							return u'<=50K'
						    if (data['race'] == 'Amer-Indian-Eskimo'):
							return u'<=50K'
						    if (data['race'] != 'Amer-Indian-Eskimo'):
							if (data['final_weight'] > 28067):
							    return u'<=50K'
							if (data['final_weight'] <= 28067):
							    return u'>50K'
					if (data['relationship'] != 'Husband'):
					    if (data['occupation'] == 'Adm-clerical'):
						if (data['age'] > 42):
						    return u'>50K'
						if (data['age'] <= 42):
						    return u'<=50K'
					    if (data['occupation'] != 'Adm-clerical'):
						if (not 'race' in data or data['race'] is None):
						    return u'<=50K'
						if (data['race'] == 'Black'):
						    if (data['hours_per_week'] > 52):
							return u'>50K'
						    if (data['hours_per_week'] <= 52):
							return u'<=50K'
						if (data['race'] != 'Black'):
						    return u'<=50K'
				    if (data['hours_per_week'] <= 41):
					if (data['age'] > 60):
					    if (data['occupation'] == 'Tech-support'):
						return u'>50K'
					    if (data['occupation'] != 'Tech-support'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 291903):
						    return u'<=50K'
						if (data['final_weight'] <= 291903):
						    if (data['final_weight'] > 262692):
							if (data['age'] > 61):
							    return u'>50K'
							if (data['age'] <= 61):
							    return u'<=50K'
						    if (data['final_weight'] <= 262692):
							if (data['occupation'] == 'Prof-specialty'):
							    return u'>50K'
							if (data['occupation'] != 'Prof-specialty'):
							    return u'<=50K'
					if (data['age'] <= 60):
					    if (data['age'] > 46):
						if (data['occupation'] == 'Other-service'):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 135690):
							if (data['final_weight'] > 173314):
							    return u'<=50K'
							if (data['final_weight'] <= 173314):
							    return u'>50K'
						    if (data['final_weight'] <= 135690):
							return u'<=50K'
						if (data['occupation'] != 'Other-service'):
						    if (data['workclass'] == 'Self-emp-inc'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'>50K'
							if (data['final_weight'] > 248541):
							    return u'<=50K'
							if (data['final_weight'] <= 248541):
							    return u'>50K'
						    if (data['workclass'] != 'Self-emp-inc'):
							if (data['occupation'] == 'Farming-fishing'):
							    return u'<=50K'
							if (data['occupation'] != 'Farming-fishing'):
							    return u'<=50K'
					    if (data['age'] <= 46):
						if (data['occupation'] == 'Adm-clerical'):
						    if (data['workclass'] == 'State-gov'):
							return u'<=50K'
						    if (data['workclass'] != 'State-gov'):
							if (data['age'] > 39):
							    return u'<=50K'
							if (data['age'] <= 39):
							    return u'>50K'
						if (data['occupation'] != 'Adm-clerical'):
						    if (data['occupation'] == 'Farming-fishing'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 38247):
							    return u'<=50K'
							if (data['final_weight'] <= 38247):
							    return u'<=50K'
						    if (data['occupation'] != 'Farming-fishing'):
							if (data['occupation'] == 'Sales'):
							    return u'<=50K'
							if (data['occupation'] != 'Sales'):
							    return u'<=50K'
		    if (data['hours_per_week'] <= 33):
			if (data['education_num'] > 9):
			    if (not 'race' in data or data['race'] is None):
				return u'<=50K'
			    if (data['race'] == 'Black'):
				return u'<=50K'
			    if (data['race'] != 'Black'):
				if (not 'occupation' in data or data['occupation'] is None):
				    return u'<=50K'
				if (data['occupation'] == 'Farming-fishing'):
				    return u'<=50K'
				if (data['occupation'] != 'Farming-fishing'):
				    if (not 'workclass' in data or data['workclass'] is None):
					return u'<=50K'
				    if (data['workclass'] == 'Local-gov'):
					return u'<=50K'
				    if (data['workclass'] != 'Local-gov'):
					if (not 'relationship' in data or data['relationship'] is None):
					    return u'<=50K'
					if (data['relationship'] == 'Wife'):
					    if (data['occupation'] == 'Other-service'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 277593):
						    if (data['hours_per_week'] > 25):
							return u'<=50K'
						    if (data['hours_per_week'] <= 25):
							return u'>50K'
						if (data['final_weight'] <= 277593):
						    return u'<=50K'
					    if (data['occupation'] != 'Other-service'):
						if (data['education_num'] > 10):
						    if (data['workclass'] == 'Private'):
							if (data['hours_per_week'] > 17):
							    return u'>50K'
							if (data['hours_per_week'] <= 17):
							    return u'<=50K'
						    if (data['workclass'] != 'Private'):
							return u'>50K'
						if (data['education_num'] <= 10):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 246277):
							return u'<=50K'
						    if (data['final_weight'] <= 246277):
							if (data['final_weight'] > 160968):
							    return u'>50K'
							if (data['final_weight'] <= 160968):
							    return u'<=50K'
					if (data['relationship'] != 'Wife'):
					    if (data['education_num'] > 10):
						if (data['age'] > 74):
						    return u'>50K'
						if (data['age'] <= 74):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 248273):
							if (data['final_weight'] > 300731):
							    return u'<=50K'
							if (data['final_weight'] <= 300731):
							    return u'>50K'
						    if (data['final_weight'] <= 248273):
							if (data['occupation'] == 'Craft-repair'):
							    return u'<=50K'
							if (data['occupation'] != 'Craft-repair'):
							    return u'<=50K'
					    if (data['education_num'] <= 10):
						if (data['hours_per_week'] > 22):
						    if (data['age'] > 71):
							return u'>50K'
						    if (data['age'] <= 71):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 117035):
							    return u'<=50K'
							if (data['final_weight'] <= 117035):
							    return u'<=50K'
						if (data['hours_per_week'] <= 22):
						    if (data['workclass'] == 'Self-emp-inc'):
							return u'>50K'
						    if (data['workclass'] != 'Self-emp-inc'):
							if (data['occupation'] == 'Tech-support'):
							    return u'>50K'
							if (data['occupation'] != 'Tech-support'):
							    return u'<=50K'
			if (data['education_num'] <= 9):
			    if (not 'relationship' in data or data['relationship'] is None):
				return u'<=50K'
			    if (data['relationship'] == 'Wife'):
				if (not 'final_weight' in data or data['final_weight'] is None):
				    return u'<=50K'
				if (data['final_weight'] > 100311):
				    if (not 'race' in data or data['race'] is None):
					return u'<=50K'
				    if (data['race'] == 'Black'):
					return u'<=50K'
				    if (data['race'] != 'Black'):
					if (data['hours_per_week'] > 6):
					    if (data['final_weight'] > 319929):
						if (data['age'] > 63):
						    return u'<=50K'
						if (data['age'] <= 63):
						    return u'>50K'
					    if (data['final_weight'] <= 319929):
						if (data['final_weight'] > 196858):
						    return u'<=50K'
						if (data['final_weight'] <= 196858):
						    if (not 'occupation' in data or data['occupation'] is None):
							return u'>50K'
						    if (data['occupation'] == 'Adm-clerical'):
							return u'>50K'
						    if (data['occupation'] != 'Adm-clerical'):
							if (data['age'] > 44):
							    return u'>50K'
							if (data['age'] <= 44):
							    return u'<=50K'
					if (data['hours_per_week'] <= 6):
					    return u'<=50K'
				if (data['final_weight'] <= 100311):
				    return u'<=50K'
			    if (data['relationship'] != 'Wife'):
				if (data['hours_per_week'] > 24):
				    if (not 'workclass' in data or data['workclass'] is None):
					return u'<=50K'
				    if (data['workclass'] == 'Self-emp-not-inc'):
					return u'<=50K'
				    if (data['workclass'] != 'Self-emp-not-inc'):
					if (not 'occupation' in data or data['occupation'] is None):
					    return u'<=50K'
					if (data['occupation'] == 'Tech-support'):
					    return u'>50K'
					if (data['occupation'] != 'Tech-support'):
					    if (data['occupation'] == 'Sales'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'>50K'
						if (data['final_weight'] > 174041):
						    return u'>50K'
						if (data['final_weight'] <= 174041):
						    if (data['final_weight'] > 125449):
							return u'<=50K'
						    if (data['final_weight'] <= 125449):
							return u'>50K'
					    if (data['occupation'] != 'Sales'):
						if (data['occupation'] == 'Exec-managerial'):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 149737):
							if (data['hours_per_week'] > 31):
							    return u'<=50K'
							if (data['hours_per_week'] <= 31):
							    return u'>50K'
						    if (data['final_weight'] <= 149737):
							return u'<=50K'
						if (data['occupation'] != 'Exec-managerial'):
						    if (data['occupation'] == 'Transport-moving'):
							if (data['hours_per_week'] > 26):
							    return u'<=50K'
							if (data['hours_per_week'] <= 26):
							    return u'>50K'
						    if (data['occupation'] != 'Transport-moving'):
							return u'<=50K'
				if (data['hours_per_week'] <= 24):
				    if (data['age'] > 60):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 189262):
					    return u'<=50K'
					if (data['final_weight'] <= 189262):
					    if (data['age'] > 69):
						return u'<=50K'
					    if (data['age'] <= 69):
						if (data['final_weight'] > 184498):
						    if (data['hours_per_week'] > 10):
							return u'>50K'
						    if (data['hours_per_week'] <= 10):
							return u'<=50K'
						if (data['final_weight'] <= 184498):
						    if (not 'occupation' in data or data['occupation'] is None):
							return u'<=50K'
						    if (data['occupation'] == 'Sales'):
							if (data['final_weight'] > 119561):
							    return u'<=50K'
							if (data['final_weight'] <= 119561):
							    return u'>50K'
						    if (data['occupation'] != 'Sales'):
							return u'<=50K'
				    if (data['age'] <= 60):
					return u'<=50K'
		if (data['age'] <= 35):
		    if (data['age'] > 24):
			if (data['education_num'] > 9):
			    if (not 'final_weight' in data or data['final_weight'] is None):
				return u'<=50K'
			    if (data['final_weight'] > 161578):
				if (data['age'] > 27):
				    if (not 'occupation' in data or data['occupation'] is None):
					return u'<=50K'
				    if (data['occupation'] == 'Prof-specialty'):
					if (data['age'] > 31):
					    if (data['education_num'] > 10):
						return u'>50K'
					    if (data['education_num'] <= 10):
						if (data['final_weight'] > 179211):
						    if (data['final_weight'] > 266240):
							if (not 'sex' in data or data['sex'] is None):
							    return u'>50K'
							if (data['sex'] == 'Male'):
							    return u'>50K'
							if (data['sex'] != 'Male'):
							    return u'<=50K'
						    if (data['final_weight'] <= 266240):
							if (not 'sex' in data or data['sex'] is None):
							    return u'<=50K'
							if (data['sex'] == 'Male'):
							    return u'<=50K'
							if (data['sex'] != 'Male'):
							    return u'>50K'
						if (data['final_weight'] <= 179211):
						    return u'>50K'
					if (data['age'] <= 31):
					    if (not 'education' in data or data['education'] is None):
						return u'<=50K'
					    if (data['education'] == 'Assoc-voc'):
						if (data['final_weight'] > 238521):
						    return u'<=50K'
						if (data['final_weight'] <= 238521):
						    return u'>50K'
					    if (data['education'] != 'Assoc-voc'):
						return u'<=50K'
				    if (data['occupation'] != 'Prof-specialty'):
					if (data['occupation'] == 'Exec-managerial'):
					    if (data['age'] > 29):
						if (not 'hours_per_week' in data or data['hours_per_week'] is None):
						    return u'>50K'
						if (data['hours_per_week'] > 59):
						    return u'>50K'
						if (data['hours_per_week'] <= 59):
						    if (not 'sex' in data or data['sex'] is None):
							return u'>50K'
						    if (data['sex'] == 'Male'):
							if (data['age'] > 34):
							    return u'<=50K'
							if (data['age'] <= 34):
							    return u'>50K'
						    if (data['sex'] != 'Male'):
							if (data['hours_per_week'] > 32):
							    return u'>50K'
							if (data['hours_per_week'] <= 32):
							    return u'<=50K'
					    if (data['age'] <= 29):
						if (data['final_weight'] > 292707):
						    return u'<=50K'
						if (data['final_weight'] <= 292707):
						    if (data['final_weight'] > 216328):
							return u'>50K'
						    if (data['final_weight'] <= 216328):
							return u'<=50K'
					if (data['occupation'] != 'Exec-managerial'):
					    if (data['final_weight'] > 347437):
						if (not 'hours_per_week' in data or data['hours_per_week'] is None):
						    return u'<=50K'
						if (data['hours_per_week'] > 58):
						    return u'<=50K'
						if (data['hours_per_week'] <= 58):
						    if (data['occupation'] == 'Transport-moving'):
							return u'>50K'
						    if (data['occupation'] != 'Transport-moving'):
							if (data['occupation'] == 'Tech-support'):
							    return u'>50K'
							if (data['occupation'] != 'Tech-support'):
							    return u'<=50K'
					    if (data['final_weight'] <= 347437):
						if (data['final_weight'] > 276672):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'<=50K'
						    if (data['workclass'] == 'Private'):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'Black'):
							    return u'>50K'
							if (data['race'] != 'Black'):
							    return u'<=50K'
						    if (data['workclass'] != 'Private'):
							if (data['final_weight'] > 287284):
							    return u'<=50K'
							if (data['final_weight'] <= 287284):
							    return u'<=50K'
						if (data['final_weight'] <= 276672):
						    if (data['occupation'] == 'Transport-moving'):
							if (data['final_weight'] > 196428):
							    return u'<=50K'
							if (data['final_weight'] <= 196428):
							    return u'<=50K'
						    if (data['occupation'] != 'Transport-moving'):
							if (data['occupation'] == 'Handlers-cleaners'):
							    return u'<=50K'
							if (data['occupation'] != 'Handlers-cleaners'):
							    return u'<=50K'
				if (data['age'] <= 27):
				    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
					return u'<=50K'
				    if (data['hours_per_week'] > 35):
					if (not 'occupation' in data or data['occupation'] is None):
					    return u'<=50K'
					if (data['occupation'] == 'Machine-op-inspct'):
					    return u'<=50K'
					if (data['occupation'] != 'Machine-op-inspct'):
					    if (data['occupation'] == 'Farming-fishing'):
						return u'<=50K'
					    if (data['occupation'] != 'Farming-fishing'):
						if (data['final_weight'] > 356600):
						    if (not 'race' in data or data['race'] is None):
							return u'<=50K'
						    if (data['race'] == 'White'):
							return u'<=50K'
						    if (data['race'] != 'White'):
							return u'>50K'
						if (data['final_weight'] <= 356600):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'<=50K'
						    if (data['workclass'] == 'Self-emp-not-inc'):
							return u'>50K'
						    if (data['workclass'] != 'Self-emp-not-inc'):
							if (data['occupation'] == 'Other-service'):
							    return u'<=50K'
							if (data['occupation'] != 'Other-service'):
							    return u'<=50K'
				    if (data['hours_per_week'] <= 35):
					return u'<=50K'
			    if (data['final_weight'] <= 161578):
				if (not 'occupation' in data or data['occupation'] is None):
				    return u'<=50K'
				if (data['occupation'] == 'Handlers-cleaners'):
				    if (data['final_weight'] > 110112):
					return u'<=50K'
				    if (data['final_weight'] <= 110112):
					if (data['final_weight'] > 106791):
					    return u'>50K'
					if (data['final_weight'] <= 106791):
					    if (data['age'] > 28):
						return u'<=50K'
					    if (data['age'] <= 28):
						if (not 'hours_per_week' in data or data['hours_per_week'] is None):
						    return u'<=50K'
						if (data['hours_per_week'] > 37):
						    return u'>50K'
						if (data['hours_per_week'] <= 37):
						    return u'<=50K'
				if (data['occupation'] != 'Handlers-cleaners'):
				    if (data['occupation'] == 'Craft-repair'):
					if (not 'race' in data or data['race'] is None):
					    return u'<=50K'
					if (data['race'] == 'Asian-Pac-Islander'):
					    if (data['final_weight'] > 78589):
						return u'>50K'
					    if (data['final_weight'] <= 78589):
						return u'<=50K'
					if (data['race'] != 'Asian-Pac-Islander'):
					    if (data['final_weight'] > 125556):
						if (not 'hours_per_week' in data or data['hours_per_week'] is None):
						    return u'<=50K'
						if (data['hours_per_week'] > 52):
						    if (data['hours_per_week'] > 56):
							if (data['final_weight'] > 156019):
							    return u'>50K'
							if (data['final_weight'] <= 156019):
							    return u'<=50K'
						    if (data['hours_per_week'] <= 56):
							return u'>50K'
						if (data['hours_per_week'] <= 52):
						    if (data['final_weight'] > 155058):
							if (data['education_num'] > 11):
							    return u'<=50K'
							if (data['education_num'] <= 11):
							    return u'>50K'
						    if (data['final_weight'] <= 155058):
							if (data['age'] > 30):
							    return u'<=50K'
							if (data['age'] <= 30):
							    return u'<=50K'
					    if (data['final_weight'] <= 125556):
						if (data['final_weight'] > 36471):
						    if (data['age'] > 34):
							if (data['final_weight'] > 92025):
							    return u'<=50K'
							if (data['final_weight'] <= 92025):
							    return u'<=50K'
						    if (data['age'] <= 34):
							return u'<=50K'
						if (data['final_weight'] <= 36471):
						    if (data['final_weight'] > 33960):
							return u'>50K'
						    if (data['final_weight'] <= 33960):
							return u'<=50K'
				    if (data['occupation'] != 'Craft-repair'):
					if (not 'race' in data or data['race'] is None):
					    return u'<=50K'
					if (data['race'] == 'Amer-Indian-Eskimo'):
					    return u'<=50K'
					if (data['race'] != 'Amer-Indian-Eskimo'):
					    if (data['final_weight'] > 27336):
						if (not 'hours_per_week' in data or data['hours_per_week'] is None):
						    return u'<=50K'
						if (data['hours_per_week'] > 71):
						    return u'<=50K'
						if (data['hours_per_week'] <= 71):
						    if (data['final_weight'] > 72220):
							if (data['final_weight'] > 105076):
							    return u'<=50K'
							if (data['final_weight'] <= 105076):
							    return u'<=50K'
						    if (data['final_weight'] <= 72220):
							if (data['hours_per_week'] > 30):
							    return u'<=50K'
							if (data['hours_per_week'] <= 30):
							    return u'>50K'
					    if (data['final_weight'] <= 27336):
						if (data['occupation'] == 'Tech-support'):
						    if (data['final_weight'] > 25752):
							return u'>50K'
						    if (data['final_weight'] <= 25752):
							return u'<=50K'
						if (data['occupation'] != 'Tech-support'):
						    return u'>50K'
			if (data['education_num'] <= 9):
			    if (data['age'] > 29):
				if (not 'hours_per_week' in data or data['hours_per_week'] is None):
				    return u'<=50K'
				if (data['hours_per_week'] > 46):
				    if (not 'occupation' in data or data['occupation'] is None):
					return u'<=50K'
				    if (data['occupation'] == 'Other-service'):
					return u'<=50K'
				    if (data['occupation'] != 'Other-service'):
					if (data['age'] > 31):
					    if (not 'race' in data or data['race'] is None):
						return u'<=50K'
					    if (data['race'] == 'Asian-Pac-Islander'):
						return u'>50K'
					    if (data['race'] != 'Asian-Pac-Islander'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 179600):
						    if (data['final_weight'] > 307521):
							if (data['final_weight'] > 450303):
							    return u'<=50K'
							if (data['final_weight'] <= 450303):
							    return u'>50K'
						    if (data['final_weight'] <= 307521):
							if (data['hours_per_week'] > 53):
							    return u'<=50K'
							if (data['hours_per_week'] <= 53):
							    return u'<=50K'
						if (data['final_weight'] <= 179600):
						    if (data['occupation'] == 'Machine-op-inspct'):
							return u'>50K'
						    if (data['occupation'] != 'Machine-op-inspct'):
							if (data['final_weight'] > 131740):
							    return u'>50K'
							if (data['final_weight'] <= 131740):
							    return u'<=50K'
					if (data['age'] <= 31):
					    if (data['occupation'] == 'Sales'):
						if (data['hours_per_week'] > 53):
						    return u'<=50K'
						if (data['hours_per_week'] <= 53):
						    return u'>50K'
					    if (data['occupation'] != 'Sales'):
						if (data['age'] > 30):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 123749):
							if (data['final_weight'] > 146895):
							    return u'<=50K'
							if (data['final_weight'] <= 146895):
							    return u'>50K'
						    if (data['final_weight'] <= 123749):
							return u'<=50K'
						if (data['age'] <= 30):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 135857):
							if (data['occupation'] == 'Protective-serv'):
							    return u'>50K'
							if (data['occupation'] != 'Protective-serv'):
							    return u'<=50K'
						    if (data['final_weight'] <= 135857):
							if (data['occupation'] == 'Craft-repair'):
							    return u'<=50K'
							if (data['occupation'] != 'Craft-repair'):
							    return u'>50K'
				if (data['hours_per_week'] <= 46):
				    if (not 'race' in data or data['race'] is None):
					return u'<=50K'
				    if (data['race'] == 'White'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 88709):
					    if (data['hours_per_week'] > 39):
						if (not 'sex' in data or data['sex'] is None):
						    return u'<=50K'
						if (data['sex'] == 'Male'):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'<=50K'
						    if (data['workclass'] == 'Private'):
							if (not 'occupation' in data or data['occupation'] is None):
							    return u'<=50K'
							if (data['occupation'] == 'Sales'):
							    return u'<=50K'
							if (data['occupation'] != 'Sales'):
							    return u'<=50K'
						    if (data['workclass'] != 'Private'):
							if (data['age'] > 31):
							    return u'<=50K'
							if (data['age'] <= 31):
							    return u'>50K'
						if (data['sex'] != 'Male'):
						    if (data['final_weight'] > 138188):
							if (not 'workclass' in data or data['workclass'] is None):
							    return u'<=50K'
							if (data['workclass'] == 'Private'):
							    return u'<=50K'
							if (data['workclass'] != 'Private'):
							    return u'>50K'
						    if (data['final_weight'] <= 138188):
							return u'>50K'
					    if (data['hours_per_week'] <= 39):
						if (data['hours_per_week'] > 21):
						    if (not 'occupation' in data or data['occupation'] is None):
							return u'<=50K'
						    if (data['occupation'] == 'Transport-moving'):
							if (data['final_weight'] > 150054):
							    return u'<=50K'
							if (data['final_weight'] <= 150054):
							    return u'>50K'
						    if (data['occupation'] != 'Transport-moving'):
							return u'<=50K'
						if (data['hours_per_week'] <= 21):
						    if (data['final_weight'] > 134194):
							if (not 'occupation' in data or data['occupation'] is None):
							    return u'<=50K'
							if (data['occupation'] == 'Sales'):
							    return u'<=50K'
							if (data['occupation'] != 'Sales'):
							    return u'>50K'
						    if (data['final_weight'] <= 134194):
							return u'<=50K'
					if (data['final_weight'] <= 88709):
					    if (not 'occupation' in data or data['occupation'] is None):
						return u'<=50K'
					    if (data['occupation'] == 'Tech-support'):
						return u'>50K'
					    if (data['occupation'] != 'Tech-support'):
						if (data['final_weight'] > 35476):
						    if (data['occupation'] == 'Sales'):
							if (data['hours_per_week'] > 42):
							    return u'<=50K'
							if (data['hours_per_week'] <= 42):
							    return u'>50K'
						    if (data['occupation'] != 'Sales'):
							return u'<=50K'
						if (data['final_weight'] <= 35476):
						    if (data['age'] > 34):
							return u'<=50K'
						    if (data['age'] <= 34):
							if (data['hours_per_week'] > 30):
							    return u'<=50K'
							if (data['hours_per_week'] <= 30):
							    return u'>50K'
				    if (data['race'] != 'White'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 102540):
					    if (data['age'] > 34):
						if (not 'workclass' in data or data['workclass'] is None):
						    return u'<=50K'
						if (data['workclass'] == 'Private'):
						    return u'<=50K'
						if (data['workclass'] != 'Private'):
						    return u'>50K'
					    if (data['age'] <= 34):
						return u'<=50K'
					if (data['final_weight'] <= 102540):
					    if (not 'workclass' in data or data['workclass'] is None):
						return u'<=50K'
					    if (data['workclass'] == 'Private'):
						if (not 'relationship' in data or data['relationship'] is None):
						    return u'<=50K'
						if (data['relationship'] == 'Husband'):
						    if (not 'occupation' in data or data['occupation'] is None):
							return u'>50K'
						    if (data['occupation'] == 'Adm-clerical'):
							if (data['race'] == 'Asian-Pac-Islander'):
							    return u'<=50K'
							if (data['race'] != 'Asian-Pac-Islander'):
							    return u'>50K'
						    if (data['occupation'] != 'Adm-clerical'):
							return u'>50K'
						if (data['relationship'] != 'Husband'):
						    return u'<=50K'
					    if (data['workclass'] != 'Private'):
						return u'<=50K'
			    if (data['age'] <= 29):
				if (not 'hours_per_week' in data or data['hours_per_week'] is None):
				    return u'<=50K'
				if (data['hours_per_week'] > 76):
				    if (data['hours_per_week'] > 90):
					return u'<=50K'
				    if (data['hours_per_week'] <= 90):
					return u'>50K'
				if (data['hours_per_week'] <= 76):
				    if (not 'occupation' in data or data['occupation'] is None):
					return u'<=50K'
				    if (data['occupation'] == 'Tech-support'):
					if (data['hours_per_week'] > 44):
					    return u'>50K'
					if (data['hours_per_week'] <= 44):
					    if (not 'workclass' in data or data['workclass'] is None):
						return u'<=50K'
					    if (data['workclass'] == 'Private'):
						return u'<=50K'
					    if (data['workclass'] != 'Private'):
						return u'>50K'
				    if (data['occupation'] != 'Tech-support'):
					if (data['occupation'] == 'Prof-specialty'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 213993):
						return u'>50K'
					    if (data['final_weight'] <= 213993):
						if (data['hours_per_week'] > 22):
						    return u'<=50K'
						if (data['hours_per_week'] <= 22):
						    return u'>50K'
					if (data['occupation'] != 'Prof-specialty'):
					    if (not 'workclass' in data or data['workclass'] is None):
						return u'<=50K'
					    if (data['workclass'] == 'Self-emp-inc'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 195818):
						    return u'>50K'
						if (data['final_weight'] <= 195818):
						    if (data['final_weight'] > 152851):
							return u'<=50K'
						    if (data['final_weight'] <= 152851):
							if (data['final_weight'] > 139872):
							    return u'>50K'
							if (data['final_weight'] <= 139872):
							    return u'<=50K'
					    if (data['workclass'] != 'Self-emp-inc'):
						if (data['hours_per_week'] > 25):
						    if (data['hours_per_week'] > 28):
							if (data['hours_per_week'] > 39):
							    return u'<=50K'
							if (data['hours_per_week'] <= 39):
							    return u'<=50K'
						    if (data['hours_per_week'] <= 28):
							return u'>50K'
						if (data['hours_per_week'] <= 25):
						    return u'<=50K'
		    if (data['age'] <= 24):
			if (not 'hours_per_week' in data or data['hours_per_week'] is None):
			    return u'<=50K'
			if (data['hours_per_week'] > 47):
			    if (data['education_num'] > 9):
				if (data['hours_per_week'] > 67):
				    return u'>50K'
				if (data['hours_per_week'] <= 67):
				    if (data['hours_per_week'] > 55):
					return u'<=50K'
				    if (data['hours_per_week'] <= 55):
					if (data['age'] > 21):
					    if (data['hours_per_week'] > 49):
						if (not 'occupation' in data or data['occupation'] is None):
						    return u'<=50K'
						if (data['occupation'] == 'Craft-repair'):
						    return u'>50K'
						if (data['occupation'] != 'Craft-repair'):
						    if (data['occupation'] == 'Farming-fishing'):
							return u'>50K'
						    if (data['occupation'] != 'Farming-fishing'):
							return u'<=50K'
					    if (data['hours_per_week'] <= 49):
						return u'>50K'
					if (data['age'] <= 21):
					    return u'<=50K'
			    if (data['education_num'] <= 9):
				if (not 'workclass' in data or data['workclass'] is None):
				    return u'<=50K'
				if (data['workclass'] == 'State-gov'):
				    return u'>50K'
				if (data['workclass'] != 'State-gov'):
				    if (not 'occupation' in data or data['occupation'] is None):
					return u'<=50K'
				    if (data['occupation'] == 'Craft-repair'):
					if (data['hours_per_week'] > 55):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 278850):
						return u'<=50K'
					    if (data['final_weight'] <= 278850):
						return u'>50K'
					if (data['hours_per_week'] <= 55):
					    return u'<=50K'
				    if (data['occupation'] != 'Craft-repair'):
					return u'<=50K'
			if (data['hours_per_week'] <= 47):
			    if (not 'final_weight' in data or data['final_weight'] is None):
				return u'<=50K'
			    if (data['final_weight'] > 532050):
				return u'>50K'
			    if (data['final_weight'] <= 532050):
				if (data['age'] > 22):
				    if (data['hours_per_week'] > 39):
					if (not 'occupation' in data or data['occupation'] is None):
					    return u'<=50K'
					if (data['occupation'] == 'Craft-repair'):
					    return u'<=50K'
					if (data['occupation'] != 'Craft-repair'):
					    if (not 'race' in data or data['race'] is None):
						return u'<=50K'
					    if (data['race'] == 'White'):
						if (data['occupation'] == 'Prof-specialty'):
						    if (not 'sex' in data or data['sex'] is None):
							return u'<=50K'
						    if (data['sex'] == 'Male'):
							return u'<=50K'
						    if (data['sex'] != 'Male'):
							return u'>50K'
						if (data['occupation'] != 'Prof-specialty'):
						    if (data['final_weight'] > 66228):
							if (not 'relationship' in data or data['relationship'] is None):
							    return u'<=50K'
							if (data['relationship'] == 'Husband'):
							    return u'<=50K'
							if (data['relationship'] != 'Husband'):
							    return u'<=50K'
						    if (data['final_weight'] <= 66228):
							if (not 'sex' in data or data['sex'] is None):
							    return u'<=50K'
							if (data['sex'] == 'Male'):
							    return u'<=50K'
							if (data['sex'] != 'Male'):
							    return u'>50K'
					    if (data['race'] != 'White'):
						return u'<=50K'
				    if (data['hours_per_week'] <= 39):
					return u'<=50K'
				if (data['age'] <= 22):
				    return u'<=50K'
	    if (data['education_num'] <= 8):
		if (not 'age' in data or data['age'] is None):
		    return u'<=50K'
		if (data['age'] > 37):
		    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
			return u'<=50K'
		    if (data['hours_per_week'] > 21):
			if (data['education_num'] > 5):
			    if (not 'final_weight' in data or data['final_weight'] is None):
				return u'<=50K'
			    if (data['final_weight'] > 420456):
				if (data['final_weight'] > 441218):
				    if (data['age'] > 52):
					if (not 'occupation' in data or data['occupation'] is None):
					    return u'>50K'
					if (data['occupation'] == 'Adm-clerical'):
					    return u'<=50K'
					if (data['occupation'] != 'Adm-clerical'):
					    return u'>50K'
				    if (data['age'] <= 52):
					return u'<=50K'
				if (data['final_weight'] <= 441218):
				    return u'>50K'
			    if (data['final_weight'] <= 420456):
				if (not 'occupation' in data or data['occupation'] is None):
				    return u'<=50K'
				if (data['occupation'] == 'Prof-specialty'):
				    if (data['hours_per_week'] > 50):
					return u'<=50K'
				    if (data['hours_per_week'] <= 50):
					return u'>50K'
				if (data['occupation'] != 'Prof-specialty'):
				    if (data['hours_per_week'] > 62):
					return u'<=50K'
				    if (data['hours_per_week'] <= 62):
					if (not 'workclass' in data or data['workclass'] is None):
					    return u'<=50K'
					if (data['workclass'] == 'Local-gov'):
					    if (data['age'] > 61):
						if (data['hours_per_week'] > 37):
						    return u'>50K'
						if (data['hours_per_week'] <= 37):
						    return u'<=50K'
					    if (data['age'] <= 61):
						return u'<=50K'
					if (data['workclass'] != 'Local-gov'):
					    if (not 'education' in data or data['education'] is None):
						return u'<=50K'
					    if (data['education'] == '11th'):
						if (data['occupation'] == 'Machine-op-inspct'):
						    return u'<=50K'
						if (data['occupation'] != 'Machine-op-inspct'):
						    if (data['final_weight'] > 140443):
							if (data['occupation'] == 'Craft-repair'):
							    return u'<=50K'
							if (data['occupation'] != 'Craft-repair'):
							    return u'<=50K'
						    if (data['final_weight'] <= 140443):
							if (data['occupation'] == 'Transport-moving'):
							    return u'<=50K'
							if (data['occupation'] != 'Transport-moving'):
							    return u'<=50K'
					    if (data['education'] != '11th'):
						if (data['age'] > 59):
						    if (data['age'] > 63):
							if (data['occupation'] == 'Transport-moving'):
							    return u'>50K'
							if (data['occupation'] != 'Transport-moving'):
							    return u'<=50K'
						    if (data['age'] <= 63):
							if (data['workclass'] == 'Self-emp-not-inc'):
							    return u'<=50K'
							if (data['workclass'] != 'Self-emp-not-inc'):
							    return u'<=50K'
						if (data['age'] <= 59):
						    if (data['occupation'] == 'Farming-fishing'):
							return u'<=50K'
						    if (data['occupation'] != 'Farming-fishing'):
							if (data['age'] > 57):
							    return u'<=50K'
							if (data['age'] <= 57):
							    return u'<=50K'
			if (data['education_num'] <= 5):
			    if (data['hours_per_week'] > 54):
				if (data['age'] > 43):
				    if (not 'final_weight' in data or data['final_weight'] is None):
					return u'<=50K'
				    if (data['final_weight'] > 293546):
					return u'>50K'
				    if (data['final_weight'] <= 293546):
					if (not 'education' in data or data['education'] is None):
					    return u'<=50K'
					if (data['education'] == '1st-4th'):
					    return u'>50K'
					if (data['education'] != '1st-4th'):
					    if (data['final_weight'] > 30383):
						if (not 'occupation' in data or data['occupation'] is None):
						    return u'<=50K'
						if (data['occupation'] == 'Transport-moving'):
						    if (data['age'] > 54):
							return u'>50K'
						    if (data['age'] <= 54):
							if (data['hours_per_week'] > 72):
							    return u'>50K'
							if (data['hours_per_week'] <= 72):
							    return u'<=50K'
						if (data['occupation'] != 'Transport-moving'):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'<=50K'
						    if (data['workclass'] == 'Private'):
							return u'<=50K'
						    if (data['workclass'] != 'Private'):
							if (data['final_weight'] > 97891):
							    return u'>50K'
							if (data['final_weight'] <= 97891):
							    return u'<=50K'
					    if (data['final_weight'] <= 30383):
						return u'>50K'
				if (data['age'] <= 43):
				    return u'<=50K'
			    if (data['hours_per_week'] <= 54):
				if (not 'workclass' in data or data['workclass'] is None):
				    return u'<=50K'
				if (data['workclass'] == 'Self-emp-inc'):
				    if (not 'occupation' in data or data['occupation'] is None):
					return u'<=50K'
				    if (data['occupation'] == 'Craft-repair'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'>50K'
					if (data['final_weight'] > 196163):
					    return u'<=50K'
					if (data['final_weight'] <= 196163):
					    return u'>50K'
				    if (data['occupation'] != 'Craft-repair'):
					if (data['occupation'] == 'Sales'):
					    return u'>50K'
					if (data['occupation'] != 'Sales'):
					    return u'<=50K'
				if (data['workclass'] != 'Self-emp-inc'):
				    if (not 'occupation' in data or data['occupation'] is None):
					return u'<=50K'
				    if (data['occupation'] == 'Exec-managerial'):
					if (data['age'] > 52):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'>50K'
					    if (data['final_weight'] > 157949):
						return u'>50K'
					    if (data['final_weight'] <= 157949):
						if (data['hours_per_week'] > 44):
						    return u'>50K'
						if (data['hours_per_week'] <= 44):
						    return u'<=50K'
					if (data['age'] <= 52):
					    return u'<=50K'
				    if (data['occupation'] != 'Exec-managerial'):
					if (data['workclass'] == 'Federal-gov'):
					    return u'>50K'
					if (data['workclass'] != 'Federal-gov'):
					    if (data['occupation'] == 'Sales'):
						if (data['age'] > 58):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'>50K'
						    if (data['final_weight'] > 104904):
							return u'>50K'
						    if (data['final_weight'] <= 104904):
							if (data['hours_per_week'] > 35):
							    return u'<=50K'
							if (data['hours_per_week'] <= 35):
							    return u'>50K'
						if (data['age'] <= 58):
						    return u'<=50K'
					    if (data['occupation'] != 'Sales'):
						if (data['age'] > 66):
						    return u'<=50K'
						if (data['age'] <= 66):
						    if (data['workclass'] == 'Self-emp-not-inc'):
							if (data['occupation'] == 'Transport-moving'):
							    return u'>50K'
							if (data['occupation'] != 'Transport-moving'):
							    return u'<=50K'
						    if (data['workclass'] != 'Self-emp-not-inc'):
							if (data['occupation'] == 'Transport-moving'):
							    return u'<=50K'
							if (data['occupation'] != 'Transport-moving'):
							    return u'<=50K'
		    if (data['hours_per_week'] <= 21):
			return u'<=50K'
		if (data['age'] <= 37):
		    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
			return u'<=50K'
		    if (data['hours_per_week'] > 43):
			if (not 'workclass' in data or data['workclass'] is None):
			    return u'<=50K'
			if (data['workclass'] == 'Private'):
			    if (data['hours_per_week'] > 44):
				if (not 'relationship' in data or data['relationship'] is None):
				    return u'<=50K'
				if (data['relationship'] == 'Not-in-family'):
				    return u'>50K'
				if (data['relationship'] != 'Not-in-family'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
					return u'<=50K'
				    if (data['final_weight'] > 237345):
					return u'<=50K'
				    if (data['final_weight'] <= 237345):
					if (data['final_weight'] > 223724):
					    if (not 'occupation' in data or data['occupation'] is None):
						return u'>50K'
					    if (data['occupation'] == 'Exec-managerial'):
						return u'<=50K'
					    if (data['occupation'] != 'Exec-managerial'):
						return u'>50K'
					if (data['final_weight'] <= 223724):
					    if (data['relationship'] == 'Own-child'):
						return u'>50K'
					    if (data['relationship'] != 'Own-child'):
						if (not 'occupation' in data or data['occupation'] is None):
						    return u'<=50K'
						if (data['occupation'] == 'Exec-managerial'):
						    if (data['hours_per_week'] > 52):
							return u'<=50K'
						    if (data['hours_per_week'] <= 52):
							return u'>50K'
						if (data['occupation'] != 'Exec-managerial'):
						    if (data['hours_per_week'] > 46):
							return u'<=50K'
						    if (data['hours_per_week'] <= 46):
							if (not 'education' in data or data['education'] is None):
							    return u'<=50K'
							if (data['education'] == '10th'):
							    return u'>50K'
							if (data['education'] != '10th'):
							    return u'<=50K'
			    if (data['hours_per_week'] <= 44):
				return u'>50K'
			if (data['workclass'] != 'Private'):
			    if (data['age'] > 35):
				return u'>50K'
			    if (data['age'] <= 35):
				if (not 'final_weight' in data or data['final_weight'] is None):
				    return u'<=50K'
				if (data['final_weight'] > 208210):
				    if (data['final_weight'] > 312494):
					return u'<=50K'
				    if (data['final_weight'] <= 312494):
					if (data['education_num'] > 6):
					    return u'>50K'
					if (data['education_num'] <= 6):
					    if (data['education_num'] > 3):
						return u'<=50K'
					    if (data['education_num'] <= 3):
						return u'>50K'
				if (data['final_weight'] <= 208210):
				    return u'<=50K'
		    if (data['hours_per_week'] <= 43):
			if (not 'occupation' in data or data['occupation'] is None):
			    return u'<=50K'
			if (data['occupation'] == 'Tech-support'):
			    if (not 'final_weight' in data or data['final_weight'] is None):
				return u'<=50K'
			    if (data['final_weight'] > 273083):
				return u'>50K'
			    if (data['final_weight'] <= 273083):
				return u'<=50K'
			if (data['occupation'] != 'Tech-support'):
			    if (not 'final_weight' in data or data['final_weight'] is None):
				return u'<=50K'
			    if (data['final_weight'] > 188653):
				if (data['occupation'] == 'Adm-clerical'):
				    if (not 'sex' in data or data['sex'] is None):
					return u'<=50K'
				    if (data['sex'] == 'Male'):
					return u'>50K'
				    if (data['sex'] != 'Male'):
					return u'<=50K'
				if (data['occupation'] != 'Adm-clerical'):
				    if (data['occupation'] == 'Sales'):
					if (data['education_num'] > 7):
					    return u'>50K'
					if (data['education_num'] <= 7):
					    return u'<=50K'
				    if (data['occupation'] != 'Sales'):
					if (not 'workclass' in data or data['workclass'] is None):
					    return u'<=50K'
					if (data['workclass'] == 'Self-emp-not-inc'):
					    if (data['occupation'] == 'Transport-moving'):
						if (data['education_num'] > 5):
						    return u'<=50K'
						if (data['education_num'] <= 5):
						    return u'>50K'
					    if (data['occupation'] != 'Transport-moving'):
						return u'<=50K'
					if (data['workclass'] != 'Self-emp-not-inc'):
					    return u'<=50K'
			    if (data['final_weight'] <= 188653):
				if (data['final_weight'] > 159477):
				    if (data['occupation'] == 'Craft-repair'):
					if (data['age'] > 30):
					    if (data['final_weight'] > 185266):
						return u'>50K'
					    if (data['final_weight'] <= 185266):
						return u'<=50K'
					if (data['age'] <= 30):
					    return u'>50K'
				    if (data['occupation'] != 'Craft-repair'):
					return u'<=50K'
				if (data['final_weight'] <= 159477):
				    if (data['occupation'] == 'Machine-op-inspct'):
					if (data['final_weight'] > 106298):
					    return u'<=50K'
					if (data['final_weight'] <= 106298):
					    if (data['education_num'] > 4):
						return u'<=50K'
					    if (data['education_num'] <= 4):
						return u'>50K'
				    if (data['occupation'] != 'Machine-op-inspct'):
					if (data['occupation'] == 'Transport-moving'):
					    if (data['final_weight'] > 114645):
						if (not 'race' in data or data['race'] is None):
						    return u'<=50K'
						if (data['race'] == 'White'):
						    return u'>50K'
						if (data['race'] != 'White'):
						    return u'<=50K'
					    if (data['final_weight'] <= 114645):
						return u'<=50K'
					if (data['occupation'] != 'Transport-moving'):
					    return u'<=50K'
    if (data['marital_status'] != 'Married-civ-spouse'):
	if (not 'education_num' in data or data['education_num'] is None):
	    return u'<=50K'
	if (data['education_num'] > 12):
	    if (not 'age' in data or data['age'] is None):
		return u'<=50K'
	    if (data['age'] > 28):
		if (not 'hours_per_week' in data or data['hours_per_week'] is None):
		    return u'<=50K'
		if (data['hours_per_week'] > 43):
		    if (not 'occupation' in data or data['occupation'] is None):
			return u'<=50K'
		    if (data['occupation'] == 'Exec-managerial'):
			if (data['age'] > 48):
			    if (data['hours_per_week'] > 73):
				return u'<=50K'
			    if (data['hours_per_week'] <= 73):
				if (not 'final_weight' in data or data['final_weight'] is None):
				    return u'>50K'
				if (data['final_weight'] > 337482):
				    return u'<=50K'
				if (data['final_weight'] <= 337482):
				    if (data['hours_per_week'] > 47):
					if (data['education_num'] > 13):
					    if (data['age'] > 50):
						return u'>50K'
					    if (data['age'] <= 50):
						if (not 'sex' in data or data['sex'] is None):
						    return u'>50K'
						if (data['sex'] == 'Male'):
						    return u'>50K'
						if (data['sex'] != 'Male'):
						    if (not 'race' in data or data['race'] is None):
							return u'<=50K'
						    if (data['race'] == 'White'):
							return u'<=50K'
						    if (data['race'] != 'White'):
							return u'>50K'
					if (data['education_num'] <= 13):
					    if (data['age'] > 50):
						if (data['hours_per_week'] > 57):
						    return u'<=50K'
						if (data['hours_per_week'] <= 57):
						    if (data['final_weight'] > 74715):
							if (not 'race' in data or data['race'] is None):
							    return u'>50K'
							if (data['race'] == 'Asian-Pac-Islander'):
							    return u'<=50K'
							if (data['race'] != 'Asian-Pac-Islander'):
							    return u'>50K'
						    if (data['final_weight'] <= 74715):
							return u'<=50K'
					    if (data['age'] <= 50):
						return u'>50K'
				    if (data['hours_per_week'] <= 47):
					return u'>50K'
			if (data['age'] <= 48):
			    if (data['education_num'] > 13):
				if (data['age'] > 30):
				    if (not 'final_weight' in data or data['final_weight'] is None):
					return u'>50K'
				    if (data['final_weight'] > 302223):
					return u'<=50K'
				    if (data['final_weight'] <= 302223):
					if (data['hours_per_week'] > 55):
					    return u'>50K'
					if (data['hours_per_week'] <= 55):
					    if (data['final_weight'] > 264830):
						return u'>50K'
					    if (data['final_weight'] <= 264830):
						if (not 'relationship' in data or data['relationship'] is None):
						    return u'>50K'
						if (data['relationship'] == 'Unmarried'):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'<=50K'
						    if (data['workclass'] == 'Private'):
							return u'<=50K'
						    if (data['workclass'] != 'Private'):
							return u'>50K'
						if (data['relationship'] != 'Unmarried'):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'>50K'
						    if (data['workclass'] == 'State-gov'):
							return u'<=50K'
						    if (data['workclass'] != 'State-gov'):
							if (data['final_weight'] > 125475):
							    return u'>50K'
							if (data['final_weight'] <= 125475):
							    return u'>50K'
				if (data['age'] <= 30):
				    return u'<=50K'
			    if (data['education_num'] <= 13):
				if (not 'workclass' in data or data['workclass'] is None):
				    return u'<=50K'
				if (data['workclass'] == 'Private'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
					return u'>50K'
				    if (data['final_weight'] > 241717):
					if (data['final_weight'] > 572687):
					    return u'>50K'
					if (data['final_weight'] <= 572687):
					    if (data['age'] > 42):
						return u'>50K'
					    if (data['age'] <= 42):
						if (data['hours_per_week'] > 46):
						    if (data['hours_per_week'] > 52):
							return u'<=50K'
						    if (data['hours_per_week'] <= 52):
							if (data['marital_status'] == 'Never-married'):
							    return u'<=50K'
							if (data['marital_status'] != 'Never-married'):
							    return u'>50K'
						if (data['hours_per_week'] <= 46):
						    return u'<=50K'
				    if (data['final_weight'] <= 241717):
					if (data['final_weight'] > 215534):
					    return u'>50K'
					if (data['final_weight'] <= 215534):
					    if (data['final_weight'] > 142003):
						if (data['final_weight'] > 158101):
						    if (data['final_weight'] > 162787):
							if (data['marital_status'] == 'Never-married'):
							    return u'<=50K'
							if (data['marital_status'] != 'Never-married'):
							    return u'>50K'
						    if (data['final_weight'] <= 162787):
							return u'>50K'
						if (data['final_weight'] <= 158101):
						    return u'<=50K'
					    if (data['final_weight'] <= 142003):
						if (data['hours_per_week'] > 57):
						    return u'>50K'
						if (data['hours_per_week'] <= 57):
						    if (data['final_weight'] > 128794):
							return u'>50K'
						    if (data['final_weight'] <= 128794):
							if (data['hours_per_week'] > 52):
							    return u'<=50K'
							if (data['hours_per_week'] <= 52):
							    return u'>50K'
				if (data['workclass'] != 'Private'):
				    if (data['age'] > 41):
					if (not 'sex' in data or data['sex'] is None):
					    return u'<=50K'
					if (data['sex'] == 'Male'):
					    if (data['workclass'] == 'Self-emp-inc'):
						return u'>50K'
					    if (data['workclass'] != 'Self-emp-inc'):
						if (data['marital_status'] == 'Divorced'):
						    return u'<=50K'
						if (data['marital_status'] != 'Divorced'):
						    if (data['age'] > 46):
							return u'>50K'
						    if (data['age'] <= 46):
							if (data['marital_status'] == 'Separated'):
							    return u'>50K'
							if (data['marital_status'] != 'Separated'):
							    return u'<=50K'
					if (data['sex'] != 'Male'):
					    return u'<=50K'
				    if (data['age'] <= 41):
					return u'<=50K'
		    if (data['occupation'] != 'Exec-managerial'):
			if (data['education_num'] > 14):
			    if (data['age'] > 32):
				if (data['hours_per_week'] > 89):
				    return u'<=50K'
				if (data['hours_per_week'] <= 89):
				    if (not 'workclass' in data or data['workclass'] is None):
					return u'>50K'
				    if (data['workclass'] == 'Federal-gov'):
					return u'>50K'
				    if (data['workclass'] != 'Federal-gov'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'>50K'
					if (data['final_weight'] > 39435):
					    if (data['hours_per_week'] > 68):
						return u'>50K'
					    if (data['hours_per_week'] <= 68):
						if (data['final_weight'] > 75227):
						    if (data['age'] > 35):
							if (data['marital_status'] == 'Never-married'):
							    return u'>50K'
							if (data['marital_status'] != 'Never-married'):
							    return u'>50K'
						    if (data['age'] <= 35):
							return u'>50K'
						if (data['final_weight'] <= 75227):
						    if (data['workclass'] == 'Self-emp-inc'):
							return u'>50K'
						    if (data['workclass'] != 'Self-emp-inc'):
							return u'<=50K'
					if (data['final_weight'] <= 39435):
					    return u'<=50K'
			    if (data['age'] <= 32):
				if (data['marital_status'] == 'Divorced'):
				    if (not 'relationship' in data or data['relationship'] is None):
					return u'>50K'
				    if (data['relationship'] == 'Not-in-family'):
					return u'>50K'
				    if (data['relationship'] != 'Not-in-family'):
					return u'<=50K'
				if (data['marital_status'] != 'Divorced'):
				    if (data['hours_per_week'] > 52):
					return u'<=50K'
				    if (data['hours_per_week'] <= 52):
					if (not 'sex' in data or data['sex'] is None):
					    return u'<=50K'
					if (data['sex'] == 'Male'):
					    if (not 'workclass' in data or data['workclass'] is None):
						return u'>50K'
					    if (data['workclass'] == 'Private'):
						if (data['hours_per_week'] > 47):
						    return u'<=50K'
						if (data['hours_per_week'] <= 47):
						    return u'>50K'
					    if (data['workclass'] != 'Private'):
						return u'>50K'
					if (data['sex'] != 'Male'):
					    return u'<=50K'
			if (data['education_num'] <= 14):
			    if (not 'sex' in data or data['sex'] is None):
				return u'<=50K'
			    if (data['sex'] == 'Male'):
				if (data['hours_per_week'] > 44):
				    if (not 'relationship' in data or data['relationship'] is None):
					return u'<=50K'
				    if (data['relationship'] == 'Own-child'):
					if (data['age'] > 45):
					    if (data['hours_per_week'] > 55):
						return u'<=50K'
					    if (data['hours_per_week'] <= 55):
						return u'>50K'
					if (data['age'] <= 45):
					    return u'<=50K'
				    if (data['relationship'] != 'Own-child'):
					if (data['age'] > 55):
					    if (data['age'] > 58):
						if (data['education_num'] > 13):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'<=50K'
						    if (data['workclass'] == 'Self-emp-inc'):
							return u'>50K'
						    if (data['workclass'] != 'Self-emp-inc'):
							return u'<=50K'
						if (data['education_num'] <= 13):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'>50K'
						    if (data['final_weight'] > 313729):
							return u'<=50K'
						    if (data['final_weight'] <= 313729):
							if (not 'workclass' in data or data['workclass'] is None):
							    return u'>50K'
							if (data['workclass'] == 'Self-emp-inc'):
							    return u'<=50K'
							if (data['workclass'] != 'Self-emp-inc'):
							    return u'>50K'
					    if (data['age'] <= 58):
						return u'<=50K'
					if (data['age'] <= 55):
					    if (data['age'] > 44):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'>50K'
						if (data['final_weight'] > 246234):
						    if (data['hours_per_week'] > 47):
							return u'>50K'
						    if (data['hours_per_week'] <= 47):
							if (data['occupation'] == 'Prof-specialty'):
							    return u'<=50K'
							if (data['occupation'] != 'Prof-specialty'):
							    return u'>50K'
						if (data['final_weight'] <= 246234):
						    if (data['age'] > 46):
							if (data['hours_per_week'] > 47):
							    return u'<=50K'
							if (data['hours_per_week'] <= 47):
							    return u'<=50K'
						    if (data['age'] <= 46):
							if (not 'workclass' in data or data['workclass'] is None):
							    return u'>50K'
							if (data['workclass'] == 'Self-emp-not-inc'):
							    return u'<=50K'
							if (data['workclass'] != 'Self-emp-not-inc'):
							    return u'>50K'
					    if (data['age'] <= 44):
						if (not 'workclass' in data or data['workclass'] is None):
						    return u'<=50K'
						if (data['workclass'] == 'State-gov'):
						    return u'<=50K'
						if (data['workclass'] != 'State-gov'):
						    if (data['workclass'] == 'Local-gov'):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'Black'):
							    return u'>50K'
							if (data['race'] != 'Black'):
							    return u'<=50K'
						    if (data['workclass'] != 'Local-gov'):
							if (data['occupation'] == 'Tech-support'):
							    return u'<=50K'
							if (data['occupation'] != 'Tech-support'):
							    return u'<=50K'
				if (data['hours_per_week'] <= 44):
				    return u'>50K'
			    if (data['sex'] != 'Male'):
				if (not 'final_weight' in data or data['final_weight'] is None):
				    return u'<=50K'
				if (data['final_weight'] > 40849):
				    if (data['age'] > 48):
					if (data['age'] > 58):
					    if (data['hours_per_week'] > 57):
						return u'>50K'
					    if (data['hours_per_week'] <= 57):
						if (data['marital_status'] == 'Never-married'):
						    return u'>50K'
						if (data['marital_status'] != 'Never-married'):
						    if (data['hours_per_week'] > 49):
							return u'<=50K'
						    if (data['hours_per_week'] <= 49):
							if (data['final_weight'] > 184976):
							    return u'<=50K'
							if (data['final_weight'] <= 184976):
							    return u'>50K'
					if (data['age'] <= 58):
					    if (not 'race' in data or data['race'] is None):
						return u'<=50K'
					    if (data['race'] == 'Amer-Indian-Eskimo'):
						return u'>50K'
					    if (data['race'] != 'Amer-Indian-Eskimo'):
						return u'<=50K'
				    if (data['age'] <= 48):
					if (data['final_weight'] > 278879):
					    if (data['occupation'] == 'Prof-specialty'):
						if (data['education_num'] > 13):
						    return u'<=50K'
						if (data['education_num'] <= 13):
						    if (data['hours_per_week'] > 46):
							return u'>50K'
						    if (data['hours_per_week'] <= 46):
							if (data['marital_status'] == 'Never-married'):
							    return u'<=50K'
							if (data['marital_status'] != 'Never-married'):
							    return u'>50K'
					    if (data['occupation'] != 'Prof-specialty'):
						if (not 'race' in data or data['race'] is None):
						    return u'>50K'
						if (data['race'] == 'White'):
						    if (data['occupation'] == 'Adm-clerical'):
							if (data['education_num'] > 13):
							    return u'>50K'
							if (data['education_num'] <= 13):
							    return u'<=50K'
						    if (data['occupation'] != 'Adm-clerical'):
							return u'>50K'
						if (data['race'] != 'White'):
						    return u'<=50K'
					if (data['final_weight'] <= 278879):
					    if (data['final_weight'] > 243739):
						return u'<=50K'
					    if (data['final_weight'] <= 243739):
						if (data['final_weight'] > 221142):
						    if (data['final_weight'] > 227347):
							if (data['hours_per_week'] > 52):
							    return u'>50K'
							if (data['hours_per_week'] <= 52):
							    return u'<=50K'
						    if (data['final_weight'] <= 227347):
							if (data['occupation'] == 'Prof-specialty'):
							    return u'>50K'
							if (data['occupation'] != 'Prof-specialty'):
							    return u'<=50K'
						if (data['final_weight'] <= 221142):
						    if (data['age'] > 34):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'Black'):
							    return u'>50K'
							if (data['race'] != 'Black'):
							    return u'<=50K'
						    if (data['age'] <= 34):
							if (data['hours_per_week'] > 48):
							    return u'<=50K'
							if (data['hours_per_week'] <= 48):
							    return u'<=50K'
				if (data['final_weight'] <= 40849):
				    return u'<=50K'
		if (data['hours_per_week'] <= 43):
		    if (data['education_num'] > 14):
			if (data['age'] > 32):
			    if (not 'sex' in data or data['sex'] is None):
				return u'<=50K'
			    if (data['sex'] == 'Male'):
				if (data['age'] > 54):
				    if (data['marital_status'] == 'Married-spouse-absent'):
					return u'>50K'
				    if (data['marital_status'] != 'Married-spouse-absent'):
					return u'<=50K'
				if (data['age'] <= 54):
				    if (not 'relationship' in data or data['relationship'] is None):
					return u'>50K'
				    if (data['relationship'] == 'Not-in-family'):
					if (not 'workclass' in data or data['workclass'] is None):
					    return u'>50K'
					if (data['workclass'] == 'State-gov'):
					    return u'<=50K'
					if (data['workclass'] != 'State-gov'):
					    if (data['workclass'] == 'Self-emp-inc'):
						return u'<=50K'
					    if (data['workclass'] != 'Self-emp-inc'):
						if (data['marital_status'] == 'Divorced'):
						    if (not 'occupation' in data or data['occupation'] is None):
							return u'<=50K'
						    if (data['occupation'] == 'Prof-specialty'):
							return u'>50K'
						    if (data['occupation'] != 'Prof-specialty'):
							return u'<=50K'
						if (data['marital_status'] != 'Divorced'):
						    if (data['workclass'] == 'Local-gov'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 193280):
							    return u'<=50K'
							if (data['final_weight'] <= 193280):
							    return u'>50K'
						    if (data['workclass'] != 'Local-gov'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'>50K'
							if (data['final_weight'] > 107043):
							    return u'>50K'
							if (data['final_weight'] <= 107043):
							    return u'>50K'
				    if (data['relationship'] != 'Not-in-family'):
					return u'>50K'
			    if (data['sex'] != 'Male'):
				if (data['education_num'] > 15):
				    if (data['marital_status'] == 'Never-married'):
					if (not 'race' in data or data['race'] is None):
					    return u'>50K'
					if (data['race'] == 'White'):
					    return u'>50K'
					if (data['race'] != 'White'):
					    return u'<=50K'
				    if (data['marital_status'] != 'Never-married'):
					if (data['age'] > 54):
					    return u'<=50K'
					if (data['age'] <= 54):
					    if (data['age'] > 42):
						if (data['marital_status'] == 'Married-spouse-absent'):
						    return u'<=50K'
						if (data['marital_status'] != 'Married-spouse-absent'):
						    return u'>50K'
					    if (data['age'] <= 42):
						return u'<=50K'
				if (data['education_num'] <= 15):
				    if (data['marital_status'] == 'Never-married'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 174189):
					    if (data['final_weight'] > 192060):
						return u'<=50K'
					    if (data['final_weight'] <= 192060):
						return u'>50K'
					if (data['final_weight'] <= 174189):
					    return u'<=50K'
				    if (data['marital_status'] != 'Never-married'):
					return u'<=50K'
			if (data['age'] <= 32):
			    return u'<=50K'
		    if (data['education_num'] <= 14):
			if (data['age'] > 44):
			    if (data['hours_per_week'] > 31):
				if (not 'occupation' in data or data['occupation'] is None):
				    return u'<=50K'
				if (data['occupation'] == 'Other-service'):
				    return u'<=50K'
				if (data['occupation'] != 'Other-service'):
				    if (not 'sex' in data or data['sex'] is None):
					return u'<=50K'
				    if (data['sex'] == 'Male'):
					if (not 'workclass' in data or data['workclass'] is None):
					    return u'<=50K'
					if (data['workclass'] == 'Self-emp-not-inc'):
					    return u'<=50K'
					if (data['workclass'] != 'Self-emp-not-inc'):
					    if (not 'race' in data or data['race'] is None):
						return u'<=50K'
					    if (data['race'] == 'White'):
						if (data['marital_status'] == 'Widowed'):
						    return u'>50K'
						if (data['marital_status'] != 'Widowed'):
						    if (data['education_num'] > 13):
							if (data['occupation'] == 'Prof-specialty'):
							    return u'>50K'
							if (data['occupation'] != 'Prof-specialty'):
							    return u'<=50K'
						    if (data['education_num'] <= 13):
							if (data['occupation'] == 'Sales'):
							    return u'>50K'
							if (data['occupation'] != 'Sales'):
							    return u'<=50K'
					    if (data['race'] != 'White'):
						if (data['age'] > 48):
						    return u'<=50K'
						if (data['age'] <= 48):
						    if (data['education_num'] > 13):
							return u'<=50K'
						    if (data['education_num'] <= 13):
							return u'>50K'
				    if (data['sex'] != 'Male'):
					if (data['marital_status'] == 'Divorced'):
					    if (not 'relationship' in data or data['relationship'] is None):
						return u'<=50K'
					    if (data['relationship'] == 'Not-in-family'):
						if (not 'workclass' in data or data['workclass'] is None):
						    return u'<=50K'
						if (data['workclass'] == 'State-gov'):
						    if (data['age'] > 48):
							return u'<=50K'
						    if (data['age'] <= 48):
							if (data['occupation'] == 'Exec-managerial'):
							    return u'>50K'
							if (data['occupation'] != 'Exec-managerial'):
							    return u'<=50K'
						if (data['workclass'] != 'State-gov'):
						    if (data['age'] > 63):
							return u'<=50K'
						    if (data['age'] <= 63):
							if (data['age'] > 51):
							    return u'>50K'
							if (data['age'] <= 51):
							    return u'<=50K'
					    if (data['relationship'] != 'Not-in-family'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 115955):
						    if (data['age'] > 52):
							return u'<=50K'
						    if (data['age'] <= 52):
							if (data['final_weight'] > 132442):
							    return u'<=50K'
							if (data['final_weight'] <= 132442):
							    return u'>50K'
						if (data['final_weight'] <= 115955):
						    return u'<=50K'
					if (data['marital_status'] != 'Divorced'):
					    if (data['age'] > 58):
						if (data['education_num'] > 13):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 124521):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'White'):
							    return u'<=50K'
							if (data['race'] != 'White'):
							    return u'>50K'
						    if (data['final_weight'] <= 124521):
							return u'>50K'
						if (data['education_num'] <= 13):
						    return u'<=50K'
					    if (data['age'] <= 58):
						if (not 'workclass' in data or data['workclass'] is None):
						    return u'<=50K'
						if (data['workclass'] == 'Self-emp-not-inc'):
						    if (data['marital_status'] == 'Never-married'):
							return u'<=50K'
						    if (data['marital_status'] != 'Never-married'):
							if (data['occupation'] == 'Sales'):
							    return u'<=50K'
							if (data['occupation'] != 'Sales'):
							    return u'>50K'
						if (data['workclass'] != 'Self-emp-not-inc'):
						    if (data['education_num'] > 13):
							return u'<=50K'
						    if (data['education_num'] <= 13):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'Asian-Pac-Islander'):
							    return u'<=50K'
							if (data['race'] != 'Asian-Pac-Islander'):
							    return u'<=50K'
			    if (data['hours_per_week'] <= 31):
				if (data['hours_per_week'] > 2):
				    if (not 'race' in data or data['race'] is None):
					return u'<=50K'
				    if (data['race'] == 'Asian-Pac-Islander'):
					return u'>50K'
				    if (data['race'] != 'Asian-Pac-Islander'):
					if (not 'relationship' in data or data['relationship'] is None):
					    return u'<=50K'
					if (data['relationship'] == 'Not-in-family'):
					    if (data['hours_per_week'] > 26):
						return u'<=50K'
					    if (data['hours_per_week'] <= 26):
						if (data['hours_per_week'] > 15):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 148730):
							if (data['age'] > 77):
							    return u'>50K'
							if (data['age'] <= 77):
							    return u'<=50K'
						    if (data['final_weight'] <= 148730):
							if (data['final_weight'] > 110513):
							    return u'>50K'
							if (data['final_weight'] <= 110513):
							    return u'<=50K'
						if (data['hours_per_week'] <= 15):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 60421):
							return u'<=50K'
						    if (data['final_weight'] <= 60421):
							if (not 'sex' in data or data['sex'] is None):
							    return u'<=50K'
							if (data['sex'] == 'Male'):
							    return u'>50K'
							if (data['sex'] != 'Male'):
							    return u'<=50K'
					if (data['relationship'] != 'Not-in-family'):
					    return u'<=50K'
				if (data['hours_per_week'] <= 2):
				    return u'>50K'
			if (data['age'] <= 44):
			    if (data['hours_per_week'] > 34):
				if (data['age'] > 33):
				    if (not 'relationship' in data or data['relationship'] is None):
					return u'<=50K'
				    if (data['relationship'] == 'Not-in-family'):
					if (data['hours_per_week'] > 37):
					    if (not 'occupation' in data or data['occupation'] is None):
						return u'<=50K'
					    if (data['occupation'] == 'Exec-managerial'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 89724):
						    if (not 'sex' in data or data['sex'] is None):
							return u'<=50K'
						    if (data['sex'] == 'Male'):
							if (data['final_weight'] > 180722):
							    return u'<=50K'
							if (data['final_weight'] <= 180722):
							    return u'>50K'
						    if (data['sex'] != 'Male'):
							if (data['education_num'] > 13):
							    return u'>50K'
							if (data['education_num'] <= 13):
							    return u'<=50K'
						if (data['final_weight'] <= 89724):
						    return u'<=50K'
					    if (data['occupation'] != 'Exec-managerial'):
						if (data['occupation'] == 'Prof-specialty'):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'<=50K'
						    if (data['workclass'] == 'Private'):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'Asian-Pac-Islander'):
							    return u'>50K'
							if (data['race'] != 'Asian-Pac-Islander'):
							    return u'<=50K'
						    if (data['workclass'] != 'Private'):
							if (data['workclass'] == 'Self-emp-not-inc'):
							    return u'>50K'
							if (data['workclass'] != 'Self-emp-not-inc'):
							    return u'<=50K'
						if (data['occupation'] != 'Prof-specialty'):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'<=50K'
						    if (data['workclass'] == 'Private'):
							if (not 'sex' in data or data['sex'] is None):
							    return u'<=50K'
							if (data['sex'] == 'Male'):
							    return u'<=50K'
							if (data['sex'] != 'Male'):
							    return u'<=50K'
						    if (data['workclass'] != 'Private'):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'White'):
							    return u'<=50K'
							if (data['race'] != 'White'):
							    return u'<=50K'
					if (data['hours_per_week'] <= 37):
					    return u'<=50K'
				    if (data['relationship'] != 'Not-in-family'):
					if (not 'workclass' in data or data['workclass'] is None):
					    return u'<=50K'
					if (data['workclass'] == 'Private'):
					    if (not 'occupation' in data or data['occupation'] is None):
						return u'<=50K'
					    if (data['occupation'] == 'Adm-clerical'):
						return u'<=50K'
					    if (data['occupation'] != 'Adm-clerical'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 112612):
						    if (data['age'] > 42):
							if (data['marital_status'] == 'Never-married'):
							    return u'>50K'
							if (data['marital_status'] != 'Never-married'):
							    return u'<=50K'
						    if (data['age'] <= 42):
							if (data['occupation'] == 'Exec-managerial'):
							    return u'<=50K'
							if (data['occupation'] != 'Exec-managerial'):
							    return u'<=50K'
						if (data['final_weight'] <= 112612):
						    return u'<=50K'
					if (data['workclass'] != 'Private'):
					    if (data['hours_per_week'] > 37):
						return u'<=50K'
					    if (data['hours_per_week'] <= 37):
						if (data['hours_per_week'] > 35):
						    if (data['education_num'] > 13):
							return u'>50K'
						    if (data['education_num'] <= 13):
							return u'<=50K'
						if (data['hours_per_week'] <= 35):
						    return u'<=50K'
				if (data['age'] <= 33):
				    if (not 'relationship' in data or data['relationship'] is None):
					return u'<=50K'
				    if (data['relationship'] == 'Wife'):
					return u'>50K'
				    if (data['relationship'] != 'Wife'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 882662):
					    return u'>50K'
					if (data['final_weight'] <= 882662):
					    if (data['final_weight'] > 183928):
						if (data['final_weight'] > 314533):
						    if (data['final_weight'] > 329088):
							if (data['education_num'] > 13):
							    return u'<=50K'
							if (data['education_num'] <= 13):
							    return u'<=50K'
						    if (data['final_weight'] <= 329088):
							if (data['marital_status'] == 'Divorced'):
							    return u'>50K'
							if (data['marital_status'] != 'Divorced'):
							    return u'<=50K'
						if (data['final_weight'] <= 314533):
						    return u'<=50K'
					    if (data['final_weight'] <= 183928):
						if (not 'occupation' in data or data['occupation'] is None):
						    return u'<=50K'
						if (data['occupation'] == 'Adm-clerical'):
						    return u'<=50K'
						if (data['occupation'] != 'Adm-clerical'):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'<=50K'
						    if (data['workclass'] == 'Local-gov'):
							return u'<=50K'
						    if (data['workclass'] != 'Local-gov'):
							if (data['final_weight'] > 65504):
							    return u'<=50K'
							if (data['final_weight'] <= 65504):
							    return u'<=50K'
			    if (data['hours_per_week'] <= 34):
				return u'<=50K'
	    if (data['age'] <= 28):
		if (data['age'] > 27):
		    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
			return u'<=50K'
		    if (data['hours_per_week'] > 46):
			if (not 'workclass' in data or data['workclass'] is None):
			    return u'<=50K'
			if (data['workclass'] == 'Local-gov'):
			    return u'<=50K'
			if (data['workclass'] != 'Local-gov'):
			    if (not 'final_weight' in data or data['final_weight'] is None):
				return u'<=50K'
			    if (data['final_weight'] > 390353):
				return u'>50K'
			    if (data['final_weight'] <= 390353):
				if (not 'relationship' in data or data['relationship'] is None):
				    return u'<=50K'
				if (data['relationship'] == 'Unmarried'):
				    return u'<=50K'
				if (data['relationship'] != 'Unmarried'):
				    if (data['marital_status'] == 'Never-married'):
					if (data['hours_per_week'] > 70):
					    return u'<=50K'
					if (data['hours_per_week'] <= 70):
					    if (data['relationship'] == 'Not-in-family'):
						if (not 'occupation' in data or data['occupation'] is None):
						    return u'<=50K'
						if (data['occupation'] == 'Adm-clerical'):
						    return u'>50K'
						if (data['occupation'] != 'Adm-clerical'):
						    if (data['final_weight'] > 238880):
							return u'<=50K'
						    if (data['final_weight'] <= 238880):
							if (data['final_weight'] > 189986):
							    return u'>50K'
							if (data['final_weight'] <= 189986):
							    return u'<=50K'
					    if (data['relationship'] != 'Not-in-family'):
						return u'>50K'
				    if (data['marital_status'] != 'Never-married'):
					return u'>50K'
		    if (data['hours_per_week'] <= 46):
			if (not 'occupation' in data or data['occupation'] is None):
			    return u'<=50K'
			if (data['occupation'] == 'Craft-repair'):
			    if (not 'race' in data or data['race'] is None):
				return u'<=50K'
			    if (data['race'] == 'White'):
				return u'>50K'
			    if (data['race'] != 'White'):
				return u'<=50K'
			if (data['occupation'] != 'Craft-repair'):
			    if (data['hours_per_week'] > 37):
				if (not 'workclass' in data or data['workclass'] is None):
				    return u'<=50K'
				if (data['workclass'] == 'Private'):
				    if (data['occupation'] == 'Adm-clerical'):
					return u'<=50K'
				    if (data['occupation'] != 'Adm-clerical'):
					if (not 'race' in data or data['race'] is None):
					    return u'<=50K'
					if (data['race'] == 'White'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 346817):
						if (not 'sex' in data or data['sex'] is None):
						    return u'<=50K'
						if (data['sex'] == 'Male'):
						    return u'<=50K'
						if (data['sex'] != 'Male'):
						    return u'>50K'
					    if (data['final_weight'] <= 346817):
						if (data['final_weight'] > 190229):
						    return u'<=50K'
						if (data['final_weight'] <= 190229):
						    if (data['final_weight'] > 173729):
							return u'>50K'
						    if (data['final_weight'] <= 173729):
							if (not 'sex' in data or data['sex'] is None):
							    return u'<=50K'
							if (data['sex'] == 'Male'):
							    return u'<=50K'
							if (data['sex'] != 'Male'):
							    return u'<=50K'
					if (data['race'] != 'White'):
					    return u'<=50K'
				if (data['workclass'] != 'Private'):
				    return u'<=50K'
			    if (data['hours_per_week'] <= 37):
				return u'<=50K'
		if (data['age'] <= 27):
		    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
			return u'<=50K'
		    if (data['hours_per_week'] > 38):
			if (data['hours_per_week'] > 62):
			    if (not 'final_weight' in data or data['final_weight'] is None):
				return u'<=50K'
			    if (data['final_weight'] > 78354):
				if (data['age'] > 25):
				    if (not 'occupation' in data or data['occupation'] is None):
					return u'<=50K'
				    if (data['occupation'] == 'Sales'):
					return u'>50K'
				    if (data['occupation'] != 'Sales'):
					if (data['occupation'] == 'Exec-managerial'):
					    if (data['hours_per_week'] > 84):
						return u'<=50K'
					    if (data['hours_per_week'] <= 84):
						return u'>50K'
					if (data['occupation'] != 'Exec-managerial'):
					    return u'<=50K'
				if (data['age'] <= 25):
				    return u'<=50K'
			    if (data['final_weight'] <= 78354):
				return u'>50K'
			if (data['hours_per_week'] <= 62):
			    if (not 'workclass' in data or data['workclass'] is None):
				return u'<=50K'
			    if (data['workclass'] == 'Local-gov'):
				return u'<=50K'
			    if (data['workclass'] != 'Local-gov'):
				if (not 'occupation' in data or data['occupation'] is None):
				    return u'<=50K'
				if (data['occupation'] == 'Prof-specialty'):
				    if (not 'race' in data or data['race'] is None):
					return u'<=50K'
				    if (data['race'] == 'Amer-Indian-Eskimo'):
					return u'>50K'
				    if (data['race'] != 'Amer-Indian-Eskimo'):
					if (data['marital_status'] == 'Separated'):
					    return u'>50K'
					if (data['marital_status'] != 'Separated'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 90101):
						if (data['final_weight'] > 335053):
						    return u'<=50K'
						if (data['final_weight'] <= 335053):
						    if (data['final_weight'] > 318325):
							if (data['hours_per_week'] > 42):
							    return u'<=50K'
							if (data['hours_per_week'] <= 42):
							    return u'>50K'
						    if (data['final_weight'] <= 318325):
							if (data['final_weight'] > 196449):
							    return u'<=50K'
							if (data['final_weight'] <= 196449):
							    return u'<=50K'
					    if (data['final_weight'] <= 90101):
						return u'<=50K'
				if (data['occupation'] != 'Prof-specialty'):
				    if (data['workclass'] == 'Self-emp-not-inc'):
					if (not 'relationship' in data or data['relationship'] is None):
					    return u'<=50K'
					if (data['relationship'] == 'Own-child'):
					    return u'>50K'
					if (data['relationship'] != 'Own-child'):
					    return u'<=50K'
				    if (data['workclass'] != 'Self-emp-not-inc'):
					if (data['hours_per_week'] > 44):
					    if (data['occupation'] == 'Farming-fishing'):
						return u'>50K'
					    if (data['occupation'] != 'Farming-fishing'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 272584):
						    if (data['hours_per_week'] > 47):
							return u'<=50K'
						    if (data['hours_per_week'] <= 47):
							if (data['occupation'] == 'Exec-managerial'):
							    return u'<=50K'
							if (data['occupation'] != 'Exec-managerial'):
							    return u'>50K'
						if (data['final_weight'] <= 272584):
						    if (data['hours_per_week'] > 58):
							if (data['occupation'] == 'Tech-support'):
							    return u'<=50K'
							if (data['occupation'] != 'Tech-support'):
							    return u'<=50K'
						    if (data['hours_per_week'] <= 58):
							return u'<=50K'
					if (data['hours_per_week'] <= 44):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 184666):
						return u'<=50K'
					    if (data['final_weight'] <= 184666):
						if (not 'relationship' in data or data['relationship'] is None):
						    return u'<=50K'
						if (data['relationship'] == 'Unmarried'):
						    if (not 'race' in data or data['race'] is None):
							return u'<=50K'
						    if (data['race'] == 'White'):
							return u'>50K'
						    if (data['race'] != 'White'):
							return u'<=50K'
						if (data['relationship'] != 'Unmarried'):
						    if (not 'sex' in data or data['sex'] is None):
							return u'<=50K'
						    if (data['sex'] == 'Male'):
							return u'<=50K'
						    if (data['sex'] != 'Male'):
							if (data['final_weight'] > 42283):
							    return u'<=50K'
							if (data['final_weight'] <= 42283):
							    return u'<=50K'
		    if (data['hours_per_week'] <= 38):
			return u'<=50K'
	if (data['education_num'] <= 12):
	    if (not 'age' in data or data['age'] is None):
		return u'<=50K'
	    if (data['age'] > 27):
		if (not 'hours_per_week' in data or data['hours_per_week'] is None):
		    return u'<=50K'
		if (data['hours_per_week'] > 41):
		    if (not 'sex' in data or data['sex'] is None):
			return u'<=50K'
		    if (data['sex'] == 'Male'):
			if (data['age'] > 39):
			    if (not 'education' in data or data['education'] is None):
				return u'<=50K'
			    if (data['education'] == 'Some-college'):
				if (not 'final_weight' in data or data['final_weight'] is None):
				    return u'<=50K'
				if (data['final_weight'] > 241538):
				    if (data['hours_per_week'] > 62):
					return u'>50K'
				    if (data['hours_per_week'] <= 62):
					if (data['age'] > 41):
					    if (data['hours_per_week'] > 51):
						if (not 'relationship' in data or data['relationship'] is None):
						    return u'<=50K'
						if (data['relationship'] == 'Unmarried'):
						    return u'>50K'
						if (data['relationship'] != 'Unmarried'):
						    return u'<=50K'
					    if (data['hours_per_week'] <= 51):
						if (data['hours_per_week'] > 46):
						    if (not 'occupation' in data or data['occupation'] is None):
							return u'>50K'
						    if (data['occupation'] == 'Exec-managerial'):
							if (data['final_weight'] > 358246):
							    return u'>50K'
							if (data['final_weight'] <= 358246):
							    return u'<=50K'
						    if (data['occupation'] != 'Exec-managerial'):
							return u'>50K'
						if (data['hours_per_week'] <= 46):
						    if (not 'occupation' in data or data['occupation'] is None):
							return u'<=50K'
						    if (data['occupation'] == 'Adm-clerical'):
							return u'<=50K'
						    if (data['occupation'] != 'Adm-clerical'):
							if (data['final_weight'] > 354776):
							    return u'<=50K'
							if (data['final_weight'] <= 354776):
							    return u'>50K'
					if (data['age'] <= 41):
					    return u'<=50K'
				if (data['final_weight'] <= 241538):
				    if (not 'workclass' in data or data['workclass'] is None):
					return u'<=50K'
				    if (data['workclass'] == 'Self-emp-not-inc'):
					return u'<=50K'
				    if (data['workclass'] != 'Self-emp-not-inc'):
					if (data['workclass'] == 'Self-emp-inc'):
					    return u'<=50K'
					if (data['workclass'] != 'Self-emp-inc'):
					    if (data['hours_per_week'] > 45):
						if (data['workclass'] == 'Private'):
						    if (data['final_weight'] > 52727):
							if (data['hours_per_week'] > 46):
							    return u'<=50K'
							if (data['hours_per_week'] <= 46):
							    return u'>50K'
						    if (data['final_weight'] <= 52727):
							if (not 'relationship' in data or data['relationship'] is None):
							    return u'>50K'
							if (data['relationship'] == 'Not-in-family'):
							    return u'>50K'
							if (data['relationship'] != 'Not-in-family'):
							    return u'<=50K'
						if (data['workclass'] != 'Private'):
						    if (not 'occupation' in data or data['occupation'] is None):
							return u'>50K'
						    if (data['occupation'] == 'Protective-serv'):
							return u'<=50K'
						    if (data['occupation'] != 'Protective-serv'):
							return u'>50K'
					    if (data['hours_per_week'] <= 45):
						if (data['marital_status'] == 'Separated'):
						    return u'>50K'
						if (data['marital_status'] != 'Separated'):
						    if (data['age'] > 48):
							if (not 'relationship' in data or data['relationship'] is None):
							    return u'<=50K'
							if (data['relationship'] == 'Own-child'):
							    return u'>50K'
							if (data['relationship'] != 'Own-child'):
							    return u'<=50K'
						    if (data['age'] <= 48):
							return u'<=50K'
			    if (data['education'] != 'Some-college'):
				if (not 'occupation' in data or data['occupation'] is None):
				    return u'<=50K'
				if (data['occupation'] == 'Tech-support'):
				    return u'>50K'
				if (data['occupation'] != 'Tech-support'):
				    if (data['occupation'] == 'Machine-op-inspct'):
					return u'<=50K'
				    if (data['occupation'] != 'Machine-op-inspct'):
					if (data['occupation'] == 'Other-service'):
					    return u'<=50K'
					if (data['occupation'] != 'Other-service'):
					    if (data['marital_status'] == 'Married-spouse-absent'):
						return u'<=50K'
					    if (data['marital_status'] != 'Married-spouse-absent'):
						if (data['marital_status'] == 'Never-married'):
						    if (data['education_num'] > 11):
							return u'>50K'
						    if (data['education_num'] <= 11):
							if (not 'workclass' in data or data['workclass'] is None):
							    return u'<=50K'
							if (data['workclass'] == 'Private'):
							    return u'<=50K'
							if (data['workclass'] != 'Private'):
							    return u'<=50K'
						if (data['marital_status'] != 'Never-married'):
						    if (data['education_num'] > 5):
							if (data['age'] > 53):
							    return u'<=50K'
							if (data['age'] <= 53):
							    return u'<=50K'
						    if (data['education_num'] <= 5):
							return u'<=50K'
			if (data['age'] <= 39):
			    if (not 'relationship' in data or data['relationship'] is None):
				return u'<=50K'
			    if (data['relationship'] == 'Own-child'):
				if (data['marital_status'] == 'Married-spouse-absent'):
				    return u'>50K'
				if (data['marital_status'] != 'Married-spouse-absent'):
				    if (data['hours_per_week'] > 43):
					return u'<=50K'
				    if (data['hours_per_week'] <= 43):
					if (not 'occupation' in data or data['occupation'] is None):
					    return u'<=50K'
					if (data['occupation'] == 'Craft-repair'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 171842):
						return u'<=50K'
					    if (data['final_weight'] <= 171842):
						return u'>50K'
					if (data['occupation'] != 'Craft-repair'):
					    return u'<=50K'
			    if (data['relationship'] != 'Own-child'):
				if (not 'race' in data or data['race'] is None):
				    return u'<=50K'
				if (data['race'] == 'Amer-Indian-Eskimo'):
				    if (data['relationship'] == 'Unmarried'):
					return u'<=50K'
				    if (data['relationship'] != 'Unmarried'):
					if (data['hours_per_week'] > 46):
					    return u'>50K'
					if (data['hours_per_week'] <= 46):
					    return u'<=50K'
				if (data['race'] != 'Amer-Indian-Eskimo'):
				    if (not 'workclass' in data or data['workclass'] is None):
					return u'<=50K'
				    if (data['workclass'] == 'Private'):
					if (data['education_num'] > 10):
					    if (data['hours_per_week'] > 42):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 113520):
						    if (data['final_weight'] > 226931):
							if (data['relationship'] == 'Not-in-family'):
							    return u'<=50K'
							if (data['relationship'] != 'Not-in-family'):
							    return u'<=50K'
						    if (data['final_weight'] <= 226931):
							if (not 'occupation' in data or data['occupation'] is None):
							    return u'<=50K'
							if (data['occupation'] == 'Exec-managerial'):
							    return u'>50K'
							if (data['occupation'] != 'Exec-managerial'):
							    return u'<=50K'
						if (data['final_weight'] <= 113520):
						    return u'<=50K'
					    if (data['hours_per_week'] <= 42):
						return u'>50K'
					if (data['education_num'] <= 10):
					    if (not 'occupation' in data or data['occupation'] is None):
						return u'<=50K'
					    if (data['occupation'] == 'Prof-specialty'):
						if (data['hours_per_week'] > 47):
						    if (data['marital_status'] == 'Never-married'):
							return u'>50K'
						    if (data['marital_status'] != 'Never-married'):
							return u'<=50K'
						if (data['hours_per_week'] <= 47):
						    return u'<=50K'
					    if (data['occupation'] != 'Prof-specialty'):
						if (data['hours_per_week'] > 61):
						    return u'<=50K'
						if (data['hours_per_week'] <= 61):
						    if (data['age'] > 35):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 117480):
							    return u'<=50K'
							if (data['final_weight'] <= 117480):
							    return u'<=50K'
						    if (data['age'] <= 35):
							if (data['occupation'] == 'Sales'):
							    return u'<=50K'
							if (data['occupation'] != 'Sales'):
							    return u'<=50K'
				    if (data['workclass'] != 'Private'):
					if (data['education_num'] > 9):
					    if (data['workclass'] == 'Federal-gov'):
						if (data['marital_status'] == 'Never-married'):
						    return u'<=50K'
						if (data['marital_status'] != 'Never-married'):
						    return u'>50K'
					    if (data['workclass'] != 'Federal-gov'):
						if (not 'education' in data or data['education'] is None):
						    return u'<=50K'
						if (data['education'] == 'Assoc-voc'):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 246356):
							return u'>50K'
						    if (data['final_weight'] <= 246356):
							return u'<=50K'
						if (data['education'] != 'Assoc-voc'):
						    return u'<=50K'
					if (data['education_num'] <= 9):
					    if (data['relationship'] == 'Unmarried'):
						return u'<=50K'
					    if (data['relationship'] != 'Unmarried'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 315551):
						    if (data['hours_per_week'] > 44):
							return u'>50K'
						    if (data['hours_per_week'] <= 44):
							return u'<=50K'
						if (data['final_weight'] <= 315551):
						    if (data['final_weight'] > 209085):
							return u'<=50K'
						    if (data['final_weight'] <= 209085):
							if (data['age'] > 30):
							    return u'<=50K'
							if (data['age'] <= 30):
							    return u'>50K'
		    if (data['sex'] != 'Male'):
			if (not 'workclass' in data or data['workclass'] is None):
			    return u'<=50K'
			if (data['workclass'] == 'Self-emp-inc'):
			    if (data['age'] > 52):
				return u'>50K'
			    if (data['age'] <= 52):
				return u'<=50K'
			if (data['workclass'] != 'Self-emp-inc'):
			    if (not 'occupation' in data or data['occupation'] is None):
				return u'<=50K'
			    if (data['occupation'] == 'Protective-serv'):
				if (data['hours_per_week'] > 53):
				    return u'>50K'
				if (data['hours_per_week'] <= 53):
				    return u'<=50K'
			    if (data['occupation'] != 'Protective-serv'):
				if (not 'final_weight' in data or data['final_weight'] is None):
				    return u'<=50K'
				if (data['final_weight'] > 109893):
				    if (data['age'] > 30):
					if (not 'relationship' in data or data['relationship'] is None):
					    return u'<=50K'
					if (data['relationship'] == 'Wife'):
					    return u'>50K'
					if (data['relationship'] != 'Wife'):
					    if (data['workclass'] == 'Self-emp-not-inc'):
						return u'<=50K'
					    if (data['workclass'] != 'Self-emp-not-inc'):
						if (data['hours_per_week'] > 49):
						    if (data['final_weight'] > 252168):
							if (data['education_num'] > 11):
							    return u'<=50K'
							if (data['education_num'] <= 11):
							    return u'<=50K'
						    if (data['final_weight'] <= 252168):
							if (data['marital_status'] == 'Never-married'):
							    return u'<=50K'
							if (data['marital_status'] != 'Never-married'):
							    return u'<=50K'
						if (data['hours_per_week'] <= 49):
						    if (not 'education' in data or data['education'] is None):
							return u'<=50K'
						    if (data['education'] == 'Some-college'):
							if (data['final_weight'] > 360381):
							    return u'<=50K'
							if (data['final_weight'] <= 360381):
							    return u'<=50K'
						    if (data['education'] != 'Some-college'):
							if (data['final_weight'] > 114638):
							    return u'<=50K'
							if (data['final_weight'] <= 114638):
							    return u'<=50K'
				    if (data['age'] <= 30):
					return u'<=50K'
				if (data['final_weight'] <= 109893):
				    if (data['hours_per_week'] > 59):
					if (not 'education' in data or data['education'] is None):
					    return u'<=50K'
					if (data['education'] == '11th'):
					    return u'>50K'
					if (data['education'] != '11th'):
					    if (not 'race' in data or data['race'] is None):
						return u'<=50K'
					    if (data['race'] == 'Asian-Pac-Islander'):
						if (data['hours_per_week'] > 67):
						    return u'<=50K'
						if (data['hours_per_week'] <= 67):
						    return u'>50K'
					    if (data['race'] != 'Asian-Pac-Islander'):
						return u'<=50K'
				    if (data['hours_per_week'] <= 59):
					return u'<=50K'
		if (data['hours_per_week'] <= 41):
		    if (not 'occupation' in data or data['occupation'] is None):
			return u'<=50K'
		    if (data['occupation'] == 'Other-service'):
			if (data['hours_per_week'] > 40):
			    if (data['marital_status'] == 'Never-married'):
				return u'>50K'
			    if (data['marital_status'] != 'Never-married'):
				return u'<=50K'
			if (data['hours_per_week'] <= 40):
			    if (not 'relationship' in data or data['relationship'] is None):
				return u'<=50K'
			    if (data['relationship'] == 'Wife'):
				if (data['hours_per_week'] > 32):
				    return u'>50K'
				if (data['hours_per_week'] <= 32):
				    return u'<=50K'
			    if (data['relationship'] != 'Wife'):
				if (not 'workclass' in data or data['workclass'] is None):
				    return u'<=50K'
				if (data['workclass'] == 'Private'):
				    if (not 'race' in data or data['race'] is None):
					return u'<=50K'
				    if (data['race'] == 'Asian-Pac-Islander'):
					if (data['marital_status'] == 'Widowed'):
					    if (data['hours_per_week'] > 30):
						if (data['relationship'] == 'Unmarried'):
						    return u'>50K'
						if (data['relationship'] != 'Unmarried'):
						    return u'<=50K'
					    if (data['hours_per_week'] <= 30):
						return u'<=50K'
					if (data['marital_status'] != 'Widowed'):
					    return u'<=50K'
				    if (data['race'] != 'Asian-Pac-Islander'):
					if (data['age'] > 29):
					    return u'<=50K'
					if (data['age'] <= 29):
					    if (data['marital_status'] == 'Divorced'):
						if (data['hours_per_week'] > 38):
						    if (not 'sex' in data or data['sex'] is None):
							return u'<=50K'
						    if (data['sex'] == 'Male'):
							return u'>50K'
						    if (data['sex'] != 'Male'):
							return u'<=50K'
						if (data['hours_per_week'] <= 38):
						    return u'<=50K'
					    if (data['marital_status'] != 'Divorced'):
						return u'<=50K'
				if (data['workclass'] != 'Private'):
				    if (not 'education' in data or data['education'] is None):
					return u'<=50K'
				    if (data['education'] == '11th'):
					if (data['marital_status'] == 'Widowed'):
					    return u'>50K'
					if (data['marital_status'] != 'Widowed'):
					    return u'<=50K'
				    if (data['education'] != '11th'):
					if (data['education'] == 'Some-college'):
					    if (data['age'] > 62):
						return u'>50K'
					    if (data['age'] <= 62):
						if (data['age'] > 29):
						    return u'<=50K'
						if (data['age'] <= 29):
						    if (data['relationship'] == 'Not-in-family'):
							return u'>50K'
						    if (data['relationship'] != 'Not-in-family'):
							return u'<=50K'
					if (data['education'] != 'Some-college'):
					    return u'<=50K'
		    if (data['occupation'] != 'Other-service'):
			if (data['age'] > 33):
			    if (not 'relationship' in data or data['relationship'] is None):
				return u'<=50K'
			    if (data['relationship'] == 'Not-in-family'):
				if (data['occupation'] == 'Exec-managerial'):
				    if (not 'workclass' in data or data['workclass'] is None):
					return u'<=50K'
				    if (data['workclass'] == 'Local-gov'):
					return u'<=50K'
				    if (data['workclass'] != 'Local-gov'):
					if (not 'race' in data or data['race'] is None):
					    return u'<=50K'
					if (data['race'] == 'Asian-Pac-Islander'):
					    return u'>50K'
					if (data['race'] != 'Asian-Pac-Islander'):
					    if (data['workclass'] == 'Self-emp-inc'):
						if (data['hours_per_week'] > 35):
						    if (data['age'] > 49):
							if (data['age'] > 54):
							    return u'<=50K'
							if (data['age'] <= 54):
							    return u'>50K'
						    if (data['age'] <= 49):
							return u'<=50K'
						if (data['hours_per_week'] <= 35):
						    return u'<=50K'
					    if (data['workclass'] != 'Self-emp-inc'):
						if (data['education_num'] > 10):
						    if (data['age'] > 62):
							return u'<=50K'
						    if (data['age'] <= 62):
							if (data['age'] > 57):
							    return u'>50K'
							if (data['age'] <= 57):
							    return u'<=50K'
						if (data['education_num'] <= 10):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 199705):
							if (data['final_weight'] > 344017):
							    return u'<=50K'
							if (data['final_weight'] <= 344017):
							    return u'<=50K'
						    if (data['final_weight'] <= 199705):
							if (data['final_weight'] > 184205):
							    return u'<=50K'
							if (data['final_weight'] <= 184205):
							    return u'<=50K'
				if (data['occupation'] != 'Exec-managerial'):
				    if (not 'sex' in data or data['sex'] is None):
					return u'<=50K'
				    if (data['sex'] == 'Male'):
					if (data['occupation'] == 'Prof-specialty'):
					    if (data['age'] > 42):
						if (not 'education' in data or data['education'] is None):
						    return u'<=50K'
						if (data['education'] == 'Some-college'):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 194938):
							return u'>50K'
						    if (data['final_weight'] <= 194938):
							return u'<=50K'
						if (data['education'] != 'Some-college'):
						    return u'<=50K'
					    if (data['age'] <= 42):
						if (data['marital_status'] == 'Divorced'):
						    return u'<=50K'
						if (data['marital_status'] != 'Divorced'):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'>50K'
						    if (data['final_weight'] > 147172):
							if (data['education_num'] > 10):
							    return u'>50K'
							if (data['education_num'] <= 10):
							    return u'<=50K'
						    if (data['final_weight'] <= 147172):
							return u'>50K'
					if (data['occupation'] != 'Prof-specialty'):
					    if (data['occupation'] == 'Tech-support'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 69829):
						    if (data['final_weight'] > 180331):
							if (data['age'] > 43):
							    return u'<=50K'
							if (data['age'] <= 43):
							    return u'<=50K'
						    if (data['final_weight'] <= 180331):
							return u'<=50K'
						if (data['final_weight'] <= 69829):
						    return u'>50K'
					    if (data['occupation'] != 'Tech-support'):
						if (data['age'] > 49):
						    if (data['marital_status'] == 'Separated'):
							return u'<=50K'
						    if (data['marital_status'] != 'Separated'):
							if (data['occupation'] == 'Craft-repair'):
							    return u'<=50K'
							if (data['occupation'] != 'Craft-repair'):
							    return u'<=50K'
						if (data['age'] <= 49):
						    if (data['occupation'] == 'Protective-serv'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 187996):
							    return u'<=50K'
							if (data['final_weight'] <= 187996):
							    return u'<=50K'
						    if (data['occupation'] != 'Protective-serv'):
							if (data['education_num'] > 8):
							    return u'<=50K'
							if (data['education_num'] <= 8):
							    return u'<=50K'
				    if (data['sex'] != 'Male'):
					if (data['occupation'] == 'Craft-repair'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 126341):
						if (data['final_weight'] > 324908):
						    if (data['marital_status'] == 'Divorced'):
							return u'>50K'
						    if (data['marital_status'] != 'Divorced'):
							return u'<=50K'
						if (data['final_weight'] <= 324908):
						    return u'<=50K'
					    if (data['final_weight'] <= 126341):
						if (data['education_num'] > 8):
						    if (not 'education' in data or data['education'] is None):
							return u'<=50K'
						    if (data['education'] == 'Some-college'):
							return u'>50K'
						    if (data['education'] != 'Some-college'):
							return u'<=50K'
						if (data['education_num'] <= 8):
						    return u'>50K'
					if (data['occupation'] != 'Craft-repair'):
					    if (data['marital_status'] == 'Divorced'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 35780):
						    if (data['final_weight'] > 209523):
							if (not 'education' in data or data['education'] is None):
							    return u'<=50K'
							if (data['education'] == 'Assoc-voc'):
							    return u'<=50K'
							if (data['education'] != 'Assoc-voc'):
							    return u'<=50K'
						    if (data['final_weight'] <= 209523):
							return u'<=50K'
						if (data['final_weight'] <= 35780):
						    if (data['final_weight'] > 21395):
							return u'<=50K'
						    if (data['final_weight'] <= 21395):
							return u'>50K'
					    if (data['marital_status'] != 'Divorced'):
						if (data['education_num'] > 8):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 270961):
							return u'<=50K'
						    if (data['final_weight'] <= 270961):
							if (data['age'] > 59):
							    return u'<=50K'
							if (data['age'] <= 59):
							    return u'<=50K'
						if (data['education_num'] <= 8):
						    return u'<=50K'
			    if (data['relationship'] != 'Not-in-family'):
				if (data['occupation'] == 'Prof-specialty'):
				    if (data['hours_per_week'] > 37):
					if (not 'education' in data or data['education'] is None):
					    return u'<=50K'
					if (data['education'] == 'Some-college'):
					    return u'<=50K'
					if (data['education'] != 'Some-college'):
					    if (not 'sex' in data or data['sex'] is None):
						return u'<=50K'
					    if (data['sex'] == 'Male'):
						if (data['education'] == 'HS-grad'):
						    return u'<=50K'
						if (data['education'] != 'HS-grad'):
						    if (data['age'] > 43):
							return u'>50K'
						    if (data['age'] <= 43):
							return u'<=50K'
					    if (data['sex'] != 'Male'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 179661):
						    if (data['final_weight'] > 338923):
							if (data['relationship'] == 'Unmarried'):
							    return u'>50K'
							if (data['relationship'] != 'Unmarried'):
							    return u'<=50K'
						    if (data['final_weight'] <= 338923):
							return u'<=50K'
						if (data['final_weight'] <= 179661):
						    if (data['final_weight'] > 156995):
							return u'>50K'
						    if (data['final_weight'] <= 156995):
							if (data['age'] > 49):
							    return u'<=50K'
							if (data['age'] <= 49):
							    return u'<=50K'
				    if (data['hours_per_week'] <= 37):
					return u'<=50K'
				if (data['occupation'] != 'Prof-specialty'):
				    if (data['marital_status'] == 'Separated'):
					return u'<=50K'
				    if (data['marital_status'] != 'Separated'):
					if (not 'education' in data or data['education'] is None):
					    return u'<=50K'
					if (data['education'] == '9th'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 107002):
						if (data['occupation'] == 'Craft-repair'):
						    if (not 'sex' in data or data['sex'] is None):
							return u'<=50K'
						    if (data['sex'] == 'Male'):
							return u'<=50K'
						    if (data['sex'] != 'Male'):
							return u'>50K'
						if (data['occupation'] != 'Craft-repair'):
						    return u'<=50K'
					    if (data['final_weight'] <= 107002):
						if (data['relationship'] == 'Unmarried'):
						    return u'>50K'
						if (data['relationship'] != 'Unmarried'):
						    return u'<=50K'
					if (data['education'] != '9th'):
					    if (data['relationship'] == 'Wife'):
						if (data['education_num'] > 11):
						    return u'<=50K'
						if (data['education_num'] <= 11):
						    return u'>50K'
					    if (data['relationship'] != 'Wife'):
						if (not 'race' in data or data['race'] is None):
						    return u'<=50K'
						if (data['race'] == 'Asian-Pac-Islander'):
						    if (data['hours_per_week'] > 36):
							if (data['age'] > 58):
							    return u'<=50K'
							if (data['age'] <= 58):
							    return u'<=50K'
						    if (data['hours_per_week'] <= 36):
							return u'>50K'
						if (data['race'] != 'Asian-Pac-Islander'):
						    if (data['age'] > 59):
							return u'<=50K'
						    if (data['age'] <= 59):
							if (data['age'] > 50):
							    return u'<=50K'
							if (data['age'] <= 50):
							    return u'<=50K'
			if (data['age'] <= 33):
			    if (not 'education' in data or data['education'] is None):
				return u'<=50K'
			    if (data['education'] == 'HS-grad'):
				if (not 'final_weight' in data or data['final_weight'] is None):
				    return u'<=50K'
				if (data['final_weight'] > 331299):
				    if (data['age'] > 32):
					if (data['occupation'] == 'Craft-repair'):
					    if (data['hours_per_week'] > 37):
						return u'>50K'
					    if (data['hours_per_week'] <= 37):
						return u'<=50K'
					if (data['occupation'] != 'Craft-repair'):
					    return u'<=50K'
				    if (data['age'] <= 32):
					return u'<=50K'
				if (data['final_weight'] <= 331299):
				    return u'<=50K'
			    if (data['education'] != 'HS-grad'):
				if (data['marital_status'] == 'Divorced'):
				    if (data['occupation'] == 'Adm-clerical'):
					return u'<=50K'
				    if (data['occupation'] != 'Adm-clerical'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 360189):
					    if (not 'relationship' in data or data['relationship'] is None):
						return u'<=50K'
					    if (data['relationship'] == 'Not-in-family'):
						return u'>50K'
					    if (data['relationship'] != 'Not-in-family'):
						return u'<=50K'
					if (data['final_weight'] <= 360189):
					    if (data['occupation'] == 'Craft-repair'):
						if (not 'relationship' in data or data['relationship'] is None):
						    return u'<=50K'
						if (data['relationship'] == 'Not-in-family'):
						    return u'<=50K'
						if (data['relationship'] != 'Not-in-family'):
						    if (data['final_weight'] > 225058):
							return u'<=50K'
						    if (data['final_weight'] <= 225058):
							if (data['final_weight'] > 210146):
							    return u'>50K'
							if (data['final_weight'] <= 210146):
							    return u'<=50K'
					    if (data['occupation'] != 'Craft-repair'):
						if (data['occupation'] == 'Tech-support'):
						    if (not 'race' in data or data['race'] is None):
							return u'<=50K'
						    if (data['race'] == 'White'):
							return u'<=50K'
						    if (data['race'] != 'White'):
							return u'>50K'
						if (data['occupation'] != 'Tech-support'):
						    if (data['education'] == '11th'):
							if (data['occupation'] == 'Exec-managerial'):
							    return u'>50K'
							if (data['occupation'] != 'Exec-managerial'):
							    return u'<=50K'
						    if (data['education'] != '11th'):
							return u'<=50K'
				if (data['marital_status'] != 'Divorced'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
					return u'<=50K'
				    if (data['final_weight'] > 124813):
					if (data['final_weight'] > 291150):
					    return u'<=50K'
					if (data['final_weight'] <= 291150):
					    if (data['occupation'] == 'Prof-specialty'):
						if (data['age'] > 29):
						    return u'<=50K'
						if (data['age'] <= 29):
						    if (not 'relationship' in data or data['relationship'] is None):
							return u'<=50K'
						    if (data['relationship'] == 'Not-in-family'):
							if (data['hours_per_week'] > 37):
							    return u'>50K'
							if (data['hours_per_week'] <= 37):
							    return u'<=50K'
						    if (data['relationship'] != 'Not-in-family'):
							return u'<=50K'
					    if (data['occupation'] != 'Prof-specialty'):
						if (data['occupation'] == 'Farming-fishing'):
						    if (data['education'] == '7th-8th'):
							return u'>50K'
						    if (data['education'] != '7th-8th'):
							return u'<=50K'
						if (data['occupation'] != 'Farming-fishing'):
						    if (data['education'] == 'Some-college'):
							if (data['final_weight'] > 170506):
							    return u'<=50K'
							if (data['final_weight'] <= 170506):
							    return u'<=50K'
						    if (data['education'] != 'Some-college'):
							return u'<=50K'
				    if (data['final_weight'] <= 124813):
					return u'<=50K'
	    if (data['age'] <= 27):
		if (not 'hours_per_week' in data or data['hours_per_week'] is None):
		    return u'<=50K'
		if (data['hours_per_week'] > 43):
		    if (not 'race' in data or data['race'] is None):
			return u'<=50K'
		    if (data['race'] == 'Asian-Pac-Islander'):
			if (not 'occupation' in data or data['occupation'] is None):
			    return u'<=50K'
			if (data['occupation'] == 'Machine-op-inspct'):
			    return u'>50K'
			if (data['occupation'] != 'Machine-op-inspct'):
			    if (not 'final_weight' in data or data['final_weight'] is None):
				return u'<=50K'
			    if (data['final_weight'] > 71121):
				return u'<=50K'
			    if (data['final_weight'] <= 71121):
				return u'>50K'
		    if (data['race'] != 'Asian-Pac-Islander'):
			if (not 'occupation' in data or data['occupation'] is None):
			    return u'<=50K'
			if (data['occupation'] == 'Exec-managerial'):
			    if (not 'education' in data or data['education'] is None):
				return u'<=50K'
			    if (data['education'] == '12th'):
				return u'>50K'
			    if (data['education'] != '12th'):
				if (not 'final_weight' in data or data['final_weight'] is None):
				    return u'<=50K'
				if (data['final_weight'] > 168084):
				    return u'<=50K'
				if (data['final_weight'] <= 168084):
				    if (data['final_weight'] > 155328):
					return u'>50K'
				    if (data['final_weight'] <= 155328):
					if (data['hours_per_week'] > 57):
					    if (not 'sex' in data or data['sex'] is None):
						return u'<=50K'
					    if (data['sex'] == 'Male'):
						return u'>50K'
					    if (data['sex'] != 'Male'):
						return u'<=50K'
					if (data['hours_per_week'] <= 57):
					    return u'<=50K'
			if (data['occupation'] != 'Exec-managerial'):
			    if (data['hours_per_week'] > 49):
				if (data['occupation'] == 'Other-service'):
				    if (not 'education' in data or data['education'] is None):
					return u'<=50K'
				    if (data['education'] == '7th-8th'):
					return u'>50K'
				    if (data['education'] != '7th-8th'):
					if (data['age'] > 23):
					    if (data['hours_per_week'] > 51):
						return u'<=50K'
					    if (data['hours_per_week'] <= 51):
						if (data['education'] == 'HS-grad'):
						    if (data['marital_status'] == 'Never-married'):
							return u'>50K'
						    if (data['marital_status'] != 'Never-married'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 184107):
							    return u'<=50K'
							if (data['final_weight'] <= 184107):
							    return u'>50K'
						if (data['education'] != 'HS-grad'):
						    return u'<=50K'
					if (data['age'] <= 23):
					    return u'<=50K'
				if (data['occupation'] != 'Other-service'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
					return u'<=50K'
				    if (data['final_weight'] > 181155):
					if (data['hours_per_week'] > 55):
					    return u'<=50K'
					if (data['hours_per_week'] <= 55):
					    if (data['education_num'] > 9):
						if (data['final_weight'] > 211410):
						    if (data['final_weight'] > 217007):
							if (data['occupation'] == 'Transport-moving'):
							    return u'>50K'
							if (data['occupation'] != 'Transport-moving'):
							    return u'<=50K'
						    if (data['final_weight'] <= 217007):
							return u'>50K'
						if (data['final_weight'] <= 211410):
						    return u'<=50K'
					    if (data['education_num'] <= 9):
						if (data['final_weight'] > 192257):
						    return u'<=50K'
						if (data['final_weight'] <= 192257):
						    if (data['age'] > 26):
							return u'>50K'
						    if (data['age'] <= 26):
							return u'<=50K'
				    if (data['final_weight'] <= 181155):
					return u'<=50K'
			    if (data['hours_per_week'] <= 49):
				return u'<=50K'
		if (data['hours_per_week'] <= 43):
		    if (data['age'] > 20):
			if (not 'final_weight' in data or data['final_weight'] is None):
			    return u'<=50K'
			if (data['final_weight'] > 44947):
			    if (not 'race' in data or data['race'] is None):
				return u'<=50K'
			    if (data['race'] == 'Asian-Pac-Islander'):
				if (data['marital_status'] == 'Separated'):
				    return u'>50K'
				if (data['marital_status'] != 'Separated'):
				    if (data['final_weight'] > 110616):
					return u'<=50K'
				    if (data['final_weight'] <= 110616):
					if (not 'education' in data or data['education'] is None):
					    return u'<=50K'
					if (data['education'] == '11th'):
					    return u'>50K'
					if (data['education'] != '11th'):
					    if (not 'workclass' in data or data['workclass'] is None):
						return u'<=50K'
					    if (data['workclass'] == 'Self-emp-not-inc'):
						return u'>50K'
					    if (data['workclass'] != 'Self-emp-not-inc'):
						return u'<=50K'
			    if (data['race'] != 'Asian-Pac-Islander'):
				if (not 'occupation' in data or data['occupation'] is None):
				    return u'<=50K'
				if (data['occupation'] == 'Protective-serv'):
				    if (not 'sex' in data or data['sex'] is None):
					return u'<=50K'
				    if (data['sex'] == 'Male'):
					return u'<=50K'
				    if (data['sex'] != 'Male'):
					if (not 'relationship' in data or data['relationship'] is None):
					    return u'<=50K'
					if (data['relationship'] == 'Not-in-family'):
					    return u'>50K'
					if (data['relationship'] != 'Not-in-family'):
					    if (data['age'] > 25):
						return u'>50K'
					    if (data['age'] <= 25):
						return u'<=50K'
				if (data['occupation'] != 'Protective-serv'):
				    if (data['occupation'] == 'Prof-specialty'):
					if (data['final_weight'] > 455391):
					    if (data['hours_per_week'] > 21):
						return u'>50K'
					    if (data['hours_per_week'] <= 21):
						return u'<=50K'
					if (data['final_weight'] <= 455391):
					    if (not 'workclass' in data or data['workclass'] is None):
						return u'<=50K'
					    if (data['workclass'] == 'Self-emp-not-inc'):
						if (not 'relationship' in data or data['relationship'] is None):
						    return u'<=50K'
						if (data['relationship'] == 'Unmarried'):
						    return u'>50K'
						if (data['relationship'] != 'Unmarried'):
						    return u'<=50K'
					    if (data['workclass'] != 'Self-emp-not-inc'):
						return u'<=50K'
				    if (data['occupation'] != 'Prof-specialty'):
					if (data['final_weight'] > 130483):
					    return u'<=50K'
					if (data['final_weight'] <= 130483):
					    if (data['final_weight'] > 118987):
						if (data['age'] > 22):
						    return u'<=50K'
						if (data['age'] <= 22):
						    if (not 'sex' in data or data['sex'] is None):
							return u'<=50K'
						    if (data['sex'] == 'Male'):
							if (data['race'] == 'White'):
							    return u'<=50K'
							if (data['race'] != 'White'):
							    return u'>50K'
						    if (data['sex'] != 'Male'):
							return u'<=50K'
					    if (data['final_weight'] <= 118987):
						return u'<=50K'
			if (data['final_weight'] <= 44947):
			    if (not 'relationship' in data or data['relationship'] is None):
				return u'<=50K'
			    if (data['relationship'] == 'Husband'):
				return u'>50K'
			    if (data['relationship'] != 'Husband'):
				if (data['final_weight'] > 23828):
				    if (data['final_weight'] > 43834):
					if (data['hours_per_week'] > 37):
					    return u'>50K'
					if (data['hours_per_week'] <= 37):
					    return u'<=50K'
				    if (data['final_weight'] <= 43834):
					return u'<=50K'
				if (data['final_weight'] <= 23828):
				    if (data['final_weight'] > 23202):
					if (data['hours_per_week'] > 39):
					    return u'<=50K'
					if (data['hours_per_week'] <= 39):
					    return u'>50K'
				    if (data['final_weight'] <= 23202):
					return u'<=50K'
		    if (data['age'] <= 20):
			return u'<=50K'