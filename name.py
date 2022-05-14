def print_full_name(first,last):
    print("Hello", first,last ,"! You just delved in python.")
print_full_name("Barsha","Rani")
# &&&&&&&&&&&&&&&&&&&&&&&&&&
def print_full_name(first,last):
    print("Hello {} {}! You just delved into python.". format(first,last))
if __name__ == '__main__':
    first_name = input("Enter any name=")
    last_name = input("Enter any name=")
    print_full_name(first_name, last_name)