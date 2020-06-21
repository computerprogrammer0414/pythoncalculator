# Program name     : Wk8_Jaime_Smith.py
# Student Name     : Jaime Smith
# Course           : ENTD220
# Instructor       : Georgia Brown
# Date             : March 30th, 2019
# Copy Wrong       : This is my work
# Created by       : Jaime Smith
# Version:         : 20190330

from math import ceil, floor # Import built-in from Python to create dashed box on screen.
from Mylib import welcome, outside, loop, Calculator # import file Mylib
                                  
lowest = -100 # Set Lowest number allowed (-100)
highest = 101 # Set highest number allowed (100)

#----------------------- FUNCTION to create DASHED BOX on Screen
def boxed_msg(msg):
    lines = msg.split('\n')
    max_length = max([len(line) for line in lines])
    horizontal = '+' + '-' * (max_length + 2) + '+\n'
    res = horizontal
    for l in lines:
        res += format_line(l, max_length)
    res += horizontal
    return res.strip()

def format_line(line, max_length):
    half_dif = (max_length - len(line)) / 2 
    return '| ' + ' ' * ceil(half_dif) + line + ' ' * floor(half_dif) + ' |\n'


#-----------------------------------------------------------------
def user_inputs(): # Start Routine to obtain user entries
    
    while True: #Execute this routing if true
        try:
            def getLowestRange(): #FUNCTION here - Establish lowest range
                while True:
                    try:
                        numl = int(input("Enter your Lower range (<=-100):\n>>>"))
                    except Exception as e: #Will NOT ACCEPT anything that's NOT an INTEGER/NUMBER
                        print (e.__doc__)
                        print (e.message) # Will print message on the screen
                    else:
                        if numl in range (lowest, highest): # If all good run ELSE command
                            return numl #Return num1 to be used somewhere else
                        
            def getHighestRange(): # FUNCTION here = Establish highest range
                while True:
                    try:
                        numh = int(input("Enter your Higher range (<=100):\n>>>"))
                    except ValueError: # Another instance to TRAP an ERROR. 
                        print ("Invalid Entry. Please Retry: ")
                    else:
                        if numh in range (lowest, highest):
                            return numh
            low = getLowestRange() # Obtain value for lowest number and assign to low
            high = getHighestRange() #Obtain value for highest number and assign to high       
        # Start asking for two integers/numbers to start operations.
            global number1, number2 # These two variables need to be global, in order to use them later.
            number1 = int(input("Enter First number:" + "(range: " + str(low)+ " and " + str(high)+"):\n>>>"))
            if number1 in range(low, high):   # Check to see if input values are in RANGE
                pass 
            else:
                outside() # If INPUT VALUES are outside of INPUT ranges, provide message and 
                break #Break routine
            number2 = int(input("Enter Second number:" + "(range: " + str(low)+ " and " + str(high)+"):\n>>>"))
            print()
            if number2 in range(low, high):
                break                
            else:
                outside() # Call OUTSIDE routine and print message to the screen
                pass        
        except ValueError: # Trap error to assure the user enters numbers; OTHER CHARACTERS NOT ACCEPTED
            print("Please enter only numbers: ") # Notify user and try again                              
            continue 

# CLASS WRFILE with TWO METHODS - to WRITE AND READ the RESULTS from a FILE.
class Wrfile():
    def write(): # To write variables, entered by user; create file "myfile.txt"
        variables = [str(number1), str(number2)]
        with open ("myfile.txt", "w") as integer_file:
            for integer in variables:
                integer_file.write(integer)
                integer_file.write("\n")
               
    def read(): # To read variables, from file; IF NOT found, then stop and provide with a error message.
        try:
            theFile = open("myfile.txt", "r")
        except IOError as err:
            print ("""\n     Sorry, Unable to read from file; File NOT found. TRY AGAIN;
     Choose #6 (Write Results TO File) to create calculation file.
     Thanks for using Calculator """)
            exit() # Will exit routine
        # If all good, then proceed to SPLIT variables, and store to two new variables = number_saved1, and number_saved2    
        theInts = []
        for val in theFile.read().split():
            theInts.append(int(val))
            theFile.close()

        split = theInts
        number_saved1, number_saved2 = split
        
        # USING LAMBDA for these operations.
        addition = lambda  number1, number2: number1 + number2
        subtract = lambda number1,number2:number1-number2 
        multi = lambda number1, number2: number1*number2 
             
        # TRY BLOCK here, to catch any errors when dividing by ZERO.
        try: 
            divi = lambda number1, number2: number1/number2 # Lambda Function
            print("The Result of " + str(number_saved1) + "+" + str(number_saved2) + " = " , addition(number_saved1,number_saved2))
            print("The Result of " + str(number_saved1) + "-" + str(number_saved2) + " = " , subtract(number_saved1,number_saved2))
            print("The Result of " + str(number_saved1) + "*" + str(number_saved2) + " = " , multi(number_saved1,number_saved2))
            totaldiv = (round(number_saved1 / number_saved2, 2))
            print("The Result of " + str(number_saved1) + "/" + str(number_saved2) + " = " + str(totaldiv))
        except ZeroDivisionError: 
            print("The Result of " + str(number_saved1) + "/" + str(number_saved2) + " = You cannot divide by Zero")

