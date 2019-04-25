import pyautogui

#Point(x=273, y=62)
print(pyautogui.position())

pyautogui.click(273,62)
pyautogui.hotkey("ctrl","c")
pyautogui.typewrite("Hello world?")
pyautogui.typewrite(["enter"])