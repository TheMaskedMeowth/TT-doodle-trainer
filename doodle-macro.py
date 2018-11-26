#requires maximized window at 1920x1080

import win32api
import win32gui
import win32con
import time
import random

title = "Toontown Rewritten"
sleep = 0

def screenClick(x, y):
	coords = win32api.MAKELONG(x, y)
	win32gui.PostMessage(win32gui.FindWindow(None, title), win32con.WM_LBUTTONDOWN, 1, coords)
	win32gui.PostMessage(win32gui.FindWindow(None, title), win32con.WM_LBUTTONUP, 0, coords)
	time.sleep(0.1)

while 1:
	screenClick(100, 40)
	screenClick(220, 130)
	screenClick(400, 130)
	#Y value: Speak = 330, Rollover = 230
	screenClick(480, 230)
	time.sleep(sleep)
	sleep = random.uniform(4.5, 6)
	print(str(sleep) + " seconds until the next trick")
