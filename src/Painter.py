import tkinter as tk
import message

class Scribble:

    def on_pressed(self, event):
        self.sx = event.x
        self.sy = event.y
        self.canvas.create_oval(self.sx, self.sy, event.x, event.y,
                                outline = self.color.get(),
                                width = self.width.get())

    def on_dragged(self, event):
        self.canvas.create_line(self.sx, self.sy, event.x, event.y,
                                fill = self.color.get(),
                                width = self.width.get())
        self.sx = event.x
        self.sy = event.y

    def create_window(self):
        window = tk.Tk()
        window.title('Painterz')

        self.canvas = tk.Canvas(window, bg = "white", width = 600, height = 300)
        self.canvas.pack()

        menu = tk.Menu(window)
        window.config(menu=menu)
        filemenu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=message.callback)
        filemenu.add_command(label="Open...", command=message.callback)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=message.callback)

        helpmenu = tk.Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=message.callback)

        quit_button = tk.Button(window, text = "終了", command = window.quit)
        quit_button.pack(side = tk.RIGHT)

        self.canvas.bind("<ButtonPress-1>", self.on_pressed)
        self.canvas.bind("<B1-Motion>", self.on_dragged)

        COLORS = ["red", "green", "blue", "#FF00FF", "black"]
        self.color = tk.StringVar()                    
        self.color.set(COLORS[1])                             
        b = tk.OptionMenu(window, self.color, *COLORS) 
        b.pack(side = tk.LEFT)

        self.width = tk.Scale(window, from_ = 1, to = 15, orient = tk.HORIZONTAL) 
        self.width.set(5)                                       
        self.width.pack(side = tk.LEFT)
        
        return window;
    
    def __init__(self):
        self.window = self.create_window();
            
    def run(self):
        self.window.mainloop()
 
Scribble().run()