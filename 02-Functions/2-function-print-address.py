#Function to print

def print_parameter(a):
    print "Parameter: ", a

def print_address(a):
    print "Addres of parameter is: ", hex(id(a)) 

    
a = 'a'
b = 2
c = 6.5

    
print_parameter(a)
print_address(a)
print_parameter(b)
print_address(b)
print_parameter(c)
print_address(c)


