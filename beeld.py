import tkinter as tk
from PIL import Image,ImageTk
import glob
import sqlite3

folder_list = []
connection = sqlite3.connect('location') #sql bestand invoeren
cursor = connection.cursor()
cursor.execute("SELECT imageFilePath FROM image WHERE ")
results = cursor.fetchall()
# alle folders worden in een lijst gezet
for folder in results:
	folder_list.append(folder)

bookname = "test"



class gui:
	def __init__(self, mainwin, bookname):
		self.counter = 0
		self.mainwin = mainwin
		self.mainwin.title(bookname)
		self.mainwin.state('zoomed')

		self.mainwin.configure(bg='black')
		self.frame = tk.Frame(mainwin)
		self.frame.configure(bg='black')


		self.img = tk.Label(self.frame)

		self.frame.place(relheight=0.85, relwidth=0.9, relx=0.05, rely=0.08)
		self.img.pack()

		self.pic()



	def pic(self):

		self.pic_list = []
		for name in glob.glob(r'Slideshow/*'):  # folder ingeven waarvan je een slideshow wilt afspelen met ster na / voor alle bestanden
			val = name
			self.pic_list.append(val)


		if self.counter == len(self.pic_list) - 1:
			self.counter = 0
		else:
			self.counter += 1

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
		root.after(2000,self.pic)




root = tk.Tk()
myprog = gui(root)
root.mainloop()