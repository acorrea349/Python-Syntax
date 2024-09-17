# Task 1: Identify the Greatest.  Write a Python program that asks the user to 
# enter three numbers. Your code should then identify and print out the largest 
# number among the three.

print("Welcome user, please input 3 numbers.")

number_1 = int(input("Input the first number: "))
number_2 = int(input("Input the second number: "))
number_3 = int(input("Input the third number: "))

if number_1 >= number_2 and number_1 >= number_3:
    print(f"The largest number is {number_1}.")
elif number_2 >= number_1 and number_2 >= number_3:
    print(f"The largest number is {number_2}.")
else:
    print(f"The largest number is {number_3}.")



# Task 2: Identify the Smallest Improve upon your code from Task 1 to also 
# determine the smallest number among the three and print it out.

if number_1 <= number_2 and number_1 <= number_3:
    print(f"The smallest number is {number_1}.")
elif number_2 <= number_1 and number_2 <= number_3:
    print(f"The smallest number is {number_2}.")
else:
    print(f"The smallest number is {number_3}.")





# Expected Outcome: If we provide the numbers 3, 3, and 4, 
# it should print out that "The smallest number is 3. 
# The largest number is 4. "


