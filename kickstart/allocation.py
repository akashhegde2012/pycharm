T=int(input('test cases'))

for i in range(T):
    N,B = input('enter').split(' ')
    N = int(N)
    B = int(B)
    rate = [int(item) for item in input("Enter the list items : ").split()]
    count = 0
    for house_rate in sorted(rate):
        print(house_rate)

        if B >=house_rate:
            B = B - house_rate
            count = count + 1
        else:
            break
    print(f' you can buy {count} no of houses')
