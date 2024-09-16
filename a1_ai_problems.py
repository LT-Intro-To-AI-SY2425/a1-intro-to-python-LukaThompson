# Complete your individualized AI problems here


# Palindrome checker
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(c.lower() for c in s if c.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage
input_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
############################################################

# Farenheit to Celcius
def f_to_c(f):
    return (f - 32) * 5 / 9

def c_to_f(c):
    return (c * 9 / 5) + 32

def start():
    print("celsius converter")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    
    choice = input("Choose 1 or 2: ")

    if choice == '1':
        f = float(input("enter temp"))
        c = f_to_c(f)
        print(f"{f}F is equal to {c:.2f}C")
    elif choice == '2':
        c = float(input("enter temp"))
        f = c_to_f(c)
        print(f"{c}C is equal to {f:.2f}F")
    else:
        print("Please choose 1 or 2.")

if __name__ == "__main__":
    start()
############################################################

#Fizbuzz
def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

