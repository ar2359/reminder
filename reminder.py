#run this code whenever you want to add, remove or list the reminders
#Python 2.7

import time
from datetime import datetime
import delorean
import pickle
import os

print "*******Welcome to Reminder*******"
print "What do you want to do?\n"
print "1.List your reminders\n2.Add a reminder\n3.Delete a reminder\n"
choice="0"
choice=raw_input("Enter 1/2/3: ")

ip=pickle.load(open("save.p","rb"))

os.environ['TZ']='Asia/Kolkata'

if (choice=="1"):
	print ip

elif (choice=="2"):

	raw_tim=raw_input("Enter the time in D/MM/YYYY/HH(24)/MM: ")

	tim=raw_tim.split('/')

	m=tim[1]

	if m=="01":
		mm="Jan"
	elif m=="02":
		mm="Feb"
	elif m=="03":
		mm="Mar"
	elif m=="04":
		mm="Apr"
	elif m=="05":
		mm="May"
	elif m=="06":
		mm="Jun"
	elif m=="07":
		mm="Jul"
	elif m=="08":
		mm="Aug"
	elif m=="09":
		mm="Sep"
	elif m=="10":
		mm="Oct"
	elif m=="11":
		mm="Nov"
	elif m=="12":
		mm="Dec"

	d=tim[0]
	y=tim[2]
	h=tim[3]
	min=tim[4]

	h1=int(h)
	d1=int(d)

	if h1>12:
		ampm="PM"
		h1=h1-12
	else:
		ampm="AM"
	h=str(h1)
		
	if h1>24:
		ch=raw_input("Invalid Time ")
		exit()
	elif mm=="Feb" and d1>28:
		ch=raw_input("Invalid Date ")
		exit()

	st=mm + " " + d + " " + y + " " + h + ":"+ min + ampm
	date_object=datetime.strptime(st,'%b %d %Y %I:%M%p') #converting string to datetime
	print date_object
	date_object_string=str(date_object)
	print date_object_string
	p='%Y-%m-%d %H:%M:%S'
	epoch=int(time.mktime(time.strptime(date_object_string,p)))
	
	reason=raw_input("Enter the reminder: ")



	ip[reason]=epoch

	pickle.dump(ip,open("save.p","wb"))

elif (choice=="3"):
	reason=raw_input("Enter the reminder description you want to delete: ")
	del ip[reason]
	pickle.dump(ip,open("save.p","wb"))
	
else:
	ch=raw_input("Invalid Choice.. ")
	exit()

ch=raw_input("Thank You for using Reminder :) ")
exit()


