[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DpCY8B3G)


Evan.S:
![image](https://github.com/user-attachments/assets/7f3bdef5-768b-4fa6-a77d-ed228a6a40ca)
This program is for travelers who wish to have a convenient way to track activities and check them off, once they completed them
The program asks the user to input activities, and then displays them.  Clicking on an activity will change its color.  You also individually remove any activity you do not want.  All activities are accessed via a scrollable interface.



```python def dlear():
    drop["menu"].delete(0, "end")
    options = [item for item in activities if item]
    select.set("Remove")
    
    for i,name in enumerate(options):
        drop["menu"].add_command(label=name, command=lambda n=name, z=i: clear(n,z)) ```
```python def switch(name,row):
    global color
    for widget in frame.winfo_children():
        if isinstance(widget, Button):  
            if widget.cget("text") == name:
                if widget.grid_info().get("row")==row:
                    color[row] = "g" if widget.cget("bg") == "red" else "r"
                    widget.configure(bg="green" if widget.cget("bg") == "red" else "red")  ```
```python def convert():
    for widget in frame.winfo_children():
        widget.destroy() 
    
    for i, item in enumerate(activities):
        if item:
            button = Button(frame, text=item, bg="red" if color[i] == "r" else "green", width=20, command=lambda k=item, g=i: switch(k,g))
            button.grid(row=i, column=0, pady=5) ```

Sergey D:
![image](https://github.com/user-attachments/assets/4e89b604-73fe-43cc-8a39-e6df24558b34)
This program is for bored people who want to not only track their summer activities and check them off, but to spice up their boring activities by adding adjectives and places where they can do it. This program adds adjectives and places to the activities inputted by the user. You can also save the code as a .txt file and load other summeractivities.txt files into the program. 

```python codecodecode ```
adj = [
    "Exciting", "Challenging", "Fun", "Creative", "Relaxing", "Adventurous", "Mysterious", "Energetic",
    "Thrilling", "Inspiring", "Refreshing", "Engaging", "Curious", "Daring", "Lively", "Vibrant",
    "Joyful", "Dynamic", "Spontaneous", "Stimulating", "Hilarious", "Playful", "Unique", "Motivating"
]
places = [
    "at 3 am in the forest", "at sunrise downtown", "in the afternoon by the seaside",
    "at midnight on top of a mountain", "in the evening inside a cozy café", "at noon at a bustling market"
]

def convert():
    for widget in frame.winfo_children():
        widget.destroy()
    
    for i, item in enumerate(activities):
        if item:
            button = Button(frame, text=item, bg="red", width=40, command=lambda k=item, g=i: switch(k, g))
            button.grid(row=i, column=0, pady=5)

def loading():
    if os.path.exists("summeractivities.txt"):
        with open("summeractivities.txt", 'r') as file:
            for line in file:
                activities.append(line.strip())
            convert()
def save_activities():
    with open("summeractivities.txt", "w") as file:
        for activity in activities:
            file.write(activity +"\n")

def switch(name, row):
    for widget in frame.winfo_children():
        if isinstance(widget, Button):
            if widget.cget("text") == name:
                if widget.grid_info().get("row") == row:
                    widget.configure(bg="green" if widget.cget("bg") == "red" else "red")

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
