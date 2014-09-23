def predict_income(impala_function_context, age, workclass, final_weight, education, education_num, marital_status, occupation, relationship, race, sex, hours_per_week, native_country, income):
    """ Predictor for income from model/5360311dffa04466f60007dc

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
					return '>50K'
			    if (education_num <= 14):
				if (hours_per_week > 36):
				    if (workclass is None):
					return '>50K'
				    if (workclass == 'Self-emp-inc'):
					return '>50K'
				    if (workclass != 'Self-emp-inc'):
					return '>50K'
				if (hours_per_week <= 36):
				    return '<=50K'
			if (age <= 58):
			    if (age > 38):
				if (education_num > 14):
				    if (hours_per_week > 49):
					return '>50K'
				    if (hours_per_week <= 49):
					return '>50K'
				if (education_num <= 14):
				    if (workclass is None):
					return '>50K'
				    if (workclass == 'Self-emp-not-inc'):
					return '>50K'
				    if (workclass != 'Self-emp-not-inc'):
					return '>50K'
			    if (age <= 38):
				if (occupation is None):
				    return '>50K'
				if (occupation == 'Farming-fishing'):
				    return '<=50K'
				if (occupation != 'Farming-fishing'):
				    if (hours_per_week > 42):
					return '>50K'
				    if (hours_per_week <= 42):
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
					return '>50K'
				    if (age <= 48):
					return '<=50K'
				if (final_weight <= 90244):
				    return '<=50K'
			    if (workclass != 'Self-emp-not-inc'):
				if (hours_per_week > 67):
				    if (hours_per_week > 73):
					return '>50K'
				    if (hours_per_week <= 73):
					return '<=50K'
				if (hours_per_week <= 67):
				    if (race is None):
					return '>50K'
				    if (race == 'Other'):
					return '<=50K'
				    if (race != 'Other'):
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
					return '>50K'
				    if (final_weight <= 121061):
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
					return '<=50K'
				if (hours_per_week <= 46):
				    if (occupation == 'Adm-clerical'):
					return '<=50K'
				    if (occupation != 'Adm-clerical'):
					return '>50K'
			    if (hours_per_week <= 41):
				if (final_weight is None):
				    return '<=50K'
				if (final_weight > 159383):
				    if (final_weight > 260996):
					return '>50K'
				    if (final_weight <= 260996):
					return '<=50K'
				if (final_weight <= 159383):
				    if (final_weight > 100631):
					return '>50K'
				    if (final_weight <= 100631):
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
					return '<=50K'
				    if (race != 'White'):
					return '>50K'
				if (hours_per_week <= 13):
				    if (occupation is None):
					return '<=50K'
				    if (occupation == 'Exec-managerial'):
					return '>50K'
				    if (occupation != 'Exec-managerial'):
					return '<=50K'
			if (age <= 62):
			    if (hours_per_week > 12):
				if (workclass is None):
				    return '>50K'
				if (workclass == 'State-gov'):
				    return '<=50K'
				if (workclass != 'State-gov'):
				    if (hours_per_week > 21):
					return '<=50K'
				    if (hours_per_week <= 21):
					return '>50K'
			    if (hours_per_week <= 12):
				if (hours_per_week > 2):
				    if (education_num > 14):
					return '<=50K'
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
					return '<=50K'
				    if (occupation != 'Other-service'):
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
					return '<=50K'
			    if (occupation != 'Farming-fishing'):
				if (occupation == 'Other-service'):
				    if (age > 40):
					return '<=50K'
				    if (age <= 40):
					return '<=50K'
				if (occupation != 'Other-service'):
				    if (occupation == 'Exec-managerial'):
					return '>50K'
				    if (occupation != 'Exec-managerial'):
					return '>50K'
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
					return '<=50K'
				    if (final_weight <= 92214):
					return '>50K'
				if (workclass != 'Self-emp-not-inc'):
				    if (final_weight is None):
					return '>50K'
				    if (final_weight > 189527):
					return '>50K'
				    if (final_weight <= 189527):
					return '>50K'
			    if (occupation != 'Exec-managerial'):
				if (occupation == 'Other-service'):
				    if (sex is None):
					return '<=50K'
				    if (sex == 'Male'):
					return '<=50K'
				    if (sex != 'Male'):
					return '<=50K'
				if (occupation != 'Other-service'):
				    if (occupation == 'Farming-fishing'):
					return '<=50K'
				    if (occupation != 'Farming-fishing'):
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
					return '>50K'
				    if (education_num <= 9):
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
					return '<=50K'
				if (workclass != 'Self-emp-not-inc'):
				    if (age > 32):
					return '>50K'
				    if (age <= 32):
					return '<=50K'
			    if (age <= 27):
				if (final_weight is None):
				    return '<=50K'
				if (final_weight > 162313):
				    if (final_weight > 190463):
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
					return '<=50K'
				    if (age <= 31):
					return '<=50K'
				if (hours_per_week <= 46):
				    if (occupation == 'Prof-specialty'):
					return '<=50K'
				    if (occupation != 'Prof-specialty'):
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
					return '<=50K'
				    if (sex != 'Male'):
					return '<=50K'
				if (occupation != 'Adm-clerical'):
				    if (occupation == 'Handlers-cleaners'):
					return '<=50K'
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
					return '<=50K'
				    if (final_weight <= 89485):
					return '<=50K'
				if (occupation != 'Transport-moving'):
				    if (final_weight is None):
					return '<=50K'
				    if (final_weight > 162184):
					return '<=50K'
				    if (final_weight <= 162184):
					return '<=50K'
			    if (age <= 53):
				if (occupation is None):
				    return '<=50K'
				if (occupation == 'Sales'):
				    if (hours_per_week > 52):
					return '<=50K'
				    if (hours_per_week <= 52):
					return '>50K'
				if (occupation != 'Sales'):
				    if (workclass is None):
					return '<=50K'
				    if (workclass == 'Local-gov'):
					return '<=50K'
				    if (workclass != 'Local-gov'):
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
					return '>50K'
				if (occupation != 'Exec-managerial'):
				    if (occupation == 'Sales'):
					return '<=50K'
				    if (occupation != 'Sales'):
					return '<=50K'
			    if (workclass != 'Private'):
				if (hours_per_week > 55):
				    if (workclass == 'Self-emp-not-inc'):
					return '>50K'
				    if (workclass != 'Self-emp-not-inc'):
					return '<=50K'
				if (hours_per_week <= 55):
				    if (workclass == 'Self-emp-inc'):
					return '>50K'
				    if (workclass != 'Self-emp-inc'):
					return '<=50K'
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
					return '<=50K'
				    if (final_weight <= 219946):
					return '<=50K'
				if (occupation != 'Adm-clerical'):
				    if (final_weight is None):
					return '<=50K'
				    if (final_weight > 145325):
					return '<=50K'
				    if (final_weight <= 145325):
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
					return '>50K'
				    if (education_num <= 13):
					return '<=50K'
				if (hours_per_week <= 58):
				    if (race is None):
					return '>50K'
				    if (race == 'Amer-Indian-Eskimo'):
					return '<=50K'
				    if (race != 'Amer-Indian-Eskimo'):
					return '>50K'
			    if (final_weight <= 160393):
				if (hours_per_week > 47):
				    if (final_weight > 51818):
					return '>50K'
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
					return '>50K'
		    if (occupation != 'Exec-managerial'):
			if (education_num > 14):
			    if (age > 32):
				if (age > 52):
				    if (marital_status == 'Widowed'):
					return '>50K'
				    if (marital_status != 'Widowed'):
					return '<=50K'
				if (age <= 52):
				    if (hours_per_week > 52):
					return '>50K'
				    if (hours_per_week <= 52):
					return '>50K'
			    if (age <= 32):
				if (age > 29):
				    return '<=50K'
				if (age <= 29):
				    if (marital_status == 'Never-married'):
					return '<=50K'
				    if (marital_status != 'Never-married'):
					return '>50K'
			if (education_num <= 14):
			    if (sex is None):
				return '<=50K'
			    if (sex == 'Male'):
				if (hours_per_week > 55):
				    if (occupation == 'Sales'):
					return '<=50K'
				    if (occupation != 'Sales'):
					return '<=50K'
				if (hours_per_week <= 55):
				    if (workclass is None):
					return '<=50K'
				    if (workclass == 'State-gov'):
					return '<=50K'
				    if (workclass != 'State-gov'):
					return '<=50K'
			    if (sex != 'Male'):
				if (final_weight is None):
				    return '<=50K'
				if (final_weight > 151124):
				    if (final_weight > 158605):
					return '<=50K'
				    if (final_weight <= 158605):
					return '>50K'
				if (final_weight <= 151124):
				    if (workclass is None):
					return '<=50K'
				    if (workclass == 'Federal-gov'):
					return '>50K'
				    if (workclass != 'Federal-gov'):
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
					return '>50K'
				if (marital_status != 'Never-married'):
				    if (final_weight is None):
					return '<=50K'
				    if (final_weight > 170081):
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
					return '<=50K'
				if (relationship != 'Not-in-family'):
				    if (age > 49):
					return '<=50K'
				    if (age <= 49):
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
					return '<=50K'
			if (age <= 45):
			    if (hours_per_week > 34):
				if (workclass is None):
				    return '<=50K'
				if (workclass == 'State-gov'):
				    return '<=50K'
				if (workclass != 'State-gov'):
				    if (workclass == 'Federal-gov'):
					return '<=50K'
				    if (workclass != 'Federal-gov'):
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
					return '<=50K'
			if (age <= 53):
			    if (relationship is None):
				return '<=50K'
			    if (relationship == 'Not-in-family'):
				if (education is None):
				    return '<=50K'
				if (education == 'HS-grad'):
				    if (hours_per_week > 47):
					return '<=50K'
				    if (hours_per_week <= 47):
					return '<=50K'
				if (education != 'HS-grad'):
				    if (workclass is None):
					return '<=50K'
				    if (workclass == 'Self-emp-not-inc'):
					return '<=50K'
				    if (workclass != 'Self-emp-not-inc'):
					return '<=50K'
			    if (relationship != 'Not-in-family'):
				if (age > 39):
				    if (age > 45):
					return '<=50K'
				    if (age <= 45):
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
					return '<=50K'
				    if (marital_status != 'Married-spouse-absent'):
					return '<=50K'
				if (occupation != 'Adm-clerical'):
				    if (workclass is None):
					return '<=50K'
				    if (workclass == 'Self-emp-inc'):
					return '<=50K'
				    if (workclass != 'Self-emp-inc'):
					return '<=50K'
			    if (relationship != 'Not-in-family'):
				if (occupation == 'Prof-specialty'):
				    if (workclass is None):
					return '<=50K'
				    if (workclass == 'Federal-gov'):
					return '<=50K'
				    if (workclass != 'Federal-gov'):
					return '<=50K'
				if (occupation != 'Prof-specialty'):
				    if (relationship == 'Wife'):
					return '<=50K'
				    if (relationship != 'Wife'):
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
					return '<=50K'
				    if (marital_status != 'Never-married'):
					return '>50K'
				if (occupation != 'Exec-managerial'):
				    if (education is None):
					return '<=50K'
				    if (education == '9th'):
					return '<=50K'
				    if (education != '9th'):
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
					return '<=50K'
				if (hours_per_week <= 49):
				    if (education_num > 8):
					return '<=50K'
				    if (education_num <= 8):
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
					return '<=50K'
				    if (occupation != 'Protective-serv'):
					return '<=50K'
			    if (hours_per_week <= 29):
				return '<=50K'
			if (education_num <= 9):
			    if (age > 27):
				if (final_weight is None):
				    return '<=50K'
				if (final_weight > 94030):
				    if (final_weight > 334106):
					return '<=50K'
				    if (final_weight <= 334106):
					return '<=50K'
				if (final_weight <= 94030):
				    if (marital_status == 'Divorced'):
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
