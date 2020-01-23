import sqlite3
import sys
import random

def generator(cursor, name, configuration): #first initial last name configuration
	if name == "" or name == "\n":
		return None
	fullname = name.split(",")
	print(fullname)
	print(fullname[0]+" "+fullname[1][:-1])
	cursor.execute("SELECT cred_id FROM credentials WHERE first = ? AND last = ?", (fullname[0], fullname[1][:-1]))
	data = cursor.fetchone()
	count = 0
	print(data)
	if data == None:
		if configuration == "0":
			first = fullname[0]
			last = fullname[1]
			user = first[0][0]+last[:-1]
		elif configuration == "1":
			first = fullname[0]
			last = fullname[1]
			user = first+last[0][0]
		return user, first, last
	else:
		print("else")
		user = ""
		while data != None:
			if configuration == "0":
				first = fullname[0]
				last = fullname[1]
				user = first[0][0]+last[:-1]+str(count)

			elif configuration == "1":
				first = fullname[0]
				last = fullname[1]
				user = first+last[0][0]+str(count)
			count+=1
			cursor.execute("SELECT cred_id FROM credentials WHERE user = ?", (user,))
			data = cursor.fetchone()
		if user != "":
			return user, first, last
		return None


def generateUsers(cursor, filename, passwords, configuration):#input format should be name of input file followed by intger value for what type of credentials you want to generate e.g. "python3 generateCreds.py input.csv 0"
	'''
	Type 0: 
		- first initial followed by last name. e.g. Tommy Smith would get coonverted to tsmith
	Type 1:

	'''
	creds = []
	pwdfile = open(passwords, "r")
	passwds = pwdfile.readlines()
	with open(filename, "r") as file:
		name = "."
		while name:
			name = file.readline()
			pair = generator(cursor, name.lower(), configuration)
			if pair != None:
				passwd = random.choice(passwds)
				creds.append((pair, passwd[:-1]))
				print(pair[0] + " " + passwd[:-1])
				cursor.execute("INSERT INTO credentials(first, last, user,pass) VALUES(?,?,?,?);", (pair[1], pair[2], pair[0], passwd))
	pwdfile.close()

#MAIN
con = sqlite3.connect('hdx.db')
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS credentials (cred_id INTEGER PRIMARY KEY AUTOINCREMENT, first TEXT NOT NULL, last TEXT NOT NULL, user TEXT NOT NULL, pass TEXT NOT NULL, UNIQUE(cred_id, first, last, user, pass));")
allnames = sys.argv[1]
passwords = sys.argv[2]
configuration = sys.argv[3]
generateUsers(cursor, allnames, passwords, configuration)
con.commit()
con.close()