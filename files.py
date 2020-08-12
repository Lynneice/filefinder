import os
import tkinter as tk
import itertools
import threading
import time
import sys



#function for search by extension
def go():
    ftype = extEntry.get().lower()
    direct = leftDirectory.get().lower()
    print("go")
    #user input directory and extension including '.'
    for dirpath, dirs, files in os.walk(str(direct)):
        for filename in files:
            fname = os.path.join(dirpath, filename)
            if fname.endswith(str(ftype)):
#                print(fname)
               textbx.insert('1.0', fname + "\n")          
    return       

#search by name is only slightly8 different
def goByName():
    searchTerm = nameEntry.get()
    direct = rightDirectory.get().lower()
    print("working")
    #nested for loops using os.walk (user input directory to search in)
    for dirpath, dirs, files in os.walk(str(direct)):
        for filename in files:
            if searchTerm in filename:
                textbx.insert('0.0', filename + "\n")
    return
 
#Tkinter GUI
WIDTH = 800
HEIGHT = 600
 
#where is that file?????
root = tk.Tk()
root.title("Where is that file?")
 
#set the default dimensions
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()
 
background_label = tk.Label(root, bg = '#2d2d2d')
background_label.place(relwidth = 1, relheight = 1)
 
#The question of the hour. display question
topframe = tk.Frame(root, bg = '#2d2d2d')
topframe.place(relwidth = 0.8, relheight = 0.3, relx = .10, rely = 0.05)
 
toplabel = tk.Label(topframe, font = 30, bg = '#2d2d2d', fg = 'white', text = "What are you looking for?\nSearch by extension or name")
toplabel.place(relwidth = 0.5, relheight = .25, relx = .25, rely = .2)
 
#where search A will be
leftFrame = tk.Frame(root, bd = 5, bg = '#2d2d2d')
leftFrame.place(relwidth = 0.4, relheight = .6, relx = 0.1, rely = 0.2)
 
leftTopLabel = tk.Label(leftFrame, bg = '#2d2d2d', fg = 'white', text = "Please specify extension (include '.'):")
leftTopLabel.place(relwidth = 0.75, relheight = 0.1, relx = 0.15, rely = 0.15)
 
extEntry = tk.Entry(leftFrame, bd=3)
extEntry.place(relwidth = 0.5, relheight = 0.1, relx = 0.25, rely = 0.3)
 
leftMidLabel = tk.Label(leftFrame, bg = '#2d2d2d', fg = 'white', text = "Please specify a directory:")
leftMidLabel.place(relwidth = 0.75, relheight = 0.1, relx = 0.15, rely = 0.5)
 
leftDirectory = tk.Entry(leftFrame, bd = 3)
leftDirectory.place(relwidth = 0.85, relheight = 0.1, relx = 0.1, rely = 0.65)
 
 
 
getExt = tk.Button(leftFrame, bd = 2, text = "Search by extension", command=lambda:go())
getExt.place(relheight = 0.08, relwidth = 0.75, relx = 0.15, rely = 0.8)
 
#search area B
rightFrame = tk.Frame(root, bd = 5, bg = '#2d2d2d')
rightFrame.place(relwidth = 0.4, relheight = .6, relx = 0.5, rely = 0.2)
 
rightTopLabel = tk.Label(rightFrame, fg = 'white', bg = '#2d2d2d', text = "Search by name:")
rightTopLabel.place(relwidth = 0.75, relheight = 0.1, relx = 0.15, rely = 0.15)
 
nameEntry = tk.Entry(rightFrame, bd=3)
nameEntry.place(relwidth = 0.75, relheight = 0.1, relx = 0.15, rely = 0.3)
 
rightMidLabel = tk.Label(rightFrame, fg= 'white', bg = '#2d2d2d', text = "Please specify a directory:")
rightMidLabel.place(relwidth = 0.75, relheight = 0.1, relx = 0.15, rely = 0.5)
 
rightDirectory = tk.Entry(rightFrame, bd = 3)
rightDirectory.place(relwidth = 0.85, relheight = 0.1, relx = 0.1, rely = 0.65)
 
getName = tk.Button(rightFrame, bd = 2, text = "Search by name", command=lambda:goByName())
getName.place(relheight = 0.08, relwidth = 0.75, relx = 0.15, rely = 0.8)
 
 
#results
bottomframe = tk.Frame(root, bd = 5, bg = '#2d2d2d')
bottomframe.place(relwidth = 0.8, relheight = 0.2, relx = .10, rely = 0.8)
 
textbx = tk.Text(bottomframe, wrap = tk.WORD)
textbx.place(relwidth = 1, relheight = 1)
 
scroll = tk.Scrollbar(bottomframe)
scroll.pack(fill = tk.Y, side = tk.RIGHT)
 
scroll.config(command=textbx.yview)
textbx.config(yscrollcommand=scroll.set)
 
 
#don't close window 
root.mainloop()
