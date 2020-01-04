import pyautogui

pyautogui.size()
width, height = pyautogui.size()
print(f"width={width},height={height}")

print(f"the mouse position is {pyautogui.position()}")

file_name = "test.png
save_path = ""
#get whole display screenshot
pyautogui.screenshot("test.png")

#specify zone of interest
#draw a square with cliks over screen after execution to specify zone of interest

#crop out screenshot to just zone of interest

#get specific zone screenshot and save to specified path
