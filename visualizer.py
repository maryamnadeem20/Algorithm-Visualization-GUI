import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from sortVisualise import Visualize

root = tk.Tk()    
root.title("ALGORITHMS VISUALIZER")

image = Image.open("bg.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.image = photo
label.grid(row=2, column=0)

size=tk.Label(label, text="ARRAY SIZE: ", font="Helvetica 14 bold")
size.place(relx=0.15, rely=0.2)
entrysize=tk.Entry(label, font="Helvetica 14")
entrysize.place(relx=0.45, rely=0.2)
dsButton=tk.Button(label, text="CHOOSE DATA SET", font="Helvetica 11 bold", command= lambda : chooseDataSet())
dsButton.place(height=40, width=180, rely=0.55, relx=0.13)
arrButton=tk.Button(label, text="CHOOSE ALGORITHM", font="Helvetica 11 bold", command=lambda : chooseAlgo())
arrButton.place(height=40, width=180, rely=0.55, relx=0.53)

var=tk.StringVar()
# var.set("1")
arr=tk.StringVar()
# arr.set("a")


go2d=tk.Button(label, text="2D VISUALIZATION", font="Helvetica 12 bold", command=lambda : show(entrysize.get(), var.get(), arr.get(), "2d"))
go2d.place(height=40, width=170, rely=0.75, relx=0.35)

go3d=tk.Button(label, text="3D VISUALIZATION", font="Helvetica 12 bold", command=lambda : show(entrysize.get(), var.get(), arr.get(), "3d"))
go3d.place(height=40, width=170, rely=0.85, relx=0.35)

def chooseDataSet():
	dswin=tk.Toplevel()
	dswin.geometry("300x200")
	dswin.title("DATA SETS")
	dswin.configure(bg="#892534")
	var.set("1")
	r1 = tk.Radiobutton(dswin, text="Random Data Set", variable=var, value="1")                
	r1.place(relx=0.15, rely=0.2)
	r2 = tk.Radiobutton(dswin, text="Array with Few Unique Elements", variable=var, value="2")                 
	r2.place(relx=0.15, rely=0.4)
	r3 = tk.Radiobutton(dswin, text="Reversed Sorted Array", variable=var, value="3")               
	r3.place(relx=0.15, rely=0.6)
	next=tk.Button(dswin, text="SET", font="Helvetica 10 bold", command=lambda : var.get())
	next.place(rely=0.8, relx=0.5)
	next.bind("<Button-1>", lambda x: dswin.withdraw())

def chooseAlgo():
	algo=tk.Toplevel()
	algo.geometry("300x300")
	algo.title("ALGORITHMS")
	algo.configure(bg="#892534")
	arr.set("a")
	s1 = tk.Radiobutton(algo, text="Selection Sort", variable=arr, value="a")                
	s1.place(relx=0.15, rely=0.15)
	s2 = tk.Radiobutton(algo, text="Bubble Sort", variable=arr, value="b")                 
	s2.place(relx=0.15, rely=0.3)
	s3 = tk.Radiobutton(algo, text="Merge Sort", variable=arr, value="c")               
	s3.place(relx=0.15, rely=0.45)
	s4 = tk.Radiobutton(algo, text="Insertion Sort", variable=arr, value="d")               
	s4.place(relx=0.15, rely=0.6)
	s5 = tk.Radiobutton(algo, text="Quick Sort", variable=arr, value="e")               
	s5.place(relx=0.15, rely=0.75)
	next=tk.Button(algo, text="SET", font="Helvetica 10 bold", command=lambda : arr.get())
	next.place(rely=0.85, relx=0.5)
	next.bind("<Button-1>", lambda x: algo.withdraw())



def show(n, dataSet, algo, mode):
	try:
		if n.isdecimal()==False or dataSet=='' or algo=='':
			messagebox.showerror("Error", "Try Again")
		n=int(n)
		v=Visualize(n, dataSet, algo)
		if mode=="2d":
			v.visual2d()
		elif mode=="3d":
			v.visual3d()
	except:
		pass



root.mainloop()



