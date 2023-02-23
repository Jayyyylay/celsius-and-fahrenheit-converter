print("\nCELSIUS AND FAHRENHEIT CALCULATOR")
def conv(temp):
       if temp == "c":
            return "Celsius to Fahrenheit"
       else:
            return "Fahrenheit to Celsius"

def calculate(temp,number):
    while True:
        if temp != "c" and temp != "f":
            print("Please type 'c' and 'f' only!")
        elif temp == "c":
            total_c = (number * 9/5) + 32
            print(f"\n{number}°Celsius is {total_c}°Fahrenheit\n")
            break
        else:
            total_f = (number - 32) * 5/9
            print(f"\n{number}°Fahrenheit is {total_f}°Celsius\n")
            break

def again():
    while True:
        calc_again = input("Do you want to calculate again? Yes or No: ").lower()
        if calc_again != "yes" and calc_again != "no":
            print("Type Yes or No only please!")
        elif calc_again == "yes":
            return  True
        else:
            return False

def main():
    a = True
    while a:
        while True:
            temp = input("\npress 'c' to calculate for Celsius to Fahrenheit \npress 'f' to calculate for Fahrenheit to Celsius\nEnter your choice: ").lower()
            if temp != "c" and temp != "f":
                print("\nPlease type 'c' and 'f' only!\n")
            else:
                break
        choice = conv(temp)
        while True:
            try:
                number = float(input(f"\nEnter a number to convert from {choice}: "))
                break
            except ValueError:
                print("Integer only please.")
        calculate(temp, number)
        a = again()
main()