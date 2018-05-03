user_input = 'y'

while user_input == 'y' :
    Y = 1  
    X = 1 
    number  = int(input("Please enter the number to factor: ")) 

    while Y < number +1 :
        X = X*Y
        Y = Y+1

    print(f"The factorial of {number} is {X}")
    user_input = input("Would you like to do another? (y or n) ")
    

print("Thank you!")




