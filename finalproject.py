from tkinter import *
import cv2 as v
from PIL import ImageTk,Image
def start():
    global op
    op=Tk()
    bg = ImageTk.PhotoImage(Image.open("img16.jpg"))
    bimg=ImageTk.PhotoImage(Image.open("img18.png"))
    label=Label(op,image=bg)
    label.pack()
    bu=Button(op,image=bimg,padx=10,pady=10,command=main)
    bu.pack()
    op.mainloop()
    
    
def facedetect():
    #a=v.imread("C:\\Users\\B.VENKATESWARA RAO\\Documents\\opencv\\k.png")
    #e=v.CascadeClassifier("C:\\Users\\B.VENKATESWARA RAO\\Documents\\opencv\\haarcascade_eye_tree_eyeglasses.xml")
    fc=v.CascadeClassifier("C:\\Users\\B.VENKATESWARA RAO\\Documents\\opencv\\haarcascade_frontalface_default.xml") 
    b=v.VideoCapture(0)
    while True:
        #fc=v.CascadeClassifier("C:\\Users\\B.VENKATESWARA RAO\\Documents\\opencv\\haarcascade_frontalface_default.xml")              
        a1,a=b.read()
        g=v.cvtColor(a,v.COLOR_BGR2GRAY)
        f=fc.detectMultiScale(g,1.1,5)
        
        for x,y,w,h in f:
            v.rectangle(a,(x,y),(x+w,y+h),(255,0,250),9)
        #v.imwrite("C:\\Users\\B.VENKATESWARA RAO\\Documents\\opencv\\haarcascade_frontalface_default.jpg",a)
            #this is for eye detcet remove quotes
            '''roig=g[y:y+h,x:x+w]
            roic=a[y:y+h,x:x+w]
            eye=e.detectMultiScale(roig)
            for ex,ey,eh,ew in eye:
                v.rectangle(roic,(ex,ey),(ex+ew,ey+eh),(255,250,250),1)'''
            
        v.imshow('l',a)
        if v.waitKey(1) & 0xFF==ord('q'):
            break
    b.release()
    v.destroyAllWindows()
        
def basicmotiondection():
    a=v.VideoCapture(0)
    r,b1=a.read()
    r,b2=a.read()
    while a.isOpened():
        diff=v.absdiff(b1,b2)
        gray=v.cvtColor(diff,v.COLOR_BGR2GRAY)
        blur=v.GaussianBlur(gray,(5,5),0)
        t,thresh=v.threshold(blur,20,255,v.THRESH_BINARY)
        dilated=v.dilate(thresh,None,iterations=3)
        contours,c=v.findContours(dilated,v.RETR_TREE,v.CHAIN_APPROX_SIMPLE)
        v.putText(b1,'Enter q to exit',(350,20),v.FONT_HERSHEY_SIMPLEX,1,(255,0,455),3)
        for contour in contours:
            (x,y,w,h)=v.boundingRect(contour)
            #motion value wii here
            if v.contourArea(contour)<10000:
                continue
            v.rectangle(b1,(x,y),(x+w,y+h),(0,255,0),2)
            v.putText(b1,"Status:{}".format('Movement'),(10,20),v.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
            
        #v.drawContours(b1,contours,-1,(0,255,0),2)
        v.imshow('feed',b1)
        b1=b2
        r,b2=a.read()
        if v.waitKey(1) & 0xFF==ord('q'):
            break
    v.destroyAllWindows()
        
def your_edge_dection():
    #a=v.imread("C:\\Users\\B.VENKATESWARA RAO\\Documents\\opencv\\k.png")
    b=v.VideoCapture(0)
    while True:
        r,a=b.read()
        g=v.cvtColor(a,v.COLOR_BGR2GRAY)
        c=v.Canny(g,60,85)
        v.imshow('a',c)
        if v.waitKey(1) & 0xFF==ord('q'):
            break
    v.destroyAllWindows()
def main():
    op.destroy()
    global s
    s=Tk()
    s.title('MY PROJECT')
    label=Label(s,text='WELCOME TO MY PROJECT')
    label.grid(row=1,column=0,columnspan=3)
    img=ImageTk.PhotoImage(Image.open('img21.png'))
    l=Label(image=img)
    l.grid(row=2,column=0,columnspan=3)
    b1=Button(s,text='click here!\n'+'Face Detection',fg='blue',padx=42,pady=20,command=facedetect)
    b1.grid(row=3,column=0)
    b2=Button(s,text='click here!\n'+'Basic Motion Detection',fg='blue',padx=15,pady=22,command=basicmotiondection)
    b2.grid(row=3,column=1)
    b3=Button(s,text='click here!\n'+'your Edge dection',fg='blue',padx=40,pady=15,command=your_edge_dection)
    b3.grid(row=4,column=0)
    b4=Button(s,text='click here!\n'+'To Exit  ',fg='blue',padx=50,pady=20,command=end)
    b4.grid(row=4,column=1)
    s.mainloop()
def end():
    global th
    s.destroy()
    th=Tk()
    timg=ImageTk.PhotoImage(Image.open("img15.png"))
    tlabel=Label(th,image=timg)
    tlabel.pack()
    def des():
        th.destroy()
    th.after(5000,des)
    th.mainloop()
    
start()


    
    

