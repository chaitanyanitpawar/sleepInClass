import pyautogui 
import schedule 
import time 
meetId = ""
email = ""
def attend():
    time.sleep(0.2)
    pyautogui.press('esc',interval=0.1)
    time.sleep(0.3)
    pyautogui.press('win',interval=0.5)
    pyautogui.write('GoToWebinar')
    pyautogui.press('enter',interval=0.5)
    time.sleep(5)
    x,y = pyautogui.locateCenterOnScreen('ID.png', confidence = 0.8)
    pyautogui.click(x,y)
    pyautogui.write(meetId)
    pyautogui.press('tab',interval=5)
    pyautogui.write(email)
    pyautogui.press('enter',interval=5)
    x,y = pyautogui.locateCenterOnScreen('Open.png', confidence = 0.8)
    pyautogui.click(x,y)
    
if __name__ == "__main__":
    attend()
