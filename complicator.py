# list of variables that need to be taken into account
complicators = ["age", "gender", "status", "ignorance", "money", "popularity_online", "rl_friends"]


def money_score(money):
	if money == 0:
		return 2
	elif money > 0:
		return 0
	elif money < 0 and money >= -1000:
		return 5
	else:
		return 10


def age_calc(age):
	if age <= 10:
		return 2
	elif age >= 11 and age <= 20:
		return 8
	elif age >= 21 and age <= 30:
		return 4
	elif age >= 31 and age <= 50:
		return 10
	elif age >= 51:
		return 0
	else:
		return 0

def klout_calc(score):
	if score >= 1 and score <= 40:
		return 1
	elif score > 40 and score <= 50:
		return 4
	elif score > 50 and score <= 60:
		return 6
	elif score > 60 and score <= 80:
		return 8
	elif score > 80 and score <= 100:
		return 10
	else:
		return 0

def overall_score(age, gender, status, ignorance, money, popularity_online, rl_friends):
	my_score = age_calc(age) + gender + status - ignorance + money_score(money) + klout_calc(popularity_online) + rl_friends
	max_score = 10 * 6
	result = int((my_score / float(max_score)) * 100)
	if result < 0:
		return 0
	return result

def check_level(complexity):
	if complexity <= 25:
		return "low"
	elif complexity > 20 and complexity <= 50:
		return "medium"
	elif complexity > 50 and complexity <= 75:
		return "high"
	else:
		return "extreme"
