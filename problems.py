## BASIC CURRENCY CONVERTER
# sample input : amount_in_usd = 100
#                exchange_rate_usd_to_eur = 0.85
# sample output : equivalent amount in eur: 85.0

#amount = int(input("Give amount: "))
#eur = 0.85
#usd = (eur*amount)
#print(f"Equivalent amount in eur:{usd}")

## CONVERTIGN TEMPERATURE UNNITS
# sample input : temperature_celsius = 30
# sample output : temperature in fahrenheit:86.0
#                 temperature in kelvin: 303.15

#c = int(input("Give c: "))
#f = c*(9/5)+32
#k = 273 + c
#print(f"temperature in fahrenheit:{f}") 
#print(f"temperature in kelvin:{k}") 

## SWAP THE VALUESNOF TWO VARIABLES WITHOUT USING A TEMPORARY VARIABLE
# sample input: a=10
#               b=20
# sample output: After swapping
#                a=20
#                b=10 
### with temporary ues

#a = int(input("Give a: "))
#b = int(input("Give b: "))
#temp = b 
#b = a
#a = temp
#print(f"Value of a is: {a}")
#print(f"Value of b is: {b}")

## without temp

#a = int(input("Give a: "))
#b = int(input("Give b: "))
#b = b + a
#a = b - a 
#b = b -a
#print(f"After a is swapping: {a}")
#print(f"After b is swapping: {b}")

##SOLVE QUADRATIC EQUATIONS
# sample input: a=1
#               b=-3
#               c=2
# sample output: Root:(2.0, 1.0)

#a = int(input("Give a: "))
#b = int(input("Give b: "))
#c = int(input("Give c: ")) 
#d = (b**2)- 4*a*c
#root1 = (-b + (d**(0.5)))/2*a
#root2 = (-b - (d**(0.5)))/2*a
#print(f"Roots:({root1},{root2})")

## AREA OF CIRCLE
#sample input: radius=5
#sample output : are of circle : 78.53

#radius = int(input())
#print(3.14*radius*radius)

#radius = int(input("Give radius:"))
#a = 3.14*(radius**2)
#print("Area of circle:",a)
#print("Area of circle:",a,sep="")
#print(f"Area of circle:{a}")

##SUM OF TWO NUMBERS 
#sample input: num1=5, num2=10
#sample output: sum:15

#num1 = int(input())
#num2 = int(input())
#print("sum:", num1+num2,sep="")
# print(f"sum:{num1+num2}")