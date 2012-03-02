import sqlite3

connection = sqlite3.connect('cochdata.sqlite')
cursor = connection.cursor()

import glob
import athletemodel
data_giles = glob.glob("../data/*.txt")

for each_ath in athletes:
	name = athletes[each_ath].name
	dob = athletes[each_ath].dob
	cursor.execute("INSERT INTO athletes (name, dob) VALUES (?,?)", (name, dob))
	connection.commit()

connection.close()
