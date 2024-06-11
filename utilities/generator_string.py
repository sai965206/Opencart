import random

alph = "abcdefghijklmnopqrstuvwxy"
numeric = "0123456789"
length = 5
def random_String():
	return ''.join(random.choice(alph+numeric) for i in range(length))
