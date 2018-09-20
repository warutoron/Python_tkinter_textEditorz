import tkinter as tk

class Scribble:

    def create_window(self):
        window = tk.Tk()
        window.title('Painterz')

        self.text_widget = tk.Text(window)
        self.text_widget.pack()

        menu = tk.Menu(window)
        window.config(menu=menu)
        filemenu = tk.Menu(menu)
        
        return window;
    
    def __init__(self):
        self.window = self.create_window();
            
    def run(self):
        self.window.mainloop()
 
Scribble().run()