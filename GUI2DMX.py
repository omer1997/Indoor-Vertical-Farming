#As the libraries for the OLA server do not support Python 3
#it is nescessery that this program written in Python 2.7, exists as a passthrough between our python3 UI and the DMX controller.

from __future__ import print_function
from ola.ClientWrapper import ClientWrapper
from array import array
import sys
import json
from time import sleep
import numpy as np
from datetime import datetime, timedelta, time
import csv

__author__ = 'Nehemiah Myers'

wrapper = None


def DmxSent(status):
	if status.Succeeded():
		print('Success!')
	else:
		print('Error: %s' % status.message, file=sys.stderr)

	global wrapper
	if wrapper:
		wrapper.Stop()



def main():
	universe = 2

	x = 0
	growcycleConditions = readCSV()
	format_string = "%Y-%m-%d %H:%M:%S"
	daydelta = timedelta(days = 1)
	thymedelta = timedelta(hours = 12)

	startDate = growcycleConditions[x][0] #Grab the first element of the list which is the date


	endDate = growcycleConditions[(len(growcycleConditions) - 1)][0] #Last date in the list

	startDate = datetime.strptime(startDate, format_string)
	endDate = datetime.strptime(endDate, format_string)

	currentDay = datetime.now().date()
	tomorrow = startDate + daydelta
	startDay = startDate.date()

	lastDay = endDate.date()



	startTime = startDate.time()
	endTime = (startDate + thymedelta)




	onTime = 0
	offTime = 0

	startCycle = False

	global wrapper
	wrapper = ClientWrapper()
	client = wrapper.Client()

	currentDay = datetime.now().date()
	now = datetime.now().time()
	print("Today is: " + currentDay.strftime("%Y-%m-%d"))
	print("Lights will turn on: " + startDay.strftime("%Y-%m-%d"))

	while currentDay <= lastDay:

		nowTime = datetime.now().time()
		nowDT = datetime.now()

		if currentDay >= startDay:

			print("Today is start of cycle!")
			print("Time is: " + datetime.now().strftime("%H:%M:%S"))
			print("Lights will turn on at: " + startTime.strftime("%H:%M:%S"))
			print("Lights will turn off at: " + endTime.strftime("%Y-%m-%d %H:%M:%S"))
			startCycle = True
			sleep(2)

		if nowTime >= startTime and nowDT <= endTime and startCycle == True:		# If time is between or equal to our set points then turn the lights on,
			print("Starting Saturation at ", datetime.now().strftime("%H:%M:%S"))  	# this is so that if you reset the lights at 2 PM they wont run until 2 AM.
			dmxData = json.loads(growcycleConditions[x][1])
			dmxData = array('B', dmxData)
			client.SendDmx(universe, dmxData, DmxSent)
			wrapper.Run()
			sleep(10)												# This block of code turns the lights on for a few seconds so
			dmxData = turnLightsOff()									# they dont get overwhelmed, or at least thats what i was told.
			dmxData = array('B', dmxData)
			client.SendDmx(universe, dmxData, DmxSent)
			wrapper.Run()
			print("Ending saturation at ", datetime.now().strftime("%H:%M:%S"))
			sleep(10)
			#Now we turn the lights on for the duration of the day
			print("Starting/Continuing day at ", datetime.now().strftime("%H:%M:%S"))
			dmxData = json.loads(growcycleConditions[x][1])
			dmxData = array('B', dmxData)
			client.SendDmx(universe, dmxData, DmxSent)
			wrapper.Run()
			onTime = int((endTime - nowDT ).seconds) #If you happen to restart the lights in the middle of the day they won't run for an additional 12+ Hours.
			print("Lights will be on for: " + str(onTime / 3600) + " Hours")
			sleep(onTime) # time.sleep only accepts seconds units
			nowDT = datetime.now()

		else:
			dmxData = turnLightsOff()
			dmxData = array('B', dmxData)
			client.SendDmx(universe, dmxData, DmxSent)
			wrapper.Run()
			offTime = int((tomorrow - nowDT ).seconds)
			print("Lights will be off for: " + str(offTime / 3600) + " Hours")
			sleep(offTime) #Keep lights off until its startTime
			currentDate = datetime.now()
			currentDay = datetime.now().date()
			tomorrow = currentDate + daydelta
			endTime = (currentDate + thymedelta)
			x = x + 1






	# send 1 dmx frame with values for channels 1-3

def turnLightsOff():
	farm1 = [0] * 8
	farm2 = [0] * 8
	farm3 = [0] * 8
	farm4 = [0] * 8
	blankChannels = [0] * 9
	UVAlight1 = [255, 0, 0, 0, 0, 0, 0, 0, 0, 0] #First channel of UVA light bar must be always be 255 for it to properly function
	UVAlight2 = [255, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	UVAlight3 = [255, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	UVAlight4 = [255, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	farmArray = farm1 + farm3 + farm2 + farm4 + blankChannels + UVAlight1 + UVAlight2 + UVAlight3 + UVAlight4 #Order of these are based upon the ola_send_dmx python files created by Tom O'Donnell

	return farmArray


def readCSV():
	with open('growcycleConditions.csv', mode='r') as csv_file:
	  reader = csv.reader(csv_file)
	  conditions = [(rows[0], rows[1]) for rows in reader] #Rows have to be read into a list as python2.7 cannot convert dictionaries to lists in a useable fashion


	return conditions

if __name__ == '__main__':
  main()
