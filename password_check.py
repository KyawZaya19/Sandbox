MIN_LENGTH = 6
password = input("Type a passsword : ")
while len(password) < MIN_LENGTH:
	print("Your password is too short")
	password = input("Type a passsword : ")
for x in password:
	print("*",end="")