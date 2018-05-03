user_input = 'Y'
numbers = [2,13,15,16,23]

while user_input == 'Y' :

    search_num = int(input("Please enter the number you are looking for: "))
    found = -1
    for index in range(0,len(numbers)):
        if numbers[index] == search_num :
            found = index
            break

    if found >=0:
        print(f"found {search_num}.  It is at index {index}")
        print(" ")
    else:
        print("Sorry I did not find your number.")  
        print(" ")      


    user_input = input("Search Again? Y or N  ")

print("Thank you!")    
    

