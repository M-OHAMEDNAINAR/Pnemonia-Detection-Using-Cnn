from tkinter import *
import ctypes,os
from PIL import ImageTk, Image
import tkinter.messagebox as tkMessageBox
from tkinter.filedialog import askopenfilename
import tensorflow as tf
import tensorflow.keras.models as models
import cv2
import matplotlib.pyplot as plt
import  numpy as np

        
home = Tk()
home.title("Pneumonia Disease Detection")

img = Image.open("images/home.png")
img = ImageTk.PhotoImage(img)
panel = Label(home, image=img)
panel.pack(side="top", fill="both", expand="yes")
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
lt = [w, h]
a = str(lt[0]//2-450)
b= str(lt[1]//2-320)
home.geometry("900x653+"+a+"+"+b)
home.resizable(0,0)
file = ''

def Exit():
    global home
    result = tkMessageBox.askquestion(
        "Pneumonia Disease Detection", 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        home.destroy()
        exit()
    else:
        tkMessageBox.showinfo(
            'Return', 'You will now return to the main screen')
        
def browse():
    
    global file,l1
    try:
        l1.destroy()
    except:
        pass
    file = askopenfilename(initialdir=os.getcwd(), title="Select Image", filetypes=( ("images", ".png"),("images", ".jpg"),("images", ".jpeg")))

def predict():
    global file,l1
    if file!='' or file!= None:
        SIZE = 150
        model = models.load_model('model/pneumonia.h5')
        nimage = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(nimage,(SIZE,SIZE))
        image = image/255.0
        pred = model.predict(np.array(image).reshape(-1,SIZE,SIZE,1))
        pred = pred[0][0]*100
        print(pred)
        if pred>80:
            predt = "Normal"
        else:
            predt = "Pneumonia"
            pred = 100-pred
            
        acc = '('+str(round(pred,2))+'%)'
        l1 = Label(home,text="Predicted Output Is: "+predt+acc,font=('',20,'bold'),bg="#FFE5DC",fg="#6B2E2F")
        l1.place(x=35,y=600)
        plt.imshow(nimage,cmap="gray")
        pValue = "Prediction : {0}".format(predt+acc)
        plt.title(pValue)
        plt.show()

def about():
    about = Toplevel()
    about.title("Pneumonia Disease Detection")

    img = Image.open("images/about.png")
    img = ImageTk.PhotoImage(img)
    panel = Label(about, image=img)
    panel.pack(side="top", fill="both", expand="yes")
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    lt = [w, h]
    a = str(lt[0]//2-450)
    b= str(lt[1]//2-320)
    about.geometry("900x653+"+a+"+"+b)
    about.resizable(0,0)
    photo = Image.open("images/5.png")
    img2 = ImageTk.PhotoImage(photo)
    b1=Button(about, highlightthickness = 0, bd = 0,activebackground="#FFE5DC", image = img2,command=about.destroy)
    b1.place(x=250,y=577)
    about.mainloop()
    
photo = Image.open("images/1.png")
img2 = ImageTk.PhotoImage(photo)
b1=Button(home, highlightthickness = 0, bd = 0,activebackground="#343434", image = img2,command=browse)
b1.place(x=35,y=210)

photo = Image.open("images/2.png")
img3 = ImageTk.PhotoImage(photo)
b2=Button(home, highlightthickness = 0, bd = 0,activebackground="#343434", image = img3,command=predict)
b2.place(x=35,y=282)

photo = Image.open("images/3.png")
img4 = ImageTk.PhotoImage(photo)
b3=Button(home, highlightthickness = 0, bd = 0,activebackground="#343434", image = img4,command=about)
b3.place(x=35,y=354)

photo = Image.open("images/4.png")
img5 = ImageTk.PhotoImage(photo)
b4=Button(home, highlightthickness = 0, bd = 0,activebackground="#343434", image = img5,command=Exit)
b4.place(x=35,y=426)

home.mainloop()
