from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

url = 'https://vasd.powerschool.com/public/home.html'
sceduleURL = 'https://vasd.powerschool.com/guardian/studentSchedule.html'

# open browser
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

# load page
driver.get(url)

# enter in info and login
driver.find_element(By.ID, 'fieldAccount').send_keys(input("Username: "))
driver.find_element(By.ID, 'fieldPassword').send_keys(input("Password: "))
driver.find_element(By.ID, 'btn-enter-sign-in').click()

# go to scedule URL
driver.get(sceduleURL)
# go forward a week
#driver.find_element(By.XPATH, "//a[@ng-click=\"changeWeek(7)\"]").click() commented out for testing
driver.find_element(By.XPATH, "//button[@ng-click=\"showSessions(period.id,day.dateString)\"]").click()
#driver.find_element(By.XPATH, "//span[@ng-click=\"getHope(1,'pray','smile')\"]").click()


