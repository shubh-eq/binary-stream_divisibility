# Check divisibility in a binary stream (Finite State Machine)

state = 0

def divisible_test(digit,quotient):
    """Takes the current state of number and tests the divisiblility"""
    global state
    state = state*2 + digit
    state = state % quotient
    if(state==0):
        print(f"Divisible")
    else:
        print(f"NOT Divisible")


def main():
    quotient = int(input("Enter the quotient:"))
    while True:
        digit = int(input("Enter the digit:"))
        divisible_test(digit,quotient)


main()