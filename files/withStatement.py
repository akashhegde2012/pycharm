try:
    with open('tst.txt','r') as my_file:
        text=my_file.write(':)')
        print(text)
except FileNotFoundError as err:
    print('file doesnot exist')
    raise err
