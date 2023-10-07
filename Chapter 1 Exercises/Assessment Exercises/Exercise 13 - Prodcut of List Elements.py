# Write a program that passes a list as an argument to a function. The function should then calculate the product (values multiplied) of the list values and return this value back to the main program.

# We import these functions as we will use them again for this exercise
from random import seed
from random import randint


def list_product(my_list):
    
    # We will call the 'seed()' function to seed our 'randint()' functions. The seed of 'randint()' function inside 'seed()' will be the current system time  
    seed(randint(0,10))

    # Initialize a counter for the total product. For some reason, putting this variable outside the function will not work
    total_product = 1

    print(f"These are the numbers in that list: {rand_list}! \n")
    
    for i in my_list:
        product = total_product

        # We can use a variable's previous value and assign it to the same variable, which will replace the old one
        product = product * i

        # Assign the new value of 'product' to our counter for the next iteration
        total_product = product

    return product

rand_list = [randint(1,10) for i in range(3)]

print(f"And the product of all the numbers is... {list_product(rand_list)}!")
