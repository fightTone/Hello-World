import sqlite3
print "already in '.db' "
db_name = raw_input("Enter your database name:")+'.db'

conn = sqlite3.connect(db_name)
quer = conn.cursor()

def create_table():
	quer.execute('''CREATE TABLE IF NOT EXISTS student
	(idno TEXT, name TEXT, course TEXT)''')
	
	print "table is successfully created"

def add(idno,name,course):
	quer.execute('''INSERT INTO student(idno,name,course)
	VALUES(?,?,?)''',(idno,name,course))
	
	conn.commit()

def printing():
	quer.execute('SELECT * FROM student')
	for row in quer.fetchall():
		print(row)


	#for row in quer.fetchall():
  	#	 print "ID = ", row[0]
 	#	 print "NAME = ", row[1]
  	#	 print "ADDRESS = ", row[2],"\n"

def search():

	target = raw_input("input ID: ")
	quer.execute("SELECT * FROM student WHERE idno = ?", (target,))
	for row in quer.fetchall():
		print(row)
def deleting():
	dlet = raw_input("enter ID: ")
	
	quer.execute("DELETE from student where idno = ?", (dlet,))
	conn.commit()

def update():
	entr_ID = raw_input("Enter ID: ")
	choice =raw_input("what to update? \n\t>>Name\n\t>>Course\n>>>>")
	if(choice == "Name"):
		change = raw_input("enter changes: ")
		conn.execute("UPDATE student set name = ? where idno = ?", (change, entr_ID,))
		conn.commit()
	elif(choice == "Course"):
		changes = raw_input("enter changes: ")
		conn.execute("UPDATE student set course = ? where idno = ?", (changes,entr_ID))
		conn.commit()
def sorting():
	choice = raw_input("Ascending or Descending: \n>>>")
	if choice == 'Ascending':
		quer.execute("SELECT * FROM student ORDER BY name ASC")
		for row in quer.fetchall():
			print(row)
	elif choice == 'Descending':
		quer.execute("SELECT * FROM student ORDER BY name DESC")
		for row in quer.fetchall():
			print(row)




create_table()

printing()
while(True):
	print "\n\t\t<<<ADD>>>"
	idno = raw_input("Enter your ID no: ")
	name = raw_input("Enter your Name: ")
	course = raw_input("Enter your Course: ")
	add(idno,name,course)

	stop = raw_input("again? ")
	if stop == 'no':
		break


while (True):
	print"\n\t\t<<<SEARCH>>>"
	search()
	end = raw_input("again? ")
	if end == 'no':
		break

while (True):
	print "\n\t\t<<<DELETE>>>"
	deleting()
	fin =raw_input("again? ")
	if fin == 'no':
		break

while (True):
	print "\n\t\t<<<UPDATE>>>"
	update()
	last = raw_input("again? ")
	if last == 'no':
		break

print "\n\t\t<<<SORTING>>>"
sorting()


quer.close()
conn.close()		
