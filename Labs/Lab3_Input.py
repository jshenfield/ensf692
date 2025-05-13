# ENSF 692 Spring 2025
# May 13 Lab 3
# Exercise 3 - Solutions

# Add comments to explain the functionality of this program

# Input Method 1
print('\n')
print("***METHOD 1***")
input1 = input("Please enter your name: ")
print("This is the first input:", input1)


# Input Method 2

print('\n' * 2) 
print("***METHOD 2***")
while True:
    input2 = input("I am looking for specific input. You must type x: ")
    if input2 == "x":
        break
print("This is the second input: " + input2)


# Rewrite Input Method 2 so that no break statement is necessary 

# Input Method 2.5
print('\n' * 2)  # skip 2 lines
print("***METHOD 2.5***") #New Method name
input3 = 0 # saves 0 as input value for first check in while loop
i=0
while(input3 !='x'): # checks that the inputted value is not equal to x
    if(i != 1): # If this is not the first time this loop as ran, print statement below
        input3 = input("That is not the correct input. Please try to input x again below:")
    else: # If this if the first time this loop has ran, print statement below
        input3 = input("I am looking for a specific input. Please type x below:") # Actual input function for user, asking for the correct input
    i=i+1 # increase counter

print("It took you", i, "tries! Thank you for your participation.") # Print how many tries it took the user 