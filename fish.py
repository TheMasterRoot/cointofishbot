import pyautogui
import time
import sys
import os 
import shlex
import subprocess
count = 0
def python_to_bash_without_output(cli_args):
    args = shlex.split(cli_args)
    subprocess.Popen(args)

# while True:
# 	time.sleep(3)
# 	try:		
# 		start03 = pyautogui.locateCenterOnScreen('03.jpg', confidence = 0.97)
# 		print(start03)
# 		if start03 is not None:
# 			print("Mission 6")
# 			pyautogui.moveTo(start03, duration=0.3, tween=pyautogui.easeInOutQuad)
# 	except:
# 		continue


# try:			
# 				start = pyautogui.locateCenterOnScreen('01.jpg', confidence = 0.7)
# 				if start is not None:
# 					print("Mission", start)
# 					pyautogui.moveTo(start, duration=0.3, tween=pyautogui.easeInOutQuad)		
# 					pyautogui.click()
# 					continue
# 			except Exception as e:
# 				pass


while True:
	botoes = list(pyautogui.locateAllOnScreen('botao.jpg',confidence = 0.95))


	for botao in botoes:
		while True:
			try:
				l,t,w,h = botao
				x,y=int(l+(w/2)),int(t+(h/2))
				pyautogui.moveTo((x,y), duration=0.3, tween=pyautogui.easeInOutQuad)
				pyautogui.click()
				time.sleep(2)
				form = pyautogui.locateCenterOnScreen('form.jpg', confidence = 0.90)
				pyautogui.moveTo(form, duration=0.3, tween=pyautogui.easeInOutQuad)
				if form is None:
					fechar = list(pyautogui.locateCenterOnScreen('fechar.jpg', confidence = 0.90))
					pyautogui.moveTo(fechar, duration=0.3, tween=pyautogui.easeInOutQuad)
					pyautogui.click()
					time.sleep(0.5)
					break
				pyautogui.click()
				pyautogui.press('down')
				time.sleep(0.5)
				pyautogui.press('enter')
				feed = pyautogui.locateCenterOnScreen('feed.jpg', confidence = 0.90)
				pyautogui.moveTo(feed, duration=0.3, tween=pyautogui.easeInOutQuad)
				pyautogui.click()
				time.sleep(2)
				break
			except:
				continue
	time.sleep(300)
	invent = pyautogui.locateCenterOnScreen('invent.jpg', confidence = 0.90)
	pyautogui.click()
	time.sleep(5)

