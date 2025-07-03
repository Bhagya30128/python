"""
Netsed if : A if within a if is called Nested if
syntax: if condition:
                outer if statements
                if condition:
                    inner if statements
                else:
                     inner else ststements
        else:
              outer else statements
"""
# A program on weather Advisories
is_snowing=True
temp=int(input("enter the temperature:"))
if is_snowing>10:
    print("Please carry Umbrella")
    if is_snowing==-10:
        print("Please carry Umbrella and jacket")
    else:
        print("Enjoy the sunny day!!")
else:
    print("U have a great day")  

#Express Delivery 
weight=int(input("enter the weight:"))
if weight==4:
    print("the delivery can be expected within 24 hrs..")
    if weight<=10:
        print("Need to pay an extra amonut for extra weigh..")
    else:
        print("No need to pay any extra charge Have a Great Delivery!!")
else:
    print("Need to wait 3-5 Bussiness days to expect the delivery")  
                           