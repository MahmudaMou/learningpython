# if __name__ == '__main__'
#let's say we are making a module which will be imported in another file, and also it can run standalone.
#In this module or script there will be function and class. Now if we need to call the functions/classes
#within the module then we have to call the function inside this condition(if __name__ == '__main__').otherwise
#when we will import this module all the function will be called automatically inside that file.
#if __name__ == '__main__'-> this condition means that if it is the origin
#Example->Library =import library for functionality when running library directly
#Benifits->code is modular,helps readability, leaves no global variables,avoid united execution

def favourite_food(food):
    print(f"your favourite food is {food}")
def main():
    print("Hello")
    favourite_food("pizza")
    print("Good Bye!")
#now if we need to call main() function here we have to write inside the condition
if __name__ == '__main__':
    main()
#now lets import this inside example file
