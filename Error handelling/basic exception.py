# error handelling
while 1:
    try:
        age=int(input('what is your age'))
        10/age
    except ValueError :
        print('please enter a number')
    except ZeroDivisionError:
        print("Enter a natural number")
    else:
        print('thankyou')
        break;