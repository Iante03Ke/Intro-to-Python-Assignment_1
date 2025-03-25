#Basic Calculator Program

#This program asks the user for two input numbers and a mathematical operation, then does the other job. 

#Get first input(number)
firstNumber = input("Enter the first Number: ")

#Get the Second Number
secondNumber = input("Enter the Second Number: ")

#Convert the Inputs to floats

ffirstNumber = float(firstNumber)
fsecondNumber = float(secondNumber)

#Get the mathematical operation from user

mathOperation = input('Enter the Mathematical Operation of your choice (+, -, *, and, /): ')

#Condtions for each mathematical Operation 

if mathOperation == "+": #Get the Sum for the numbers
    solution = ffirstNumber + fsecondNumber
    
elif mathOperation == "-": #Get the Difference of the numbers
    solution = ffirstNumber - fsecondNumber
    
elif mathOperation == "/": #Get the division of the numbers 
    #To remove undefined solutions
    if fsecondNumber != 0:
        solution = ffirstNumber / fsecondNumber
    
    else:
        solution = print ("The mathematical Operation cannot be done. It is UNDEFINED!")
    
elif mathOperation == "*":
    solution = ffirstNumber * fsecondNumber
    
else:
    print("Choice different from the required choices. Check mathematical operation!")
    
#Print the final solution based on user inputs

print(ffirstNumber, mathOperation, fsecondNumber, "=", solution)
    