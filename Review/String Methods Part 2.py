#Take input from user and print the 3rd and 5th character of their input.
print("*****************************************")

inptstr= input("Write a Word of which 3rd and 5th Character you want to print:")
thirdchrac= inptstr[2]
fifthcharac=inptstr[4]
print(f"Your third character is:{thirdchrac}")
print(f"Your Fifth Character is:{fifthcharac}")

#Take input and print the length of the string

print("*****************************************")

length= input("Write your statement here:")
length= len(length)
print(f"your statement has {length} Characters")

#Take input and print the number of spaces in the input
print("*****************************************")
Space= input("Whats your feedback, write here:")
space= Space.count(" ")
print(f"Your statement has {space} number of spaces")
 

 #Take input and print if the text starts with "hello"
print("*****************************************")
hey=input("Type your statement and make sure it starts with Hello:")
Yo=hey.startswith('Hello')
print(Yo)

#Take input and replace "http" with "https"
print("*****************************************")
site=input("Search here with the Full Site name:")
site=site.replace("http","https")
print(f"You Search for this Website: {site}")

#Take input and print the fk off text
print("*****************************************")
text= input("Type text which you want to reverse:")
reverse= text[::-1]
print(f"Your Statement format is: {reverse}")


#Done