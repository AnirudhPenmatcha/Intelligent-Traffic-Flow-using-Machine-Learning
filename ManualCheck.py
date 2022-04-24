import datetime

def manual_check():
	log = open("ManualCheckLog.txt","a")#append mode
	x = datetime.datetime.now()
	log.write(f'Manual Check Alert at {x.strftime("%H:%M:%S, %d-%b-%y")}\n')
	log.close()
	print("Manual Check Required")
