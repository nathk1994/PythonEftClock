from tkinter import *
import time
import arrow

root = Tk()
root.title ('Single Escape From Tarkov In-Game Clock')
root.geometry("400x300")
# root['bg']='black'
# root['background']='black'
# root.config(bg='black')
root.iconbitmap('C:/Users/nathk/Documents/GitHub/eftclock/favicon.ico')
bg = PhotoImage(file = "C:/Users/nathk/Documents/GitHub/eftclock/bgimg.png")
label = Label(root, image=bg, width = 400, height = 300)
#label.place(x=0, y=0)

# Create Canvas
canvas1 = Canvas( root, width = 400, height = 300)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

def g_time(check=False):
    time = arrow.utcnow().shift(hours=3)
    offset1 = 3600 * 3
    if check:
        offset1 += 3600 * 12
    
    offset2 = 3600 * 3
    if check:
        offset2 += 3600 * 12
    use1 = (arrow.get(offset1 + (arrow.utcnow().timestamp() * 7)).format("HH:mm:ss"))
    use2 = (arrow.get(offset2 + (arrow.utcnow().timestamp() * 7)).format("HH:mm:ss"))
    #print(arrow.get(offset + (arrow.utcnow().timestamp() * 7)).format("HH:mm:ss"))

    #canvas1.create_text(200, 250, root, text=use1)

    my_label.config(text=use1)
    my_label.place(x=75, y=100)
    #my_label2.config(text=use2)
    my_label.after(1, g_time)


def update():
    my_label.config(text="New Text")


my_label = Label(root, text="", font=("Helvetica", 48), fg="green", bg="black")
my_label.pack(pady=3)

# my_label2 = Label(root, text="", font=("Helvetica", 48), fg="green", bg="black")
# my_label2.pack(pady=20)

g_time()

#my_label.after(1000, update)

root.mainloop()