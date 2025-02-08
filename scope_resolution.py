#variable scope-> where a variable is visible and accessible
#the order of preference is-> 1.Local->2.Enclosed->3.Global->Build-in(LEGB)

def func1():
    x=1
    def func2():
        x=2
        print(x)
    func2()
func1()
#as Local is prioritized over Enclosed, in func2 x has local value 2 so it will print 2,although it has a Enclosed value 1
y=2
def func3():
    y=1
    def func4():
        print(y)
    func4()
func3()
#as Enclosed is prioritized over global, in func3 y has Enclosed function value 1 so it will print 1,
# although it has a global value 2
from math import e
def func5():
    print(e)
e=2
func5()
#Although in build-in module math e has value of 2.718281828459045.As Global is prioritized over built in and e has a
#global value of 2 so,it will print 2


