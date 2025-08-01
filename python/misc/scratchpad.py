def main():
    print('Hello World!')
    name = input('Who goes there?\n')
    # print ("hello", name)
    # print (f"hello {name}...")
    print ("hello {}!".format(name))
    
    sum_of_two_numbers = 4 + 2

    print (sum_of_two_numbers)
    
    # casting
    print(
        int(1),
        float(1),
        bool(1),
        str(1)
    )
    
    # The bool() function will always return True unless the variable is empty, 0, None or False.
    
    #       Operator	    Name of Operation	Example	Description
    # +	    Addition	    x + y	            x plus y
    # -	    Subtraction	    x - y	            x minus y
    # *	    Multiplication	x * y	            x multiplied by y
    # **	Exponentiation	x ** y	            x raised to the power of y
    # /	    Division	    x / y	            x divided by y
    # //	Floor Division	x // y           	x divided by y, returning integer
    # %	    Modulo	        x % y	            The remainder of x divided by y
    
    #       Operator	    Description	                                        Example
    #       and	            If both statements are true, returns True	        x > 2 and y > 1
    #       or	            If one of the statements are true, returns True	    x > 3 or y > 5
    #       not	            If used, returns the reverse of the actual result	not(x > 10 and y > 5)
    
    print(type(1.2))
    print(type(True))
    
    k = 42
    
    if k < 33:
        print('not likely')
    elif k > 41:
        print('somewhat certain')
    else:
        print('wah?!')
    
    
    list = [1, 2, 3, 4, 5]
    
    for item in list:
        print(item)
    
    for i in range(3):
        print(i)
    
if __name__ == '__main__':
    main()

# ---

class MyDog:
    def __init__(self, name: str):
        self.name = name

    def show_name(self):
        print("My dog's name is ", self.name)

    def calculate_force(self, mass: int, acc: int) -> int:
        force = mass * acc
        return force


x = MyDog("pepper")
# force = x.calculate_force(1, 1)
# print(force)
