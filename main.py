import replit
import time
import math
import matplotlib.pyplot as plt
import numpy as np


D= -1  
R = "Y" 
E = "N"
answer = "Y"

print (" ")
print ("-------------------------------------------------------------------")
print("        This program will solve quadratic equations for you!")
print ("-------------------------------------------------------------------")

while answer==R:
  
  print ("Quadratic equation general form: [a*x^2+b*x+c = 0]")
  print (" ")

  while True:
    try:
      a=int(input("Please enter the value of coefficient a: "))
      print (" ")
    except ValueError:
        print (" ")
        print ("Please enter an integer!")
        print (" ")
    else:
        break

  while True:
    try:
      b=int(input("Please enter the value of coefficient b: "))
      print (" ")
    except ValueError:
        print (" ")
        print ("Please enter a integer!")
        print (" ")
    else:
        break

  while True:
    try:
      c=int(input("Please enter the value of coefficient c: "))
      print (" ")
    except ValueError:
        print (" ")
        print ("Please enter a integer!")
        print (" ")
    else:
        break

  if a==0:
    if b==0:
      print("----------------------------------------------------------------")
      print("             !This equation cannot be solved!")
      print("----------------------------------------------------------------")
    else:
      print("Since a=o , we will solve this one as a primary equation!")
      x=-c/b
      print (" ")
      print (("Your chosen equation is: ["),(b),("*x +"),(c),("= 0]"))
      print (" ")
      print("----------------------------------------------------------------")
      print (("The root of the equation is: x ="),(x))
      print("----------------------------------------------------------------")
  else:
    print (("Your chosen equation is: ["),(a),("x^2 +"),(b),("*x +"),(c),("= 0]"))
    D=b**2-4*a*c
    print(" ")
    print("Let's calculate D = b^2-4*a*c first")
    print(" ")
    print(("[D ="),(D),("]"))
    print(" ")
    if D<0:
      print("----------------------------------------------------------------")
      print("             !This equation cannot be solved!")
      print("----------------------------------------------------------------")
    elif D==0:
      x1=-b/(2*a)
      print("----------------------------------------------------------------")
      print(("This equation has a double solution therefore x1 = x2 ="),(x1))
      print("----------------------------------------------------------------")
    else:
      x1=(-b+math.sqrt(D))/(2*a)
      x2=(-b-math.sqrt(D))/(2*a)
      print("----------------------------------------------------------------")
      print("This equation has two roots, therefore:") 
      print(("x1 ="),(x1),("and"))
      print(("x2 ="),(x2))
      print("----------------------------------------------------------------")
  
  if D>=0 or (a==0 and b!=0):

    def f(x):
      return a*x**2+b*x+c

    # Create the vectors X and Y
    x = np.linspace(-20,20)
    y = f(x)


    # Create the plot
    plt.plot(x,y,label='y = a*x**2+b*x+c')

    # Add a title
    plt.title('Graph')

    # Add X and y Label
    plt.xlabel('x axis')
    plt.ylabel('y axis')

    # Add a grid
    plt.grid(alpha=.4,linestyle='--')

    # Add a Legend
    plt.legend()

    # Show the plot
    plt.ion
    plt.show() 
    plt.pause(0.001)
    input("Press [enter] to continue.")
  else:
    pass  

#This loop asks the user whether he/she wants to do another division
  while True:
    print (" ")
    answer = str(input("Do you want to try another equation? (Y/N): "))
    if (answer!=R and answer!=E):
      print (" ")
      print ("!Please select Yes or No as your answer(Y/N)!")
    elif answer==R:
      time.sleep(0.25)
      replit.clear()
      time.sleep(0.25)
      print (" ")
      print ("-------------------------------------------------------------------")
      print("        This program will solve quadratic equations for you!")
      print ("-------------------------------------------------------------------")
      print (" ")
      print ("------------------------Let's try another one!---------------------")
      print (" ")
      break
    elif answer==E:
      print (" ")
      print ("-------------------------------------------------------------------")
      print ("                  Hope to see you again!")
      print ("-------------------------------------------------------------------")
      print (" ")
      exit("                          Goodbye!")
  else:
    break
       
else:
 exit("                               Goodbye!")