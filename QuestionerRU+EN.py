# Спрашивальник 2.6, Questioner 2.6
from colorama import init, Fore, Back, Style

# To initaliaze colorama on windows
init()

print("Enter a language")
print("Rus = Русский, Eng = English")
lang = input("Enter a language: ")

def eng():
	# This is english version:
	print("Welcome to english version")
	input()

	en_age = input("Enter your age: ")
	if int(en_age) < 10:
		print("You are too small for that!")
		exit()
	if int(en_age) >= 10:
		print("We continue!")
	else:
		print("What you said?")
		input("Click on enter to exit from app")
		exit()

	en_name = input("Enter your name: ")
	if en_name == "Donald Trump":
		print("Kill fake president!")
		input()
		exit()

def rus():
	# Это Русская версия:
	print("Допро пожаловать в Русскую версию!")
	input()

	ru_age = input("Введите ваш возраст: ")
	if int(ru_age) < 10:
		print("Вам слишком мало!")
		input("Нажмите клавишу Enter чтобы выйти из приложения")
		exit()
	if int(ru_age) >= 10:
		print("Продолжаем!")

	ru_name = input("Введите ваше имя: ")
	if ru_name == "Мафиозник":
		print("Мафиозников не пускаем!")
		input()
		exit()
	if ru_name == "Путин":
		print("Президентов мы не пускаем!")

if lang == "Rus":
	rus()
if lang == "Eng":
	eng()
if lang == "rus":
	rus()
if lang == "eng":
	eng()
else:
	print("What?!")
	exit()