try:
    a=int(input("Enter vale of First Number: "))
    b=int(input("Enter Value of Second Number: "))
    print("What kind of operation you want to perform\nPress + for Addition\nPress - for Subtraction\nPress * for  Multiplication\nPress / for Division")
    o=input("Enter Operation: ")
    match o:
        case "+":
            print(f"Answer is {a+b}")
        case "-":
            print(f"Answer is {a-b}")
        case "*":
            print(f"Answer is {a*b}")
        case "/":
            print(f"Answer is {a/b}")   
        case default:
            print("There was an error")
except Exception as e:
    print("Enter Valid Number")
            
