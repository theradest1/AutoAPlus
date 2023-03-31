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
APlusButtonTimout = 5

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
	WebDriverWait(driver, timeout=APlusButtonTimout).until(lambda d: d.find_element(By.XPATH, "//*[@id=\"content-main\"]/div[3]/div/div[1]/a[2]")) #wait for move week button
	driver.find_element(By.XPATH, "//*[@id=\"content-main\"]/div[3]/div/div[1]/a[2]").click() #move forward a week
	# go forward a week
	#driver.find_element(By.XPATH, "//a[@ng-click=\"changeWeek(7)\"]").click()
	for day in range(3, 7):
		try:
			WebDriverWait(driver, timeout=APlusButtonTimout).until(lambda d: d.find_element(By.XPATH, "//*[@id=\"content-main\"]/div[3]/div/table/tbody/tr[2]/td[" + str(day) + "]/button")) #wait for A+ button
			driver.find_element(By.XPATH, "//*[@id=\"content-main\"]/div[3]/div/table/tbody/tr[2]/td[" + str(day) + "]/button").click()	#click A+ button
			WebDriverWait(driver, timeout=buttonTimout).until(lambda d: d.find_element(By.XPATH, "//*[@id=\"sessionPicker\"]/table[2]/tbody/tr[15]/td[1]/a")) #wait for double lunch
			driver.find_element(By.XPATH, "//*[@id=\"sessionPicker\"]/table[2]/tbody/tr[15]/td[1]/a").click() #schedule double lunch
		except:
			print("A+ for day with ID " + str(day) + " are not open")
	
	driver.implicitly_wait(5)
	time.sleep(5)

	#//*[@id="content-main"]/div[3]/div/table/tbody/tr[2]/td[4]/button		wed, A
	#//*[@id="content-main"]/div[3]/div/table/tbody/tr[3]/td[4]/button		wed, B
	#//*[@id="content-main"]/div[3]/div/table/tbody/tr[2]/td[5]/button		thurs, A
	#//*[@id="content-main"]/div[3]/div/table/tbody/tr[3]/td[5]/button		thurs, B
	#//*[@id="sessionPicker"]/table[2]/tbody/tr[15]/td[1]/a		double lunch



#starting
chrome_options = Options()
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument("--headless") #uncomment if you dont want GUI
#//chrome_options.add_argument('--disable-dev-shm-usage')

for client in clientInfo['clients']:
	chooseAPlusses(client)