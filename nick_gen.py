import names
from nickname_generator import generate
import random






def get_nick():
	symbols = ['', '_', '__', '___']
	fname = names.get_first_name()
	lname = names.get_last_name()
	full_nick = fname + random.choice(symbols) + lname + str(random.randint(0, 98))
	nick = generate()
	variants = [full_nick, nick]
	bot_nick = random.choice(variants)
	return bot_nick


