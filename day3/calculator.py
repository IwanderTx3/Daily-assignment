import calc_functions

first_number = float(input("Enter the first numer: "))
operator = str(input("Enter the operator: "))
second_number = float(input("Enter the second numer: "))
result = 0.0



if operator == '*':
    result = calc_functions.multiply(first_number,second_number)
elif operator == '/':
    result = calc_functions.divide(first_number,second_number)
elif operator == '+':
    result = calc_functions.add(first_number,second_number)
elif operator == '-':
    result = calc_functions.subtract(first_number,second_number)
else:
    print("Invailid Operator")

    
print(f"{first_number}  {operator}  {second_number} = {result}")    