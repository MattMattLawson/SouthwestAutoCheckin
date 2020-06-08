from selenium import webdriver
import time

# Initialize global chrome webdriver for use in all functions
chrome = webdriver.Chrome('/Users/matt/Google Drive/SouthwestAutoCheckin/chromedriver')
chrome.set_page_load_timeout(10)


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


	# This doesn't work yet. I am trying to find a way to detect 'Departing', the flight date, and the flight number so that I can retreive the exact checkin time
	fdh = chrome.find_element_by_class_name('flight-detail--heading')
	print(fdh)



def Checkin(myconfNum, myfName, mylName):
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

	time.sleep(8)
	chrome.close()
