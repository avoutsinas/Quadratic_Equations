import replit
import time
import math
#---------------------------To bypass matplotlib error for tempfile-----------------------------------
import os    
import tempfile
os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp()
#-----------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

R = "Y"
E = "N"
answer = "Y"

print()
print("-------------------------------------------------------------------")
print("        This program will solve quadratic equations for you!")
print("-------------------------------------------------------------------")

while answer == R:

  x1 = 0
  x2 = 0
  D = -1

  print("Quadratic equation general form: [a*x^2+b*x+c = 0]")
  print()

  while True:
      try:
          a = int(input("Please enter the value of coefficient a: "))
          print()
      except ValueError:
          print()
          print("Please enter an integer!")
          print()
      else:
          break

  while True:
      try:
          b = int(input("Please enter the value of coefficient b: "))
          print()
      except ValueError:
          print()
          print("Please enter a integer!")
          print()
      else:
          break

  while True:
      try:
          c = int(input("Please enter the value of coefficient c: "))
          print()
      except ValueError:
          print()
          print("Please enter a integer!")
          print()
      else:
          break

  if a == 0:
    if b == 0 and c != 0 :
      print(
          "----------------------------------------------------------------"
      )
      print("             !This equation has no real roots!")
      print(
          "----------------------------------------------------------------"
      )
    elif b == 0 and c == 0:
      print(
          "----------------------------------------------------------------"
      )
      print("          This is equation can be solved for any xεR")
      print(
          "----------------------------------------------------------------"
      )
    else:
      print("Since a=o , we will solve this one as a primary equation!")
      x1 = -c / b
      print()
      print(("Your chosen equation is: [{0: d}x{1:+d} = 0]".format(b,c)))
      print()
      print(
          "----------------------------------------------------------------"
      )
      print(("The root of the equation is: x ="), (x1))
      print(
          "----------------------------------------------------------------"
      )
  else:
      print(("Your chosen equation is: [{0: d}x^2{1:+d}x{2:+d} = 0]".format(a,b,c)))
      D = b**2 - 4 * a * c
      print()
      print("Let's calculate D = b^2-4*a*c first")
      print()
      print(("[D ="), (D), ("]"))
      print()
      
      if D < 0:
        print(
            "----------------------------------------------------------------"
        )
        print("             !This equation has no real roots!")
        print(
            "----------------------------------------------------------------"
        )
      elif D == 0:
        x1 = -b / (2 * a)
        print(
            "----------------------------------------------------------------"
        )
        print(("This equation has one double solution therefore x1 = x2 ="),
              (x1))
        print(
            "----------------------------------------------------------------"
        )
      elif D >0 :
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(
            "----------------------------------------------------------------"
        )
        print("This equation has two roots, therefore:")
        print(("x1 ="), (x1), ("and"))
        print(("x2 ="), (x2))
        print(
            "----------------------------------------------------------------"
        )

  if D >= 0 or (a == 0 and b != 0):

    def f(x):
        return a * x**2 + b * x + c

    #vectorize function
    f = np.vectorize(f)

    #generate values between -10-abs(x2,x1) and 10+abs(x1,x2) depending on the sign of a
    if a > 0:
        x = np.linspace(-10 - abs(x2), 10 + abs(x1))
    elif a==0:
      x = np.linspace(-20 - abs(x1), 20 + abs(x1))
    elif a < 0:
        x = np.linspace(-10 - abs(x1), 10 + abs(x2))

    #Define the figure along with its grid size
    fig = plt.figure(num=None, figsize=(8.1,5.6))
    #Define the axis
    ax = fig.add_subplot(1, 1, 1)

    #spine placement data centered  
    ax.spines['left'].set_position(('data',0.0))
    ax.spines['bottom'].set_position(('data',0.0))

    #make top and right axis disappear
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    #show only roots of x on graph
    if a == 0:
        ax.set_xticks([x1])
    else:
        ax.set_xticks([x1, x2])
    #Do not display number on y axis
    ax.set_yticks([])

    # naming the x axis
    plt.xlabel('x - axis',labelpad=5)
    # naming the y axis
    plt.ylabel('y - axis',labelpad=5)

    # giving a title to my graph
    plt.title('-Equation Graph-')

    #display plot, pause it and ask for input to continue
    plt.plot(x,f(x),color='red',linestyle='dashed',linewidth=1)
    plt.legend(['f(x) ={0: d}x$^{{2}}${1:+d}x{2:+d}'.format(a,b,c)],loc='upper left') # showing legend
    plt.pause(0.001)
    input("Press [enter] to continue.")

  else:
      pass

  #This loop asks the user whether he/she wants to enter another equation
  while True:
      print()
      answer = str(input("Do you want to try another equation? (Y/N): ").upper())
      if (answer != R and answer != E):
          print()
          print("!Please select Yes or No as your answer(Y/N)!")
      elif answer == R:
          time.sleep(0.25)
          # Close a figure window
          plt.close() 
          #clear the terminal 
          replit.clear()
          #refresh
          time.sleep(0.25)
          print()
          print(
              "-------------------------------------------------------------------"
          )
          print(
              "        This program will solve quadratic equations for you!")
          print(
              "-------------------------------------------------------------------"
          )
          print()
          print(
              "------------------------Let's try another one!---------------------"
          )
          print()
          break
      elif answer == E:
          print()
          print(
              "-------------------------------------------------------------------"
          )
          print("                  Hope to see you again!")
          print(
              "-------------------------------------------------------------------"
          )
          print()
          exit("                         Goodbye!")
  else:
      break

else:
    exit("                                 Goodbye!")
