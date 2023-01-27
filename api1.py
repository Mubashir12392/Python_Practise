import time
import requests
result = requests.get(f"https://meowfacts.herokuapp.com/?count=1").json()
for data in result.values():
    for elements in data:
        elements


wordcount=len(elements.split())

while True:
    print(elements)
    print("----------------------------------------")
    startTime=time.time()
    textInput=str(input("Type the sentence: " ))
    endTime=time.time()
    accuracy= len(set(textInput.split())&set(elements.split()))
    accuracy=accuracy/wordcount*100
    timeTaken=round(endTime-startTime,2)
    wpm=round(wordcount/timeTaken*60)
    print("----------------------------------------")

    print ("Your accuracy is: ", accuracy)
    print ("Time taken: ", timeTaken, "seconds")
    print("Your typing speed is: ",wpm,"words per minute")

    if accuracy < 50 or wpm < 30:
        print("You need to practice typing more!")
    elif accuracy < 80 or wpm < 60:
        print("You are doing great!")
    elif accuracy <= 100 or wpm <= 100:
        print("You are a pro in typing!")
    else:
        print("You are a typing machine!")
    choice = input("Do you want to try again? (y/n): ")
    if  choice == "y":
        continue
    else:
        break
