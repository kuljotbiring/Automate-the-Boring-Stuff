import pyautogui

# return screen resolution size
width, height = pyautogui.size()

# get the position of the mouse
pyautogui.position()

# control the mouse of where to move with x and y coordinate
pyautogui.move(10, 10)

# move the mouse naturally with duration movement to coordinate over time
pyautogui.move(10, 10, duration=1.5)

# move the mouse relative to where it it - can add duration as optional argument
pyautogui.moveRel(20, 0)

# make the mouse click - if you dont pass it arguments, will click where it currently is
pyautogui.click(339, 38)

# make it double click
pyautogui.doubleClick(339, 38)

# make it middle click
pyautogui.middleClick(339, 38)

# make it right click
pyautogui.rightClick(339, 38)

# show real time position of the mouse - only use on terminal
pyautogui.displayMousePosition()