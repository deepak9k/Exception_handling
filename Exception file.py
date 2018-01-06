







# creating the user defined exception

class my_exception(Exception):
    def __init__(self,value):
        self.value=value

    def __str__(self):
        return (repr(self.value))






class Error(my_exception):
    def __init__(self,arg):
        self.args=arg



if __name__=="__main__" :
    try:
        raise (my_exception(5))
    except my_exception as error:
        print(error)

    try:
        a = 5
        c = 0
        m = a / 2

    except ArithmeticError:
        print("Zero division not allowed")

    else:
        print("there is not any exception")