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