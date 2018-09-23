#this code runs indefinitely to check the reminders and alert the user


import pickle
import time
import datetime
import os
import ctypes

i=0
ip2={'0':0}
try:
	while True:
		st1=time.time()
		ip = pickle.load( open( "save.p", "rb" ) )
		i=0
		
		
		while True:
			st2=time.time()
			if ((st1-st2)>3600):
				break
			
			for count in range(0,len(ip)-1):
				if(ip.values()[count]>st1 and ip.values()[count]<=st1+3600):
						
						ip2[ip.keys()[count]]=ip.values()[count]
						del ip[ip.keys()[count]]
				
			while (len(ip2) !=0):
				st3=time.time()
				
				for i in range(0,len(ip2)-1):
					if (ip2.values()[i]>=st3 and ip2.values()[i]<st3+2) :
						os.startfile("Path:\Song.mp3")        #add the path of your song here. This song plays when the time is reached
						ctypes.windll.user32.MessageBoxA(0,ip2.keys()[i],"ALERT",1)  #to open a message box 
						del ip2[ip2.keys()[i]]
						del ip[ip2.keys()[i]]
						pickle.dump(ip,open("save.p","wb"))
except KeyboardInterrupt:
	exit()

						
			

			