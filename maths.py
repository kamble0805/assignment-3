import math

def main():
    num = int(input("Enter a number: "))
    
    if num <= 0:
        print("Please enter a number greater than 0")
        return

    print("Log:", math.log(num))
    print("Sine:", math.sin(num))
    print("Square root:", math.sqrt(num))

main()
