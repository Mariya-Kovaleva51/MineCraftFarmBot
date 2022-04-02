#------------------------- Основной код бота -------------------------------------------
import names
import time as t
import pyautogui as pag
import random
from colorama import init, Fore
import sqlite3
from nickname_generator import generate
import webbrowser
init()

class DBots():
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def check(self, nick):
        with self.connection:
            res = self.cursor.execute("SELECT `nick` FROM `bots` WHERE `nick` = ?", (nick, )).fetchall()
            return bool(len(res))

    def reg(self, nick):
        with self.connection:
            estnick = self.cursor.execute("SELECT `nick` FROM `bots` WHERE `nick` = ?", (nick, )).fetchall()
            res = bool(len(estnick))
            if res == False:
                self.cursor.execute("INSERT INTO `bots` (`nick`) VALUES(?)", (nick, ))
            else:
                pass




db = DBots('date.db')



print(f"""

██╗░░░██╗░█████╗░███╗░░░███╗██████╗░██╗░██████╗░█████╗░██████╗░░█████╗░██╗░░░░░██╗░░░░░███████╗██████╗░
╚██╗░██╔╝██╔══██╗████╗░████║██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░░░░██║░░░░░██╔════╝██╔══██╗
░╚████╔╝░███████║██╔████╔██║██████╔╝██║╚█████╗░██║░░╚═╝██████╔╝██║░░██║██║░░░░░██║░░░░░█████╗░░██████╔╝
░░╚██╔╝░░██╔══██║██║╚██╔╝██║██╔═══╝░██║░╚═══██╗██║░░██╗██╔══██╗██║░░██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗
░░░██║░░░██║░░██║██║░╚═╝░██║██║░░░░░██║██████╔╝╚█████╔╝██║░░██║╚█████╔╝███████╗███████╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝{Fore.RED} <----scripts---->{Fore.WHITE}
"""
)

print(
	f"""{Fore.LIGHTMAGENTA_EX}
░░░░░░░░░░░░░██████╗░██████╗░███████╗░░░░░░███████╗██████╗░██╗████████╗██╗░█████╗░███╗░░██╗░░░░░░░░░░░░
░░░░░░░░░░░░██╔════╝░╚════██╗██╔════╝░░░░░░██╔════╝██╔══██╗██║╚══██╔══╝██║██╔══██╗████╗░██║░░░░░░░░░░░░
█████╗█████╗██║░░██╗░░░███╔═╝██████╗░█████╗█████╗░░██║░░██║██║░░░██║░░░██║██║░░██║██╔██╗██║█████╗█████╗
╚════╝╚════╝██║░░╚██╗██╔══╝░░╚════██╗╚════╝██╔══╝░░██║░░██║██║░░░██║░░░██║██║░░██║██║╚████║╚════╝╚════╝
░░░░░░░░░░░░╚██████╔╝███████╗██████╔╝░░░░░░███████╗██████╔╝██║░░░██║░░░██║╚█████╔╝██║░╚███║░░░░░░░░░░░░
░░░░░░░░░░░░░╚═════╝░╚══════╝╚═════╝░░░░░░░╚══════╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝░░░░░░░░░░░░ 
{Fore.WHITE}"""
)

print(Fore.GREEN + 'Связь с нами - https://vk.com/yampiscripts' + Fore.WHITE)

webbrowser.open_new_tab('https://vk.com/yampiscripts')
t.sleep(5)

input('Нажми что-нибудь для продолжения...')


nickname = input('Введи ник накрутки: ')


print(Fore.RED + """!Инфо 
Доступны грифы от 1 до 14. Вводите только целым числом, иначе скрипт КРАШНЕТСЯ!""" + Fore.WHITE)
server = int(input('Веди номер грифа: '))

print(Fore.GREEN)
print("""!Инфо
У вас есть 10 секунд перед началом скрипта. Откройте майнкрафт в главном меню и оконном виде""")


print(Fore.WHITE)
def get_nick():
	fname = names.get_first_name()
	lname = names.get_last_name()
	full_nick = fname + lname + str(random.randint(0, 98))
	one_name = fname + str(random.randint(0, 90))
	one_lname = lname + str(random.randint(0, 90))
	nick = generate()
	variants = [full_nick, nick, one_name, one_lname]
	bot_nick = random.choice(variants)
	return bot_nick




def lclick(x, y):
	pag.moveTo(x, y)
	t.sleep(0.5)
	pag.leftClick(x, y)
	t.sleep(1)

def write(text):
	pag.typewrite(text)
	t.sleep(1)


def press(key):
	pag.press(key)
	t.sleep(1)

# Основные позиции -------------------------------------------
# Главное Меню: 959, 323
# In Game Account Switcher: 1185, 485
# Изменить Аккаунт: 954, 947
# Ввод почты: 933, 160
# Изменит Аккаунт Оффлайн: 806, 997
# Войти Оффлайн: 735, 996
# Сетевая игра: 947, 436
# Войти на RW: 700, 123
# Гриферское Выживание: 962 ,445
# Гриф-6: 1029, 388
# Кнопка Отключиться: 957, 502

#Корды грифов --------------------------------
# 5: 995, 390
# 4: 959, 390
# 3: 927, 390
# 2: 888, 390
# 1: 848, 390
# 7: 1068, 390
# 8: 852, 426
# 9: 887, 426
# 10: 924, 426
# 11: 959, 426
# 12: 995, 426
# 13: 1031, 426
# 14: 1068, 426
# 6: 1029, 388




t.sleep(10)

while True:
	print('новый круг бота ----------------------------------')
	t.sleep(1)
	lclick(959, 323)
	lclick(1185, 485)
	lclick(954, 947)
	lclick(933, 160)
	n = get_nick()
	pag.typewrite(n)
	t.sleep(1)
	print('1. Бот сменил ник')
	lclick(806, 997)
	lclick(735, 996)
	press('esc')
	lclick(947, 436)
	lclick(700, 123)
	t.sleep(10)
	press('/')
	if db.check(n) == True:
		write('login FarmBotForG25')
		print(f'2. Логин под ником {n}')
	elif db.check(n) == False:
		write('reg FarmBotForG25 FarmBotForG25')
		db.reg(n)
		print(f'2. Регистрация под ником {n}')

	press('enter')
	t.sleep(5)
	pag.rightClick()
	t.sleep(1)
	lclick(962 ,445)
	
	#---------------
	if server == 1:
		lclick(848, 390)
	elif server == 2:
		lclick(888, 390)
	elif server == 3:
		lclick(927, 390)
	elif server == 4:
		lclick(959, 390)
	elif server == 5:
		lclick(995, 390)
	elif server == 6:
		lclick(1029, 388)
	elif server == 7:
		lclick(1068, 390)
	elif server == 8:
		lclick(852, 426)
	elif server == 9:
		lclick(887, 426)
	elif server == 10:
		lclick(924, 426)
	elif server == 11:
		lclick(959, 426)
	elif server == 12:
		lclick(995, 426)
	elif server == 13:
		lclick(1031, 426)
	elif server == 14:
		lclick(1068, 426)
		
	print('3. Бот выбрал гриф')
	
	#---------------
	t.sleep(4)
	press('/')
	write(f'pay {nickname} 2000')
	press('enter')
	print('4. Бот отправил валюту')
	press('esc')
	lclick(957, 502)
	press('esc')
	lclick(1140, 584)
	press('esc')