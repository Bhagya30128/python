"""""
Looping statements are also called as Iterative statements
These statements are used to run a praticular condintion
no of time... divided into 2 types 
1. while 
2. for
"""""
#while: it executes when the condition is true 
"""
syntax: while condition:
            statements
            exit condition/incrementation
""" 
#eg1:
i = 1
while i<=10:
    print(i) 
    #in this particular line the 
    # "i" value runs "n" times because no incrementation/exit cond specif
    print("the value", i)
    i+=1

#eg2:
while True:
    print("the while condition")
#Note: As defaultcondition is True the while loop runs "infinity times"    

#eg3:
while False:
    print("the while condition")
#As while is also called entry control
#loop if just checks the condition in the entrance
#as default False is given as condition it wont execute