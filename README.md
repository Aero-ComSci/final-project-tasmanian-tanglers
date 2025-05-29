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
