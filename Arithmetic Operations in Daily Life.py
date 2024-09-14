# Task 1: Grocery Store Math Calculate the total cost of three 
# items you'd commonly find in a grocery store, given their individual prices.
#  For example, what would be the cost of bread, peanut butter, and jelly be?
#   Prices don't need to be realistic!


bread = 4.34
peanut_butter = 8.00
jelly = 6.52

total = bread + peanut_butter + jelly

print("Your total will come out to $" + str(total))




# Task 2: Bank Interest If you have a savings account with a particular 
# initial amount and a fixed yearly interest rate, calculate the total amount
# in your account after a year. So if you had $10,000 at a 7% interest write
# code that would tell us the amount at the end of the year. For the example
# the expected outcome would be $10,700.

initial_balance = 10000
fixed_interest = 7

yearly_balance = (initial_balance * fixed_interest) / 100
final_balance = yearly_balance + initial_balance

print("This year you have made $" + str(yearly_balance) + " in interest. Youre total balace is $" + str(final_balance))