import tkinter as tk
import subprocess

root = tk.Tk()
root.title("My First Tkinter Window")
root.geometry("500x150+0+900") 
root.configure(bg="White")
root.overrideredirect(True)

app1 = r"C:/Windows/System32/notepad.exe"
app2 = r"C:/Windows/System32/mspaint.exe"
app3= r"C:\Program Files (x86)\Windows Media Player\wmplayer.exe"                  

photo = tk.PhotoImage(file="icons/notepad icon.png")
photo2 = tk.PhotoImage(file="icons/paint icon.png")
photo3 = tk.PhotoImage(file="icons/media player icon.png") 

def open_app_one():
    root.destroy()
    subprocess.run([app1])
    
def open_app_two():
    root.destroy()
    subprocess.run([app2])
    
def open_app_three():
    root.destroy()
    subprocess.run([app3])

label = tk.Label(root, text="Simple App Menu", font=("Verdana"), bg="White", fg="Black")
label.pack(pady=20)


button_container = tk.Frame(root, bg="White")
button_container.pack(pady=10)


button1 = tk.Button(button_container, image=photo, command=open_app_one)
button1.grid(row=0, column=0, padx=5)

button2 = tk.Button(button_container, image=photo2, command=open_app_two)
button2.grid(row=0, column=1, padx=5)

button3 = tk.Button(button_container, image=photo3, command=open_app_three)
button3.grid(row=0, column=2, padx=5)

buttonexit = tk.Button(button_container, text="Exit", command=root.destroy)
buttonexit.grid(row=0, column=3, padx=15,)

root.mainloop()
