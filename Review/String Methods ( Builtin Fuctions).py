#String Methods


#Str. Capitalize() , make first letter capital, rest become lower case
print("********************")
name = "hello How are u doing"
name = name.capitalize()
print(name)
print("********************")

#Str. Casefold, make all text into lowercase
print("********************")
all_lower_case = "MY NAME IS MUBASHIR"
all_lower_case = all_lower_case.casefold()
print(all_lower_case)
print("********************")

#str. isalnum, if all letters are alphabets or numbers without space, it is true
print("********************")
alphanum = "233ba"
alphanum = alphanum.isalnum()
print(alphanum)
print("********************")

#str.isalpha, if all letters are in alphabets without space, it is true
print("********************")
alphabet = "hellohowareu"
alphabet = alphabet.isalpha()
print(alphabet)
print("********************")

#str.isdecimal problem
print("********************")
decimal = "0.2"
decimal = decimal.isdecimal()
print(decimal)
print("********************")

#str. isdigit, if all letters are in numbers or decimal, it is true
print("********************")
digit = "2334"
digit = digit.isdigit()
print(digit)
print("********************")

#str.isidentifier if all letters are in text, it is true
print("********************")
text = "Motherfucker"
text = text.isidentifier()
print(text)
print("********************")

#str.islower() if all text letters are small, it is true
print("********************")
small= "i have mercedes s class"
small = small.islower()
print(small)
print("********************")

#str. isnumeric, if all letters are in numbers or in decimals
print("********************")
numbers = "234567"
numbers = numbers.isnumeric()
print(numbers)
print("********************")

#str.isprintable, if letters are in numbers, alphabets, decimals or empty string, it is true
print("********************")
write= "23 ab -2.32"
write= write.isprintable()
print(write)
print("********************")

#str.isspace, it is true, if whitespace characters are in string
print("********************")
text= " "
text = text.isspace()
print(text)
print("********************")

#str.istitle, it is true, every first character after space should be capital and rest are lowercase
print("********************")
head= "Royal Education Complex"
head= head.istitle()
print(head)
print("********************")

#str.isupper, it is true, if all characters are uppercase
print("********************")
high= "ROYAL EDUCATION COMPLEX"
high= high.isupper()
print(high)
print("********************")

#str.lower, convert all characters to lowercase
print("********************")
low= "ROYAL Education CoMPlex"
low= low.lower()
print(low)
print("********************")

#str.swapcase() convert upper case characters to lowercase and lower case to upper case
print("********************")
down=" PunJab GROup of COLLeges"
down= down.swapcase()
print(down)
print("********************")

#str.title(), Convert string characters as title with 1st letter upper case and rest are lower case
print("********************")
header= "university OF Central Punjab"
header= header.title()
print(header)
print("********************")

#str.upper, convert all characters to upper case
print("********************")
long=" fuck israel, fuck america, fuck india"
long= long.upper()
print(long)
print("********************")
