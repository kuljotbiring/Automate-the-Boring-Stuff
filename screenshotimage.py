import pyautogui

# returns pil image object after taking a screenshot
pyautogui.screenshot('example.png')

# image recognition - will return xy coordinates and width and height
pyautogui.locateOnScreen('password.png')

# locate the center of an image location
pyautogui.locateCenterOnScreen('password.png')

