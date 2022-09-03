from unicodedata import name
import cv2
import imutils
import numpy as np
from imutils.perspective import four_point_transform
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd

from tkinter import messagebox
tkWindow = tk.Tk()

tkWindow.geometry('570x349')
tkWindow.title('Document Scanner')

bg = PhotoImage(file = "resources/bg.png")
  

label1 = Label( tkWindow, image = bg)
label1.place(x = 0, y = 0)

def screenshot():
    # screenshot
    try:
        cap = cv2.VideoCapture(0)

        imgcounter =0 

        while True:
            success , photo = cap.read() #read image and tell whether it is done successfully  or not , success is just a boolean value.
            cv2.imshow("Original Image",photo)
            x =  cv2.waitKey(1) 
            if  x%0xFF == ord('q'):
                break

            elif x%0xFF == ord('s'):
                imagename = "opencv{}.png".format(imgcounter)
                cv2.imwrite(imagename,photo)
                print("ss taken")
                imgcounter +=1

        cap.release()
        cv2.destroyAllWindows()

        scanner(imagename)

    except:
        print("Document not found")

def imagesc():
    filetypes = (
        ('All files', '*.*'),
        ('text files', '*.txt')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=r'C:\Users\Swastik Computers\PycharmProjects\opencvv',
        filetypes=filetypes)

    name=filename
    print(name)
    path = r"C:\Users\Swastik Computers\PycharmProjects\opencvv\ex.jpg"
    scanner(name)

def scanner(image_name):
    try:
        img_path = image_name
        big_img = cv2.imread(img_path)
        cv2.imshow('org img',big_img)


        ratio = big_img.shape[0] / 500.0
        org = big_img.copy()
        img = imutils.resize(big_img, height = 500)
        # cv2.imshow('resizing',img)
        # cv2.waitKey(0)


        gray_img = cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY)
        blur_img = cv2.GaussianBlur(gray_img,(5,5),0)
        edged_img = cv2.Canny(blur_img,50,50)
        # cv2.imshow('edged',edged_img)
        # cv2.waitKey(0)


        cnts,_ = cv2.findContours(edged_img.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts,key=cv2.contourArea,reverse=True)[:5]
        for c in cnts:
            peri = cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,0.02*peri,True)
            if len(approx)==4:
                doc = approx
                break
                

        warped = four_point_transform(org, doc.reshape(4, 2) * ratio)
        warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Warped", imutils.resize(warped, height = 650))
        cv2.waitKey(0)

        # a =  cv2.imwrite("newimage.png",warped)

        cv2.destroyAllWindows()
    except:
            print("Document not found")
 
w = Label(tkWindow, text='Document Scanner')
w.config(font =("Courier", 18),bd=7)
w.place(x=150,y=150)

w.pack()

button = tk.Button(tkWindow,
	text = 'Camera', bd=7,fg='red',width=25,
	command = screenshot)
button.pack(side =LEFT)
button.place(x=80,y=280)


button = tk.Button(tkWindow,
        text = 'image', bd =7,fg='red',width=25,
	command = imagesc)
button.pack(side = BOTTOM)
button.place(x=300,y=280)
tkWindow.mainloop()