#Simple Calculator(Add,Subt,Mul, Div)
#Using OOPS Concept

class Calculator:
    def add(self, n1, n2):
        return n1 + n2
    def subtract(self, n1, n2):
        return n1-n2
    def multiply(self, n1, n2):
        return n1 * n2
    def divide(self, n1, n2):
        return n1/n2

def main():
    calc = Calculator()

    print("Welcome to Python Simple Calculator!!")

    while True:
        try:
            n1 = float(input("Enter the first number: "))
            n2 = float(input("Enter the first number: "))
            print("Choose an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
        
            ops = input("Enter the number corresponding to the operation (1/2/3/4): ")
        
            if ops == '1':
                res = calc.add(n1,n2)
                ops_Str = "addition"
            elif ops == '2':
                res = calc.subtract(n1,n2)
                ops_Str = "subtraction"
            elif ops == '3':
                res = calc.multiply(n1,n2) 
                ops_Str = "Multiplication"
            elif ops == '4':
                res = calc.divide(n1,n2)
                ops_Str = "Division"
            else:
                print("Invalid operation choice. Please try again.")
                continue
        
            print(f"The result of the {ops_Str} of {n1} and {n2} is: {res}")                      
    
        except ValueError as e:
            print(f"Error: {e}")    
        
        next_calculation = input("Do you want to perform another calculation? (y/n): ").lower()
        if next_calculation != 'y':
            print("Thank you for using the calculator. Goodbye!")
            break
    

if __name__ == "__main__":
    main()