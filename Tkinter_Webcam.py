#!/usr/bin/env python
# coding: utf-8

# In[35]:


import tkinter as tk
import cv2
from PIL import Image, ImageTk
root=tk.Tk()
# Set the size of the window
root.geometry("780x600")

# Set the window background color
root.configure(bg="#a8dba8")

def start_webcam():
    ret, frame= cap.read()
    if flip_var.get():
        frame=cv2.flip(frame,1)
    if gray_var.get():
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    img=Image.fromarray(cv2image)
    imgtk=ImageTk.PhotoImage(image=img)
    lmain.imgTk=imgtk
    lmain.configure(image=imgtk)
    lmain.after(10,start_webcam)

root.title=("Webcam Viewer")
cap=cv2.VideoCapture(0)
flip_var=tk.BooleanVar()
gray_var=tk.BooleanVar()
flip_var.set(True)
gray_var.set(False)
flip_checkbox= tk.Checkbutton(root,text='Flip',variable=flip_var,bg="#a8dba8")
flip_checkbox.pack()

gray_checkbox = tk.Checkbutton(root , text='GrayScale',variable=gray_var,bg="#a8dba8")
gray_checkbox.pack()

lmain = tk.Label(root)
lmain.pack()
start_button = tk.Button(root ,text='Start Webcam',command = start_webcam,bg="#57BE85")
start_button.pack()
def stop_webcam():
    cap.release()
    root.destroy()
stop_button = tk.Button(root ,text='Stop Webcam',command = stop_webcam,bg="#3b8686")
stop_button.pack()
root.mainloop()


# In[ ]:





# In[ ]:




