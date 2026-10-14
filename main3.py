import tkinter as tk
import time
from PIL import Image,ImageTk

# main window
root = tk.Tk()
root.title("Photo Sileshow Album") # It will Give The Title To THe page
root.geometry("900x900")# geometry  method is used to give the size to the page
#List of Images 
image_path =[
     r"c:\Users\hp\OneDrive\Desktop\photo\image1.jpg",
     r"c:\Users\hp\OneDrive\Desktop\photo\image2.jpg",
     r"c:\Users\hp\OneDrive\Desktop\photo\image3.jpg",
     r"c:\Users\hp\OneDrive\Desktop\photo\image4.jpg",
     r"c:\Users\hp\OneDrive\Desktop\photo\image5.jpg"
]
image_size =(700,700)
image =[]
for path in image_path:
    img= Image.open(path)
    img= img.resize(image_size)
    image.append(img)

#Converting IPL Images into Tkinter friendly Image 
final_images=[]
for img in image:
    photo=ImageTk.PhotoImage(img)
    final_images.append(photo) 
#label vist to keep photo 
image_lable =tk.Label(root)#this method is used to add lable to image
image_lable.pack(pady=30)   #whenever we used button or label we should use pack method

#Sliding function
def start_slideshow():
    for photo in final_images:
        image_lable.config(image=photo)
        image_lable.image=photo
        root.update()
        time.sleep(2)
#button 
play_button =tk.Button(
    root,
    text =("Play the SildeShow"),
    font=("Arial",17),
    command=start_slideshow,
    background="pink"
) 
play_button.pack (pady=30)     

root.mainloop()
