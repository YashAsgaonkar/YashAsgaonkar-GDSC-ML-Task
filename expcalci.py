import string
if __name__ == '__main__':

    express=input("Enter an Expression\n")
    valid="1234567890+-*/%.()"
    if all( char in valid for char in express ):
        result=eval(express)
        print("The Result is:",result)
    else:
        print("Invalid Input")