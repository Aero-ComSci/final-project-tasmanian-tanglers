import random
from tkinter import *
import os

root = Tk()
root.title("Summertip")
root.geometry('400x500')  
lbl = Label(root, text="What activity would you like?")
lbl.grid(column=2, row=0)
select = StringVar()
select.set("Remove")
drop = OptionMenu(root, select, *[""], command=lambda choice: clear(choice))
drop.grid(column=2, row=7)
adj = [
    "Exciting", "Challenging", "Fun", "Creative", "Relaxing", "Adventurous", "Mysterious", "Energetic",
    "Thrilling", "Inspiring", "Refreshing", "Engaging", "Curious", "Daring", "Lively", "Vibrant",
    "Joyful", "Dynamic", "Spontaneous", "Stimulating", "Hilarious", "Playful", "Unique", "Motivating"
]
places = [
    "at 3 am in the forest", "at sunrise downtown", "in the afternoon by the seaside",
    "at midnight on top of a mountain", "in the evening inside a cozy café", "at noon at a bustling market"
]
activities = []
canvas = Canvas(root, width=300, height=300)  
canvas.grid(column=2, row=3, sticky="nsew")

scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.grid(column=3, row=3, sticky="ns")
canvas.configure(yscrollcommand=scrollbar.set)

frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")
frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

def convert():
    for widget in frame.winfo_children():
        widget.destroy()
    
    for i, item in enumerate(activities):
        if item:
            button = Button(frame, text=item, bg="red", width=40, command=lambda k=item, g=i: switch(k, g))  
            button.grid(row=i, column=0, pady=5)

def switch(name, row):
    for widget in frame.winfo_children():
        if isinstance(widget, Button):
            if widget.cget("text") == name:
                if widget.grid_info().get("row") == row:
                    widget.configure(bg="green" if widget.cget("bg") == "red" else "red")

def clear(choice):
    global activities
    try:
        activities.remove(choice)
    except ValueError:
        lbl.configure(fg="red")
    convert()
    dlear()

def dlear():
    drop["menu"].delete(0, "end")
    options = [item for item in activities if item]
    select.set("Remove")

    for name in options:
        drop["menu"].add_command(label=name, command=lambda n=name: clear(n))

    drop.grid(column=2, row=7) if options else drop.grid_forget()

def reset():
    lbl.configure(text="Add any activities you want", fg="black")
    
    global entry
    entry = Entry(root, width=30)
    entry.grid(column=2, row=1)

    Button(root, text="Input", command=s7).grid(column=2, row=2)

    dlear()
    convert()

def save_activities():
    with open("summeractivities.txt", "w") as file:
        for activity in activities:
            file.write(activity +"\n")
        file.close()

savebutton = Button(root, text="Save", command=save_activities)
savebutton.grid_forget()

def loading():
    if os.path.exists("summeractivities.txt"):
        with open("summeractivities.txt", 'r') as file:
            for line in file:
                activities.append(line.strip())
            convert()
#was stuck on how to load the file, .strip() and convert() written by AI
loadbutton = Button(root, text="Load", command=loading)

def s7():
    global entry, activities, adj, places
    if entry.get():
        randadj = random.choice(adj)
        randplace = random.choice(places)
        actadj = f"{randadj} {entry.get()} {randplace}"
        activities.append(actadj)
        if activities:
            savebutton.grid(column=2, row=8)
            loadbutton.grid(column=2, row=9)
        reset()

reset()
root.mainloop()
