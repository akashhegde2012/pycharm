# list,sets,dictionary

my_list=[]
for char in 'hello':
    my_list.append(char)
# using list comprehensoion
my_list2=[c for c in 'hello']
print(my_list2,my_list)
print([x for x in range(0,100)])
print([x*2 for x in range(0,100) ])

# list containing only even squares
print([x**2 for x in range(20) if x%2==0])

# set
print({x for x in range(0,100)})
# dictionary comprehesion
simple={
    'a':1,'b':2,'c':3
}
my_dict={key:value**2 for key,value in simple.items()}
print(my_dict)
print({num:num*2 for num in [1,2,3,5]})