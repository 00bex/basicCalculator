print('WELCOME')
num1 =int(input('ENTER FIRST NUMBER:'))
num2 = int(input('ENTER SECOND NUMBER:'))
cal = 0
while cal<5 :
    print ('MENU')
    print ('1.ADD')
    print ('2.SUBTRACT')
    print ('3.MULTIPLY')
    print ('4.DIVIDE')
    print ('5.EXIT')
    
    cal = int(input('ENTER YOUR CHOICE :'))
    if cal == 1:
        sum = num1 + num2
        print('Sum:',sum)
    elif cal == 2:
        diff = num1 - num2
        print('Difference:',diff)
    elif cal == 3:
         times = num1 * num2
         print('Product:', times)
    elif cal == 4:
        div = num1 / num2
        print('Quotient :', div)
    elif cal == 5:
        break
    else:
        print('INVALID CHOICE')