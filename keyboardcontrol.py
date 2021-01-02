import pyautogui

# send key presses by first making it select the window and then type. use interval argument to make natural
pyautogui.click(100, 100), pyautogui.typewrite('Hello World', interval=0.2)

# list of keyboard commands in a list
print(pyautogui.KEYBOARD_KEYS)

# press a certain key
pyautogui.press('f1')

# key board shortcuts
pyautogui.hotkey('ctrl', 'o')