import tkinter as tk
from tkinter import filedialog, Text
import os
from PIL import Image
import datetime
from pynput import mouse
import pyautogui
root = tk.Tk()

root.title('pyScreenshot App')

canvas = tk.Canvas(root, height = 200, width= 1200, bg = "#132a45")
canvas.pack()

frame = tk.Frame(root, bg= "white")
frame.place(relwidth = 0.9, relheight = 0.9, relx=0.05, rely=0.05)

savePath = [""]
filename_start = "pyScreenshot_"
click_box =[]

def addApp():
    filename = filedialog.askdirectory(initialdir="/", title = "Select Folder")
    #savePath = filename
    savePath[0]=filename
    label = tk.Label(frame, text="Save Folder is " + ",".join(savePath), bg = "grey")
    label.pack()

def addZone():
    click_box.clear()
    #specify zone of interest
    #record two points with clicks over screen after execution to specify zone of interest
    def on_click(x, y, button, pressed):
    #print('{0} at {1}'.format(
    #    'Pressed' if pressed else 'Released',
    #    (x, y)))
        if not pressed:
            # Stop listener
            click_box.append([x,y])
            return False
        # Collect events until released
    with mouse.Listener(
            on_click=on_click) as listener:
        listener.join()
    with mouse.Listener(
            on_click=on_click) as listener:
        listener.join()
    #print(click_box)
    label = tk.Label(frame, text='New Screenshot Zone Captured', bg = "grey")
    label.pack()

def addZnShot():
    #if user specifies zone screenshot then crop out to zone of interest
    im=pyautogui.screenshot()
    # Setting the points for cropped image & adjust coordinates
    #x1,y1 = click_box[0]
    #x2,y2 = click_box[1]
    x1,y1 = [i*2 for i in click_box[0]]
    x2,y2 = [i*2 for i in click_box[1]]
    #print(x1,y1,x2,y2)
    #correct crop box coordinates if non-standard opposite ends are selected
    #x1 should be less then x2
    #y1 should be less than y2 for the crop to work successfully
    if y1<y2 and x1>x2:
        x1,x2 = x2,x1
    elif y1>y2 and x1>x2:
        x1,x2,y1,y2 = x2,x1,y2,y1
    elif y1>y2 and x1<x2:
        y1,y2 = y2,y1
    #print(x1,y1,x2,y2)
    #crop specified zone screenshot
    im1 = im.crop((x1, y1, x2, y2))
    direc = savePath[0]
    dt = datetime.datetime.now().strftime("%m-%d-%Y_%I-%M-%S_%p")
    filename_start = "pyZoneScreenshot_"
    save_path = direc + "/" +  filename_start + dt + ".png"
    #save cropped image
    im1.save(save_path)
    label = tk.Label(frame, text="Zone screenshot saved at "+save_path, bg = "grey")
    label.pack()


def addFsShot():
    # if user specifies full display screenshot then
    # get full screenshot
    direc = savePath[0]
    dt = datetime.datetime.now().strftime("%m-%d-%Y_%I-%M-%S_%p")
    filename_start = "pyFullScreenshot_"
    save_path = direc + "/" +  filename_start + dt + ".png"
    pyautogui.screenshot(save_path)
    label = tk.Label(frame, text="Full screenshot saved at "+save_path, bg = "grey")
    label.pack()


DeclareSavePath = tk.Button(root,text="Declare Save Path", padx=10, pady=5, bg = "#132a45", fg = "#9e2d29",
command = addApp )
DeclareSavePath.pack()

ScreenZone = tk.Button(root,text="Declare Screenshot Zone", padx=10, pady=5, bg = "#132a45", fg = "#d6a02b",
command = addZone )
ScreenZone.pack()

TakeShot = tk.Button(root,text="Zone Screen Screenshot", padx=10, pady=5, bg = "#132a45", fg = "#29449e",
command =  addZnShot)
TakeShot.pack()

TakeFullScrShot =tk.Button(root,text="Full Screen Screenshot", padx=10, pady=5, bg = "#132a45", fg = "#4a8a1a",
command =  addFsShot)
TakeFullScrShot.pack()

root.mainloop()
