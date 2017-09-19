import fileinput
from Tkinter import *

root = Tk()
root.title("First GUI Project")
root.geometry("365x450+0+0")

heading = Label(root, text="HELLO!!!", font=("arial",40,"bold"), fg="steelblue").pack()

file_naming= Label(root,text="Enter filename: ").place(x=10,y=110)

file = StringVar()
entry_box = Entry(root, textvariable=file,width=25, bg="lightblue").place(x=100,y=110)








def open_file():

	def go_to_add():

		def adding():
			st_ID = str(ID_num.get())+" "
			st_name = str(name.get())+" "
			st_course = str(Crs.get())+" "
			f = open(str(file.get()),'a+')
			f.write(st_ID + st_name + st_course + '\n')


			f.close()
			ID_box.delete(0, END)
			name_box.delete(0, END)
			course_box.delete(0, END)
			fop=open(filename,'a+')
			Lb1 = Listbox(root,width=57, height=15,bg="lightblue")

			for line in fop:
				Lb1.insert(END,line)


			Lb1.place(x=9,y=200)

			fop.close()



		new_win=Toplevel()
		new_win.title("Adding Window")
		new_win.geometry("294x70")
		ID_label= Label(new_win,text="ID num: ").place(x=3,y=5)
		name_label= Label(new_win,text="Name: ").place(x=3,y=25)
		course_label= Label(new_win,text="Course: ").place(x=3,y=45)
		
		ID_num = StringVar(None)
		ID_box= Entry(new_win,textvariable=ID_num,width=25,bg="pink")
		ID_box.place(x=50,y=5)
		name = StringVar(None)
		name_box= Entry(new_win,textvariable=name,width=25,bg="pink")
		name_box.place(x=50,y=25)
		Crs = StringVar(None)
		course_box= Entry(new_win,textvariable=Crs,width=25,bg="pink")
		course_box.place(x=50,y=45)
		add_but = Button(new_win,text="Add",width=10, height=1,command=adding).place(x=207,y=37)

		

	def go_to_delete():


		def delete_dis():

			st_ID = str(ID_num.get())
			file_op = str(file.get())
			
			f = open(file_op)
			output = []
			for line in f:
				curl = line.split()
				if not st_ID == curl[0]:
					output.append(line)
					disp = Label(del_win, text=st_ID + " not existed\n try another ID", font=("arial",10,"bold"), fg="red").place(x=3,y=30)

				if st_ID == curl[0]:
					disp = Label(del_win, text=line + "\nSuccessfully Deleted", font=("arial",10,"bold"), fg="steelblue").place(x=3,y=30)

			f.close()
			f=open(file_op,'w')
			f.writelines(output)
			f.close()
			ID_box.delete(0,END)
			
			fop=open(filename,'a+')
			Lb1 = Listbox(root,width=57, height=15,bg="lightblue")

			for line in fop:
				Lb1.insert(END,line)


			Lb1.place(x=9,y=200)

			fop.close()

		del_win = Toplevel()
		del_win.title("Delete Window")
		del_win.geometry("294x85")
		ID_label = Label(del_win,text="ID num: ").place(x=3,y=5)
		ID_num = StringVar(None)
		ID_box= Entry(del_win,textvariable=ID_num,width=25,bg="pink")
		ID_box.place(x=50,y=5)
		del_but = Button(del_win,text="Delete",width=10, height=1,command= delete_dis).place(x=207,y=3)


	def go_to_update():

		def update_dis():

			def update_thing():
				stud_ID = str(ID_num.get())+" "
				stud_name = str(name.get())+" "
				stud_course = str(Crs.get())+" "
				replace = stud_ID + stud_name + stud_course + '\n'
				for line in fileinput.FileInput(str(file.get()),inplace=1):

    					if st_ID in line:
    				
       		 					line=line.replace(line,replace)

    					print line,
    					disp = Label(upd_win, text="Successfully Updated", font=("arial",12,"bold"), fg="red").place(x=3,y=120)
				ID_box.delete(0,END)
				name_box.delete(0, END)
				course_box.delete(0, END)
				fop=open(filename,'a+')
				Lb1 = Listbox(root,width=57, height=15,bg="lightblue")

				for line in fop:
					Lb1.insert(END,line)


				Lb1.place(x=9,y=200)

				fop.close()

			st_ID = str(sID_num.get())
			file_op = str(file.get())
			f = open(file_op,'r')
			for line in f:
				curl = line.split()
				if curl [0] == st_ID:
					Disp = Label(upd_win,text= line,font="arial 9 bold").place(x=5,y=25)
					
					ID_label= Label(upd_win,text="ID num: ").place(x=3,y=50)
					name_label= Label(upd_win,text="Name: ").place(x=3,y=70)
					course_label= Label(upd_win,text="Course: ").place(x=3,y=90)

					ID_num = StringVar(None)
					ID_box= Entry(upd_win,textvariable=ID_num,width=25,bg="pink")
					ID_box.place(x=60,y=50)
					name = StringVar(None)
					name_box= Entry(upd_win,textvariable=name,width=25,bg="pink")
					name_box.place(x=60,y=70)
					Crs = StringVar(None)
					course_box= Entry(upd_win,textvariable=Crs,width=25,bg="pink")
					course_box.place(x=60,y=90)
					add_but = Button(upd_win,text="Update",width=10, height=1,command=update_thing).place(x=215,y=83)
			f.close()
			sID_box.delete(0,END)


		

		upd_win = Toplevel()
		upd_win.title("Update Window")
		upd_win.geometry("299x150")
		ID_label = Label(upd_win,text="Search ID: ").place(x=3,y=5)
		sID_num = StringVar(None)
		sID_box= Entry(upd_win,textvariable=sID_num,width=25,bg="pink")
		sID_box.place(x=60,y=5)
		upd_but = Button(upd_win,text="Search",width=10, height=1,command= update_dis).place(x=215,y=3)


	filename = str(file.get())
	fop=open(filename,'a+')
	display = Label(root, text="you've successfully open the File", font=("arial",12,"bold"), fg="red").place(x=5,y=130)
	print "you've successfuly open " + filename
	
	
	Lb1 = Listbox(root,width=57, height=15,bg="lightblue")

	for line in fop:
		Lb1.insert(END,line)


	Lb1.place(x=9,y=200)

	fop.close()
	add = Button(root,text="Add",width=15, height=2,command=go_to_add).place(x=5,y=155)
	delete = Button(root,text="Delete",width=15, height=2,command=go_to_delete).place(x= 125,y=155)
	update = Button(root,text="Update",width=15, height=2,command=go_to_update).place(x=245,y=155)





work = Button(root,text="Enter",width=10, height=1,command=open_file).place(x=270, y=105)






root.mainloop()