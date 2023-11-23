def calcule(num1,operator,num2):
    if operator=='*':
        print(num1*num2)
    elif operator=='-':
        print(num1-num2)
    elif operator=='+':
        print(num1+num2)
    elif operator=='/':
        print(num1/num2)
    elif operator=='%': 
        print(num1%num2)

calcule(15,'*',69)
calcule(50,'%',100)
calcule(16,'-',80)