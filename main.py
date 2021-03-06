from _ast import Lambda
from pynput import keyboard
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('BJ Image Viewer')
root.iconbitmap('c:/Users/szote/PycharmProjects/pythonProject55/icon55.ico')


image1 = ImageTk.PhotoImage(Image.open("c:/Users/szote/PycharmProjects/pythonProject55/img1.png"))
image2 = ImageTk.PhotoImage(Image.open("c:/Users/szote/PycharmProjects/pythonProject55/img2.jpg"))
image3 = ImageTk.PhotoImage(Image.open("c:/Users/szote/PycharmProjects/pythonProject55/img3.jpg"))
image4 = ImageTk.PhotoImage(Image.open("c:/Users/szote/PycharmProjects/pythonProject55/img4.jpg"))
image5 = ImageTk.PhotoImage(Image.open("c:/Users/szote/PycharmProjects/pythonProject55/img5.png"))

counter = 0


def on_press(key):
    global counter
    global my_label
    if key == keyboard.Key.right:
        print(">")
        counter = counter + 1
        if counter < 0:
            counter=4
        if counter > 4:
            counter=0
        my_label.grid_forget()
        my_label = Label(image=image_list[counter])
        my_label.grid(row=0, column=0, columnspan=3)
    if key == keyboard.Key.left:
        print("<")
        counter = counter - 1
        if counter < 0:
            counter=4
        if counter > 4:
            counter=0
        my_label.grid_forget()
        my_label = Label(image=image_list[counter])
        my_label.grid(row=0, column=0, columnspan=4)


def back():
    global counter
    global my_label
    counter = counter - 1
    if counter < 0:
        counter = 4
    if counter > 4:
        counter = 0
    my_label.grid_forget()
    my_label = Label(image=image_list[counter])
    my_label.grid(row=0, column=0, columnspan=4)


def forward():
    global counter
    global my_label
    counter = counter + 1
    if counter < 0:
        counter = 4
    if counter > 4:
        counter = 0
    my_label.grid_forget()
    my_label = Label(image=image_list[counter])
    my_label.grid(row=0, column=0, columnspan=4)


def openpic():
    global my_label
    global imageopened
    root.filename = filedialog.askopenfilename(initialdir="c:/Users/szote/PycharmProjects/pythonProject55/", title="Select A File", filetypes=(("png files", "*.png"),("all files","*.*")))
    imageopened = ImageTk.PhotoImage(Image.open(root.filename))
    my_label.grid_forget()
    my_label = Label(image=imageopened)
    my_label.grid(row=0, column=0, columnspan=4)


image_list = [image1, image2, image3, image4, image5]

listener = keyboard.Listener(on_press=on_press)
listener.start()

my_label = Label(image=image_list[counter])
button_back = Button(root, text="Back", command=lambda: back())
button_forward = Button(root, text="Next", command=lambda: forward())
button_exit = Button(root, text="Exit", command=root.quit)
button_open = Button(root, text="Open", command=lambda: openpic())
my_label.grid(row=0, column=0, columnspan=4)
button_back.grid(row=1, column=1)
button_exit.grid(row=1, column=0)
button_forward.grid(row=1, column=2)
button_open.grid(row=1, column=3)


root.mainloop()