# FUNCTIONS from MAIN MENU
while True:
# Using Functions that return results of the operations in a dictionary "oper = 
    def my_add_fn():      # For Addition
        user_inputs()     # Ask user for Input numbers
        add = Calculator(number1, number2, '+')
        addition = add.calculate()
        print(boxed_msg("ADDITION\n"+ str(number1) + "+" + str(number2)+ " = " +  str(addition)))
        #print("The Result of " + str(number1) + "+" + str(number2) + " = " , str(addition))
        print() # Print Space
        loop() # Ask user if he/she wants to continue - loop
    
    def my_sub_fn():      # For Substraction
        user_inputs()     # Ask user for Input numbers
        sub = Calculator(number1, number2, '-')
        subtract = sub.calculate()
        print(boxed_msg("SUBTRACTION\n"+ str(number1) + "-" + str(number2)+ " = " +  str(subtract)))
        #print("The Result of " + str(number1) + "-" + str(number2) + " = " , str(subtract))
        print()
        loop()
        
    def my_mul_fn():       # For Multiplication
        user_inputs()     # Ask user for Input numbers
        mul = Calculator(number1, number2, '*')
        multiply = mul.calculate()
        print(boxed_msg("MULTIPLICATION\n"+ str(number1) + "*" + str(number2)+ " = " +  str(multiply)))
        #print("The Result of " + str(number1) + "*" + str(number2) + " = " , str(multiply))
        print()
        loop()
        
    def my_div_fn():       # For Division
        user_inputs()     # Ask user for Input numbers                          
        try: 
                div = Calculator(number1, number2, '/')
                division = (round(div.calculate(), 2))
                print(boxed_msg("DIVISION\n"+ str(number1) + "/" + str(number2)+ " = " +  str(division))) # PRINT RESULT INSIDE A BOX 
                print()
                loop()
        except ZeroDivisionError: 
                print ("Cannot divide by ZERO.. retry:")
                input("Press [Enter] to continue...")
        print()
        
    def my_all_fn(): # ROUTINE FOR ALL IN ONE...
        try:   
            user_inputs()      # Call Function
            print("All In One Calculations")
            print ('-' *24) #Print lines
            add = Calculator(number1, number2, '+')
            addition = add.calculate()
            print("The Result of " + str(number1) + "+" + str(number2) + " = " , str(addition))

            sub = Calculator(number1, number2, '-')
            subtract = sub.calculate()
            print("The Result of " + str(number1) + "-" + str(number2) + " = " , str(subtract))

            mul = Calculator(number1, number2, '*')
            multiply = mul.calculate()
            print("The Result of " + str(number1) + "*" + str(number2) + " = " , str(multiply))
              
            div = Calculator(number1, number2, '/')
            division = (round(div.calculate(), 2))            
            print("The Result of " + str(number1) + "/" + str(number2) + " = " , str(division))                  
        except ZeroDivisionError:
            print("The Result of " + str(number1) + "/" + str(number2) + " = You cannot divide by Zero")          
        print()
        loop()          

    # ROUTINE to WRITE TO FILE FROM MENU
    def my_write_fn():
        user_inputs()
        print("Saving results TO file...")
        input("Press [Enter] to continue")
        Wrfile.write()
    
    #ROUTING TO READ FROM FILE FROM MENU
    def my_read_fn():
        print("Calculations FROM File")
        print ('-' *24) #Print lines
        Wrfile.read()
        print()
        loop()
    
    def my_quit_fn(): # Quit Function for Menu
        print("Thanks for using Calculator")
        raise SystemExit # Raise EXIT - QUIT
        
    def invalid():
        print ("Invalid Choice!") # Function to print invalid choice, and have menu displayed again.
     
    welcome() # Print Welcome Message
# Use List to create a menu
    menu = {"1":("Addition", my_add_fn),
            "2":("Subtraction",my_sub_fn),
            "3":("Multiplication", my_mul_fn),
            "4":("Division",my_div_fn),
            "5":("All in One", my_all_fn),
            "6":("Write Results TO File", my_write_fn),
            "7":("Read Results FROM File", my_read_fn),
            "8":("Quit", my_quit_fn)
           }
    for key in sorted(menu.keys()):
        print (key+":" + menu[key][0])

    ans = input("Make A Choice \n>>> ")
    print()
    menu.get(ans,[None,invalid])[1]() # Do NOT accept any numbers outside of range 1-8
#---------------- END OF MENU ROUTINE ------------------------        
