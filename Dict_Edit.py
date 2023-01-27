# EDIT OF DICTS

person = {
    "name" : "pornhub",
    "creation" : "12/02/2000",
    "founder" : "Booba",
    "ceo" : "Ranta",
    "dalaal" : "Jara g",
}

# CHANGING VALUE OF KEY>>>>>>>>>>>>>>>>>>>>>
person["founder"] = "Choora"
person.update({"founder" : "phatti"})


# ADD A NEW KEY AND VALUE>>>>>>>>>>>>>>>>>>>
person["senior manager"] = "Soban"


# REMOVE A KEY FROM DICT>>>>>>>>>>>>>>>>>>
person.pop("dalaal")
# step 2:
del person["name"]


# REMOVE THE LAST INSERTED ITEM
person.popitem()


# CLEAR A DICTIONARY>>>>>>>>>>>>>>>>>>>
person.clear()

print(person)
# del keyword will delete the whole dict -) del person>>>>>>>>>>>>>>>>>>