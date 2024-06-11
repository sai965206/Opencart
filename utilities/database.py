import mysql.connector

def user_crediental():
	try:
		con = mysql.connector.connect(host="localhost",port="3306",user="root",passwd="root",database="opncart")
		curs = con.cursor()
		for row in curs:
			return row[1]
		con.commit()
		con.close()
	except:
		print("Connection unsuccessful")
	print("Finished")
user_crediental()

def pwd_crediental():
	try:
		con = mysql.connector.connect(host="localhost",port="3306",user="root",passwd="root",database="opncart")
		curs = con.cursor()
		for row in curs:
			return row[2]
		con.commit()
		con.close()
	except:
		print("Connection unsuccessful")
	print("Finished")
pwd_crediental()