from selenium import webdriver
import time

# Initialize global chrome webdriver for use in all functions
chrome = webdriver.Chrome('/Users/matt/Google Drive/SouthwestAutoCheckin/chromedriver')
chrome.implicitly_wait(10)


def Find_Flight_Time(myconfNum, myfName, mylName):
	chrome.get('https://www.southwest.com/air/manage-reservation/')

	try:
		confNumField = chrome.find_element_by_id('confirmationNumber')
		fNameField = chrome.find_element_by_id('passengerFirstName')
		lNameField = chrome.find_element_by_id('passengerLastName')
	except Exception as e:
		print('{}: Could not find the proper fields'.format(e))
		return

	confNumField.send_keys(myconfNum)
	fNameField.send_keys(myfName)
	lNameField.send_keys(mylName)

	checkinBtn = chrome.find_element_by_id('form-mixin--submit-button')
	checkinBtn.click()


	# This doesn't work yet. I am trying to find a way to detect 'Departing', the flight date, and the flight number so that I can retrieve the exact check-in time
	fdh = chrome.find_element_by_class_name('flight-detail--heading')
	print(fdh)


def Checkin(myconfNum, myfName, mylName):
	chrome.get('https://www.southwest.com/air/check-in/index.html')

	try:
		confNumField = chrome.find_element_by_id('confirmationNumber')
		fNameField = chrome.find_element_by_id('passengerFirstName')
		lNameField = chrome.find_element_by_id('passengerLastName')
	except Exception as e:
		print('{}: Could not find the proper fields'.format(e))
		return

	confNumField.send_keys(myconfNum)
	fNameField.send_keys(myfName)
	lNameField.send_keys(mylName)

	checkinBtn = chrome.find_element_by_id('form-mixin--submit-button')
	checkinBtn.click()

	checkinXpath1 = "//div[@class='information--content']/a[@aria-label='Check-in link redirects to check in page']"
	checkinXpath1a = '//*[@id="air-reservation"]/div[2]/div[2]/div[3]/div/div[3]/div/a'

	checkinBtn = chrome.find_element_by_xpath(checkinXpath1)
	chrome.find_element_by_xpath('/html').send_keys(' ')  # Scroll down the page?
	time.sleep(1)
	print(checkinBtn.is_displayed())
	checkinBtn.click()

	checkinXpath2='//*[@id="swa-content"]/div/div[2]/div/section/div/div/div[3]/button'
	checkinBtn = chrome.find_element_by_xpath(checkinXpath2)
	time.sleep(1)
	print(checkinBtn.is_displayed())
	checkinBtn.click()
