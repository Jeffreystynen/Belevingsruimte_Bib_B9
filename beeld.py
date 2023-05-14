import tkinter as tk
from PIL import Image, ImageTk


def window(lijst):

    order = lijst[0]
    timing_list = lijst[1]
    path_list = lijst[2]
    
                
    class GUI():

        def __init__(self, mainwin, bookname):
            self.counter = 0
            self.mainwin = mainwin
            self.mainwin.title(bookname)
            self.mainwin.attributes('-fullscreen', True)
            self.mainwin.configure(bg='black')
            self.frame = tk.Frame(mainwin)
            self.frame.configure(bg='black')
            self.img = tk.Label(self.frame)
            self.frame.place(relheight=0.85, relwidth=0.9, relx=0.05, rely=0.08)
            self.img.pack()
            self.pic()

        def pic(self):
            self.pic_list = []
            for name in path_list:
                val = name
                self.pic_list.append(val)

            if self.counter != len(self.pic_list) - 1:
                self.counter += 1
            else:
                self.mainwin.destroy()  # close the window when slideshow is finished

            self.file = self.pic_list[self.counter]
            self.load = Image.open(self.file)
            self.pic_width = self.load.size[0]
            self.pic_height = self.load.size[1]
            self.real_aspect = self.pic_width / self.pic_height
            self.cal_width = int(self.real_aspect * 800)
            self.load2 = self.load.resize((self.cal_width, 800))
            self.render = ImageTk.PhotoImage(self.load2)
            self.img.config(image=self.render)
            self.img.image = self.render
            for timing in timing_list:
                root.after(timing, self.pic)

            
    root = tk.Tk()
    myprog = GUI(root, 'My Book')
    root.mainloop()