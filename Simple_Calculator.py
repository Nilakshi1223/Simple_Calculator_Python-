# Arithmatic operations 
def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b
    
def div(a,b):
    try:
        return a/b
    except Exception as e:
        print(e)
        
def power(a,b):
    return a**b
    
def remind(a,b):
    return a%b

# Select choices function 

def select_op(choice):
    if(choice=="#"):
        return -1
    elif(choice=="$"):
        return 0
    elif(choice in('+','-','*','/','^','%')):
        while True:
            num1=str(input("Enter first number: "))
            print(num1)
            if num1.endswith('$'):
                return 0
            if num1.endswith('#'):
                return -1
            try:
                x1=float(num1)
                break
            except:
                print("Not a valid Number,please enter again")
                continue
        
        while True:
            num2=str(input("Enter second number: "))
            print(num2)
            if num2.endswith('$'):
                return 0
            if num2.endswith('#'):
                return -1
            try:
                x2=float(num2)
                break
            except:
                print("Not a valid Number,please enter again")
                continue
        if choice=="+":
            print(x1,"+",x2,"=",add(x1,x2))
        elif choice=="-":
            print(x1,"-",x2,"=",sub(x1,x2))
        elif choice=="*":
            print(x1,"*",x2,"=",mul(x1,x2))
        elif choice=="/":
            print(x1,"/",x2,"=",div(x1,x2))
        elif choice=='':
            print(x1,"",x2,"=",power(x1,x2))
        elif choice=="%":
            print(x1,"%",x2,"=",remind(x1,x2))
        else:
            print("Something Went Wrong")
    else:
        print("Unrecognized operation")
        
#This is the main loop. 
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()


