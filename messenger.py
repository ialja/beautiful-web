from random import choice

m_20 = ["You have it easy, you're lucky.",
		"Can I have your life?",
		"You want to hear my problems, huh?",
		"I'm jealous, but happy for you.",
		"You've got nothing to complain about."]
m_40 = ["That's not so bad, you know?",
		"Life is pretty good for you.",
		"Don't have much to complain about.",
		"There are people who have it way worse.",
		"That's a decent score, don't worry."]
m_60 = ["Could be better, could be worse.",
		"You're right in the middle, that's gotta be worth something.",
		"Take it easy and relax.",
		"About average. Nothing wrong with that in this case.",
		"There are good and bad days. Hope you're having a good one."]
m_80 = ["Well, it could still be worse.",
		"You want to share your problems with me?",
		"It's pretty complicated, but not unmanageable.",
		"It only gets better, you know?",
		"Some days it's even worse for me. Keep on smiling."]
m_100 = ["Ugh, I don't want to be in your shoes.",
		"What can I tell you? Good luck?",
		"Just keep swimming, can't get much worse.",
		"You want a hug or two?",
		"I hope you know how to make lemonade."]

def interpret_score(score):
	if score >=0 and score <= 20:
		return choice(m_20)
	elif score > 20 and score <= 40:
		return choice(m_40)
	elif score > 40 and score <= 60:
		return choice(m_60)
	elif score > 60 and score <= 80:
		return choice(m_80)
	elif score > 80 and score <= 100:
		return choice(m_100)
	else:
		return "Can't say for sure."

def check_level(complexity):
	if complexity <= 25:
		return "low"
	elif complexity > 20 and complexity <= 50:
		return "medium"
	elif complexity > 50 and complexity <= 75:
		return "high"
	else:
		return "extreme"
