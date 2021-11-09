import pywhatkit as kit
import datetime

phnum = input('Enter The Phone Number')
msg = input('Enter the message')
timehour = datetime.datetime.now().hour
timemin = datetime.datetime.now().minute + 2
kit.sendwhatmsg(phnum, msg, timehour,timemin)
