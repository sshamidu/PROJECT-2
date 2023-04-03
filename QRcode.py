from tkinter import *
import qrcode
from tkinter import filedialog, colorchooser
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("QR Code Generator")
root.geometry('500x650')

# global variables for storing the colors
bg_color = 'white'
fg_color = 'black'
button_bg_color = 'lightgrey'
button_fg_color = 'black'

def create_code():
    global get_image
    input_path = filedialog.asksaveasfilename(title="Save Image", filetypes=(("PNG File", ".png"),("All Files","*.*")))
    
    # check if entry is not empty and is a valid URL
    if my_entry.get() and (my_entry.get().startswith("http://") or my_entry.get().startswith("https://")):
        if input_path:
            if input_path.endswith(".png"):
                get_code = qrcode.QRCode(version=None, box_size=10, border=4)
                get_code.add_data(my_entry.get())
                get_code.make(fit=True)
                img = get_code.make_image(fill_color=fg_color, back_color=bg_color)
                img.save(input_path)
            else:
                input_path = f'{input_path}.png'
                get_code = qrcode.QRCode(version=None, box_size=10, border=4)
                get_code.add_data(my_entry.get())
                get_code.make(fit=True)
                img = get_code.make_image(fill_color=fg_color, back_color=bg_color)
                img.save(input_path)

            get_image = ImageTk.PhotoImage(Image.open(input_path))
            my_label.config(image=get_image)
        else:
            messagebox.showerror("Invalid input", "Please select a file path to save the QR code image.")
    else:
        messagebox.showerror("Invalid URL", "Please enter a valid URL starting with http:// or https://")

def clear_all():
    my_entry.delete(0, "end")
    my_label.config(image=None)

def choose_bg_color():
    global bg_color
    color = colorchooser.askcolor(title="Choose background color")
    bg_color = color[1]

def choose_fg_color():
    global fg_color
    color = colorchooser.askcolor(title="Choose foreground color")
    fg_color = color[1]


# create GUI
my_entry = Entry(root, font=("helvetica", 18))
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

my_button = Button(button_frame, text="Create QR Code", command=create_code, bg=button_bg_color, fg=button_fg_color)
my_button.pack(side=LEFT, padx=10)

my_button2 = Button(button_frame, text="Clear", command=clear_all, bg=button_bg_color, fg=button_fg_color)
my_button2.pack(side=LEFT, padx=10)

# add button to choose background color
bg_color_button = Button(root, text="Choose background color", command=choose_bg_color, bg=button_bg_color, fg=button_fg_color)
bg_color_button.pack(side=TOP, padx=10, pady=10)

# add button to choose foreground color
fg_color_button = Button(root, text="Choose foreground color", command=choose_fg_color, bg=button_bg_color, fg=button_fg_color)
fg_color_button.pack(side=TOP, padx=10, pady=10)

my_label = Label(root, text=None)
my_label.pack(pady=20)

root.mainloop()
