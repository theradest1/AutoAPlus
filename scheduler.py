from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json

#load info
clientInfoJson = open('clientInfo.json')
clientInfo = json.load(clientInfoJson)
clientInfoJson.close()

url = 'https://vasd.powerschool.com/public/home.html'
sceduleURL = 'https://vasd.powerschool.com/guardian/studentSchedule.html'

def chooseAPlusses(_client):
	username = _client["username"]
	password = _client["password"]
	

	# load page
	driver = webdriver.Chrome(options=chrome_options)
	driver.get(url)

	# enter in info and login
	driver.find_element(By.ID, 'fieldAccount').send_keys(username)
	driver.find_element(By.ID, 'fieldPassword').send_keys(password)
	driver.find_element(By.ID, 'btn-enter-sign-in').click()

	# go to scedule URL
	driver.get(sceduleURL)
	# go forward a week
	driver.find_element(By.XPATH, "//a[@ng-click=\"changeWeek(7)\"]").click()
	#driver.find_element(By.XPATH, "//button[@ng-click=\"showSessions(period.id,day.dateString)\"]").click()
	#driver.find_element(By.XPATH, "//span[@ng-click=\"getHope(1,'pray','smile')\"]").click()



#starting
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument("--headless") #uncomment if you dont want GUI
chrome_options.add_argument('--disable-dev-shm-usage')

for client in clientInfo['clients']:
	chooseAPlusses(client)