#murag final nani
#libog man
import fileinput
import sys

print "(already .txt)"
fname = raw_input ("Filename: ") + ".txt"
fop = open(fname,'a+')
fop.close()
	
print "___________________________________________________________________________\n"
#print ")"
print "\tHELLO! This program will search through ID no. from your file\n\tthen you can add, delete and update if you want to change something"
print "\n\t Type -> [print] if you want to see what's inside the file"
print "___________________________________________________________________________"

def add(student):

	

		idno = raw_input("Enter your ID no: ")+ " "
		name = raw_input("Enter your Name: ")+ " "
		course = raw_input("Enter your Course: ")+ " "
		return idno + name + course 

def printing():
	fl=open(fname,'r')
	for line in fl:
		print(line)
	fl.close

def searching(target):
	file = open(f_name,'r')
	for line in file:
		curl = line.split()
		if target == curl[0]:
			print("\n -->: "+line)
	file.close()	
while True:





	option = raw_input("\tSelect -> add, delete, update, search and print: ")
	print "\n"
	if( option == "add"):
		dfile = open(fname,"a+")
		while True:
			print "[ADD]"
			student = ""
			dfile.write(add(student)+ "\n")
			npt = raw_input("you want to add more? ")
			if npt == "no":
				break
		dfile.close()

	elif(option == "delete"):
		while True:

			f = open(fname)
			print "[DELETE]"
			output = []
			dlet = raw_input("enter the ID no.: ")
			for line in f:
				cur=line.split()
				if  dlet == cur[0]:
					print("\n"+line + "\n[Successfully deleted]")
					
				elif not dlet == cur[0]:
					output.append(line)
			f.close()
			f = open(fname,'w')
			f.writelines(output)
			f.close()
			n = raw_input("you want to delete more? ")
			if n == "no":
				break


	elif(option == "update"):
		print "[UPDATE]"
		search = raw_input("search ID no.  ")

		idno = raw_input("change ID no: ")+ " "
		name = raw_input("change Name: ")+ " "
		course = raw_input("Shift: ")+ " "

		replace = idno + name + course + '\n'

		
		for line in fileinput.FileInput(fname,inplace=1):
			
    			if search in line:
    				stored = ""
    				stored = line
       		 		line=line.replace(line,replace)

    			print line,

    		print '\n'+ stored + "\nis successfully updated to\n" + line

	elif(option == "print"):
		printing()

	elif(option == "search"):
		searchID = raw_input("search IDno : ")
		searching(searchID)

	nt = raw_input("do you want to make some changes? or view the changes(print)? \n\t type [yes] or [no]\n\t input: ")
	if nt == "no":
		break

#else	
			
