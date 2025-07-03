"if"
""""
if condition:
    statements
"""
#write a python program to find whether a number is positive or not
#num = int(input("enter a number:"))
#if num > 0:
        #print("the number is positive", num)


#write a pyhton program to find biggest of two numbers
##a = int(input("enter a number: "))
#b = int(input("enter a number: "))
#if a>b:
 #       print("A is greater:", a)
#else:
 #       print("B is greater:", b)


#Accept the percentage from the user and display the grade according to the following criteria 
"""
BelowD - 25
25 to 45 -- C
45 to 50 --b
50 to 60--B+
60 to 80--- A
Above 80+-- A
"""

pr = int(input("enter your percentage:"))
if pr <= 25:
    print("The grade is D..")
elif pr>=25 and pr<=45:
    print("The grade is C..")
elif pr>=45 and pr<=50:
    print("The grade is B..")
elif pr>=50 and pr<=60:
    print("The grade is B+..")
elif pr>=60 and pr<=80:
    print("The grade is A..")
elif pr>=80:
    print("The grade is A++..")
else:
    print("Your failed")

# write a pytho program to display the week names by taking input form user 
day = int(input("enter your week names:"))
if day==1:
    print("Sunday")
elif day==2:
    print("Monday")
elif day==3:
    print("Tuesday")
elif day==4:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==6:
    print("Friday")
elif day==7:
    print("Saturday")

#write a python program to display the monuments according to city given by user
city = int(input("enter your city"))
if city == "Hyderabad":
    print("Charminar")
elif city == "Mnmbai":
    print("Gate Way of India")          
elif city == "Delhi":
    print("Red fort")          
elif city == "Agra":
    print("Tajmahal")          
elif city == "Chennai":
    print("Marina beach")  
else:
    print("Wrong city Selected..")            

