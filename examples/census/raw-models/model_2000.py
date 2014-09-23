def predict_income(data={}):
    """ Predictor for income from model/536031d6ffa04466f3001b49

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
					if (data['age'] > 74):
					    if (data['hours_per_week'] > 45):
						return u'>50K'
					    if (data['hours_per_week'] <= 45):
						if (data['education_num'] > 15):
						    return u'>50K'
						if (data['education_num'] <= 15):
						    return u'<=50K'
					if (data['age'] <= 74):
					    if (data['workclass'] == 'State-gov'):
						if (data['hours_per_week'] > 47):
						    if (data['hours_per_week'] > 57):
							return u'>50K'
						    if (data['hours_per_week'] <= 57):
							return u'<=50K'
						if (data['hours_per_week'] <= 47):
						    return u'>50K'
					    if (data['workclass'] != 'State-gov'):
						return u'>50K'
			    if (data['education_num'] <= 14):
				if (data['hours_per_week'] > 36):
				    if (not 'workclass' in data or data['workclass'] is None):
					return u'>50K'
				    if (data['workclass'] == 'Self-emp-inc'):
					return u'>50K'
				    if (data['workclass'] != 'Self-emp-inc'):
					if (not 'occupation' in data or data['occupation'] is None):
					    return u'>50K'
					if (data['occupation'] == 'Adm-clerical'):
					    return u'>50K'
					if (data['occupation'] != 'Adm-clerical'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'>50K'
					    if (data['final_weight'] > 142784):
						if (data['workclass'] == 'Self-emp-not-inc'):
						    return u'<=50K'
						if (data['workclass'] != 'Self-emp-not-inc'):
						    if (data['occupation'] == 'Exec-managerial'):
							return u'>50K'
						    if (data['occupation'] != 'Exec-managerial'):
							if (data['final_weight'] > 195635):
							    return u'>50K'
							if (data['final_weight'] <= 195635):
							    return u'<=50K'
					    if (data['final_weight'] <= 142784):
						if (data['final_weight'] > 92181):
						    return u'>50K'
						if (data['final_weight'] <= 92181):
						    if (data['age'] > 59):
							if (data['workclass'] == 'Local-gov'):
							    return u'<=50K'
							if (data['workclass'] != 'Local-gov'):
							    return u'>50K'
						    if (data['age'] <= 59):
							return u'<=50K'
				if (data['hours_per_week'] <= 36):
				    return u'<=50K'
			if (data['age'] <= 58):
			    if (data['age'] > 38):
				if (data['education_num'] > 14):
				    if (data['hours_per_week'] > 49):
					if (not 'occupation' in data or data['occupation'] is None):
					    return u'>50K'
					if (data['occupation'] == 'Craft-repair'):
					    return u'<=50K'
					if (data['occupation'] != 'Craft-repair'):
					    if (not 'workclass' in data or data['workclass'] is None):
						return u'>50K'
					    if (data['workclass'] == 'Private'):
						if (not 'race' in data or data['race'] is None):
						    return u'>50K'
						if (data['race'] == 'Asian-Pac-Islander'):
						    return u'<=50K'
						if (data['race'] != 'Asian-Pac-Islander'):
						    if (data['age'] > 42):
							return u'>50K'
						    if (data['age'] <= 42):
							if (data['age'] > 41):
							    if (data['hours_per_week'] > 55):
								return u'<=50K'
							    if (data['hours_per_week'] <= 55):
								return u'<=50K'
							if (data['age'] <= 41):
							    return u'>50K'
					    if (data['workclass'] != 'Private'):
						return u'>50K'
				    if (data['hours_per_week'] <= 49):
					if (not 'relationship' in data or data['relationship'] is None):
					    return u'>50K'
					if (data['relationship'] == 'Not-in-family'):
					    return u'<=50K'
					if (data['relationship'] != 'Not-in-family'):
					    if (not 'occupation' in data or data['occupation'] is None):
						return u'>50K'
					    if (data['occupation'] == 'Transport-moving'):
						return u'<=50K'
					    if (data['occupation'] != 'Transport-moving'):
						if (data['age'] > 57):
						    return u'<=50K'
						if (data['age'] <= 57):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'>50K'
						    if (data['final_weight'] > 95223):
							if (data['final_weight'] > 317314):
							    return u'>50K'
							if (data['final_weight'] <= 317314):
							    if (data['hours_per_week'] > 47):
								return u'<=50K'
							    if (data['hours_per_week'] <= 47):
								return u'>50K'
						    if (data['final_weight'] <= 95223):
							return u'>50K'
				if (data['education_num'] <= 14):
				    if (not 'workclass' in data or data['workclass'] is None):
					return u'>50K'
				    if (data['workclass'] == 'Self-emp-not-inc'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'>50K'
					if (data['final_weight'] > 243112):
					    return u'>50K'
					if (data['final_weight'] <= 243112):
					    if (data['hours_per_week'] > 57):
						if (not 'occupation' in data or data['occupation'] is None):
						    return u'<=50K'
						if (data['occupation'] == 'Exec-managerial'):
						    return u'>50K'
						if (data['occupation'] != 'Exec-managerial'):
						    return u'<=50K'
					    if (data['hours_per_week'] <= 57):
						if (data['hours_per_week'] > 39):
						    if (data['final_weight'] > 226073):
							return u'>50K'
						    if (data['final_weight'] <= 226073):
							if (data['final_weight'] > 211455):
							    return u'<=50K'
							if (data['final_weight'] <= 211455):
							    if (data['age'] > 53):
								return u'<=50K'
							    if (data['age'] <= 53):
								return u'>50K'
						if (data['hours_per_week'] <= 39):
						    return u'>50K'
				    if (data['workclass'] != 'Self-emp-not-inc'):
					if (not 'occupation' in data or data['occupation'] is None):
					    return u'>50K'
					if (data['occupation'] == 'Adm-clerical'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'>50K'
					    if (data['final_weight'] > 347159):
						return u'<=50K'
					    if (data['final_weight'] <= 347159):
						if (data['final_weight'] > 188705):
						    return u'>50K'
						if (data['final_weight'] <= 188705):
						    if (data['hours_per_week'] > 39):
							if (data['final_weight'] > 63143):
							    if (data['hours_per_week'] > 42):
								return u'<=50K'
							    if (data['hours_per_week'] <= 42):
								return u'<=50K'
							if (data['final_weight'] <= 63143):
							    return u'>50K'
						    if (data['hours_per_week'] <= 39):
							return u'>50K'
					if (data['occupation'] != 'Adm-clerical'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'>50K'
					    if (data['final_weight'] > 323185):
						return u'>50K'
					    if (data['final_weight'] <= 323185):
						if (not 'race' in data or data['race'] is None):
						    return u'>50K'
						if (data['race'] == 'Amer-Indian-Eskimo'):
						    return u'<=50K'
						if (data['race'] != 'Amer-Indian-Eskimo'):
						    if (data['occupation'] == 'Other-service'):
							return u'<=50K'
						    if (data['occupation'] != 'Other-service'):
							if (data['final_weight'] > 151676):
							    if (data['hours_per_week'] > 62):
								return u'>50K'
							    if (data['hours_per_week'] <= 62):
								return u'>50K'
							if (data['final_weight'] <= 151676):
							    if (data['final_weight'] > 73703):
								return u'>50K'
							    if (data['final_weight'] <= 73703):
								return u'>50K'
			    if (data['age'] <= 38):
				if (not 'occupation' in data or data['occupation'] is None):
				    return u'>50K'
				if (data['occupation'] == 'Farming-fishing'):
				    return u'<=50K'
				if (data['occupation'] != 'Farming-fishing'):
				    if (data['hours_per_week'] > 42):
					if (data['occupation'] == 'Exec-managerial'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'>50K'
					    if (data['final_weight'] > 285656):
						if (data['final_weight'] > 296849):
						    return u'>50K'
						if (data['final_weight'] <= 296849):
						    return u'<=50K'
					    if (data['final_weight'] <= 285656):
						return u'>50K'
					if (data['occupation'] != 'Exec-managerial'):
					    if (not 'sex' in data or data['sex'] is None):
						return u'>50K'
					    if (data['sex'] == 'Male'):
						if (data['occupation'] == 'Machine-op-inspct'):
						    return u'<=50K'
						if (data['occupation'] != 'Machine-op-inspct'):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'>50K'
						    if (data['workclass'] == 'Private'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'>50K'
							if (data['final_weight'] > 35814):
							    if (data['final_weight'] > 344743):
								return u'<=50K'
							    if (data['final_weight'] <= 344743):
								return u'>50K'
							if (data['final_weight'] <= 35814):
							    return u'<=50K'
						    if (data['workclass'] != 'Private'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'>50K'
							if (data['final_weight'] > 252034):
							    return u'>50K'
							if (data['final_weight'] <= 252034):
							    if (data['age'] > 37):
								return u'>50K'
							    if (data['age'] <= 37):
								return u'<=50K'
					    if (data['sex'] != 'Male'):
						return u'>50K'
				    if (data['hours_per_week'] <= 42):
					if (data['occupation'] == 'Craft-repair'):
					    return u'<=50K'
					if (data['occupation'] != 'Craft-repair'):
					    if (data['hours_per_week'] > 39):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'>50K'
						if (data['final_weight'] > 323491):
						    return u'>50K'
						if (data['final_weight'] <= 323491):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'>50K'
						    if (data['workclass'] == 'Self-emp-inc'):
							return u'>50K'
						    if (data['workclass'] != 'Self-emp-inc'):
							if (data['final_weight'] > 270317):
							    if (data['final_weight'] > 321197):
								return u'>50K'
							    if (data['final_weight'] <= 321197):
								return u'<=50K'
							if (data['final_weight'] <= 270317):
							    if (data['final_weight'] > 203903):
								return u'>50K'
							    if (data['final_weight'] <= 203903):
								return u'>50K'
					    if (data['hours_per_week'] <= 39):
						if (data['hours_per_week'] > 37):
						    return u'<=50K'
						if (data['hours_per_week'] <= 37):
						    if (not 'relationship' in data or data['relationship'] is None):
							return u'>50K'
						    if (data['relationship'] == 'Other-relative'):
							return u'<=50K'
						    if (data['relationship'] != 'Other-relative'):
							if (data['education_num'] > 15):
							    if (data['hours_per_week'] > 35):
								return u'>50K'
							    if (data['hours_per_week'] <= 35):
								return u'<=50K'
							if (data['education_num'] <= 15):
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
					if (data['age'] > 65):
					    return u'<=50K'
					if (data['age'] <= 65):
					    return u'>50K'
				    if (data['age'] <= 48):
					if (data['age'] > 35):
					    if (data['age'] > 43):
						if (data['hours_per_week'] > 42):
						    if (data['hours_per_week'] > 55):
							return u'<=50K'
						    if (data['hours_per_week'] <= 55):
							return u'>50K'
						if (data['hours_per_week'] <= 42):
						    return u'<=50K'
					    if (data['age'] <= 43):
						if (data['final_weight'] > 187120):
						    return u'<=50K'
						if (data['final_weight'] <= 187120):
						    if (data['final_weight'] > 152625):
							return u'>50K'
						    if (data['final_weight'] <= 152625):
							return u'<=50K'
					if (data['age'] <= 35):
					    return u'>50K'
				if (data['final_weight'] <= 90244):
				    return u'<=50K'
			    if (data['workclass'] != 'Self-emp-not-inc'):
				if (data['hours_per_week'] > 67):
				    if (data['hours_per_week'] > 73):
					return u'>50K'
				    if (data['hours_per_week'] <= 73):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 134993):
					    if (data['hours_per_week'] > 71):
						if (data['final_weight'] > 322085):
						    return u'<=50K'
						if (data['final_weight'] <= 322085):
						    return u'>50K'
					    if (data['hours_per_week'] <= 71):
						return u'<=50K'
					if (data['final_weight'] <= 134993):
					    return u'>50K'
				if (data['hours_per_week'] <= 67):
				    if (not 'race' in data or data['race'] is None):
					return u'>50K'
				    if (data['race'] == 'Other'):
					return u'<=50K'
				    if (data['race'] != 'Other'):
					if (not 'relationship' in data or data['relationship'] is None):
					    return u'>50K'
					if (data['relationship'] == 'Other-relative'):
					    return u'<=50K'
					if (data['relationship'] != 'Other-relative'):
					    if (data['hours_per_week'] > 41):
						if (data['age'] > 84):
						    return u'<=50K'
						if (data['age'] <= 84):
						    if (data['age'] > 51):
							if (data['workclass'] == 'Local-gov'):
							    return u'<=50K'
							if (data['workclass'] != 'Local-gov'):
							    if (data['age'] > 58):
								return u'>50K'
							    if (data['age'] <= 58):
								return u'>50K'
						    if (data['age'] <= 51):
							if (data['age'] > 32):
							    if (data['age'] > 33):
								return u'>50K'
							    if (data['age'] <= 33):
								return u'<=50K'
							if (data['age'] <= 32):
							    if (not 'final_weight' in data or data['final_weight'] is None):
								return u'>50K'
							    if (data['final_weight'] > 81292):
								return u'>50K'
							    if (data['final_weight'] <= 81292):
								return u'<=50K'
					    if (data['hours_per_week'] <= 41):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'>50K'
						if (data['final_weight'] > 364614):
						    return u'>50K'
						if (data['final_weight'] <= 364614):
						    if (data['final_weight'] > 337643):
							return u'<=50K'
						    if (data['final_weight'] <= 337643):
							if (data['workclass'] == 'State-gov'):
							    if (data['age'] > 55):
								return u'<=50K'
							    if (data['age'] <= 55):
								return u'>50K'
							if (data['workclass'] != 'State-gov'):
							    if (data['final_weight'] > 202813):
								return u'>50K'
							    if (data['final_weight'] <= 202813):
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
					if (data['final_weight'] > 232277):
					    if (data['age'] > 36):
						if (data['occupation'] == 'Other-service'):
						    return u'<=50K'
						if (data['occupation'] != 'Other-service'):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'>50K'
						    if (data['workclass'] == 'Local-gov'):
							if (data['final_weight'] > 308865):
							    if (data['race'] == 'Black'):
								return u'<=50K'
							    if (data['race'] != 'Black'):
								return u'>50K'
							if (data['final_weight'] <= 308865):
							    return u'<=50K'
						    if (data['workclass'] != 'Local-gov'):
							if (data['occupation'] == 'Farming-fishing'):
							    return u'<=50K'
							if (data['occupation'] != 'Farming-fishing'):
							    if (data['final_weight'] > 407546):
								return u'>50K'
							    if (data['final_weight'] <= 407546):
								return u'>50K'
					    if (data['age'] <= 36):
						if (data['hours_per_week'] > 39):
						    if (data['occupation'] == 'Other-service'):
							return u'<=50K'
						    if (data['occupation'] != 'Other-service'):
							if (data['age'] > 35):
							    if (data['final_weight'] > 326016):
								return u'<=50K'
							    if (data['final_weight'] <= 326016):
								return u'<=50K'
							if (data['age'] <= 35):
							    if (data['final_weight'] > 365060):
								return u'>50K'
							    if (data['final_weight'] <= 365060):
								return u'<=50K'
						if (data['hours_per_week'] <= 39):
						    return u'>50K'
					if (data['final_weight'] <= 232277):
					    if (data['occupation'] == 'Transport-moving'):
						if (data['hours_per_week'] > 42):
						    if (data['final_weight'] > 191925):
							return u'>50K'
						    if (data['final_weight'] <= 191925):
							if (data['age'] > 43):
							    if (data['final_weight'] > 184791):
								return u'<=50K'
							    if (data['final_weight'] <= 184791):
								return u'>50K'
							if (data['age'] <= 43):
							    return u'<=50K'
						if (data['hours_per_week'] <= 42):
						    return u'<=50K'
					    if (data['occupation'] != 'Transport-moving'):
						if (not 'workclass' in data or data['workclass'] is None):
						    return u'>50K'
						if (data['workclass'] == 'Local-gov'):
						    if (data['age'] > 29):
							if (data['final_weight'] > 192388):
							    if (data['age'] > 38):
								return u'>50K'
							    if (data['age'] <= 38):
								return u'>50K'
							if (data['final_weight'] <= 192388):
							    if (data['age'] > 47):
								return u'>50K'
							    if (data['age'] <= 47):
								return u'>50K'
						    if (data['age'] <= 29):
							return u'<=50K'
						if (data['workclass'] != 'Local-gov'):
						    if (data['age'] > 42):
							if (data['race'] == 'Asian-Pac-Islander'):
							    return u'<=50K'
							if (data['race'] != 'Asian-Pac-Islander'):
							    if (data['final_weight'] > 201359):
								return u'>50K'
							    if (data['final_weight'] <= 201359):
								return u'>50K'
						    if (data['age'] <= 42):
							if (data['race'] == 'Asian-Pac-Islander'):
							    if (data['workclass'] == 'Federal-gov'):
								return u'<=50K'
							    if (data['workclass'] != 'Federal-gov'):
								return u'>50K'
							if (data['race'] != 'Asian-Pac-Islander'):
							    if (data['age'] > 37):
								return u'>50K'
							    if (data['age'] <= 37):
								return u'>50K'
				    if (data['final_weight'] <= 121061):
					if (data['occupation'] == 'Machine-op-inspct'):
					    return u'<=50K'
					if (data['occupation'] != 'Machine-op-inspct'):
					    if (data['hours_per_week'] > 53):
						if (data['occupation'] == 'Sales'):
						    if (not 'sex' in data or data['sex'] is None):
							return u'<=50K'
						    if (data['sex'] == 'Male'):
							if (data['age'] > 46):
							    if (data['hours_per_week'] > 57):
								return u'>50K'
							    if (data['hours_per_week'] <= 57):
								return u'<=50K'
							if (data['age'] <= 46):
							    return u'<=50K'
						    if (data['sex'] != 'Male'):
							return u'>50K'
						if (data['occupation'] != 'Sales'):
						    if (data['relationship'] == 'Husband'):
							if (data['final_weight'] > 86725):
							    if (data['final_weight'] > 98678):
								return u'>50K'
							    if (data['final_weight'] <= 98678):
								return u'<=50K'
							if (data['final_weight'] <= 86725):
							    if (not 'workclass' in data or data['workclass'] is None):
								return u'>50K'
							    if (data['workclass'] == 'Self-emp-inc'):
								return u'<=50K'
							    if (data['workclass'] != 'Self-emp-inc'):
								return u'>50K'
						    if (data['relationship'] != 'Husband'):
							return u'<=50K'
					    if (data['hours_per_week'] <= 53):
						if (not 'workclass' in data or data['workclass'] is None):
						    return u'>50K'
						if (data['workclass'] == 'Self-emp-not-inc'):
						    if (data['age'] > 40):
							if (data['hours_per_week'] > 44):
							    if (data['final_weight'] > 110239):
								return u'>50K'
							    if (data['final_weight'] <= 110239):
								return u'<=50K'
							if (data['hours_per_week'] <= 44):
							    if (data['occupation'] == 'Sales'):
								return u'>50K'
							    if (data['occupation'] != 'Sales'):
								return u'<=50K'
						    if (data['age'] <= 40):
							return u'<=50K'
						if (data['workclass'] != 'Self-emp-not-inc'):
						    if (data['hours_per_week'] > 44):
							if (data['hours_per_week'] > 49):
							    if (data['age'] > 36):
								return u'>50K'
							    if (data['age'] <= 36):
								return u'<=50K'
							if (data['hours_per_week'] <= 49):
							    return u'>50K'
						    if (data['hours_per_week'] <= 44):
							if (data['final_weight'] > 117105):
							    return u'>50K'
							if (data['final_weight'] <= 117105):
							    if (data['final_weight'] > 110039):
								return u'<=50K'
							    if (data['final_weight'] <= 110039):
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
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 59538):
					    if (not 'workclass' in data or data['workclass'] is None):
						return u'<=50K'
					    if (data['workclass'] == 'Self-emp-inc'):
						return u'>50K'
					    if (data['workclass'] != 'Self-emp-inc'):
						if (data['final_weight'] > 165889):
						    if (data['final_weight'] > 179942):
							if (data['age'] > 25):
							    if (data['age'] > 26):
								return u'<=50K'
							    if (data['age'] <= 26):
								return u'>50K'
							if (data['age'] <= 25):
							    return u'<=50K'
						    if (data['final_weight'] <= 179942):
							return u'>50K'
						if (data['final_weight'] <= 165889):
						    if (data['hours_per_week'] > 52):
							if (data['hours_per_week'] > 57):
							    return u'<=50K'
							if (data['hours_per_week'] <= 57):
							    return u'>50K'
						    if (data['hours_per_week'] <= 52):
							return u'<=50K'
					if (data['final_weight'] <= 59538):
					    return u'>50K'
				if (data['hours_per_week'] <= 46):
				    if (data['occupation'] == 'Adm-clerical'):
					return u'<=50K'
				    if (data['occupation'] != 'Adm-clerical'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'>50K'
					if (data['final_weight'] > 155506):
					    return u'>50K'
					if (data['final_weight'] <= 155506):
					    if (data['age'] > 27):
						return u'<=50K'
					    if (data['age'] <= 27):
						return u'>50K'
			    if (data['hours_per_week'] <= 41):
				if (not 'final_weight' in data or data['final_weight'] is None):
				    return u'<=50K'
				if (data['final_weight'] > 159383):
				    if (data['final_weight'] > 260996):
					if (data['age'] > 27):
					    if (data['final_weight'] > 263671):
						return u'<=50K'
					    if (data['final_weight'] <= 263671):
						return u'>50K'
					if (data['age'] <= 27):
					    return u'>50K'
				    if (data['final_weight'] <= 260996):
					if (data['occupation'] == 'Exec-managerial'):
					    if (data['age'] > 27):
						return u'>50K'
					    if (data['age'] <= 27):
						return u'<=50K'
					if (data['occupation'] != 'Exec-managerial'):
					    return u'<=50K'
				if (data['final_weight'] <= 159383):
				    if (data['final_weight'] > 100631):
					if (data['age'] > 27):
					    return u'>50K'
					if (data['age'] <= 27):
					    if (data['occupation'] == 'Sales'):
						return u'>50K'
					    if (data['occupation'] != 'Sales'):
						return u'<=50K'
				    if (data['final_weight'] <= 100631):
					if (data['occupation'] == 'Exec-managerial'):
					    if (not 'race' in data or data['race'] is None):
						return u'<=50K'
					    if (data['race'] == 'White'):
						return u'>50K'
					    if (data['race'] != 'White'):
						return u'<=50K'
					if (data['occupation'] != 'Exec-managerial'):
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
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 38129):
					    if (data['age'] > 66):
						return u'<=50K'
					    if (data['age'] <= 66):
						if (not 'occupation' in data or data['occupation'] is None):
						    return u'<=50K'
						if (data['occupation'] == 'Sales'):
						    if (data['final_weight'] > 196834):
							return u'<=50K'
						    if (data['final_weight'] <= 196834):
							return u'>50K'
						if (data['occupation'] != 'Sales'):
						    return u'<=50K'
					if (data['final_weight'] <= 38129):
					    return u'>50K'
				    if (data['race'] != 'White'):
					return u'>50K'
				if (data['hours_per_week'] <= 13):
				    if (not 'occupation' in data or data['occupation'] is None):
					return u'<=50K'
				    if (data['occupation'] == 'Exec-managerial'):
					return u'>50K'
				    if (data['occupation'] != 'Exec-managerial'):
					if (data['occupation'] == 'Prof-specialty'):
					    return u'<=50K'
					if (data['occupation'] != 'Prof-specialty'):
					    if (data['hours_per_week'] > 11):
						return u'>50K'
					    if (data['hours_per_week'] <= 11):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 180316):
						    return u'>50K'
						if (data['final_weight'] <= 180316):
						    return u'<=50K'
			if (data['age'] <= 62):
			    if (data['hours_per_week'] > 12):
				if (not 'workclass' in data or data['workclass'] is None):
				    return u'>50K'
				if (data['workclass'] == 'State-gov'):
				    return u'<=50K'
				if (data['workclass'] != 'State-gov'):
				    if (data['hours_per_week'] > 21):
					if (not 'education' in data or data['education'] is None):
					    return u'<=50K'
					if (data['education'] == 'Prof-school'):
					    return u'>50K'
					if (data['education'] != 'Prof-school'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 302817):
						return u'<=50K'
					    if (data['final_weight'] <= 302817):
						if (data['final_weight'] > 234356):
						    if (data['workclass'] == 'Self-emp-inc'):
							return u'<=50K'
						    if (data['workclass'] != 'Self-emp-inc'):
							return u'>50K'
						if (data['final_weight'] <= 234356):
						    if (data['workclass'] == 'Self-emp-inc'):
							return u'>50K'
						    if (data['workclass'] != 'Self-emp-inc'):
							if (data['final_weight'] > 120839):
							    return u'<=50K'
							if (data['final_weight'] <= 120839):
							    if (data['final_weight'] > 101625):
								return u'>50K'
							    if (data['final_weight'] <= 101625):
								return u'<=50K'
				    if (data['hours_per_week'] <= 21):
					if (data['workclass'] == 'Self-emp-inc'):
					    return u'<=50K'
					if (data['workclass'] != 'Self-emp-inc'):
					    if (not 'relationship' in data or data['relationship'] is None):
						return u'>50K'
					    if (data['relationship'] == 'Husband'):
						if (data['education_num'] > 13):
						    if (not 'occupation' in data or data['occupation'] is None):
							return u'>50K'
						    if (data['occupation'] == 'Exec-managerial'):
							return u'<=50K'
						    if (data['occupation'] != 'Exec-managerial'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'>50K'
							if (data['final_weight'] > 217428):
							    if (data['hours_per_week'] > 17):
								return u'>50K'
							    if (data['hours_per_week'] <= 17):
								return u'<=50K'
							if (data['final_weight'] <= 217428):
							    return u'>50K'
						if (data['education_num'] <= 13):
						    return u'>50K'
					    if (data['relationship'] != 'Husband'):
						return u'<=50K'
			    if (data['hours_per_week'] <= 12):
				if (data['hours_per_week'] > 2):
				    if (data['education_num'] > 14):
					if (data['hours_per_week'] > 5):
					    return u'<=50K'
					if (data['hours_per_week'] <= 5):
					    return u'>50K'
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
					if (data['hours_per_week'] > 27):
					    return u'>50K'
					if (data['hours_per_week'] <= 27):
					    return u'<=50K'
				    if (data['occupation'] != 'Other-service'):
					if (data['workclass'] == 'Local-gov'):
					    if (data['hours_per_week'] > 23):
						if (data['hours_per_week'] > 24):
						    return u'>50K'
						if (data['hours_per_week'] <= 24):
						    return u'<=50K'
					    if (data['hours_per_week'] <= 23):
						return u'>50K'
					if (data['workclass'] != 'Local-gov'):
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
					if (data['hours_per_week'] > 67):
					    return u'>50K'
					if (data['hours_per_week'] <= 67):
					    if (data['age'] > 49):
						if (data['hours_per_week'] > 45):
						    if (data['final_weight'] > 155617):
							return u'>50K'
						    if (data['final_weight'] <= 155617):
							return u'<=50K'
						if (data['hours_per_week'] <= 45):
						    return u'>50K'
					    if (data['age'] <= 49):
						if (data['age'] > 39):
						    return u'<=50K'
						if (data['age'] <= 39):
						    if (data['hours_per_week'] > 47):
							return u'>50K'
						    if (data['hours_per_week'] <= 47):
							return u'<=50K'
			    if (data['occupation'] != 'Farming-fishing'):
				if (data['occupation'] == 'Other-service'):
				    if (data['age'] > 40):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 196473):
					    if (data['hours_per_week'] > 37):
						if (data['hours_per_week'] > 46):
						    return u'<=50K'
						if (data['hours_per_week'] <= 46):
						    return u'>50K'
					    if (data['hours_per_week'] <= 37):
						return u'<=50K'
					if (data['final_weight'] <= 196473):
					    if (data['age'] > 46):
						if (data['age'] > 48):
						    if (not 'sex' in data or data['sex'] is None):
							return u'<=50K'
						    if (data['sex'] == 'Male'):
							return u'<=50K'
						    if (data['sex'] != 'Male'):
							return u'>50K'
						if (data['age'] <= 48):
						    return u'>50K'
					    if (data['age'] <= 46):
						return u'<=50K'
				    if (data['age'] <= 40):
					return u'<=50K'
				if (data['occupation'] != 'Other-service'):
				    if (data['occupation'] == 'Exec-managerial'):
					if (not 'workclass' in data or data['workclass'] is None):
					    return u'>50K'
					if (data['workclass'] == 'State-gov'):
					    if (not 'sex' in data or data['sex'] is None):
						return u'<=50K'
					    if (data['sex'] == 'Male'):
						return u'<=50K'
					    if (data['sex'] != 'Male'):
						return u'>50K'
					if (data['workclass'] != 'State-gov'):
					    if (data['workclass'] == 'Self-emp-not-inc'):
						if (not 'education' in data or data['education'] is None):
						    return u'<=50K'
						if (data['education'] == 'Assoc-voc'):
						    return u'<=50K'
						if (data['education'] != 'Assoc-voc'):
						    if (data['age'] > 44):
							if (data['age'] > 50):
							    if (data['hours_per_week'] > 37):
								return u'>50K'
							    if (data['hours_per_week'] <= 37):
								return u'<=50K'
							if (data['age'] <= 50):
							    return u'<=50K'
						    if (data['age'] <= 44):
							return u'>50K'
					    if (data['workclass'] != 'Self-emp-not-inc'):
						if (data['hours_per_week'] > 48):
						    if (data['hours_per_week'] > 91):
							return u'<=50K'
						    if (data['hours_per_week'] <= 91):
							if (data['age'] > 44):
							    if (data['age'] > 60):
								return u'<=50K'
							    if (data['age'] <= 60):
								return u'>50K'
							if (data['age'] <= 44):
							    if (data['education_num'] > 10):
								return u'>50K'
							    if (data['education_num'] <= 10):
								return u'>50K'
						if (data['hours_per_week'] <= 48):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'>50K'
						    if (data['final_weight'] > 137265):
							if (data['age'] > 68):
							    return u'>50K'
							if (data['age'] <= 68):
							    if (data['age'] > 64):
								return u'<=50K'
							    if (data['age'] <= 64):
								return u'>50K'
						    if (data['final_weight'] <= 137265):
							if (data['final_weight'] > 133255):
							    return u'<=50K'
							if (data['final_weight'] <= 133255):
							    if (data['workclass'] == 'Federal-gov'):
								return u'>50K'
							    if (data['workclass'] != 'Federal-gov'):
								return u'<=50K'
				    if (data['occupation'] != 'Exec-managerial'):
					if (data['occupation'] == 'Prof-specialty'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'>50K'
					    if (data['final_weight'] > 133264):
						if (not 'workclass' in data or data['workclass'] is None):
						    return u'>50K'
						if (data['workclass'] == 'Self-emp-not-inc'):
						    return u'<=50K'
						if (data['workclass'] != 'Self-emp-not-inc'):
						    if (data['age'] > 57):
							if (data['hours_per_week'] > 46):
							    return u'>50K'
							if (data['hours_per_week'] <= 46):
							    return u'<=50K'
						    if (data['age'] <= 57):
							if (data['final_weight'] > 304409):
							    if (data['hours_per_week'] > 38):
								return u'>50K'
							    if (data['hours_per_week'] <= 38):
								return u'<=50K'
							if (data['final_weight'] <= 304409):
							    if (data['final_weight'] > 202429):
								return u'>50K'
							    if (data['final_weight'] <= 202429):
								return u'>50K'
					    if (data['final_weight'] <= 133264):
						if (data['final_weight'] > 45882):
						    if (data['final_weight'] > 56857):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'Amer-Indian-Eskimo'):
							    return u'>50K'
							if (data['race'] != 'Amer-Indian-Eskimo'):
							    if (data['final_weight'] > 101705):
								return u'<=50K'
							    if (data['final_weight'] <= 101705):
								return u'<=50K'
						    if (data['final_weight'] <= 56857):
							return u'>50K'
						if (data['final_weight'] <= 45882):
						    return u'<=50K'
					if (data['occupation'] != 'Prof-specialty'):
					    if (data['occupation'] == 'Tech-support'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'>50K'
						if (data['final_weight'] > 132978):
						    if (data['age'] > 53):
							return u'>50K'
						    if (data['age'] <= 53):
							if (data['final_weight'] > 183597):
							    if (data['final_weight'] > 343751):
								return u'>50K'
							    if (data['final_weight'] <= 343751):
								return u'<=50K'
							if (data['final_weight'] <= 183597):
							    if (data['age'] > 52):
								return u'<=50K'
							    if (data['age'] <= 52):
								return u'>50K'
						if (data['final_weight'] <= 132978):
						    if (data['hours_per_week'] > 41):
							if (data['final_weight'] > 117485):
							    return u'<=50K'
							if (data['final_weight'] <= 117485):
							    return u'>50K'
						    if (data['hours_per_week'] <= 41):
							if (not 'education' in data or data['education'] is None):
							    return u'<=50K'
							if (data['education'] == 'Assoc-voc'):
							    return u'<=50K'
							if (data['education'] != 'Assoc-voc'):
							    if (data['final_weight'] > 51969):
								return u'<=50K'
							    if (data['final_weight'] <= 51969):
								return u'>50K'
					    if (data['occupation'] != 'Tech-support'):
						if (not 'workclass' in data or data['workclass'] is None):
						    return u'<=50K'
						if (data['workclass'] == 'Self-emp-inc'):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'>50K'
						    if (data['final_weight'] > 92178):
							if (data['hours_per_week'] > 64):
							    if (data['final_weight'] > 189582):
								return u'>50K'
							    if (data['final_weight'] <= 189582):
								return u'<=50K'
							if (data['hours_per_week'] <= 64):
							    if (data['final_weight'] > 194045):
								return u'<=50K'
							    if (data['final_weight'] <= 194045):
								return u'>50K'
						    if (data['final_weight'] <= 92178):
							return u'>50K'
						if (data['workclass'] != 'Self-emp-inc'):
						    if (not 'relationship' in data or data['relationship'] is None):
							return u'<=50K'
						    if (data['relationship'] == 'Other-relative'):
							return u'<=50K'
						    if (data['relationship'] != 'Other-relative'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 62494):
							    if (data['occupation'] == 'Handlers-cleaners'):
								return u'<=50K'
							    if (data['occupation'] != 'Handlers-cleaners'):
								return u'>50K'
							if (data['final_weight'] <= 62494):
							    if (data['final_weight'] > 27834):
								return u'<=50K'
							    if (data['final_weight'] <= 27834):
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
					if (data['final_weight'] > 145136):
					    if (data['hours_per_week'] > 51):
						return u'>50K'
					    if (data['hours_per_week'] <= 51):
						if (data['final_weight'] > 199146):
						    if (data['final_weight'] > 297876):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'White'):
							    return u'>50K'
							if (data['race'] != 'White'):
							    return u'<=50K'
						    if (data['final_weight'] <= 297876):
							return u'<=50K'
						if (data['final_weight'] <= 199146):
						    if (data['hours_per_week'] > 42):
							return u'>50K'
						    if (data['hours_per_week'] <= 42):
							if (data['final_weight'] > 170195):
							    return u'<=50K'
							if (data['final_weight'] <= 170195):
							    if (data['hours_per_week'] > 37):
								return u'<=50K'
							    if (data['hours_per_week'] <= 37):
								return u'>50K'
					if (data['final_weight'] <= 145136):
					    return u'<=50K'
				    if (data['final_weight'] <= 92214):
					if (data['hours_per_week'] > 47):
					    if (data['hours_per_week'] > 55):
						return u'>50K'
					    if (data['hours_per_week'] <= 55):
						return u'<=50K'
					if (data['hours_per_week'] <= 47):
					    return u'>50K'
				if (data['workclass'] != 'Self-emp-not-inc'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
					return u'>50K'
				    if (data['final_weight'] > 189527):
					if (data['age'] > 55):
					    if (data['workclass'] == 'Private'):
						if (data['hours_per_week'] > 45):
						    return u'<=50K'
						if (data['hours_per_week'] <= 45):
						    if (data['final_weight'] > 263581):
							return u'>50K'
						    if (data['final_weight'] <= 263581):
							if (data['final_weight'] > 211118):
							    return u'<=50K'
							if (data['final_weight'] <= 211118):
							    return u'>50K'
					    if (data['workclass'] != 'Private'):
						return u'<=50K'
					if (data['age'] <= 55):
					    if (data['hours_per_week'] > 47):
						return u'>50K'
					    if (data['hours_per_week'] <= 47):
						if (data['final_weight'] > 224226):
						    if (data['final_weight'] > 278979):
							if (data['age'] > 42):
							    return u'>50K'
							if (data['age'] <= 42):
							    return u'<=50K'
						    if (data['final_weight'] <= 278979):
							return u'<=50K'
						if (data['final_weight'] <= 224226):
						    if (not 'sex' in data or data['sex'] is None):
							return u'>50K'
						    if (data['sex'] == 'Male'):
							return u'>50K'
						    if (data['sex'] != 'Male'):
							if (data['final_weight'] > 204133):
							    return u'<=50K'
							if (data['final_weight'] <= 204133):
							    return u'>50K'
				    if (data['final_weight'] <= 189527):
					if (data['hours_per_week'] > 37):
					    if (data['age'] > 63):
						return u'>50K'
					    if (data['age'] <= 63):
						if (data['age'] > 54):
						    if (data['final_weight'] > 116610):
							if (data['age'] > 61):
							    return u'>50K'
							if (data['age'] <= 61):
							    if (data['hours_per_week'] > 39):
								return u'<=50K'
							    if (data['hours_per_week'] <= 39):
								return u'<=50K'
						    if (data['final_weight'] <= 116610):
							if (data['workclass'] == 'Self-emp-inc'):
							    if (data['final_weight'] > 59224):
								return u'<=50K'
							    if (data['final_weight'] <= 59224):
								return u'>50K'
							if (data['workclass'] != 'Self-emp-inc'):
							    return u'<=50K'
						if (data['age'] <= 54):
						    if (data['age'] > 53):
							return u'>50K'
						    if (data['age'] <= 53):
							if (not 'race' in data or data['race'] is None):
							    return u'>50K'
							if (data['race'] == 'Amer-Indian-Eskimo'):
							    return u'<=50K'
							if (data['race'] != 'Amer-Indian-Eskimo'):
							    if (data['final_weight'] > 31851):
								return u'>50K'
							    if (data['final_weight'] <= 31851):
								return u'>50K'
					if (data['hours_per_week'] <= 37):
					    return u'>50K'
			    if (data['occupation'] != 'Exec-managerial'):
				if (data['occupation'] == 'Other-service'):
				    if (not 'sex' in data or data['sex'] is None):
					return u'<=50K'
				    if (data['sex'] == 'Male'):
					if (data['age'] > 47):
					    if (data['hours_per_week'] > 37):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 324775):
						    return u'>50K'
						if (data['final_weight'] <= 324775):
						    if (data['age'] > 52):
							return u'<=50K'
						    if (data['age'] <= 52):
							if (data['age'] > 50):
							    return u'>50K'
							if (data['age'] <= 50):
							    return u'<=50K'
					    if (data['hours_per_week'] <= 37):
						return u'>50K'
					if (data['age'] <= 47):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 84981):
						if (data['final_weight'] > 92314):
						    if (data['final_weight'] > 121238):
							if (data['final_weight'] > 167547):
							    if (data['age'] > 42):
								return u'<=50K'
							    if (data['age'] <= 42):
								return u'<=50K'
							if (data['final_weight'] <= 167547):
							    if (not 'race' in data or data['race'] is None):
								return u'>50K'
							    if (data['race'] == 'Asian-Pac-Islander'):
								return u'<=50K'
							    if (data['race'] != 'Asian-Pac-Islander'):
								return u'>50K'
						    if (data['final_weight'] <= 121238):
							return u'<=50K'
						if (data['final_weight'] <= 92314):
						    return u'>50K'
					    if (data['final_weight'] <= 84981):
						return u'<=50K'
				    if (data['sex'] != 'Male'):
					return u'<=50K'
				if (data['occupation'] != 'Other-service'):
				    if (data['occupation'] == 'Farming-fishing'):
					if (data['hours_per_week'] > 39):
					    if (data['age'] > 65):
						return u'<=50K'
					    if (data['age'] <= 65):
						if (data['age'] > 63):
						    return u'>50K'
						if (data['age'] <= 63):
						    if (data['hours_per_week'] > 71):
							return u'<=50K'
						    if (data['hours_per_week'] <= 71):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 243348):
							    if (not 'workclass' in data or data['workclass'] is None):
								return u'>50K'
							    if (data['workclass'] == 'Private'):
								return u'>50K'
							    if (data['workclass'] != 'Private'):
								return u'<=50K'
							if (data['final_weight'] <= 243348):
							    if (not 'workclass' in data or data['workclass'] is None):
								return u'<=50K'
							    if (data['workclass'] == 'Private'):
								return u'<=50K'
							    if (data['workclass'] != 'Private'):
								return u'<=50K'
					if (data['hours_per_week'] <= 39):
					    return u'<=50K'
				    if (data['occupation'] != 'Farming-fishing'):
					if (not 'race' in data or data['race'] is None):
					    return u'<=50K'
					if (data['race'] == 'Amer-Indian-Eskimo'):
					    return u'<=50K'
					if (data['race'] != 'Amer-Indian-Eskimo'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 535569):
						if (data['final_weight'] > 792076):
						    return u'<=50K'
						if (data['final_weight'] <= 792076):
						    return u'>50K'
					    if (data['final_weight'] <= 535569):
						if (data['hours_per_week'] > 71):
						    if (data['hours_per_week'] > 87):
							if (data['final_weight'] > 234866):
							    return u'>50K'
							if (data['final_weight'] <= 234866):
							    return u'<=50K'
						    if (data['hours_per_week'] <= 87):
							if (data['age'] > 49):
							    if (data['hours_per_week'] > 82):
								return u'>50K'
							    if (data['hours_per_week'] <= 82):
								return u'<=50K'
							if (data['age'] <= 49):
							    return u'>50K'
						if (data['hours_per_week'] <= 71):
						    if (data['occupation'] == 'Prof-specialty'):
							if (data['final_weight'] > 71716):
							    if (data['age'] > 41):
								return u'<=50K'
							    if (data['age'] <= 41):
								return u'>50K'
							if (data['final_weight'] <= 71716):
							    return u'>50K'
						    if (data['occupation'] != 'Prof-specialty'):
							if (data['age'] > 43):
							    if (not 'workclass' in data or data['workclass'] is None):
								return u'<=50K'
							    if (data['workclass'] == 'Federal-gov'):
								return u'>50K'
							    if (data['workclass'] != 'Federal-gov'):
								return u'<=50K'
							if (data['age'] <= 43):
							    if (not 'workclass' in data or data['workclass'] is None):
								return u'<=50K'
							    if (data['workclass'] == 'Self-emp-not-inc'):
								return u'<=50K'
							    if (data['workclass'] != 'Self-emp-not-inc'):
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
					if (data['education_num'] > 9):
					    return u'<=50K'
					if (data['education_num'] <= 9):
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
					if (data['workclass'] == 'Local-gov'):
					    return u'<=50K'
					if (data['workclass'] != 'Local-gov'):
					    if (not 'occupation' in data or data['occupation'] is None):
						return u'>50K'
					    if (data['occupation'] == 'Adm-clerical'):
						return u'>50K'
					    if (data['occupation'] != 'Adm-clerical'):
						if (not 'race' in data or data['race'] is None):
						    return u'>50K'
						if (data['race'] == 'White'):
						    if (data['age'] > 52):
							if (data['occupation'] == 'Sales'):
							    return u'>50K'
							if (data['occupation'] != 'Sales'):
							    return u'<=50K'
						    if (data['age'] <= 52):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'>50K'
							if (data['final_weight'] > 93252):
							    if (data['final_weight'] > 301988):
								return u'>50K'
							    if (data['final_weight'] <= 301988):
								return u'<=50K'
							if (data['final_weight'] <= 93252):
							    return u'>50K'
						if (data['race'] != 'White'):
						    return u'<=50K'
				    if (data['education_num'] <= 9):
					if (data['age'] > 57):
					    return u'>50K'
					if (data['age'] <= 57):
					    if (data['hours_per_week'] > 18):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 194378):
						    return u'<=50K'
						if (data['final_weight'] <= 194378):
						    if (data['final_weight'] > 151718):
							if (data['hours_per_week'] > 22):
							    return u'>50K'
							if (data['hours_per_week'] <= 22):
							    if (not 'occupation' in data or data['occupation'] is None):
								return u'<=50K'
							    if (data['occupation'] == 'Other-service'):
								return u'<=50K'
							    if (data['occupation'] != 'Other-service'):
								return u'>50K'
						    if (data['final_weight'] <= 151718):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'Amer-Indian-Eskimo'):
							    return u'>50K'
							if (data['race'] != 'Amer-Indian-Eskimo'):
							    if (not 'occupation' in data or data['occupation'] is None):
								return u'<=50K'
							    if (data['occupation'] == 'Exec-managerial'):
								return u'<=50K'
							    if (data['occupation'] != 'Exec-managerial'):
								return u'<=50K'
					    if (data['hours_per_week'] <= 18):
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
					if (data['age'] > 41):
					    if (data['age'] > 59):
						if (data['education_num'] > 9):
						    if (data['hours_per_week'] > 3):
							if (data['final_weight'] > 265692):
							    return u'>50K'
							if (data['final_weight'] <= 265692):
							    if (data['final_weight'] > 114061):
								return u'<=50K'
							    if (data['final_weight'] <= 114061):
								return u'<=50K'
						    if (data['hours_per_week'] <= 3):
							return u'>50K'
						if (data['education_num'] <= 9):
						    return u'<=50K'
					    if (data['age'] <= 59):
						if (data['occupation'] == 'Handlers-cleaners'):
						    return u'>50K'
						if (data['occupation'] != 'Handlers-cleaners'):
						    if (data['occupation'] == 'Sales'):
							if (data['hours_per_week'] > 22):
							    return u'>50K'
							if (data['hours_per_week'] <= 22):
							    return u'<=50K'
						    if (data['occupation'] != 'Sales'):
							if (data['final_weight'] > 184287):
							    return u'<=50K'
							if (data['final_weight'] <= 184287):
							    if (data['final_weight'] > 100729):
								return u'<=50K'
							    if (data['final_weight'] <= 100729):
								return u'<=50K'
					if (data['age'] <= 41):
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
					if (data['age'] > 32):
					    if (data['education_num'] > 10):
						return u'>50K'
					    if (data['education_num'] <= 10):
						return u'<=50K'
					if (data['age'] <= 32):
					    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
						return u'>50K'
					    if (data['hours_per_week'] > 52):
						return u'<=50K'
					    if (data['hours_per_week'] <= 52):
						return u'>50K'
				if (data['workclass'] != 'Self-emp-not-inc'):
				    if (data['age'] > 32):
					if (not 'sex' in data or data['sex'] is None):
					    return u'>50K'
					if (data['sex'] == 'Male'):
					    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
						return u'>50K'
					    if (data['hours_per_week'] > 59):
						if (data['education_num'] > 9):
						    return u'>50K'
						if (data['education_num'] <= 9):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 156615):
							return u'>50K'
						    if (data['final_weight'] <= 156615):
							return u'<=50K'
					    if (data['hours_per_week'] <= 59):
						if (data['education_num'] > 10):
						    return u'<=50K'
						if (data['education_num'] <= 10):
						    if (data['hours_per_week'] > 46):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 337190):
							    return u'>50K'
							if (data['final_weight'] <= 337190):
							    if (data['hours_per_week'] > 52):
								return u'>50K'
							    if (data['hours_per_week'] <= 52):
								return u'<=50K'
						    if (data['hours_per_week'] <= 46):
							if (data['hours_per_week'] > 38):
							    if (not 'final_weight' in data or data['final_weight'] is None):
								return u'>50K'
							    if (data['final_weight'] > 210417):
								return u'>50K'
							    if (data['final_weight'] <= 210417):
								return u'>50K'
							if (data['hours_per_week'] <= 38):
							    return u'<=50K'
					if (data['sex'] != 'Male'):
					    return u'>50K'
				    if (data['age'] <= 32):
					if (data['education_num'] > 11):
					    return u'>50K'
					if (data['education_num'] <= 11):
					    if (not 'sex' in data or data['sex'] is None):
						return u'<=50K'
					    if (data['sex'] == 'Male'):
						if (not 'hours_per_week' in data or data['hours_per_week'] is None):
						    return u'<=50K'
						if (data['hours_per_week'] > 67):
						    return u'<=50K'
						if (data['hours_per_week'] <= 67):
						    if (data['workclass'] == 'Local-gov'):
							return u'<=50K'
						    if (data['workclass'] != 'Local-gov'):
							if (not 'race' in data or data['race'] is None):
							    return u'>50K'
							if (data['race'] == 'Black'):
							    return u'<=50K'
							if (data['race'] != 'Black'):
							    if (not 'education' in data or data['education'] is None):
								return u'>50K'
							    if (data['education'] == 'Some-college'):
								return u'>50K'
							    if (data['education'] != 'Some-college'):
								return u'<=50K'
					    if (data['sex'] != 'Male'):
						return u'<=50K'
			    if (data['age'] <= 27):
				if (not 'final_weight' in data or data['final_weight'] is None):
				    return u'<=50K'
				if (data['final_weight'] > 162313):
				    if (data['final_weight'] > 190463):
					if (not 'workclass' in data or data['workclass'] is None):
					    return u'<=50K'
					if (data['workclass'] == 'Private'):
					    return u'<=50K'
					if (data['workclass'] != 'Private'):
					    if (data['education_num'] > 9):
						return u'>50K'
					    if (data['education_num'] <= 9):
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
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 133042):
					    return u'>50K'
					if (data['final_weight'] <= 133042):
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
					if (data['hours_per_week'] > 73):
					    return u'>50K'
					if (data['hours_per_week'] <= 73):
					    if (data['hours_per_week'] > 61):
						return u'<=50K'
					    if (data['hours_per_week'] <= 61):
						if (data['occupation'] == 'Adm-clerical'):
						    return u'>50K'
						if (data['occupation'] != 'Adm-clerical'):
						    if (data['occupation'] == 'Other-service'):
							return u'<=50K'
						    if (data['occupation'] != 'Other-service'):
							if (data['occupation'] == 'Protective-serv'):
							    if (not 'workclass' in data or data['workclass'] is None):
								return u'>50K'
							    if (data['workclass'] == 'Local-gov'):
								return u'>50K'
							    if (data['workclass'] != 'Local-gov'):
								return u'<=50K'
							if (data['occupation'] != 'Protective-serv'):
							    if (not 'workclass' in data or data['workclass'] is None):
								return u'<=50K'
							    if (data['workclass'] == 'Local-gov'):
								return u'<=50K'
							    if (data['workclass'] != 'Local-gov'):
								return u'<=50K'
				    if (data['age'] <= 31):
					if (data['occupation'] == 'Handlers-cleaners'):
					    return u'<=50K'
					if (data['occupation'] != 'Handlers-cleaners'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 131760):
						if (data['education_num'] > 9):
						    if (data['hours_per_week'] > 57):
							if (data['occupation'] == 'Craft-repair'):
							    if (data['hours_per_week'] > 59):
								return u'>50K'
							    if (data['hours_per_week'] <= 59):
								return u'<=50K'
							if (data['occupation'] != 'Craft-repair'):
							    return u'<=50K'
						    if (data['hours_per_week'] <= 57):
							if (data['final_weight'] > 166656):
							    if (data['occupation'] == 'Craft-repair'):
								return u'>50K'
							    if (data['occupation'] != 'Craft-repair'):
								return u'<=50K'
							if (data['final_weight'] <= 166656):
							    return u'>50K'
						if (data['education_num'] <= 9):
						    if (not 'relationship' in data or data['relationship'] is None):
							return u'<=50K'
						    if (data['relationship'] == 'Other-relative'):
							return u'>50K'
						    if (data['relationship'] != 'Other-relative'):
							if (data['occupation'] == 'Prof-specialty'):
							    return u'>50K'
							if (data['occupation'] != 'Prof-specialty'):
							    if (data['final_weight'] > 410231):
								return u'>50K'
							    if (data['final_weight'] <= 410231):
								return u'<=50K'
					    if (data['final_weight'] <= 131760):
						if (data['final_weight'] > 95351):
						    return u'<=50K'
						if (data['final_weight'] <= 95351):
						    if (data['occupation'] == 'Transport-moving'):
							if (data['hours_per_week'] > 51):
							    return u'>50K'
							if (data['hours_per_week'] <= 51):
							    return u'<=50K'
						    if (data['occupation'] != 'Transport-moving'):
							if (data['occupation'] == 'Sales'):
							    if (data['education_num'] > 9):
								return u'<=50K'
							    if (data['education_num'] <= 9):
								return u'>50K'
							if (data['occupation'] != 'Sales'):
							    if (data['occupation'] == 'Adm-clerical'):
								return u'<=50K'
							    if (data['occupation'] != 'Adm-clerical'):
								return u'<=50K'
				if (data['hours_per_week'] <= 46):
				    if (data['occupation'] == 'Prof-specialty'):
					if (data['hours_per_week'] > 39):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 316937):
						return u'<=50K'
					    if (data['final_weight'] <= 316937):
						if (data['final_weight'] > 268432):
						    return u'>50K'
						if (data['final_weight'] <= 268432):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'<=50K'
						    if (data['workclass'] == 'State-gov'):
							return u'>50K'
						    if (data['workclass'] != 'State-gov'):
							if (not 'education' in data or data['education'] is None):
							    return u'<=50K'
							if (data['education'] == 'Some-college'):
							    if (data['final_weight'] > 66920):
								return u'<=50K'
							    if (data['final_weight'] <= 66920):
								return u'>50K'
							if (data['education'] != 'Some-college'):
							    if (data['final_weight'] > 82745):
								return u'>50K'
							    if (data['final_weight'] <= 82745):
								return u'<=50K'
					if (data['hours_per_week'] <= 39):
					    if (data['hours_per_week'] > 7):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'>50K'
						if (data['final_weight'] > 151741):
						    return u'>50K'
						if (data['final_weight'] <= 151741):
						    if (data['hours_per_week'] > 17):
							if (data['final_weight'] > 71976):
							    return u'<=50K'
							if (data['final_weight'] <= 71976):
							    return u'>50K'
						    if (data['hours_per_week'] <= 17):
							return u'>50K'
					    if (data['hours_per_week'] <= 7):
						return u'<=50K'
				    if (data['occupation'] != 'Prof-specialty'):
					if (not 'workclass' in data or data['workclass'] is None):
					    return u'<=50K'
					if (data['workclass'] == 'Federal-gov'):
					    if (data['age'] > 30):
						if (data['occupation'] == 'Tech-support'):
						    return u'<=50K'
						if (data['occupation'] != 'Tech-support'):
						    if (data['occupation'] == 'Craft-repair'):
							return u'<=50K'
						    if (data['occupation'] != 'Craft-repair'):
							if (not 'race' in data or data['race'] is None):
							    return u'>50K'
							if (data['race'] == 'White'):
							    return u'>50K'
							if (data['race'] != 'White'):
							    if (data['education_num'] > 9):
								return u'>50K'
							    if (data['education_num'] <= 9):
								return u'<=50K'
					    if (data['age'] <= 30):
						return u'>50K'
					if (data['workclass'] != 'Federal-gov'):
					    if (not 'relationship' in data or data['relationship'] is None):
						return u'<=50K'
					    if (data['relationship'] == 'Own-child'):
						return u'<=50K'
					    if (data['relationship'] != 'Own-child'):
						if (data['occupation'] == 'Handlers-cleaners'):
						    if (not 'education' in data or data['education'] is None):
							return u'<=50K'
						    if (data['education'] == 'Some-college'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 186571):
							    if (data['final_weight'] > 214492):
								return u'<=50K'
							    if (data['final_weight'] <= 214492):
								return u'>50K'
							if (data['final_weight'] <= 186571):
							    if (data['final_weight'] > 37583):
								return u'<=50K'
							    if (data['final_weight'] <= 37583):
								return u'<=50K'
						    if (data['education'] != 'Some-college'):
							if (data['age'] > 30):
							    return u'<=50K'
							if (data['age'] <= 30):
							    if (data['age'] > 29):
								return u'<=50K'
							    if (data['age'] <= 29):
								return u'<=50K'
						if (data['occupation'] != 'Handlers-cleaners'):
						    if (data['relationship'] == 'Wife'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 66306):
							    if (data['final_weight'] > 202819):
								return u'<=50K'
							    if (data['final_weight'] <= 202819):
								return u'<=50K'
							if (data['final_weight'] <= 66306):
							    if (data['final_weight'] > 47362):
								return u'>50K'
							    if (data['final_weight'] <= 47362):
								return u'>50K'
						    if (data['relationship'] != 'Wife'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 170446):
							    if (data['final_weight'] > 274418):
								return u'<=50K'
							    if (data['final_weight'] <= 274418):
								return u'<=50K'
							if (data['final_weight'] <= 170446):
							    if (not 'education' in data or data['education'] is None):
								return u'<=50K'
							    if (data['education'] == 'Some-college'):
								return u'<=50K'
							    if (data['education'] != 'Some-college'):
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
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 339707):
					    return u'>50K'
					if (data['final_weight'] <= 339707):
					    if (not 'education' in data or data['education'] is None):
						return u'<=50K'
					    if (data['education'] == 'Some-college'):
						if (not 'race' in data or data['race'] is None):
						    return u'<=50K'
						if (data['race'] == 'White'):
						    if (data['final_weight'] > 121186):
							return u'>50K'
						    if (data['final_weight'] <= 121186):
							return u'<=50K'
						if (data['race'] != 'White'):
						    return u'<=50K'
					    if (data['education'] != 'Some-college'):
						return u'<=50K'
				    if (data['sex'] != 'Male'):
					return u'<=50K'
				if (data['occupation'] != 'Adm-clerical'):
				    if (data['occupation'] == 'Handlers-cleaners'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 154988):
					    return u'<=50K'
					if (data['final_weight'] <= 154988):
					    return u'>50K'
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
					if (data['hours_per_week'] > 37):
					    if (data['final_weight'] > 190475):
						if (data['final_weight'] > 226535):
						    if (data['hours_per_week'] > 45):
							return u'>50K'
						    if (data['hours_per_week'] <= 45):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'White'):
							    return u'<=50K'
							if (data['race'] != 'White'):
							    return u'>50K'
						if (data['final_weight'] <= 226535):
						    return u'>50K'
					    if (data['final_weight'] <= 190475):
						if (data['final_weight'] > 181878):
						    return u'<=50K'
						if (data['final_weight'] <= 181878):
						    if (data['hours_per_week'] > 55):
							return u'<=50K'
						    if (data['hours_per_week'] <= 55):
							if (data['final_weight'] > 156702):
							    if (data['final_weight'] > 177866):
								return u'>50K'
							    if (data['final_weight'] <= 177866):
								return u'<=50K'
							if (data['final_weight'] <= 156702):
							    return u'>50K'
					if (data['hours_per_week'] <= 37):
					    return u'<=50K'
				    if (data['final_weight'] <= 89485):
					return u'<=50K'
				if (data['occupation'] != 'Transport-moving'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
					return u'<=50K'
				    if (data['final_weight'] > 162184):
					if (data['age'] > 62):
					    if (not 'workclass' in data or data['workclass'] is None):
						return u'<=50K'
					    if (data['workclass'] == 'Local-gov'):
						return u'>50K'
					    if (data['workclass'] != 'Local-gov'):
						if (data['occupation'] == 'Sales'):
						    if (data['hours_per_week'] > 33):
							return u'>50K'
						    if (data['hours_per_week'] <= 33):
							return u'<=50K'
						if (data['occupation'] != 'Sales'):
						    return u'<=50K'
					if (data['age'] <= 62):
					    return u'<=50K'
				    if (data['final_weight'] <= 162184):
					if (data['final_weight'] > 151824):
					    if (data['occupation'] == 'Machine-op-inspct'):
						return u'<=50K'
					    if (data['occupation'] != 'Machine-op-inspct'):
						return u'>50K'
					if (data['final_weight'] <= 151824):
					    if (data['final_weight'] > 118909):
						return u'<=50K'
					    if (data['final_weight'] <= 118909):
						if (data['final_weight'] > 65018):
						    if (data['age'] > 55):
							if (data['occupation'] == 'Exec-managerial'):
							    return u'>50K'
							if (data['occupation'] != 'Exec-managerial'):
							    if (not 'race' in data or data['race'] is None):
								return u'<=50K'
							    if (data['race'] == 'White'):
								return u'<=50K'
							    if (data['race'] != 'White'):
								return u'>50K'
						    if (data['age'] <= 55):
							return u'<=50K'
						if (data['final_weight'] <= 65018):
						    return u'<=50K'
			    if (data['age'] <= 53):
				if (not 'occupation' in data or data['occupation'] is None):
				    return u'<=50K'
				if (data['occupation'] == 'Sales'):
				    if (data['hours_per_week'] > 52):
					return u'<=50K'
				    if (data['hours_per_week'] <= 52):
					if (not 'sex' in data or data['sex'] is None):
					    return u'>50K'
					if (data['sex'] == 'Male'):
					    return u'>50K'
					if (data['sex'] != 'Male'):
					    return u'<=50K'
				if (data['occupation'] != 'Sales'):
				    if (not 'workclass' in data or data['workclass'] is None):
					return u'<=50K'
				    if (data['workclass'] == 'Local-gov'):
					return u'<=50K'
				    if (data['workclass'] != 'Local-gov'):
					if (data['occupation'] == 'Exec-managerial'):
					    if (data['hours_per_week'] > 55):
						return u'<=50K'
					    if (data['hours_per_week'] <= 55):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'>50K'
						if (data['final_weight'] > 340151):
						    return u'<=50K'
						if (data['final_weight'] <= 340151):
						    return u'>50K'
					if (data['occupation'] != 'Exec-managerial'):
					    if (not 'race' in data or data['race'] is None):
						return u'<=50K'
					    if (data['race'] == 'Other'):
						return u'>50K'
					    if (data['race'] != 'Other'):
						if (data['hours_per_week'] > 39):
						    if (data['race'] == 'Asian-Pac-Islander'):
							return u'<=50K'
						    if (data['race'] != 'Asian-Pac-Islander'):
							if (data['occupation'] == 'Other-service'):
							    if (data['race'] == 'White'):
								return u'<=50K'
							    if (data['race'] != 'White'):
								return u'<=50K'
							if (data['occupation'] != 'Other-service'):
							    if (data['education_num'] > 7):
								return u'<=50K'
							    if (data['education_num'] <= 7):
								return u'<=50K'
						if (data['hours_per_week'] <= 39):
						    if (data['race'] == 'White'):
							return u'<=50K'
						    if (data['race'] != 'White'):
							if (data['hours_per_week'] > 36):
							    return u'<=50K'
							if (data['hours_per_week'] <= 36):
							    return u'>50K'
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
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'>50K'
					if (data['final_weight'] > 99690):
					    return u'>50K'
					if (data['final_weight'] <= 99690):
					    return u'<=50K'
				if (data['occupation'] != 'Exec-managerial'):
				    if (data['occupation'] == 'Sales'):
					if (data['age'] > 53):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'>50K'
					    if (data['final_weight'] > 104904):
						return u'>50K'
					    if (data['final_weight'] <= 104904):
						return u'<=50K'
					if (data['age'] <= 53):
					    return u'<=50K'
				    if (data['occupation'] != 'Sales'):
					if (data['hours_per_week'] > 39):
					    if (data['hours_per_week'] > 51):
						return u'<=50K'
					    if (data['hours_per_week'] <= 51):
						if (data['hours_per_week'] > 49):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 216613):
							return u'<=50K'
						    if (data['final_weight'] <= 216613):
							if (data['final_weight'] > 194761):
							    return u'>50K'
							if (data['final_weight'] <= 194761):
							    if (not 'sex' in data or data['sex'] is None):
								return u'<=50K'
							    if (data['sex'] == 'Male'):
								return u'<=50K'
							    if (data['sex'] != 'Male'):
								return u'>50K'
						if (data['hours_per_week'] <= 49):
						    if (data['age'] > 53):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 60233):
							    if (data['age'] > 56):
								return u'<=50K'
							    if (data['age'] <= 56):
								return u'<=50K'
							if (data['final_weight'] <= 60233):
							    return u'>50K'
						    if (data['age'] <= 53):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 221011):
							    if (data['final_weight'] > 237838):
								return u'<=50K'
							    if (data['final_weight'] <= 237838):
								return u'<=50K'
							if (data['final_weight'] <= 221011):
							    return u'<=50K'
					if (data['hours_per_week'] <= 39):
					    return u'<=50K'
			    if (data['workclass'] != 'Private'):
				if (data['hours_per_week'] > 55):
				    if (data['workclass'] == 'Self-emp-not-inc'):
					if (not 'occupation' in data or data['occupation'] is None):
					    return u'>50K'
					if (data['occupation'] == 'Farming-fishing'):
					    if (data['age'] > 61):
						if (data['education_num'] > 3):
						    return u'>50K'
						if (data['education_num'] <= 3):
						    return u'<=50K'
					    if (data['age'] <= 61):
						return u'<=50K'
					if (data['occupation'] != 'Farming-fishing'):
					    return u'>50K'
				    if (data['workclass'] != 'Self-emp-not-inc'):
					return u'<=50K'
				if (data['hours_per_week'] <= 55):
				    if (data['workclass'] == 'Self-emp-inc'):
					if (not 'occupation' in data or data['occupation'] is None):
					    return u'>50K'
					if (data['occupation'] == 'Craft-repair'):
					    return u'>50K'
					if (data['occupation'] != 'Craft-repair'):
					    if (data['occupation'] == 'Sales'):
						return u'>50K'
					    if (data['occupation'] != 'Sales'):
						if (data['occupation'] == 'Machine-op-inspct'):
						    return u'>50K'
						if (data['occupation'] != 'Machine-op-inspct'):
						    return u'<=50K'
				    if (data['workclass'] != 'Self-emp-inc'):
					if (data['age'] > 40):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 35109):
						if (data['hours_per_week'] > 27):
						    return u'<=50K'
						if (data['hours_per_week'] <= 27):
						    if (data['final_weight'] > 220800):
							return u'>50K'
						    if (data['final_weight'] <= 220800):
							return u'<=50K'
					    if (data['final_weight'] <= 35109):
						if (data['final_weight'] > 33892):
						    return u'>50K'
						if (data['final_weight'] <= 33892):
						    return u'<=50K'
					if (data['age'] <= 40):
					    if (not 'education' in data or data['education'] is None):
						return u'>50K'
					    if (data['education'] == '7th-8th'):
						return u'>50K'
					    if (data['education'] != '7th-8th'):
						if (not 'occupation' in data or data['occupation'] is None):
						    return u'<=50K'
						if (data['occupation'] == 'Craft-repair'):
						    return u'<=50K'
						if (data['occupation'] != 'Craft-repair'):
						    if (not 'relationship' in data or data['relationship'] is None):
							return u'>50K'
						    if (data['relationship'] == 'Other-relative'):
							return u'<=50K'
						    if (data['relationship'] != 'Other-relative'):
							return u'>50K'
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
					if (data['education_num'] > 6):
					    return u'>50K'
					if (data['education_num'] <= 6):
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
					if (not 'sex' in data or data['sex'] is None):
					    return u'<=50K'
					if (data['sex'] == 'Male'):
					    return u'>50K'
					if (data['sex'] != 'Male'):
					    return u'<=50K'
				    if (data['final_weight'] <= 219946):
					return u'<=50K'
				if (data['occupation'] != 'Adm-clerical'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
					return u'<=50K'
				    if (data['final_weight'] > 145325):
					return u'<=50K'
				    if (data['final_weight'] <= 145325):
					if (data['age'] > 28):
					    if (data['age'] > 29):
						if (not 'education' in data or data['education'] is None):
						    return u'<=50K'
						if (data['education'] == '7th-8th'):
						    if (data['occupation'] == 'Machine-op-inspct'):
							return u'>50K'
						    if (data['occupation'] != 'Machine-op-inspct'):
							return u'<=50K'
						if (data['education'] != '7th-8th'):
						    return u'<=50K'
					    if (data['age'] <= 29):
						if (data['occupation'] == 'Other-service'):
						    return u'<=50K'
						if (data['occupation'] != 'Other-service'):
						    return u'>50K'
					if (data['age'] <= 28):
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
					if (data['age'] > 27):
					    if (not 'hours_per_week' in data or data['hours_per_week'] is None):
						return u'>50K'
					    if (data['hours_per_week'] > 30):
						return u'>50K'
					    if (data['hours_per_week'] <= 30):
						return u'<=50K'
					if (data['age'] <= 27):
					    if (data['occupation'] == 'Transport-moving'):
						return u'>50K'
					    if (data['occupation'] != 'Transport-moving'):
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
					if (not 'workclass' in data or data['workclass'] is None):
					    return u'>50K'
					if (data['workclass'] == 'Local-gov'):
					    return u'<=50K'
					if (data['workclass'] != 'Local-gov'):
					    return u'>50K'
				    if (data['education_num'] <= 13):
					return u'<=50K'
				if (data['hours_per_week'] <= 58):
				    if (not 'race' in data or data['race'] is None):
					return u'>50K'
				    if (data['race'] == 'Amer-Indian-Eskimo'):
					return u'<=50K'
				    if (data['race'] != 'Amer-Indian-Eskimo'):
					if (data['marital_status'] == 'Never-married'):
					    if (data['age'] > 48):
						return u'>50K'
					    if (data['age'] <= 48):
						if (data['age'] > 46):
						    return u'<=50K'
						if (data['age'] <= 46):
						    return u'>50K'
					if (data['marital_status'] != 'Never-married'):
					    return u'>50K'
			    if (data['final_weight'] <= 160393):
				if (data['hours_per_week'] > 47):
				    if (data['final_weight'] > 51818):
					if (not 'workclass' in data or data['workclass'] is None):
					    return u'>50K'
					if (data['workclass'] == 'Private'):
					    if (data['marital_status'] == 'Separated'):
						return u'<=50K'
					    if (data['marital_status'] != 'Separated'):
						return u'>50K'
					if (data['workclass'] != 'Private'):
					    if (data['hours_per_week'] > 62):
						if (data['hours_per_week'] > 85):
						    return u'<=50K'
						if (data['hours_per_week'] <= 85):
						    return u'>50K'
					    if (data['hours_per_week'] <= 62):
						return u'<=50K'
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
					if (data['final_weight'] > 259049):
					    return u'<=50K'
					if (data['final_weight'] <= 259049):
					    if (not 'race' in data or data['race'] is None):
						return u'>50K'
					    if (data['race'] == 'Black'):
						return u'<=50K'
					    if (data['race'] != 'Black'):
						if (data['final_weight'] > 40926):
						    if (data['workclass'] == 'State-gov'):
							return u'<=50K'
						    if (data['workclass'] != 'State-gov'):
							if (data['age'] > 31):
							    if (data['hours_per_week'] > 49):
								return u'>50K'
							    if (data['hours_per_week'] <= 49):
								return u'>50K'
							if (data['age'] <= 31):
							    if (data['education_num'] > 13):
								return u'<=50K'
							    if (data['education_num'] <= 13):
								return u'>50K'
						if (data['final_weight'] <= 40926):
						    return u'<=50K'
		    if (data['occupation'] != 'Exec-managerial'):
			if (data['education_num'] > 14):
			    if (data['age'] > 32):
				if (data['age'] > 52):
				    if (data['marital_status'] == 'Widowed'):
					return u'>50K'
				    if (data['marital_status'] != 'Widowed'):
					if (not 'workclass' in data or data['workclass'] is None):
					    return u'<=50K'
					if (data['workclass'] == 'Private'):
					    return u'<=50K'
					if (data['workclass'] != 'Private'):
					    if (data['hours_per_week'] > 55):
						return u'<=50K'
					    if (data['hours_per_week'] <= 55):
						if (data['marital_status'] == 'Never-married'):
						    return u'>50K'
						if (data['marital_status'] != 'Never-married'):
						    if (data['hours_per_week'] > 47):
							return u'<=50K'
						    if (data['hours_per_week'] <= 47):
							return u'>50K'
				if (data['age'] <= 52):
				    if (data['hours_per_week'] > 52):
					if (data['hours_per_week'] > 75):
					    return u'<=50K'
					if (data['hours_per_week'] <= 75):
					    return u'>50K'
				    if (data['hours_per_week'] <= 52):
					if (not 'relationship' in data or data['relationship'] is None):
					    return u'>50K'
					if (data['relationship'] == 'Not-in-family'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'>50K'
					    if (data['final_weight'] > 215668):
						return u'<=50K'
					    if (data['final_weight'] <= 215668):
						if (not 'workclass' in data or data['workclass'] is None):
						    return u'>50K'
						if (data['workclass'] == 'State-gov'):
						    return u'<=50K'
						if (data['workclass'] != 'State-gov'):
						    if (data['final_weight'] > 67253):
							if (data['age'] > 45):
							    if (data['hours_per_week'] > 47):
								return u'>50K'
							    if (data['hours_per_week'] <= 47):
								return u'<=50K'
							if (data['age'] <= 45):
							    return u'>50K'
						    if (data['final_weight'] <= 67253):
							return u'<=50K'
					if (data['relationship'] != 'Not-in-family'):
					    return u'>50K'
			    if (data['age'] <= 32):
				if (data['age'] > 29):
				    return u'<=50K'
				if (data['age'] <= 29):
				    if (data['marital_status'] == 'Never-married'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 92062):
					    return u'<=50K'
					if (data['final_weight'] <= 92062):
					    if (not 'sex' in data or data['sex'] is None):
						return u'<=50K'
					    if (data['sex'] == 'Male'):
						return u'>50K'
					    if (data['sex'] != 'Male'):
						return u'<=50K'
				    if (data['marital_status'] != 'Never-married'):
					return u'>50K'
			if (data['education_num'] <= 14):
			    if (not 'sex' in data or data['sex'] is None):
				return u'<=50K'
			    if (data['sex'] == 'Male'):
				if (data['hours_per_week'] > 55):
				    if (data['occupation'] == 'Sales'):
					if (not 'relationship' in data or data['relationship'] is None):
					    return u'<=50K'
					if (data['relationship'] == 'Own-child'):
					    return u'<=50K'
					if (data['relationship'] != 'Own-child'):
					    if (not 'workclass' in data or data['workclass'] is None):
						return u'>50K'
					    if (data['workclass'] == 'Self-emp-not-inc'):
						return u'<=50K'
					    if (data['workclass'] != 'Self-emp-not-inc'):
						if (not 'race' in data or data['race'] is None):
						    return u'>50K'
						if (data['race'] == 'White'):
						    if (data['age'] > 39):
							if (data['age'] > 51):
							    return u'<=50K'
							if (data['age'] <= 51):
							    if (data['marital_status'] == 'Never-married'):
								return u'<=50K'
							    if (data['marital_status'] != 'Never-married'):
								return u'>50K'
						    if (data['age'] <= 39):
							if (data['education_num'] > 13):
							    return u'<=50K'
							if (data['education_num'] <= 13):
							    if (data['marital_status'] == 'Never-married'):
								return u'>50K'
							    if (data['marital_status'] != 'Never-married'):
								return u'<=50K'
						if (data['race'] != 'White'):
						    return u'>50K'
				    if (data['occupation'] != 'Sales'):
					if (not 'race' in data or data['race'] is None):
					    return u'<=50K'
					if (data['race'] == 'Asian-Pac-Islander'):
					    return u'>50K'
					if (data['race'] != 'Asian-Pac-Islander'):
					    if (data['occupation'] == 'Adm-clerical'):
						if (data['marital_status'] == 'Never-married'):
						    return u'>50K'
						if (data['marital_status'] != 'Never-married'):
						    return u'<=50K'
					    if (data['occupation'] != 'Adm-clerical'):
						if (data['hours_per_week'] > 87):
						    if (data['hours_per_week'] > 94):
							return u'<=50K'
						    if (data['hours_per_week'] <= 94):
							return u'>50K'
						if (data['hours_per_week'] <= 87):
						    return u'<=50K'
				if (data['hours_per_week'] <= 55):
				    if (not 'workclass' in data or data['workclass'] is None):
					return u'<=50K'
				    if (data['workclass'] == 'State-gov'):
					return u'<=50K'
				    if (data['workclass'] != 'State-gov'):
					if (data['age'] > 32):
					    if (data['workclass'] == 'Self-emp-inc'):
						return u'<=50K'
					    if (data['workclass'] != 'Self-emp-inc'):
						if (data['marital_status'] == 'Separated'):
						    return u'<=50K'
						if (data['marital_status'] != 'Separated'):
						    if (data['occupation'] == 'Craft-repair'):
							return u'>50K'
						    if (data['occupation'] != 'Craft-repair'):
							if (data['age'] > 55):
							    if (data['marital_status'] == 'Widowed'):
								return u'>50K'
							    if (data['marital_status'] != 'Widowed'):
								return u'<=50K'
							if (data['age'] <= 55):
							    if (data['age'] > 41):
								return u'>50K'
							    if (data['age'] <= 41):
								return u'<=50K'
					if (data['age'] <= 32):
					    if (not 'race' in data or data['race'] is None):
						return u'<=50K'
					    if (data['race'] == 'Black'):
						return u'>50K'
					    if (data['race'] != 'Black'):
						if (data['workclass'] == 'Private'):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 286123):
							if (data['age'] > 29):
							    if (data['hours_per_week'] > 47):
								return u'<=50K'
							    if (data['hours_per_week'] <= 47):
								return u'>50K'
							if (data['age'] <= 29):
							    return u'>50K'
						    if (data['final_weight'] <= 286123):
							if (data['final_weight'] > 222378):
							    return u'<=50K'
							if (data['final_weight'] <= 222378):
							    if (data['final_weight'] > 204109):
								return u'>50K'
							    if (data['final_weight'] <= 204109):
								return u'<=50K'
						if (data['workclass'] != 'Private'):
						    return u'<=50K'
			    if (data['sex'] != 'Male'):
				if (not 'final_weight' in data or data['final_weight'] is None):
				    return u'<=50K'
				if (data['final_weight'] > 151124):
				    if (data['final_weight'] > 158605):
					if (data['marital_status'] == 'Married-spouse-absent'):
					    return u'>50K'
					if (data['marital_status'] != 'Married-spouse-absent'):
					    if (not 'race' in data or data['race'] is None):
						return u'<=50K'
					    if (data['race'] == 'Asian-Pac-Islander'):
						return u'>50K'
					    if (data['race'] != 'Asian-Pac-Islander'):
						if (data['age'] > 43):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'<=50K'
						    if (data['workclass'] == 'State-gov'):
							return u'>50K'
						    if (data['workclass'] != 'State-gov'):
							if (data['workclass'] == 'Local-gov'):
							    if (data['age'] > 57):
								return u'>50K'
							    if (data['age'] <= 57):
								return u'<=50K'
							if (data['workclass'] != 'Local-gov'):
							    return u'<=50K'
						if (data['age'] <= 43):
						    if (data['age'] > 29):
							if (data['age'] > 32):
							    if (data['marital_status'] == 'Never-married'):
								return u'<=50K'
							    if (data['marital_status'] != 'Never-married'):
								return u'<=50K'
							if (data['age'] <= 32):
							    if (data['final_weight'] > 241978):
								return u'<=50K'
							    if (data['final_weight'] <= 241978):
								return u'>50K'
						    if (data['age'] <= 29):
							if (not 'relationship' in data or data['relationship'] is None):
							    return u'<=50K'
							if (data['relationship'] == 'Unmarried'):
							    return u'>50K'
							if (data['relationship'] != 'Unmarried'):
							    return u'<=50K'
				    if (data['final_weight'] <= 158605):
					if (data['final_weight'] > 157227):
					    return u'<=50K'
					if (data['final_weight'] <= 157227):
					    return u'>50K'
				if (data['final_weight'] <= 151124):
				    if (not 'workclass' in data or data['workclass'] is None):
					return u'<=50K'
				    if (data['workclass'] == 'Federal-gov'):
					return u'>50K'
				    if (data['workclass'] != 'Federal-gov'):
					if (not 'relationship' in data or data['relationship'] is None):
					    return u'<=50K'
					if (data['relationship'] == 'Not-in-family'):
					    if (data['hours_per_week'] > 61):
						if (data['hours_per_week'] > 67):
						    return u'<=50K'
						if (data['hours_per_week'] <= 67):
						    return u'>50K'
					    if (data['hours_per_week'] <= 61):
						if (data['final_weight'] > 107801):
						    if (data['final_weight'] > 127548):
							if (data['hours_per_week'] > 52):
							    return u'>50K'
							if (data['hours_per_week'] <= 52):
							    return u'<=50K'
						    if (data['final_weight'] <= 127548):
							if (data['education_num'] > 13):
							    return u'<=50K'
							if (data['education_num'] <= 13):
							    return u'>50K'
						if (data['final_weight'] <= 107801):
						    return u'<=50K'
					if (data['relationship'] != 'Not-in-family'):
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
					if (data['education_num'] > 15):
					    return u'<=50K'
					if (data['education_num'] <= 15):
					    if (not 'workclass' in data or data['workclass'] is None):
						return u'>50K'
					    if (data['workclass'] == 'State-gov'):
						return u'<=50K'
					    if (data['workclass'] != 'State-gov'):
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
					if (data['education_num'] > 15):
					    return u'>50K'
					if (data['education_num'] <= 15):
					    if (data['hours_per_week'] > 37):
						if (not 'occupation' in data or data['occupation'] is None):
						    return u'<=50K'
						if (data['occupation'] == 'Prof-specialty'):
						    if (data['final_weight'] > 174189):
							return u'>50K'
						    if (data['final_weight'] <= 174189):
							return u'<=50K'
						if (data['occupation'] != 'Prof-specialty'):
						    return u'<=50K'
					    if (data['hours_per_week'] <= 37):
						return u'>50K'
				if (data['marital_status'] != 'Never-married'):
				    if (not 'final_weight' in data or data['final_weight'] is None):
					return u'<=50K'
				    if (data['final_weight'] > 170081):
					if (data['final_weight'] > 227385):
					    return u'<=50K'
					if (data['final_weight'] <= 227385):
					    if (data['age'] > 40):
						if (data['age'] > 47):
						    if (not 'workclass' in data or data['workclass'] is None):
							return u'<=50K'
						    if (data['workclass'] == 'Local-gov'):
							return u'>50K'
						    if (data['workclass'] != 'Local-gov'):
							return u'<=50K'
						if (data['age'] <= 47):
						    return u'>50K'
					    if (data['age'] <= 40):
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
					if (data['marital_status'] == 'Never-married'):
					    if (data['age'] > 54):
						return u'<=50K'
					    if (data['age'] <= 54):
						if (data['education_num'] > 13):
						    if (not 'sex' in data or data['sex'] is None):
							return u'>50K'
						    if (data['sex'] == 'Male'):
							return u'>50K'
						    if (data['sex'] != 'Male'):
							return u'<=50K'
						if (data['education_num'] <= 13):
						    if (data['workclass'] == 'Local-gov'):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'White'):
							    return u'>50K'
							if (data['race'] != 'White'):
							    return u'<=50K'
						    if (data['workclass'] != 'Local-gov'):
							return u'<=50K'
					if (data['marital_status'] != 'Never-married'):
					    if (data['age'] > 59):
						if (data['age'] > 64):
						    if (data['marital_status'] == 'Widowed'):
							if (not 'sex' in data or data['sex'] is None):
							    return u'>50K'
							if (data['sex'] == 'Male'):
							    return u'>50K'
							if (data['sex'] != 'Male'):
							    return u'<=50K'
						    if (data['marital_status'] != 'Widowed'):
							return u'<=50K'
						if (data['age'] <= 64):
						    if (data['hours_per_week'] > 41):
							return u'<=50K'
						    if (data['hours_per_week'] <= 41):
							return u'>50K'
					    if (data['age'] <= 59):
						if (data['age'] > 55):
						    if (data['workclass'] == 'Self-emp-not-inc'):
							return u'>50K'
						    if (data['workclass'] != 'Self-emp-not-inc'):
							return u'<=50K'
						if (data['age'] <= 55):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 212626):
							if (not 'sex' in data or data['sex'] is None):
							    return u'>50K'
							if (data['sex'] == 'Male'):
							    return u'>50K'
							if (data['sex'] != 'Male'):
							    if (data['final_weight'] > 233333):
								return u'<=50K'
							    if (data['final_weight'] <= 233333):
								return u'>50K'
						    if (data['final_weight'] <= 212626):
							if (data['final_weight'] > 38663):
							    if (data['final_weight'] > 126205):
								return u'<=50K'
							    if (data['final_weight'] <= 126205):
								return u'<=50K'
							if (data['final_weight'] <= 38663):
							    return u'>50K'
				if (data['relationship'] != 'Not-in-family'):
				    if (data['age'] > 49):
					if (not 'sex' in data or data['sex'] is None):
					    return u'<=50K'
					if (data['sex'] == 'Male'):
					    if (not 'occupation' in data or data['occupation'] is None):
						return u'<=50K'
					    if (data['occupation'] == 'Prof-specialty'):
						return u'>50K'
					    if (data['occupation'] != 'Prof-specialty'):
						return u'<=50K'
					if (data['sex'] != 'Male'):
					    return u'<=50K'
				    if (data['age'] <= 49):
					if (data['age'] > 46):
					    if (not 'sex' in data or data['sex'] is None):
						return u'<=50K'
					    if (data['sex'] == 'Male'):
						return u'>50K'
					    if (data['sex'] != 'Male'):
						if (data['education_num'] > 13):
						    if (not 'occupation' in data or data['occupation'] is None):
							return u'<=50K'
						    if (data['occupation'] == 'Exec-managerial'):
							return u'>50K'
						    if (data['occupation'] != 'Exec-managerial'):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'Black'):
							    return u'>50K'
							if (data['race'] != 'Black'):
							    return u'<=50K'
						if (data['education_num'] <= 13):
						    if (not 'occupation' in data or data['occupation'] is None):
							return u'<=50K'
						    if (data['occupation'] == 'Priv-house-serv'):
							return u'>50K'
						    if (data['occupation'] != 'Priv-house-serv'):
							if (data['occupation'] == 'Prof-specialty'):
							    if (not 'race' in data or data['race'] is None):
								return u'<=50K'
							    if (data['race'] == 'White'):
								return u'>50K'
							    if (data['race'] != 'White'):
								return u'<=50K'
							if (data['occupation'] != 'Prof-specialty'):
							    return u'<=50K'
					if (data['age'] <= 46):
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
					if (data['hours_per_week'] > 18):
					    if (data['age'] > 77):
						return u'>50K'
					    if (data['age'] <= 77):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 154955):
						    return u'<=50K'
						if (data['final_weight'] <= 154955):
						    if (data['marital_status'] == 'Never-married'):
							return u'<=50K'
						    if (data['marital_status'] != 'Never-married'):
							return u'>50K'
					if (data['hours_per_week'] <= 18):
					    return u'<=50K'
			if (data['age'] <= 45):
			    if (data['hours_per_week'] > 34):
				if (not 'workclass' in data or data['workclass'] is None):
				    return u'<=50K'
				if (data['workclass'] == 'State-gov'):
				    return u'<=50K'
				if (data['workclass'] != 'State-gov'):
				    if (data['workclass'] == 'Federal-gov'):
					if (not 'sex' in data or data['sex'] is None):
					    return u'<=50K'
					if (data['sex'] == 'Male'):
					    if (data['age'] > 40):
						return u'>50K'
					    if (data['age'] <= 40):
						if (data['marital_status'] == 'Widowed'):
						    return u'>50K'
						if (data['marital_status'] != 'Widowed'):
						    if (not 'occupation' in data or data['occupation'] is None):
							return u'<=50K'
						    if (data['occupation'] == 'Adm-clerical'):
							return u'<=50K'
						    if (data['occupation'] != 'Adm-clerical'):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'White'):
							    if (data['occupation'] == 'Prof-specialty'):
								return u'<=50K'
							    if (data['occupation'] != 'Prof-specialty'):
								return u'>50K'
							if (data['race'] != 'White'):
							    return u'<=50K'
					if (data['sex'] != 'Male'):
					    return u'<=50K'
				    if (data['workclass'] != 'Federal-gov'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 101112):
					    if (data['age'] > 34):
						if (data['marital_status'] == 'Never-married'):
						    if (data['workclass'] == 'Private'):
							if (not 'occupation' in data or data['occupation'] is None):
							    return u'<=50K'
							if (data['occupation'] == 'Exec-managerial'):
							    if (data['final_weight'] > 183320):
								return u'<=50K'
							    if (data['final_weight'] <= 183320):
								return u'>50K'
							if (data['occupation'] != 'Exec-managerial'):
							    if (data['final_weight'] > 136616):
								return u'<=50K'
							    if (data['final_weight'] <= 136616):
								return u'<=50K'
						    if (data['workclass'] != 'Private'):
							if (data['final_weight'] > 183395):
							    return u'<=50K'
							if (data['final_weight'] <= 183395):
							    if (data['final_weight'] > 166429):
								return u'>50K'
							    if (data['final_weight'] <= 166429):
								return u'<=50K'
						if (data['marital_status'] != 'Never-married'):
						    if (data['age'] > 35):
							if (data['final_weight'] > 172291):
							    if (data['workclass'] == 'Self-emp-not-inc'):
								return u'<=50K'
							    if (data['workclass'] != 'Self-emp-not-inc'):
								return u'<=50K'
							if (data['final_weight'] <= 172291):
							    if (data['final_weight'] > 155329):
								return u'>50K'
							    if (data['final_weight'] <= 155329):
								return u'<=50K'
						    if (data['age'] <= 35):
							if (not 'occupation' in data or data['occupation'] is None):
							    return u'<=50K'
							if (data['occupation'] == 'Tech-support'):
							    return u'>50K'
							if (data['occupation'] != 'Tech-support'):
							    if (data['marital_status'] == 'Separated'):
								return u'>50K'
							    if (data['marital_status'] != 'Separated'):
								return u'<=50K'
					    if (data['age'] <= 34):
						if (not 'occupation' in data or data['occupation'] is None):
						    return u'<=50K'
						if (data['occupation'] == 'Adm-clerical'):
						    return u'<=50K'
						if (data['occupation'] != 'Adm-clerical'):
						    if (data['occupation'] == 'Exec-managerial'):
							return u'<=50K'
						    if (data['occupation'] != 'Exec-managerial'):
							if (data['final_weight'] > 137961):
							    if (data['education_num'] > 13):
								return u'<=50K'
							    if (data['education_num'] <= 13):
								return u'<=50K'
							if (data['final_weight'] <= 137961):
							    if (data['occupation'] == 'Sales'):
								return u'>50K'
							    if (data['occupation'] != 'Sales'):
								return u'<=50K'
					if (data['final_weight'] <= 101112):
					    if (data['age'] > 28):
						return u'<=50K'
					    if (data['age'] <= 28):
						if (not 'sex' in data or data['sex'] is None):
						    return u'<=50K'
						if (data['sex'] == 'Male'):
						    if (not 'relationship' in data or data['relationship'] is None):
							return u'<=50K'
						    if (data['relationship'] == 'Not-in-family'):
							return u'>50K'
						    if (data['relationship'] != 'Not-in-family'):
							if (not 'occupation' in data or data['occupation'] is None):
							    return u'<=50K'
							if (data['occupation'] == 'Craft-repair'):
							    return u'>50K'
							if (data['occupation'] != 'Craft-repair'):
							    return u'<=50K'
						if (data['sex'] != 'Male'):
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
					if (not 'occupation' in data or data['occupation'] is None):
					    return u'<=50K'
					if (data['occupation'] == 'Prof-specialty'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 187971):
						if (data['final_weight'] > 318115):
						    if (data['final_weight'] > 364262):
							return u'<=50K'
						    if (data['final_weight'] <= 364262):
							return u'>50K'
						if (data['final_weight'] <= 318115):
						    return u'<=50K'
					    if (data['final_weight'] <= 187971):
						if (data['final_weight'] > 36821):
						    if (data['final_weight'] > 184988):
							return u'>50K'
						    if (data['final_weight'] <= 184988):
							if (not 'education' in data or data['education'] is None):
							    return u'<=50K'
							if (data['education'] == 'Masters'):
							    if (data['hours_per_week'] > 50):
								return u'>50K'
							    if (data['hours_per_week'] <= 50):
								return u'<=50K'
							if (data['education'] != 'Masters'):
							    if (data['age'] > 26):
								return u'<=50K'
							    if (data['age'] <= 26):
								return u'<=50K'
						if (data['final_weight'] <= 36821):
						    return u'>50K'
					if (data['occupation'] != 'Prof-specialty'):
					    if (data['relationship'] == 'Unmarried'):
						if (data['race'] == 'White'):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 205660):
							return u'<=50K'
						    if (data['final_weight'] <= 205660):
							return u'>50K'
						if (data['race'] != 'White'):
						    return u'<=50K'
					    if (data['relationship'] != 'Unmarried'):
						if (data['occupation'] == 'Exec-managerial'):
						    return u'<=50K'
						if (data['occupation'] != 'Exec-managerial'):
						    if (data['hours_per_week'] > 43):
							if (data['occupation'] == 'Craft-repair'):
							    if (data['hours_per_week'] > 50):
								return u'>50K'
							    if (data['hours_per_week'] <= 50):
								return u'<=50K'
							if (data['occupation'] != 'Craft-repair'):
							    if (data['occupation'] == 'Farming-fishing'):
								return u'<=50K'
							    if (data['occupation'] != 'Farming-fishing'):
								return u'<=50K'
						    if (data['hours_per_week'] <= 43):
							if (data['occupation'] == 'Adm-clerical'):
							    if (not 'final_weight' in data or data['final_weight'] is None):
								return u'<=50K'
							    if (data['final_weight'] > 199150):
								return u'<=50K'
							    if (data['final_weight'] <= 199150):
								return u'<=50K'
							if (data['occupation'] != 'Adm-clerical'):
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
					if (not 'workclass' in data or data['workclass'] is None):
					    return u'<=50K'
					if (data['workclass'] == 'Self-emp-inc'):
					    if (data['marital_status'] == 'Widowed'):
						return u'>50K'
					    if (data['marital_status'] != 'Widowed'):
						return u'<=50K'
					if (data['workclass'] != 'Self-emp-inc'):
					    if (data['hours_per_week'] > 61):
						return u'>50K'
					    if (data['hours_per_week'] <= 61):
						if (data['occupation'] == 'Tech-support'):
						    return u'>50K'
						if (data['occupation'] != 'Tech-support'):
						    if (data['occupation'] == 'Other-service'):
							return u'<=50K'
						    if (data['occupation'] != 'Other-service'):
							if (data['education_num'] > 8):
							    if (not 'sex' in data or data['sex'] is None):
								return u'<=50K'
							    if (data['sex'] == 'Male'):
								return u'<=50K'
							    if (data['sex'] != 'Male'):
								return u'<=50K'
							if (data['education_num'] <= 8):
							    return u'<=50K'
			if (data['age'] <= 53):
			    if (not 'relationship' in data or data['relationship'] is None):
				return u'<=50K'
			    if (data['relationship'] == 'Not-in-family'):
				if (not 'education' in data or data['education'] is None):
				    return u'<=50K'
				if (data['education'] == 'HS-grad'):
				    if (data['hours_per_week'] > 47):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 30779):
					    if (not 'race' in data or data['race'] is None):
						return u'<=50K'
					    if (data['race'] == 'White'):
						if (data['final_weight'] > 521347):
						    return u'>50K'
						if (data['final_weight'] <= 521347):
						    if (data['marital_status'] == 'Divorced'):
							if (data['hours_per_week'] > 51):
							    if (data['final_weight'] > 33674):
								return u'<=50K'
							    if (data['final_weight'] <= 33674):
								return u'>50K'
							if (data['hours_per_week'] <= 51):
							    if (not 'occupation' in data or data['occupation'] is None):
								return u'<=50K'
							    if (data['occupation'] == 'Tech-support'):
								return u'>50K'
							    if (data['occupation'] != 'Tech-support'):
								return u'<=50K'
						    if (data['marital_status'] != 'Divorced'):
							if (data['age'] > 39):
							    return u'<=50K'
							if (data['age'] <= 39):
							    if (data['final_weight'] > 35599):
								return u'<=50K'
							    if (data['final_weight'] <= 35599):
								return u'>50K'
					    if (data['race'] != 'White'):
						return u'<=50K'
					if (data['final_weight'] <= 30779):
					    if (data['age'] > 40):
						return u'<=50K'
					    if (data['age'] <= 40):
						return u'>50K'
				    if (data['hours_per_week'] <= 47):
					if (not 'workclass' in data or data['workclass'] is None):
					    return u'<=50K'
					if (data['workclass'] == 'Federal-gov'):
					    if (data['marital_status'] == 'Never-married'):
						return u'>50K'
					    if (data['marital_status'] != 'Never-married'):
						return u'<=50K'
					if (data['workclass'] != 'Federal-gov'):
					    return u'<=50K'
				if (data['education'] != 'HS-grad'):
				    if (not 'workclass' in data or data['workclass'] is None):
					return u'<=50K'
				    if (data['workclass'] == 'Self-emp-not-inc'):
					return u'<=50K'
				    if (data['workclass'] != 'Self-emp-not-inc'):
					if (data['age'] > 52):
					    if (data['hours_per_week'] > 52):
						return u'<=50K'
					    if (data['hours_per_week'] <= 52):
						return u'>50K'
					if (data['age'] <= 52):
					    if (not 'occupation' in data or data['occupation'] is None):
						return u'<=50K'
					    if (data['occupation'] == 'Other-service'):
						return u'<=50K'
					    if (data['occupation'] != 'Other-service'):
						if (data['age'] > 35):
						    if (data['workclass'] == 'State-gov'):
							return u'>50K'
						    if (data['workclass'] != 'State-gov'):
							if (data['age'] > 41):
							    if (not 'final_weight' in data or data['final_weight'] is None):
								return u'<=50K'
							    if (data['final_weight'] > 147347):
								return u'<=50K'
							    if (data['final_weight'] <= 147347):
								return u'<=50K'
							if (data['age'] <= 41):
							    if (data['marital_status'] == 'Separated'):
								return u'>50K'
							    if (data['marital_status'] != 'Separated'):
								return u'<=50K'
						if (data['age'] <= 35):
						    if (data['hours_per_week'] > 51):
							return u'<=50K'
						    if (data['hours_per_week'] <= 51):
							if (data['education_num'] > 11):
							    return u'<=50K'
							if (data['education_num'] <= 11):
							    if (data['occupation'] == 'Protective-serv'):
								return u'>50K'
							    if (data['occupation'] != 'Protective-serv'):
								return u'<=50K'
			    if (data['relationship'] != 'Not-in-family'):
				if (data['age'] > 39):
				    if (data['age'] > 45):
					if (not 'education' in data or data['education'] is None):
					    return u'<=50K'
					if (data['education'] == 'Some-college'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 162003):
						if (data['final_weight'] > 182557):
						    if (not 'sex' in data or data['sex'] is None):
							return u'<=50K'
						    if (data['sex'] == 'Male'):
							if (data['final_weight'] > 294443):
							    return u'<=50K'
							if (data['final_weight'] <= 294443):
							    return u'>50K'
						    if (data['sex'] != 'Male'):
							return u'<=50K'
						if (data['final_weight'] <= 182557):
						    return u'>50K'
					    if (data['final_weight'] <= 162003):
						return u'<=50K'
					if (data['education'] != 'Some-college'):
					    return u'<=50K'
				    if (data['age'] <= 45):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 63827):
					    if (not 'occupation' in data or data['occupation'] is None):
						return u'<=50K'
					    if (data['occupation'] == 'Adm-clerical'):
						if (data['final_weight'] > 187713):
						    if (data['hours_per_week'] > 44):
							return u'<=50K'
						    if (data['hours_per_week'] <= 44):
							return u'>50K'
						if (data['final_weight'] <= 187713):
						    if (data['marital_status'] == 'Separated'):
							return u'<=50K'
						    if (data['marital_status'] != 'Separated'):
							return u'>50K'
					    if (data['occupation'] != 'Adm-clerical'):
						if (data['relationship'] == 'Wife'):
						    return u'>50K'
						if (data['relationship'] != 'Wife'):
						    if (data['marital_status'] == 'Married-spouse-absent'):
							return u'>50K'
						    if (data['marital_status'] != 'Married-spouse-absent'):
							if (not 'sex' in data or data['sex'] is None):
							    return u'<=50K'
							if (data['sex'] == 'Male'):
							    if (data['occupation'] == 'Exec-managerial'):
								return u'>50K'
							    if (data['occupation'] != 'Exec-managerial'):
								return u'<=50K'
							if (data['sex'] != 'Male'):
							    return u'<=50K'
					if (data['final_weight'] <= 63827):
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
					if (data['education'] == '11th'):
					    return u'>50K'
					if (data['education'] != '11th'):
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
					if (data['age'] > 36):
					    return u'>50K'
					if (data['age'] <= 36):
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
					if (not 'education' in data or data['education'] is None):
					    return u'<=50K'
					if (data['education'] == 'HS-grad'):
					    return u'<=50K'
					if (data['education'] != 'HS-grad'):
					    return u'>50K'
				    if (data['marital_status'] != 'Married-spouse-absent'):
					if (not 'sex' in data or data['sex'] is None):
					    return u'<=50K'
					if (data['sex'] == 'Male'):
					    if (data['marital_status'] == 'Never-married'):
						return u'<=50K'
					    if (data['marital_status'] != 'Never-married'):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 126659):
						    if (not 'race' in data or data['race'] is None):
							return u'<=50K'
						    if (data['race'] == 'White'):
							if (data['education_num'] > 8):
							    if (data['age'] > 40):
								return u'<=50K'
							    if (data['age'] <= 40):
								return u'>50K'
							if (data['education_num'] <= 8):
							    return u'>50K'
						    if (data['race'] != 'White'):
							return u'<=50K'
						if (data['final_weight'] <= 126659):
						    return u'<=50K'
					if (data['sex'] != 'Male'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 61433):
						if (data['hours_per_week'] > 18):
						    return u'<=50K'
						if (data['hours_per_week'] <= 18):
						    if (data['hours_per_week'] > 15):
							if (data['marital_status'] == 'Widowed'):
							    return u'>50K'
							if (data['marital_status'] != 'Widowed'):
							    return u'<=50K'
						    if (data['hours_per_week'] <= 15):
							return u'<=50K'
					    if (data['final_weight'] <= 61433):
						if (data['final_weight'] > 20997):
						    if (data['final_weight'] > 48143):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'White'):
							    return u'>50K'
							if (data['race'] != 'White'):
							    return u'<=50K'
						    if (data['final_weight'] <= 48143):
							return u'<=50K'
						if (data['final_weight'] <= 20997):
						    return u'>50K'
				if (data['occupation'] != 'Adm-clerical'):
				    if (not 'workclass' in data or data['workclass'] is None):
					return u'<=50K'
				    if (data['workclass'] == 'Self-emp-inc'):
					if (data['marital_status'] == 'Widowed'):
					    if (data['education_num'] > 8):
						return u'>50K'
					    if (data['education_num'] <= 8):
						return u'<=50K'
					if (data['marital_status'] != 'Widowed'):
					    if (not 'final_weight' in data or data['final_weight'] is None):
						return u'<=50K'
					    if (data['final_weight'] > 101318):
						return u'<=50K'
					    if (data['final_weight'] <= 101318):
						return u'>50K'
				    if (data['workclass'] != 'Self-emp-inc'):
					if (data['occupation'] == 'Protective-serv'):
					    if (data['age'] > 47):
						return u'<=50K'
					    if (data['age'] <= 47):
						if (data['education_num'] > 10):
						    return u'<=50K'
						if (data['education_num'] <= 10):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'>50K'
						    if (data['final_weight'] > 305044):
							return u'>50K'
						    if (data['final_weight'] <= 305044):
							if (data['marital_status'] == 'Never-married'):
							    if (data['final_weight'] > 132195):
								return u'>50K'
							    if (data['final_weight'] <= 132195):
								return u'<=50K'
							if (data['marital_status'] != 'Never-married'):
							    return u'<=50K'
					if (data['occupation'] != 'Protective-serv'):
					    if (data['occupation'] == 'Transport-moving'):
						if (not 'education' in data or data['education'] is None):
						    return u'<=50K'
						if (data['education'] == 'Some-college'):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 157875):
							return u'<=50K'
						    if (data['final_weight'] <= 157875):
							if (data['hours_per_week'] > 29):
							    return u'>50K'
							if (data['hours_per_week'] <= 29):
							    return u'<=50K'
						if (data['education'] != 'Some-college'):
						    return u'<=50K'
					    if (data['occupation'] != 'Transport-moving'):
						if (data['occupation'] == 'Sales'):
						    if (data['marital_status'] == 'Widowed'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 171202):
							    return u'<=50K'
							if (data['final_weight'] <= 171202):
							    if (data['hours_per_week'] > 32):
								return u'>50K'
							    if (data['hours_per_week'] <= 32):
								return u'<=50K'
						    if (data['marital_status'] != 'Widowed'):
							return u'<=50K'
						if (data['occupation'] != 'Sales'):
						    if (data['education_num'] > 3):
							if (not 'race' in data or data['race'] is None):
							    return u'<=50K'
							if (data['race'] == 'Other'):
							    return u'>50K'
							if (data['race'] != 'Other'):
							    if (data['occupation'] == 'Handlers-cleaners'):
								return u'<=50K'
							    if (data['occupation'] != 'Handlers-cleaners'):
								return u'<=50K'
						    if (data['education_num'] <= 3):
							return u'<=50K'
			    if (data['relationship'] != 'Not-in-family'):
				if (data['occupation'] == 'Prof-specialty'):
				    if (not 'workclass' in data or data['workclass'] is None):
					return u'<=50K'
				    if (data['workclass'] == 'Federal-gov'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 94417):
					    return u'>50K'
					if (data['final_weight'] <= 94417):
					    return u'<=50K'
				    if (data['workclass'] != 'Federal-gov'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 338432):
					    return u'>50K'
					if (data['final_weight'] <= 338432):
					    if (data['final_weight'] > 175915):
						return u'<=50K'
					    if (data['final_weight'] <= 175915):
						if (data['final_weight'] > 175017):
						    return u'>50K'
						if (data['final_weight'] <= 175017):
						    if (data['age'] > 46):
							if (not 'education' in data or data['education'] is None):
							    return u'<=50K'
							if (data['education'] == 'Some-college'):
							    return u'<=50K'
							if (data['education'] != 'Some-college'):
							    if (data['hours_per_week'] > 35):
								return u'<=50K'
							    if (data['hours_per_week'] <= 35):
								return u'<=50K'
						    if (data['age'] <= 46):
							return u'<=50K'
				if (data['occupation'] != 'Prof-specialty'):
				    if (data['relationship'] == 'Wife'):
					if (data['education_num'] > 11):
					    return u'<=50K'
					if (data['education_num'] <= 11):
					    return u'>50K'
				    if (data['relationship'] != 'Wife'):
					if (data['marital_status'] == 'Separated'):
					    return u'<=50K'
					if (data['marital_status'] != 'Separated'):
					    if (not 'education' in data or data['education'] is None):
						return u'<=50K'
					    if (data['education'] == 'Assoc-voc'):
						if (not 'workclass' in data or data['workclass'] is None):
						    return u'<=50K'
						if (data['workclass'] == 'Federal-gov'):
						    if (data['relationship'] == 'Own-child'):
							return u'<=50K'
						    if (data['relationship'] != 'Own-child'):
							return u'>50K'
						if (data['workclass'] != 'Federal-gov'):
						    if (data['relationship'] == 'Own-child'):
							if (data['occupation'] == 'Adm-clerical'):
							    if (not 'final_weight' in data or data['final_weight'] is None):
								return u'<=50K'
							    if (data['final_weight'] > 178700):
								return u'<=50K'
							    if (data['final_weight'] <= 178700):
								return u'>50K'
							if (data['occupation'] != 'Adm-clerical'):
							    return u'<=50K'
						    if (data['relationship'] != 'Own-child'):
							return u'<=50K'
					    if (data['education'] != 'Assoc-voc'):
						if (data['occupation'] == 'Adm-clerical'):
						    if (not 'final_weight' in data or data['final_weight'] is None):
							return u'<=50K'
						    if (data['final_weight'] > 157742):
							return u'<=50K'
						    if (data['final_weight'] <= 157742):
							if (data['final_weight'] > 119355):
							    if (data['age'] > 43):
								return u'<=50K'
							    if (data['age'] <= 43):
								return u'<=50K'
							if (data['final_weight'] <= 119355):
							    return u'<=50K'
						if (data['occupation'] != 'Adm-clerical'):
						    if (data['age'] > 45):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 322450):
							    if (data['marital_status'] == 'Never-married'):
								return u'>50K'
							    if (data['marital_status'] != 'Never-married'):
								return u'<=50K'
							if (data['final_weight'] <= 322450):
							    if (data['age'] > 48):
								return u'<=50K'
							    if (data['age'] <= 48):
								return u'<=50K'
						    if (data['age'] <= 45):
							if (data['hours_per_week'] > 39):
							    if (data['marital_status'] == 'Married-spouse-absent'):
								return u'<=50K'
							    if (data['marital_status'] != 'Married-spouse-absent'):
								return u'<=50K'
							if (data['hours_per_week'] <= 39):
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
					if (data['hours_per_week'] > 62):
					    return u'>50K'
					if (data['hours_per_week'] <= 62):
					    return u'<=50K'
				    if (data['marital_status'] != 'Never-married'):
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'>50K'
					if (data['final_weight'] > 111019):
					    return u'>50K'
					if (data['final_weight'] <= 111019):
					    return u'<=50K'
				if (data['occupation'] != 'Exec-managerial'):
				    if (not 'education' in data or data['education'] is None):
					return u'<=50K'
				    if (data['education'] == '9th'):
					if (data['hours_per_week'] > 44):
					    return u'<=50K'
					if (data['hours_per_week'] <= 44):
					    return u'>50K'
				    if (data['education'] != '9th'):
					if (data['occupation'] == 'Transport-moving'):
					    if (data['hours_per_week'] > 51):
						return u'<=50K'
					    if (data['hours_per_week'] <= 51):
						if (not 'final_weight' in data or data['final_weight'] is None):
						    return u'<=50K'
						if (data['final_weight'] > 81673):
						    if (data['hours_per_week'] > 49):
							if (data['marital_status'] == 'Never-married'):
							    return u'>50K'
							if (data['marital_status'] != 'Never-married'):
							    return u'<=50K'
						    if (data['hours_per_week'] <= 49):
							return u'<=50K'
						if (data['final_weight'] <= 81673):
						    return u'>50K'
					if (data['occupation'] != 'Transport-moving'):
					    if (not 'race' in data or data['race'] is None):
						return u'<=50K'
					    if (data['race'] == 'Asian-Pac-Islander'):
						if (not 'sex' in data or data['sex'] is None):
						    return u'<=50K'
						if (data['sex'] == 'Male'):
						    return u'>50K'
						if (data['sex'] != 'Male'):
						    return u'<=50K'
					    if (data['race'] != 'Asian-Pac-Islander'):
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
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 378259):
					    return u'>50K'
					if (data['final_weight'] <= 378259):
					    if (not 'race' in data or data['race'] is None):
						return u'<=50K'
					    if (data['race'] == 'Asian-Pac-Islander'):
						return u'>50K'
					    if (data['race'] != 'Asian-Pac-Islander'):
						if (data['final_weight'] > 174056):
						    if (data['age'] > 28):
							if (data['hours_per_week'] > 58):
							    if (not 'relationship' in data or data['relationship'] is None):
								return u'<=50K'
							    if (data['relationship'] == 'Own-child'):
								return u'>50K'
							    if (data['relationship'] != 'Own-child'):
								return u'<=50K'
							if (data['hours_per_week'] <= 58):
							    return u'>50K'
						    if (data['age'] <= 28):
							if (data['race'] == 'White'):
							    return u'<=50K'
							if (data['race'] != 'White'):
							    return u'>50K'
						if (data['final_weight'] <= 174056):
						    return u'<=50K'
				if (data['hours_per_week'] <= 49):
				    if (data['education_num'] > 8):
					return u'<=50K'
				    if (data['education_num'] <= 8):
					if (not 'race' in data or data['race'] is None):
					    return u'<=50K'
					if (data['race'] == 'White'):
					    return u'>50K'
					if (data['race'] != 'White'):
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
					if (not 'final_weight' in data or data['final_weight'] is None):
					    return u'<=50K'
					if (data['final_weight'] > 199791):
					    return u'<=50K'
					if (data['final_weight'] <= 199791):
					    if (data['relationship'] == 'Own-child'):
						return u'>50K'
					    if (data['relationship'] != 'Own-child'):
						if (data['final_weight'] > 95966):
						    return u'<=50K'
						if (data['final_weight'] <= 95966):
						    if (data['final_weight'] > 85301):
							return u'>50K'
						    if (data['final_weight'] <= 85301):
							return u'<=50K'
				    if (data['occupation'] != 'Protective-serv'):
					if (data['relationship'] == 'Own-child'):
					    if (data['age'] > 29):
						if (data['occupation'] == 'Craft-repair'):
						    if (data['education_num'] > 11):
							return u'<=50K'
						    if (data['education_num'] <= 11):
							return u'>50K'
						if (data['occupation'] != 'Craft-repair'):
						    return u'<=50K'
					    if (data['age'] <= 29):
						return u'<=50K'
					if (data['relationship'] != 'Own-child'):
					    if (data['age'] > 30):
						return u'<=50K'
					    if (data['age'] <= 30):
						if (data['education_num'] > 10):
						    if (data['relationship'] == 'Not-in-family'):
							if (not 'final_weight' in data or data['final_weight'] is None):
							    return u'<=50K'
							if (data['final_weight'] > 25105):
							    if (data['occupation'] == 'Sales'):
								return u'<=50K'
							    if (data['occupation'] != 'Sales'):
								return u'<=50K'
							if (data['final_weight'] <= 25105):
							    if (data['hours_per_week'] > 35):
								return u'<=50K'
							    if (data['hours_per_week'] <= 35):
								return u'>50K'
						    if (data['relationship'] != 'Not-in-family'):
							return u'<=50K'
						if (data['education_num'] <= 10):
						    if (data['age'] > 27):
							if (data['occupation'] == 'Adm-clerical'):
							    return u'<=50K'
							if (data['occupation'] != 'Adm-clerical'):
							    if (not 'workclass' in data or data['workclass'] is None):
								return u'<=50K'
							    if (data['workclass'] == 'Federal-gov'):
								return u'>50K'
							    if (data['workclass'] != 'Federal-gov'):
								return u'<=50K'
						    if (data['age'] <= 27):
							if (data['marital_status'] == 'Separated'):
							    if (data['occupation'] == 'Other-service'):
								return u'<=50K'
							    if (data['occupation'] != 'Other-service'):
								return u'<=50K'
							if (data['marital_status'] != 'Separated'):
							    return u'<=50K'
			    if (data['hours_per_week'] <= 29):
				return u'<=50K'
			if (data['education_num'] <= 9):
			    if (data['age'] > 27):
				if (not 'final_weight' in data or data['final_weight'] is None):
				    return u'<=50K'
				if (data['final_weight'] > 94030):
				    if (data['final_weight'] > 334106):
					if (not 'occupation' in data or data['occupation'] is None):
					    return u'<=50K'
					if (data['occupation'] == 'Craft-repair'):
					    if (data['marital_status'] == 'Never-married'):
						if (not 'relationship' in data or data['relationship'] is None):
						    return u'<=50K'
						if (data['relationship'] == 'Not-in-family'):
						    return u'<=50K'
						if (data['relationship'] != 'Not-in-family'):
						    return u'>50K'
					    if (data['marital_status'] != 'Never-married'):
						return u'<=50K'
					if (data['occupation'] != 'Craft-repair'):
					    return u'<=50K'
				    if (data['final_weight'] <= 334106):
					return u'<=50K'
				if (data['final_weight'] <= 94030):
				    if (data['marital_status'] == 'Divorced'):
					if (not 'race' in data or data['race'] is None):
					    return u'<=50K'
					if (data['race'] == 'Amer-Indian-Eskimo'):
					    return u'>50K'
					if (data['race'] != 'Amer-Indian-Eskimo'):
					    if (not 'occupation' in data or data['occupation'] is None):
						return u'<=50K'
					    if (data['occupation'] == 'Other-service'):
						return u'>50K'
					    if (data['occupation'] != 'Other-service'):
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