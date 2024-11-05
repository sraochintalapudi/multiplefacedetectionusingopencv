from tkinter import *
from PIL import ImageTk, Image
import cv2
root = Tk()
root.geometry("900x500")
root.title("Multiple face detection using opencv")
root.configure(bg="cyan")
inputimage = cv2.imread('mlbootcamp.jpg')
blue,green,red = cv2.split(inputimage)
img = cv2.merge((red,green,blue))
im = Image.fromarray(img)
image1 = im.resize((240, 240))
image1 = ImageTk.PhotoImage(image1)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


gim = Image.fromarray(gray_img)
image2 = gim.resize((240, 240))
image2 = ImageTk.PhotoImage(image2)


haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)
for (x, y, w, h) in faces_rect:
    outputimage=cv2.rectangle(inputimage, (x, y), (x + w, y + h), (255, 0, 0), 20)
#cv2.imshow('Detected faces', inputimage)
blue,green,red = cv2.split(outputimage)
outputimage = cv2.merge((red,green,blue))
oim=Image.fromarray(outputimage)
image3 = oim.resize((240, 240))
image3 = ImageTk.PhotoImage(image3)

label1 = Label(image=image1)
label2 = Label(image=image2)
label3=Label(image=image3)
label4=Label(root,text="Input Image")
label5=Label(root,text="Grayscale Image")
label6=Label(root,text="Output Image")


label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0,column=2)
label4.grid(row=1,column=0)
label5.grid(row=1,column=1)
label6.grid(row=1,column=2)

root.mainloop()