import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time
import requests
import random
from database import database

login_url = 'https://www.saltybet.com/authenticate?signin=1'

url = 'http://www.saltybet.com/'
#driver.get(url)

email = 'EMAIL'
password = 'PASS'


class SaltBot(object):
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.get(login_url)
		self.db = database()
		self.db.create_table()

	def login(self):
		#driver.get(login_url)
		login_email = self.driver.find_element_by_id('email')
		login_email.send_keys(email)
		login_password = self.driver.find_element_by_id('pword')
		login_password.send_keys(password)
		self.driver.find_element_by_class_name('graybutton').click()
		time.sleep(3)
		if "Invalid Email or Password" not in self.driver.page_source:
			print('Login Successful')
		else:
			print('Login Failed. Fix info')
			driver.close()

	def bet(self):
		redButton = self.driver.find_element_by_id('player1')
		blueButton = self.driver.find_element_by_id('player2')
		interval1 = self.driver.find_element_by_id('interval1')
		choices = ['1', '2']
		chosen = random.choice(choices)
		if chosen == '1':
			interval1.click()
			redButton.click()
		elif chosen == '2':
			interval1.click()
			blueButton.click()
		time.sleep(60)
		
	#FIX
	def getBalance(self):
		balance = self.driver.find_element_by_class_name('dollar')
		print(balance.text)

	def wait(self):
		bet_status = self.driver.find_element_by_id('betstatus')
		print('STATUS: Waiting for next match')
		while 'OPEN' not in bet_status.text:
			time.sleep(3)

	def next_match(self):
		bet_status = self.driver.find_element_by_id('betstatus')
		print('STATUS: Waiting for next match')
		while 'Bets are locked until the next match.' not in bet_status.text:
			time.sleep(3)

	def grabFight(self):
		fighterOne = self.driver.find_element_by_class_name('redtext').text.split('|')[1]
		fighterTwo = self.driver.find_element_by_class_name('bluetext').text.split('|')[0]
		print(fighterOne)
		print(fighterTwo)
		self.db.insertFight(fighterOne,fighterTwo)

	def checkWinner(self):
		#Payouts to Team Blue
		bet_status = self.driver.find_element_by_id('betstatus')
		fighterOne = self.driver.find_element_by_class_name('redtext').text.split('|')[1]
		fighterTwo = self.driver.find_element_by_class_name('bluetext').text.split('|')[0]
		while 'Payouts to team blue.' or 'Payouts to team red.' not in bet_status.text:
			if(bet_status.text.contains('Payouts to team blue')):
				print(fighterOne + ' wins')
			elif(betstatus.text.contains('Payouts to team red')):
				print(fighterTwo + ' wins')
		
		#Finish
	def checkTourney(self):
		tourneyText = self.driver.find_element_by_id('tournament-note').text
		if tourneyText == '(Tournament Balance)':
			tournamentMode()

	def tournamentMode(self):
		print('yada')

	#Check if you gained or lossed money for the day
	#def checkRevenue():


if __name__ == "__main__":
	x = SaltBot()
	x.login()
	while True:
		x.wait()
		x.bet()
		x.next_match()
		x.grabFight()