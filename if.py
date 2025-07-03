#if a ==10:
 #print("the if statement is executed")
# Accept the number of days from the user and calculate the charge  for library 

num = int(input("Enter the day:"))
if num<=5:
    print("The charge is..", num*2)
elif num>=6 and num<=10:
    print("The charge is..", num*3)
elif num>=11 and num<=15:
    print("The charge is..", num*4)
elif num>=15:
    print("The charge is..", num*5) 
else:
    print("Wrong Days selected..")

"""
Write a program to accept two numbers from user and an operator and perform operation accordingly]
num1 : 5
num2 : 10
opr : +
answer : 1 
"""
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
opr = input("enter a operator:")
if opr=="+":
    print("The answer:", num1+num2)
elif opr=="-":
    print("The answer:", num1-num2)
elif opr=="*":
    print("The answer:", num1*num2)
elif opr=="/":
    print("The answer:", num1/num2)
else:
    print("Wrong operator selected..") 
   

# write a program to accept a number from 1 to 12 then display name of the month amd days in that month 
# like 1 for january and the no of days 31 and so on 
mon_num = int(input("enter a month:"))
if mon_num==1:
    print("jan, 31days")
elif mon_num==2:
    print("feb, 28 days")
elif mon_num==3:
    print("mar, 31days")     
elif mon_num==4:
    print("apr, 30days")     
elif mon_num==5:
    print("may, 31days")     
elif mon_num==6:
    print("jun, 30days")     
elif mon_num==7:
    print("jul, 31days") 
elif mon_num==8:
    print("aug, 31days")     
elif mon_num==9:
    print("sep, 30days")     
elif mon_num==10:
    print("oct, 31days")     
elif mon_num==11:
    print("nov, 30days") 
elif mon_num==12:
    print("dec, 31days")
else:
    print("Wrong month selected..")   

    
