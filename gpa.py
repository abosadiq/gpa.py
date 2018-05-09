'''
Thi program will calculate your Gpa for your classes you took in a semester. 
'''
name_of_classes = []
grade_for_each_class = []
list_of_units =[]
i = int(input("How many classes did you take this semester "))
j =0
while(j < i):
		x = 1
		while(x <= i):
			if(x %10 == 1):
				class_name = input("What is your {}st class?. ".format(x))
				grade_letter = input("whta was your grade letter for {}st class? ".format(x)).upper()
				unit = int(input("How many units is your {}st class? ".format(x)))

			elif(x%10 == 2):
				class_name = input("What is you {}nd class?. ".format(x))
				grade_letter = input("whta was your grade letter for {}nd class? ".format(x)).upper()
				unit = int(input("How many units is your {}nd class? ".format(x)))
			elif(x%10==3):
				class_name = input("What is you {}rd class?. ".format(x))
				grade_letter = input("whta was your grade letter for {}rd class? ".format(x)).upper()
				unit = int(input("How many units is your {}rd class? ".format(x)))
			else:
				class_name = input("What is you {}th class?. ".format(x))
				grade_letter = input("whta was your grade letter for {}th class? ".format(x)).upper()
				unit = int(input("How many units is your {}th class? ".format(x)))
			x = x+ 1
			j = j +1
			name_of_classes.append(class_name)
			grade_for_each_class.append(grade_letter)
			list_of_units.append(unit)

print("\nYour Classes are:\t\tYour gardes are:")
for x, y  in zip (name_of_classes, grade_for_each_class):
	print("\n",x,"\t\t\t\t",y)
	
def claculate():
	total = 0
	total_units_taken = 0
	total_units=0
	credit_units = 0
	count = 0
	for list_units in list_of_units:
		total_units_taken += list_units
	for grade in grade_for_each_class:
		if (grade == 'A'):
			total = total + (4.0 * list_of_units[count])
		elif(grade == 'A-'):
			total =   total + (3.7 * list_of_units[count])
				   
		elif(grade == 'B+'):
			total = total + (3.3 * list_of_units[count])
			
		elif(grade == 'B'):
			total= total + (3.0 * list_of_units[count])
			
		elif(grade == 'B-'):
			total = total + (2.7 * list_of_units[count])
		
		elif (grade == 'C+'):
			total = total + (2.3 * list_of_units[count])
			
		elif (grade == 'C'):
			total = total + (2.0 * list_of_units[count])
			
		elif (grade == 'C-'):
			total = total + (1.7 * list_of_units[count])
		elif(grade == 'D+'):
			total = total + (1.3 * list_of_units[count])
		elif(grade == 'D'):
			total = total + (1.0 * list_of_units[count])
		elif(grade == 'D-'):
			total = total + (0.7 * list_of_units[count])
		elif(grade == 'F'):
			total += (0.0 * list_of_units[count])
		count += 1
	gpa = (total /total_units_taken)
	print("\n================Calculation========================\n")
	print("Total points earned: {} points ".format(total))
	print("Units taken this Semster are {} units".format(total_units_taken))
	print("Your Gpa is {:0.3f}".format(gpa,2))	       	
claculate()
