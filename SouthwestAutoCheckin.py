from SWA_funs import *

'''
TODO:
	- Add command line args for confNum, fName, lName
	- Automatically find flight date and time from confNum, fName, lName (https://www.southwest.com/air/manage-reservation/)
	- Write scrip to add job to crontab for execution at the proper time
	- Add ability to detect a 'short name' and turn it into full fName, lName
	- Ability to text (via number@vzwireless.com) confirmation that they have been checked in and their boarding position

'''

myconfNum = 'RCXB6V'
myfName = 'Matthew'
mylName = 'Lawson'

# Find_Flight_Time(myconfNum, myfName, mylName)
Checkin(myconfNum, myfName, mylName)
