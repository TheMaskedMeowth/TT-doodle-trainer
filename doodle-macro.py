#Toontown Doodle Training Macro in Python by Obligatory Unicorn
#requires maximized window at 1920x1080 and running script with administrator access

import win32api, win32gui, win32con, win32com.shell.shell as shell, time, random, msvcrt, _thread
if not shell.IsUserAnAdmin():
	print("This script must be run as an administrator. Press any key to exit...")
	junk = msvcrt.getch()
	os.system("cls")
	sys.exit()
title = "Toontown Rewritten"
trick = 7
window = win32gui.FindWindow(None, title)

try:
	import cursor
	cursor.hide()
except:
	pass

def screenClick(x, y):
	coords = win32api.MAKELONG(x, y)
	win32gui.PostMessage(window, win32con.WM_LBUTTONDOWN, 1, coords)
	win32gui.PostMessage(window, win32con.WM_LBUTTONUP, 0, coords)
	time.sleep(0.05)
	
def trickPerform():
	sleep = random.uniform(4.5, 6)
	yValues = [130, 160, 200, 230, 260, 300, 330]
	counter = 1
	while True:
		sleep = random.uniform(4.5, 6)
		counter += 1
		print(str(sleep)[:6] + " seconds until trick #" + str(counter) + " is performed.", end='\r')
		screenClick(100, 40)
		screenClick(220, 130)
		screenClick(400, 130)
		screenClick(480, yValues[trick - 1])
		time.sleep(sleep)

_thread.start_new_thread(trickPerform, ())
print("\nAt any time while the program is running, you can press the number keys 1-7 to change to a different trick\ncorresponding to that trick's placement on the SpeedChat menu (i.e. \"Jump!\" would be accessed by pressing 1.)\nAdditionally, you can press any other key to exit the script.\n")
while True:
	x = chr(int.from_bytes(msvcrt.getch(), byteorder='big'))
	if x.isdigit():
		if int(str(x)) >= 1 and int(str(x)) <= 7:
			trick = int(str(x))
	else:
		_thread.exit()
