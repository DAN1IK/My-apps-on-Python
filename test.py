# Test application for github
age = input("Enter your age: ")

if int(age) < 16:
	print("Exiting!")
	input()
	exit()
if int(age) >= 16:
	print("Hello, world!")