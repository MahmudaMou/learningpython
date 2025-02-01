#module -> a file containing code you want to include in your program
#          use import to include a module(Built-in or your own)
#          useful to break up a large program reusable separate files

#print(help("modules")) #this will print all the available built-in modules
#print(help("math")) #this will print all the variables and function within that modules

#to import and use a module
#import math
import math as m
print(m.pi)
#another way to import
#from math import pi
#print(pi) #now you don't need to write m.pi
