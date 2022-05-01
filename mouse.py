import pyautogui, time

while True:
    print(".")
    pyautogui.moveTo(100,200)
    time.sleep(5)
    pyautogui.moveTo(200,500)
    print("-")
    time.sleep(5)
    
