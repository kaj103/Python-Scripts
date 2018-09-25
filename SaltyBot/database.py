import sqlite3

conn = sqlite3.connect('saltydb.db') #Connect to db
c = conn.cursor() #Cursor to execute SQL queries

class database(object):

	def create_table(self):
		c.execute("CREATE TABLE IF NOT EXISTS SaltyTable(fighter1 TEXT, fighter2 TEXT, winner TEXT, cashWon INTEGER)")

	def insertFight(self, fighters1, fighters2):
		c.execute("INSERT INTO SaltyTable(fighter1, fighter2) VALUES (?,?)",
					(fighters1,fighters2))
		conn.commit()