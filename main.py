import cmath
from task1 import counted
from task2 import decorator1
from task3 import decorator_2
from task4 import decorator_3

import task3
import task4
# function one
def pascal_triangle(n):
    side = [0]
    top = [1]
    for i in range(n):
        print(top)
        top = [i+j for i,j in zip(top+side,side +top)]

# function 2
def quadratic_equation_with_complex_math(x,y,z):
    dis = (y ** 2) - (4 * x * z)
    ans1 = (-y - cmath.sqrt(dis)) / (2 * x)
    ans2 = (-y + cmath.sqrt(dis)) / (2 * x)
    print('The roots are :',"ans1: "+str(ans1), " ans2: ",str(ans2) )


#function 3
def sort_by_last_name(names):
    names.sort(key=lambda name: name.split(" ")[-1].lower())
    print(names)


# function 4
def build_quadratic_function(a,b,c):
    return lambda x:a*x**2+b*x+c


pascal_triangle(6)
quadratic_equation_with_complex_math(1,4,2)
sort_by_last_name(["mohammad tarek","ahmad isleem","isleem ahmad"])
func= build_quadratic_function(1,2,3)
print(func(5))

print ("_____________end of main file functions____________")
# TASK 1 Decorator  1
class MyList(list):
    @counted
    def methodOne(self, *args, **kwargs):
        return list.pop(self)

    @counted
    def addToList(self, *args, **kwargs):
        return list.append(self,*args)

x = MyList([7, 21, 12, 4, 5])
for i in range(3):
    x.methodOne()
    x.addToList(i)

print(x.methodOne.calls)
print(x.addToList.calls)

print ("_____________end of task1 ____________")

@decorator1
def func(*b,**a):
    """
this is a readable signature
     """
    # print(a)
    # print(b)
    for i in a:
        print(i)

@decorator1
def func2(*n,**y):
    print("my car")

func(5,a=3,b=2,c=4)
func2(3,h=2,w=99)


print ("_____________end of task2 ____________")


@decorator_2
def func(n):
    # f = open('myfile.txt')
    # s = f.readline()
    # i = int(s.strip())
    for _ in range(1000000):
        pass
    print(n+1)


func(2)
@decorator_2
def funb(a, b):
    return a+b

funb(2, 3)

task3.printResult()

print ("_____________end of task3 ____________")

@decorator_3
def func(n,v):
    f = open('mysgrrgfile.txt')
    s = f.readline()
    i = int(s.strip())

func(2, 3)
task4.printOut()