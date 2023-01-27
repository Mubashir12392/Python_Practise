#************************ Syntax *************************************

#str
"hello"

#int
254

#float
25.34

#how to take input
input("Enter your name:")

#how to get output
print()


#Get output of saved variable in print with text
x = "Hello World"
print(f"My name is {x}")



#put a string, int or float in Variable
x = "Mubashir"
y = 2343
z = 2.454

#************************* CONDITIONS *******************************
x = 2

# Equal
if x == 2:
    print("Wow")

#Greater than
if x > 2:
    print("nice")

#lesser than
if x < 2:
    print("No")

#greater than equal to
if x >= 2:
    print("o yes")

#lesser than equal to 
if x <= 2:
    print("o yes")

#not equal to
if x != 2:
    print (" it is not equal")

#to put another condition in "if"
if x==2:
    print("nice")
elif x > 2:
    print("hmm")
elif x < 2:
    print("wow grapeeeeeeeeeeeeeee")
elif x != 2:
    print("Sorry")

#to say otherwise in condition " if". write else
if x==2:
    print("great")
else:
    print("sorry")


# ******************************** Functions *********************************

#how to define a function:

def mubashir():
    print("Yo Boy")
    x = input(" Enter your name:")
    print (x)


#how to give Value to Function.  use "Return"
def mubashir():
    print("Yo Boy")
    x = input(" Enter your name:")
    print (x)
    y = 2 + 5
    return y

#let me call this Function
z = mubashir()
print(z)

#Arguments in Function


# ************************************ Loops **************************

#two types of loops


# While loop 
while True:
    print("Hello")
    print("LassH")


# for loop
x = ("hello", "my name is mubashir", "my age is 20")
for elements in x:
    print (elements)

# how to stop while loop
# while loop can stop by puttting conditon after while
KeyError
x = ["1", "2", "3", "4", "5"]
while True:
    print(x)


#How to Stop For Loop
#for can be stop by putting conditon in end and type break if conditon matches loop will stop

x = (1,2,3,4,5)
for elements in x:
    print (elements)
    if elements == 5:
        break



    