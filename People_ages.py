#Take input of age of 3 people by user and determine oldest and youngest among them.

First =int(input("Enter Age of 1st Person:"))
Second =int(input("Enter Age of 2nd Person:"))
Third =int(input("Enter Age of 3rd Person:"))

#oldest
if ((First > Second and First > Third) and (First != Second and First != Third)):
    print(f"{First} is the age of First Person and it is oldest")
elif ((Second > First and Second > Third) and (Second != First and Second != Third)):
    print(f"{Second} is the age of Second Person and it is oldest")
elif ((Third > Second  and Third > First) and (Third != Second and Third != First)):
    print(f"{Third} is the age of third person and it is oldest")

#Youngest
if((First < Second and First < Third) and (First != Second and First != Third)):
    print(f"{First} is the age of First Person and it is Youngest")
elif ((Second < First and Second < Third) and (Second != First and Second != Third)):
    print(f"{Second} is the age of Second Person and it is Youngest")
elif ((Third < Second and Third < First) and (Third != Second and Third != First)):
    print(f"{Third} is the age of third person and it is Youngest")

